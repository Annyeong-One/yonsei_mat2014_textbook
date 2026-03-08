# GPU Architecture

## What is a GPU?

A **Graphics Processing Unit (GPU)** is a specialized processor designed for parallel computation. Originally built for rendering graphics, GPUs now power machine learning, scientific computing, and data processing.

```
CPU vs GPU: Processing Units
┌─────────────────┐          ┌─────────────────────────────┐
│      CPU        │          │            GPU              │
│  ┌───┐ ┌───┐   │          │ ┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐   │
│  │ C │ │ C │   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  └───┘ └───┘   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  ┌───┐ ┌───┐   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │ C │ │ C │   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  └───┘ └───┘   │          │ └─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘   │
│                │          │      ... many SMs ...       │
│  Few complex   │          │  Many arithmetic lanes      │
│  processors    │          │  per processor (SM)         │
│  (OoO, BP,     │          │                             │
│   large caches)│          │  (like a vector processor)  │
└─────────────────┘          └─────────────────────────────┘
```

> **Note**: GPU "cores" (CUDA cores) are **not equivalent to CPU cores**. A CPU core is a full independent processor with out-of-order execution, branch prediction, and large caches. A CUDA core is a single arithmetic execution lane inside a Streaming Multiprocessor (SM). As a very rough analogy: a CPU core is a **latency-optimized processor**, while an SM is a **throughput-optimized processor** — they share the concept of being independent processing units, but an SM lacks deep speculation and large private caches.

## GPU vs CPU Design Philosophy

| Aspect | CPU | GPU |
|--------|-----|-----|
| **Execution Units** | Few complex cores (4-64) | Thousands of lightweight execution lanes across many SMs |
| **Unit Complexity** | High (out-of-order, branch prediction) | Simple ALUs, but SMs include sophisticated scheduling hardware |
| **Clock Speed** | High (3-5 GHz) | Lower (1-2 GHz) |
| **Cache per Core** | Large | Small |
| **Optimized For** | Latency (fast single tasks) | Throughput (many parallel tasks) |

## GPU Architecture Overview

### NVIDIA GPU Structure (CUDA Architecture)

```
┌─────────────────────────────────────────────────────────────┐
│                         GPU                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                 Streaming Multiprocessor (SM)        │   │
│  │  ┌─────┐┌─────┐┌─────┐┌─────┐  ┌─────┐┌─────┐┌─────┐│   │
│  │  │CUDA ││CUDA ││CUDA ││CUDA │  │CUDA ││CUDA ││CUDA ││   │
│  │  │Core ││Core ││Core ││Core │  │Core ││Core ││Core ││   │
│  │  └─────┘└─────┘└─────┘└─────┘  └─────┘└─────┘└─────┘│   │
│  │            ...  (32-128 cores per SM)  ...          │   │
│  │  ┌────────────────────────────────────────────────┐ │   │
│  │  │  Shared Memory + L1 Cache (same physical pool) │ │   │
│  │  └────────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │     SM      │ │     SM      │ │     SM      │  ...      │
│  └─────────────┘ └─────────────┘ └─────────────┘           │
│         (40-100+ SMs per GPU)                              │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    L2 Cache                          │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Global Memory (VRAM) - 8-80 GB         │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

| Component | Description |
|-----------|-------------|
| **CUDA Core** | Scalar execution unit for integer and floating-point arithmetic within an SM |
| **Streaming Multiprocessor (SM)** | Group of CUDA cores + shared memory + warp schedulers + load/store units + special function units |
| **Shared Memory** | Programmer-managed on-chip memory, often implemented in the same hardware pool as L1 cache but logically distinct |
| **Global Memory (VRAM)** | Large but slower GPU memory |
| **Tensor Cores** | Specialized units for fused matrix multiply-accumulate (MMA) operations (newer GPUs) |

### SM Execution Units

Each SM contains multiple types of execution units that can operate **in parallel within a single cycle**:

- **FP units** — floating-point arithmetic (CUDA cores)
- **INT units** — integer arithmetic
- **Load/store units** — memory operations
- **Special function units (SFUs)** — transcendental functions (sin, cos, exp)
- **Tensor cores** — fused matrix multiply-accumulate (MMA)

This internal parallelism means an SM can often execute different instruction types in parallel (e.g., an integer instruction, a floating-point instruction, and a memory load in the same cycle) — though this depends on issue slot availability and instruction dependencies.

Among these, **tensor cores** deserve special attention. Unlike CUDA cores, which perform one scalar multiply-add per cycle, tensor cores perform a **matrix MMA** on small fragments per cycle:

```
CUDA Core:   a * b + c → d  (scalars)
Tensor Core: D = A × B + C  (matrix fragments)
             FP16 × FP16 → FP32 accumulate (mixed precision)
