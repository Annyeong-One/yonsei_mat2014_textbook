

# GPU Architecture

Graphics Processing Units (GPUs) are specialized processors designed to execute **massively parallel workloads**.

They power many modern computational tasks including:

* deep learning
* scientific simulations
* computer graphics
* large-scale numerical computation

While CPUs prioritize **low latency for individual threads**, GPUs prioritize **high throughput across thousands of threads**.

Instead of executing a few complex threads quickly, GPUs execute **many lightweight threads simultaneously**.

This design is particularly effective for workloads exhibiting **data parallelism**, where the same operation must be applied to many elements.

---

## 1. CPU vs GPU Design Philosophy

CPUs and GPUs are built with fundamentally different architectural goals.

---

## CPU

CPUs optimize:

* low-latency execution
* complex control flow
* sequential performance

Typical features include:

* few powerful cores
* large caches
* complex out-of-order execution

---

## GPU

GPUs optimize:

* extremely high throughput
* massive thread-level parallelism
* predictable memory access patterns

Typical features include:

* thousands of simple cores
* small caches
* simple in-order execution
* hardware thread scheduling

---

### CPU vs GPU architecture

```mermaid
flowchart LR
    subgraph CPU["CPU: Few Complex Cores"]
        C1[Core]
        C2[Core]
        C3[Core]
        C4[Core]
    end

    subgraph GPU["GPU: Many Simple Cores"]
        G1[Core]
        G2[Core]
        G3[Core]
        G4[Core]
        G5[Core]
        G6[Core]
        G7[Core]
        G8[Core]
    end
```

---

## Comparison

| Property        | CPU             | GPU              |
| --------------- | --------------- | ---------------- |
| Cores           | few (4–64)      | thousands        |
| Core complexity | high            | simple           |
| Execution model | out-of-order    | mostly in-order  |
| Optimization    | latency         | throughput       |
| Best workloads  | branching logic | data parallelism |

---

## 2. System Architecture

GPUs operate as **accelerators attached to a CPU system**.

The CPU orchestrates execution while the GPU performs large parallel computations.

---

### System overview

```mermaid
flowchart LR
    RAM[System RAM]
    CPU[CPU]
    BUS[PCIe / NVLink]
    GPU[GPU]
    VRAM[GPU Memory]

    RAM <--> CPU
    CPU <--> BUS
    BUS <--> GPU
    GPU <--> VRAM
```

Execution flow:

1. CPU loads data into system RAM
2. Data is copied to GPU memory
3. CPU launches a **GPU kernel**
4. GPU executes parallel computation
5. Results may be copied back to CPU

Thus the conceptual model is:

```
CPU = controller
GPU = accelerator
```

---

## 3. Kernel Execution Model

GPU programs run functions called **kernels**.

A kernel executes **many parallel threads** organized in a hierarchical structure.

---

### Execution hierarchy

```mermaid
flowchart TD
    Kernel --> Grid
    Grid --> Block1[Thread Block]
    Grid --> Block2[Thread Block]
    Grid --> Block3[Thread Block]

    Block1 --> WarpA
    Block1 --> WarpB

    WarpA --> ThreadsA[32 Threads]
    WarpB --> ThreadsB[32 Threads]
```

Hierarchy:

```
Kernel
 └ Grid
     └ Thread Blocks
         └ Warps
             └ Threads
```

Key rules:

* **Thread blocks execute on a single SM**
* **Threads in a block share memory**
* **Warps are the hardware scheduling unit**

---

## 4. Streaming Multiprocessors (SM)

The fundamental compute unit of a GPU is the **Streaming Multiprocessor (SM)**.

A GPU contains many SMs that operate independently.

---

### SM architecture

```mermaid
flowchart TB
    SM[Streaming Multiprocessor]

    SM --> WS0[Warp Scheduler]
    SM --> WS1[Warp Scheduler]

    SM --> ALU[CUDA Cores]
    SM --> LSU[Load/Store Units]
    SM --> SFU[Special Function Units]
    SM --> TC[Tensor Cores]

    SM --> RF[Register File]
    SM --> SHMEM[Shared Memory / L1]
```

An SM manages many active threads simultaneously.

Typical hardware inside an SM:

* warp schedulers
* CUDA cores (scalar ALUs)
* tensor cores
* load/store units
* register file
* shared memory

---

## 5. Warps and SIMT Execution

GPU threads execute in groups called **warps**.

A warp contains:

```
32 threads
```

Warps execute using the **SIMT (Single Instruction Multiple Threads)** model.

All threads execute the same instruction but operate on different data.

---

### SIMT model

```mermaid
flowchart TD
    Warp --> Instruction
    Instruction --> Thread1
    Instruction --> Thread2
    Instruction --> Thread3
```

Each thread maintains its own:

* registers
* memory addresses
* control state

---

## 6. Warp Divergence

Problems occur when threads within a warp follow different branches.

Example:

```
if condition:
    path_A
else:
    path_B
```

When divergence occurs, the warp must execute both paths sequentially.

---

### Warp divergence

```mermaid
flowchart TD
    Warp --> Branch

    Branch --> PathA
    Branch --> PathB

    PathA --> Reconverge
    PathB --> Reconverge
```

This reduces effective parallelism.

Thus GPUs perform best when threads follow **similar execution paths**.

---

## 7. Latency Hiding Through Concurrency

