# CPU vs GPU

CPUs and GPUs solve fundamentally different problems. Choosing the right processor for a workload -- or combining both -- is a critical performance decision in scientific computing and machine learning.

## Definition

A **CPU** is a latency-optimized processor with a few powerful cores (4-128), large caches, branch prediction, and out-of-order execution. It minimizes the time to complete a single complex task.

A **GPU** is a throughput-optimized processor with thousands of simple cores organized into streaming multiprocessors (SMs). It maximizes total work per second on data-parallel operations by executing threads in groups called **warps** (32 threads) under the SIMT model.

## Explanation

| Feature | CPU | GPU |
|---------|-----|-----|
| Cores | 4-128, complex | Thousands, simple |
| Clock speed | 3-5 GHz | 1-2 GHz |
| Memory bandwidth | ~50-200 GB/s | ~500 GB/s - several TB/s |
| Peak FLOPS | ~1 TFLOPS | ~10-100+ TFLOPS |
| Branching | Excellent (branch prediction) | Poor (warp divergence) |

CPUs hide latency through speculation and per-core complexity. GPUs hide latency by switching between warps -- when one warp stalls on memory, another executes instantly.

The **transfer bottleneck** is the main pitfall. Data must travel between system RAM and GPU VRAM over PCIe (~32 GB/s), which can dominate total time. Effective GPU usage requires keeping data on the GPU across multiple operations.

**Decision rules**: Use the CPU for small data, complex branching, or irregular memory access. Use the GPU for large data-parallel operations (matrix math, convolutions, batch processing). Profile when uncertain.

## Examples

```python
import numpy as np
import time

# CPU: NumPy matrix multiply (uses multi-threaded BLAS)
n = 2048
a = np.random.rand(n, n)
b = np.random.rand(n, n)
start = time.perf_counter()
c = a @ b
print(f"CPU: {time.perf_counter() - start:.3f}s")
```

```python
import torch

# GPU: PyTorch matrix multiply (requires CUDA GPU)
n = 2048
a = torch.randn(n, n, device='cuda')
b = torch.randn(n, n, device='cuda')
torch.cuda.synchronize()
start = time.perf_counter()
c = torch.mm(a, b)
torch.cuda.synchronize()
print(f"GPU: {time.perf_counter() - start:.4f}s")
```

```python
import torch

# Amortize transfer cost: keep data on GPU across iterations
data_gpu = data.to('cuda')           # transfer once
for epoch in range(100):
    data_gpu = train_step(data_gpu)  # stays on GPU
result = data_gpu.to('cpu')          # transfer once
```