```

The fragment size depends on the GPU architecture and data type (e.g., 4x4 on Volta, larger fragments on Ampere and later). A key feature is **mixed-precision accumulation** — inputs can be low-precision (FP16/BF16) while the accumulator maintains higher precision (FP32), preserving numerical accuracy during training. This fused MMA operation maps directly to the matrix multiplications that dominate neural network computation, making tensor cores essential for deep learning training/inference and large matrix operations.

## The SIMT Execution Model

GPUs use **SIMT** (Single Instruction, Multiple Threads). Like CPUs, GPU SMs have internal instruction pipelines, issue units, and execution pipelines — but instead of optimizing for single-thread performance, they are designed to issue instructions across many warps simultaneously:

```
SIMT: One instruction, many threads execute it

Instruction: ADD

Thread 0:  a[0] + b[0] → c[0]
Thread 1:  a[1] + b[1] → c[1]
Thread 2:  a[2] + b[2] → c[2]
Thread 3:  a[3] + b[3] → c[3]
   ...         ...
Thread N:  a[N] + b[N] → c[N]

Each warp (32 threads) executes ADD across its threads,
while the SM schedules many warps to keep hardware busy.
```

### Warps and Thread Blocks

Threads are organized hierarchically:

```
GPU Execution Hierarchy

Grid (entire computation)
├── Block 0
│   ├── Warp 0 (32 threads)
│   ├── Warp 1 (32 threads)
│   └── ...
├── Block 1
│   ├── Warp 0 (32 threads)
│   └── ...
└── ...
```

- **Warp**: 32 threads that execute in lockstep. If threads in a warp follow different branches, the warp executes each path sequentially (**warp divergence**), reducing throughput. AMD GPUs use a similar concept called **wavefronts** (64 threads)
- **Block**: Group of warps sharing memory
- **Grid**: All blocks for a computation

### Warp Scheduling and Latency Hiding

Unlike CPUs, which use caches and out-of-order execution to hide memory latency, GPUs use a fundamentally different strategy: **massive warp-level multithreading**. Global memory latency is typically hundreds of cycles (~400–800, varying by memory type and architecture) — far longer than CPU cache misses. Instead of stalling, each SM has warp schedulers that switch between many active warps every cycle:

```
Warp A: ████ STALL (waiting for memory) ████████████████████
Warp B: ──── ████████████████████ STALL ────────────████████
Warp C: ──── ──── ████████████████████████████ STALL ───────
Warp D: ──── ──── ──── ████████████████████████████████████

SM:     always executing something — no idle cycles
```

When one warp stalls on a memory access, the scheduler instantly switches to another ready warp at near-zero overhead. This is possible because each warp's registers are permanently allocated — there is nothing to save or restore. (The scheduler still performs instruction issue decisions and scoreboard checks, but these are extremely fast compared to the memory latency being hidden.) Warps are interleaved at the instruction issue level — the scheduler picks a ready warp each cycle, so execution alternates between warps on a per-instruction basis. The more active warps an SM has, the better it can hide latency.

### Occupancy

**Occupancy** measures how well an SM's warp capacity is utilized:

```
Occupancy = active warps on SM / maximum warps SM supports
```

Higher occupancy generally means better latency hiding, because more warps are available to execute while others wait for memory. However, performance often saturates beyond ~50–70% occupancy, as instruction pipelines, memory bandwidth, or scheduler limits become the bottleneck instead. Occupancy is limited by three resources per SM:

- **Registers** — each thread consumes registers; more registers per thread means fewer concurrent threads
- **Shared memory** — each block reserves shared memory; larger allocations limit concurrent blocks
- **Block size** — thread blocks are assigned to SMs as whole units

If a kernel uses too many registers or too much shared memory per thread, fewer warps can be active, reducing the SM's ability to hide latency. This is called **register pressure** and is one of the most important GPU performance factors.

### Memory Coalescing

When threads in a warp access global memory, the hardware attempts to **coalesce** individual requests into as few memory transactions as possible:

```
Coalesced (good):                 Uncoalesced (bad):
Thread 0 → A[0]                   Thread 0 → A[7]
Thread 1 → A[1]                   Thread 1 → A[200]
Thread 2 → A[2]                   Thread 2 → A[53]
Thread 3 → A[3]                   Thread 3 → A[1001]
  → one memory transaction          → multiple separate transactions