GPU memory accesses may take **hundreds of cycles**.

Instead of relying on large caches, GPUs hide latency by switching between warps.

---

### Warp scheduling

```mermaid
flowchart LR
    Warp1[Warp waiting for memory]
    Warp2[Ready warp]
    Warp3[Ready warp]

    Scheduler --> Warp2
    Scheduler --> Warp3
```

If one warp stalls on memory, another warp immediately runs.

This switching occurs with **zero context switch cost**.

---

## Occupancy

The number of active warps on an SM is called **occupancy**.

High occupancy allows the GPU to hide memory latency effectively.

Occupancy depends on:

* registers per thread
* shared memory usage
* threads per block

---

## 8. GPU Memory Hierarchy

GPUs use a memory hierarchy similar to CPUs but optimized for throughput.

---

### GPU memory hierarchy

```mermaid
flowchart TB
    Registers --> Shared
    Shared --> L2
    L2 --> Global
    Global --> Host
```

---

## Memory types

| Memory        | Scope      | Latency         |
| ------------- | ---------- | --------------- |
| Registers     | per thread | ~1 cycle        |
| Shared memory | per block  | ~20–30 cycles   |
| L2 cache      | whole GPU  | ~200 cycles     |
| Global memory | VRAM       | ~400–800 cycles |

Additional specialized memory types include:

* constant memory
* texture memory
* local memory

---

## 9. Memory Coalescing

GPU memory bandwidth is maximized when threads in a warp access **contiguous addresses**.

---

### Coalesced access

```mermaid
flowchart LR
    T1 --> Addr0
    T2 --> Addr1
    T3 --> Addr2
    T4 --> Addr3
```

These accesses combine into a **single memory transaction**.

---

### Uncoalesced access

```mermaid
flowchart LR
    T1 --> Addr100
    T2 --> Addr3
    T3 --> Addr900
```

This requires multiple memory transactions and reduces performance.

---

## 10. Tensor Cores

Modern GPUs contain **tensor cores**, specialized units designed for matrix multiplication.

They perform the fused operation:

[
D = A \times B + C
]

in a single instruction.

---

### Tensor core operation

```mermaid
flowchart LR
    A[Matrix Tile A] --> TC[Tensor Core]
    B[Matrix Tile B] --> TC
    TC --> C[Result Tile]
```

Tensor cores dramatically accelerate deep learning workloads.

---

## 11. Tiling for High Performance

GPU kernels often use **tiling** to reduce global memory access.

Instead of repeatedly reading data from global memory, blocks load tiles into shared memory.

---

### Tiling strategy

```mermaid
flowchart LR
    GlobalMemory --> TileA
    GlobalMemory --> TileB

    TileA --> SharedMemory
    TileB --> SharedMemory

    SharedMemory --> Threads
```

This allows many threads to reuse the same data.

---

## 12. Arithmetic Intensity and the Roofline Model

GPU performance depends on **arithmetic intensity**:

$$
\text{Arithmetic Intensity}
===========================
\frac{\text{FLOPs}}{\text{bytes transferred}}
$$

Programs with:

* low arithmetic intensity → **memory bound**
* high arithmetic intensity → **compute bound**

---

### Roofline model

```
Performance
(FLOPS)
      │
      │           ________  compute limit
      │          /
      │         /
      │        /
      │_______/
      │
      └────────────────
       arithmetic intensity
```

The goal of GPU optimization is to increase **data reuse**, pushing kernels toward the compute limit.

---

## 13. Why GPUs Excel at Deep Learning

Neural networks rely heavily on:

* matrix multiplication
* convolution
* large batch processing

These operations exhibit:

* massive data parallelism
* high arithmetic intensity

Thus GPU hardware matches deep learning workloads extremely well.

---

## 14. Example GPU Usage

### CuPy example

```python
import cupy as cp

a = cp.random.rand(10000,10000)
b = cp.random.rand(10000,10000)

c = cp.dot(a,b)
```

The computation executes entirely on the GPU.

---

### PyTorch example

```python
import torch

device = torch.device("cuda")

x = torch.randn(4096,4096,device=device)
y = torch.randn(4096,4096,device=device)

z = torch.mm(x,y)
```

---

## 15. Key GPU Optimization Principles

GPU performance depends on several factors.

---

| Factor               | Impact                             |
| -------------------- | ---------------------------------- |
| Occupancy            | more active warps hide latency     |
| Memory coalescing    | maximizes bandwidth                |
| Warp divergence      | reduces parallel efficiency        |
| Arithmetic intensity | determines compute vs memory bound |
| CPU-GPU transfers    | may dominate runtime               |

---

## 16. Summary

| Concept           | Explanation                            |
| ----------------- | -------------------------------------- |
| GPU               | massively parallel processor           |
| SM                | primary compute unit                   |
| Kernel            | function executed on GPU               |
| Warp              | 32-thread execution group              |
| SIMT              | single instruction across many threads |
| Occupancy         | number of active warps                 |
| Memory coalescing | contiguous memory access               |
| Tensor cores      | specialized matrix units               |
| Roofline model    | compute vs memory limits               |

GPUs achieve extraordinary performance by combining:

* thousands of lightweight threads
* massive parallel execution
* high memory bandwidth
* latency hiding through concurrency

These architectural principles explain why GPUs excel at **deep learning, scientific computing, and large-scale numerical workloads**.
