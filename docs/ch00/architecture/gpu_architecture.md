# GPU Architecture

GPUs are massively parallel processors that power machine learning, scientific computing, and data processing. Understanding their architecture explains when and why GPU acceleration produces dramatic speedups.

## Definition

A **GPU (Graphics Processing Unit)** is a throughput-optimized processor containing many **Streaming Multiprocessors (SMs)**, each holding dozens to hundreds of simple arithmetic lanes called CUDA cores. GPUs execute under the **SIMT** (Single Instruction, Multiple Threads) model, where 32 threads form a **warp** that executes in lockstep.

## Explanation

Each SM contains CUDA cores (scalar ALUs), shared memory, warp schedulers, load/store units, and special function units. Modern GPUs also include **tensor cores** for fused matrix multiply-accumulate operations critical to deep learning.

**Latency hiding**: Unlike CPUs that use caches and out-of-order execution, GPUs hide memory latency (~400-800 cycles) by switching between many warps. When one warp stalls on memory, the scheduler instantly issues instructions from another ready warp with near-zero overhead, since each warp's registers are permanently allocated.

**Memory coalescing**: When consecutive threads access consecutive addresses, the hardware merges requests into a single wide transaction. Random access patterns force multiple separate transactions and dramatically reduce bandwidth.

**Key performance factors**:

| Factor | Impact |
|--------|--------|
| **Occupancy** | More active warps = better latency hiding |
| **Coalescing** | Consecutive access patterns maximize bandwidth |
| **Warp divergence** | Branching within a warp serializes execution |
| **Transfer overhead** | CPU-GPU data movement over PCIe (~32 GB/s) can dominate runtime |

The GPU memory hierarchy (fastest to slowest): registers, shared memory/L1 cache (same physical pool), L2 cache, global memory (VRAM, 8-80 GB at ~500-3000+ GB/s).

## Examples

```python
import cupy as cp

# CuPy: NumPy-compatible GPU arrays
a = cp.random.rand(10000, 10000)
b = cp.random.rand(10000, 10000)
c = cp.dot(a, b)           # runs on GPU
c_cpu = cp.asnumpy(c)      # transfer result to CPU
```

```python
import torch

# PyTorch: explicit device placement
device = torch.device('cuda')
x = torch.randn(4096, 4096, device=device)
y = torch.randn(4096, 4096, device=device)
z = torch.mm(x, y)  # matrix multiply on GPU

# Monitor GPU memory
print(f"Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
```

```python
import torch

# Minimize transfers: keep data on GPU across iterations
x_gpu = x_cpu.to('cuda')          # transfer once
for i in range(100):
    x_gpu = process(x_gpu)        # stays on GPU
result = x_gpu.to('cpu')          # transfer once at end
```