```

When consecutive threads access consecutive memory addresses, the hardware merges them into a single wide memory transaction. Random or strided access patterns force multiple transactions, dramatically reducing effective bandwidth. This is why memory access patterns are critical for GPU performance.

## GPU Memory Hierarchy

```
Speed                                    Size
  ▲                                        ▲
  │  ┌────────────────┐                    │
  │  │   Registers    │  per thread         │
  │  │                │  (large file: ~256  │
  │  │                │   KB/SM on many     │
  │  │                │   NVIDIA archs)     │
  │  ├────────────────┤                    │
  │  │ Shared Memory  │  programmer-managed │
  │  │ .............. │  ┐ same physical   │
  │  │ L1 Cache       │  ┘ pool (~128–228  │
  │  │                │    KB, configurable)│
  │  ├────────────────┤                    │
  │  │ Constant/      │  ~64 KB (cached,   │
  │  │ Texture Memory │   read-only)       │
  │  ├────────────────┤                    │
  │  │   L2 Cache     │  several MB to     │
  │  │                │  tens of MB        │
  │  ├────────────────┤                    │
  │  │ Global Memory  │  8-80 GB (VRAM)    │
  │  │    (HBM/GDDR)  │                    │
  │  └────────────────┘                    │
  │                                        ▼
```

**Shared memory** and **L1 cache** share the same physical on-chip memory pool but are logically distinct. Shared memory is **programmer-managed** — you explicitly load data into it for cooperative sharing between threads in a block (enabling tiling algorithms and explicit data reuse). L1 cache is **hardware-managed** — it transparently caches global memory accesses. The split between them is configurable per kernel.

**Constant memory** is optimized for broadcast access — when all threads read the same address, a single fetch serves the entire warp. **Texture memory** provides spatial caching optimized for 2D access patterns, used in graphics and some ML workloads. Both are read-only from the kernel's perspective.

### Memory Bandwidth

GPU memory bandwidth vastly exceeds CPU (approximate peak values — actual throughput depends on access patterns):

| Component | Bandwidth |
|-----------|-----------|
| CPU RAM (DDR4/DDR5) | ~50–200 GB/s |
| GPU VRAM (GDDR6) | ~500 GB/s |
| GPU VRAM (HBM2e/HBM3) | ~2000–3000+ GB/s |

This high bandwidth enables GPUs to feed thousands of execution units with data. GPUs hide memory latency by scheduling many warps — when one warp stalls waiting for memory, another warp immediately executes on the same hardware.

### Compute-Bound vs Memory-Bound

Despite their massive arithmetic throughput (10–100+ TFLOPS), most GPU kernels are actually **memory-bound** — performance is limited by how fast data arrives, not by compute speed. A GPU capable of 100 TFLOPS but with only 2 TB/s of memory bandwidth must wait for data much of the time.

This is why memory coalescing, shared memory tiling, and occupancy matter so much — they all work to keep the arithmetic units fed with data. When optimizing GPU code, the first question is always: **is this kernel compute-bound or memory-bound?**

## GPU Computing with Python

GPU computations run in **kernels** — functions launched on the GPU and executed by thousands of parallel threads. Libraries like CuPy and PyTorch abstract kernel launches so you can write GPU code without managing threads directly.

### CUDA via CuPy

```python
import cupy as cp

# Create arrays on GPU
a_gpu = cp.random.rand(10000, 10000)
b_gpu = cp.random.rand(10000, 10000)

