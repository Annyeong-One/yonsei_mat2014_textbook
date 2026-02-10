# GPU Architecture

## What is a GPU?

A **Graphics Processing Unit (GPU)** is a specialized processor designed for parallel computation. Originally built for rendering graphics, GPUs now power machine learning, scientific computing, and data processing.

```
CPU vs GPU: Core Count
┌─────────────────┐          ┌─────────────────────────────┐
│      CPU        │          │            GPU              │
│  ┌───┐ ┌───┐   │          │ ┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐   │
│  │ C │ │ C │   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  └───┘ └───┘   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  ┌───┐ ┌───┐   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │ C │ │ C │   │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  └───┘ └───┘   │          │ └─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘   │
│                │          │      ... thousands ...      │
│   4-16 cores   │          │     thousands of cores      │
│   (complex)    │          │        (simple)             │
└─────────────────┘          └─────────────────────────────┘
```

## GPU vs CPU Design Philosophy

| Aspect | CPU | GPU |
|--------|-----|-----|
| **Cores** | Few (4-64) | Many (thousands) |
| **Core Complexity** | High (out-of-order, branch prediction) | Low (simple, in-order) |
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
│  │  │              Shared Memory (L1)                │ │   │
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
| **CUDA Core** | Basic processing unit (like a simple ALU) |
| **Streaming Multiprocessor (SM)** | Group of CUDA cores + shared memory |
| **Shared Memory** | Fast memory shared within an SM |
| **Global Memory (VRAM)** | Large but slower GPU memory |
| **Tensor Cores** | Specialized units for matrix operations (newer GPUs) |

## The SIMT Execution Model

GPUs use **SIMT** (Single Instruction, Multiple Threads):

```
SIMT: One instruction, many threads execute it

Instruction: ADD

Thread 0:  a[0] + b[0] → c[0]
Thread 1:  a[1] + b[1] → c[1]
Thread 2:  a[2] + b[2] → c[2]
Thread 3:  a[3] + b[3] → c[3]
   ...         ...
Thread N:  a[N] + b[N] → c[N]

All threads execute ADD simultaneously!
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

- **Warp**: 32 threads that execute in lockstep
- **Block**: Group of warps sharing memory
- **Grid**: All blocks for a computation

## GPU Memory Hierarchy

```
Speed                                    Size
  ▲                                        ▲
  │  ┌────────────────┐                    │
  │  │   Registers    │  ~256 KB total     │
  │  ├────────────────┤                    │
  │  │ Shared Memory  │  ~100 KB per SM    │
  │  ├────────────────┤                    │
  │  │   L1 Cache     │  ~128 KB per SM    │
  │  ├────────────────┤                    │
  │  │   L2 Cache     │  ~6 MB             │
  │  ├────────────────┤                    │
  │  │ Global Memory  │  8-80 GB (VRAM)    │
  │  │    (HBM/GDDR)  │                    │
  │  └────────────────┘                    │
  │                                        ▼
```

### Memory Bandwidth

GPU memory bandwidth vastly exceeds CPU:

| Component | Bandwidth |
|-----------|-----------|
| CPU RAM (DDR4) | ~50 GB/s |
| GPU VRAM (GDDR6) | ~500 GB/s |
| GPU VRAM (HBM2e) | ~2000 GB/s |

This high bandwidth enables GPUs to feed thousands of cores with data.

## GPU Computing with Python

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

## Tensor Cores

Modern NVIDIA GPUs include **Tensor Cores** for matrix operations:

```
Traditional CUDA Core:
  One multiply-add per cycle

Tensor Core:
  4x4 matrix multiply-add per cycle (64 operations!)

┌─────────────────────────────────────────┐
│  A (4×4)  ×  B (4×4)  +  C (4×4)  =  D  │
│                                         │
│  64 multiply-adds in ONE cycle          │
└─────────────────────────────────────────┘
```

Tensor Cores accelerate:

- Deep learning training and inference
- Mixed-precision computation (FP16/BF16)
- Large matrix operations

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
              (~32 GB/s)

vs.

GPU Memory ←→ GPU Cores
           (~1000 GB/s)
```

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
| **GPU** | Massively parallel processor with thousands of cores |
| **CUDA Core** | Simple processing unit in NVIDIA GPUs |
| **SM** | Streaming Multiprocessor - group of cores + shared memory |
| **SIMT** | Single Instruction, Multiple Threads execution model |
| **Warp** | 32 threads executing in lockstep |
| **VRAM** | GPU's dedicated high-bandwidth memory |
| **Tensor Core** | Specialized unit for matrix operations |

Key takeaways for Python:

- GPUs excel at data-parallel operations (same operation on many elements)
- Memory transfer between CPU and GPU is a major bottleneck
- Libraries like CuPy, PyTorch, and TensorFlow abstract GPU programming
- Not all problems benefit from GPU acceleration
- Modern ML workloads are designed around GPU capabilities