# Computation happens on GPU
c_gpu = cp.dot(a_gpu, b_gpu)

# Transfer result back to CPU if needed
c_cpu = cp.asnumpy(c_gpu)
```

### PyTorch GPU Operations

```python
import torch

# Check GPU availability
print(torch.cuda.is_available())  # True if GPU present
print(torch.cuda.device_count())  # Number of GPUs

# Move tensors to GPU
device = torch.device('cuda')
x = torch.randn(1000, 1000, device=device)
y = torch.randn(1000, 1000, device=device)

# Computation on GPU
z = torch.mm(x, y)  # Matrix multiply on GPU
```

### Memory Management

```python
import torch

# GPU memory is limited - monitor usage
print(f"Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
print(f"Cached: {torch.cuda.memory_reserved() / 1e9:.2f} GB")

# Clear cache when needed
torch.cuda.empty_cache()
```

## When to Use GPU

### Good GPU Workloads

| Characteristic | Why GPU Helps |
|---------------|---------------|
| Data parallelism | Same operation on many elements |
| Large data | Amortize transfer overhead |
| Matrix operations | Tensor cores, high memory bandwidth |
| Regular memory access | Coalesced reads/writes |

### Poor GPU Workloads

| Characteristic | Why GPU Struggles |
|---------------|-------------------|
| Sequential logic | Can't parallelize |
| Branching code | Warp divergence |
| Small data | Transfer overhead dominates |
| Irregular memory access | Poor memory coalescing |

## Data Transfer Overhead

Moving data between CPU and GPU is expensive:

```
CPU Memory ←─── PCIe Bus ───→ GPU Memory
           (~32 GB/s PCIe 4, ~64 GB/s PCIe 5)

vs.

GPU Memory ←→ GPU Cores
           (~1000 GB/s)
```

In multi-GPU data center systems, **NVLink** provides a faster GPU-to-GPU interconnect (~600–900 GB/s) that bypasses the PCIe bottleneck, enabling efficient multi-GPU training and inference.

```python
import torch
import time

# Transfer overhead example
data_cpu = torch.randn(10000, 10000)

start = time.perf_counter()
data_gpu = data_cpu.to('cuda')  # CPU → GPU transfer
transfer_time = time.perf_counter() - start

start = time.perf_counter()
result = torch.mm(data_gpu, data_gpu)  # GPU computation
torch.cuda.synchronize()  # Wait for completion
compute_time = time.perf_counter() - start

print(f"Transfer: {transfer_time*1000:.1f} ms")
print(f"Compute:  {compute_time*1000:.1f} ms")
```

### Minimizing Transfers

```python
# Bad: Transfer every iteration
for i in range(100):
    x_gpu = x_cpu.to('cuda')
    y_gpu = process(x_gpu)
    y_cpu = y_gpu.to('cpu')

# Good: Transfer once, compute many times
x_gpu = x_cpu.to('cuda')
for i in range(100):
    x_gpu = process(x_gpu)  # Stay on GPU
y_cpu = x_gpu.to('cpu')  # Transfer once at end
```

## Summary

| Concept | Description |
|---------|-------------|
| **GPU** | Massively parallel processor with thousands of lightweight arithmetic lanes |
| **CUDA Core** | Scalar execution unit for integer and floating-point arithmetic |
| **SM** | Streaming Multiprocessor — group of cores + shared memory + warp schedulers |
| **SIMT** | Single Instruction, Multiple Threads execution model |
| **Warp** | 32 threads executing in lockstep (AMD: wavefront, 64 threads) |
| **Occupancy** | Ratio of active to maximum warps — determines latency hiding ability |
| **Coalescing** | Merging thread memory accesses into fewer transactions |
| **VRAM** | GPU's dedicated high-bandwidth memory |
| **Tensor Core** | Specialized unit for matrix multiply-accumulate operations |

Key takeaways for Python:

- GPUs excel at data-parallel operations (same operation on many elements)
- Memory transfer between CPU and GPU is a major bottleneck
- Occupancy, memory coalescing, and warp divergence are the key GPU performance factors
- Libraries like CuPy, PyTorch, and TensorFlow abstract GPU programming
- Not all problems benefit from GPU acceleration
- Modern ML workloads are designed around GPU capabilities
