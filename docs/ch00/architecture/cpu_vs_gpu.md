# CPU vs GPU

## Fundamental Design Differences

CPUs and GPUs are optimized for different types of workloads:

```
CPU: Few powerful cores              GPU: Many simple cores
┌─────────────────────────┐          ┌─────────────────────────────┐
│  ┌─────────────────┐    │          │ ┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐   │
│  │    Complex      │    │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │     Core        │    │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │  ┌───────────┐  │    │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │  │ Large     │  │    │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │  │ Cache     │  │    │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │  └───────────┘  │    │          │ ├─┤├─┤├─┤├─┤├─┤├─┤├─┤├─┤   │
│  │  Branch Pred.   │    │          │ └─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘   │
│  │  Out-of-Order   │    │          │   Streaming multiprocessors  │
│  └─────────────────┘    │          │    (many ALUs per SM)     │
│         × 4-16          │          │                             │
└─────────────────────────┘          └─────────────────────────────┘
   Latency-optimized                    Throughput-optimized
```

## Architecture Comparison

| Feature | CPU | GPU |
|---------|-----|-----|
| **Processing Units** | 4-128+ cores | Dozens to hundreds of SMs, each with many ALUs |
| **Clock Speed** | 3-5 GHz | 1-2 GHz (lower because GPUs rely on parallelism, not frequency) |
| **Cache** | Large per-core caches (MB) | Smaller per-SM caches (KB), larger shared L2 (tens of MB) |
| **Branch Prediction** | Sophisticated | Minimal |
| **Out-of-Order Execution** | Yes (general-purpose) | Limited / specialized scheduling (warp-level) |
| **Memory Bandwidth** | ~50–200 GB/s | ~500 GB/s – several TB/s (GDDR6 vs HBM) |
| **Peak FLOPS** | ~1 TFLOPS | ~10–100+ TFLOPS (depends on precision: FP32, FP16, tensor cores) |
| **Power** | 65-125W | 200-700W (consumer to data center) |

## Latency vs Throughput

CPUs hide latency using speculation and complex control logic. GPUs use a different strategy: they execute threads in groups called **warps** (typically 32 threads) using the **SIMT** (Single Instruction, Multiple Threads) model. When one warp stalls waiting for memory, the warp scheduler switches to another ready warp, hiding latency through massive thread-level parallelism rather than per-thread complexity. However, if threads within a warp take different branches, execution becomes serialized (**warp divergence**), reducing parallel efficiency — this is why GPUs perform poorly on branch-heavy code.

### CPU: Latency-Optimized

The CPU minimizes time to complete a single task:

```
CPU: Fast completion of individual tasks

Task 1: [████████]────────────────────────▶ Done!
                                            (10 ms)

Features that reduce latency:
  - Large caches (data ready when needed)
  - Branch prediction (guess correctly, don't stall)
  - Out-of-order execution (do useful work while waiting)
```

### GPU: Throughput-Optimized

The GPU maximizes total work completed per second:

```
GPU: Many tasks completed together

Task 1:    [████████████████████████████████]
Task 2:    [████████████████████████████████]
Task 3:    [████████████████████████████████]
   ...              ...
Task 1000: [████████████████████████████████]
                                            ▶ All done!
                                              (50 ms total)
                                              (0.05 ms each)
```

## When to Use CPU

### Sequential/Branching Code

```python
# Heavy branching - CPU excels
def complex_logic(data):
    result = []
    for item in data:
        if item.type == 'A':
            if item.value > threshold:
                result.append(process_a_high(item))
            else:
                result.append(process_a_low(item))
        elif item.type == 'B':
            result.append(process_b(item))
        else:
            result.append(default_process(item))
    return result
```

### Small Data

```python
# Small data - transfer overhead dominates on GPU
small_array = np.random.rand(100)

# CPU is faster - no transfer needed
result = np.sum(small_array)
```

### Irregular Memory Access

```python
# Random access patterns - CPU caches help
def sparse_lookup(indices, values):
    return [values[i] for i in indices]  # Random access
```

### Single-Threaded Performance

```python
# Complex single computation
def recursive_algorithm(n):
    if n <= 1:
        return n
    return recursive_algorithm(n-1) + recursive_algorithm(n-2)
```

## When to Use GPU

### Data-Parallel Operations

```python
import torch

# Same operation on millions of elements - GPU excels
a = torch.randn(10000, 10000, device='cuda')
b = torch.randn(10000, 10000, device='cuda')
c = a + b  # 100 million parallel additions
```

### Matrix Operations

```python
# Matrix multiply - perfect for GPU
x = torch.randn(4096, 4096, device='cuda')
y = torch.randn(4096, 4096, device='cuda')
z = torch.mm(x, y)  # ~137 billion operations
```

### Deep Learning

```python
# Neural network forward pass - massively parallel
model = model.to('cuda')
for batch in dataloader:
    inputs = batch.to('cuda')
    outputs = model(inputs)  # Parallel across batch and layers
```

### Image/Signal Processing

```python
import cupy as cp

# Convolution across entire image
image = cp.random.rand(1000, 1000)
kernel = cp.random.rand(3, 3)
result = cp.convolve2d(image, kernel)
```

## Performance Comparison

### Benchmark: Vector Addition

```python
import numpy as np
import cupy as cp
import time

sizes = [1000, 10000, 100000, 1000000, 10000000]

for n in sizes:
    # CPU
    a_cpu = np.random.rand(n)
    b_cpu = np.random.rand(n)
    start = time.perf_counter()
    c_cpu = a_cpu + b_cpu
    cpu_time = time.perf_counter() - start
    
    # GPU
    a_gpu = cp.random.rand(n)
    b_gpu = cp.random.rand(n)
    cp.cuda.Stream.null.synchronize()
    start = time.perf_counter()
    c_gpu = a_gpu + b_gpu
    cp.cuda.Stream.null.synchronize()
    gpu_time = time.perf_counter() - start
    
    print(f"n={n:>10}: CPU={cpu_time*1000:>8.3f}ms, GPU={gpu_time*1000:>8.3f}ms")
```

Typical results (compute time only, excluding CPU–GPU transfer). Note that vector addition is **memory-bandwidth bound** — the GPU advantage comes from higher memory bandwidth, not from compute power, so results vary by hardware. On CPUs with very high memory bandwidth or multi-threaded NumPy, the crossover point may occur at larger sizes:

```
n=     1,000: CPU=   0.010ms, GPU=   0.150ms  ← CPU faster (overhead)
n=    10,000: CPU=   0.050ms, GPU=   0.160ms  ← CPU faster
n=   100,000: CPU=   0.400ms, GPU=   0.180ms  ← Crossover point
n= 1,000,000: CPU=   4.000ms, GPU=   0.250ms  ← GPU faster
n=10,000,000: CPU=  40.000ms, GPU=   1.500ms  ← GPU much faster
```

### Benchmark: Matrix Multiplication

```python
import torch
import time

def benchmark_matmul(n):
    # CPU
    a_cpu = torch.randn(n, n)
    b_cpu = torch.randn(n, n)
    start = time.perf_counter()
    c_cpu = torch.mm(a_cpu, b_cpu)
    cpu_time = time.perf_counter() - start
    
    # GPU
    a_gpu = torch.randn(n, n, device='cuda')
    b_gpu = torch.randn(n, n, device='cuda')
    torch.cuda.synchronize()
    start = time.perf_counter()
    c_gpu = torch.mm(a_gpu, b_gpu)
    torch.cuda.synchronize()
    gpu_time = time.perf_counter() - start
    
    speedup = cpu_time / gpu_time
    print(f"n={n}: CPU={cpu_time:.3f}s, GPU={gpu_time:.4f}s, Speedup={speedup:.1f}x")

for n in [512, 1024, 2048, 4096]:
    benchmark_matmul(n)
```

Typical results (speedups vary widely depending on CPU BLAS library and GPU model; MKL/OpenBLAS with AVX-512 significantly narrows the gap):

```
n=512:  CPU=0.015s, GPU=0.0003s, Speedup=~50x
n=1024: CPU=0.100s, GPU=0.0008s, Speedup=~125x
n=2048: CPU=0.750s, GPU=0.0040s, Speedup=~5–50x (varies by CPU BLAS)
n=4096: CPU=6.000s, GPU=0.0250s, Speedup=~10–50x (varies by CPU BLAS)
```

Note: With optimized multi-threaded BLAS (MKL, OpenBLAS), CPU performance for large matrices improves dramatically, and realistic speedups are typically in the **5–50x** range rather than 100x+.

## The Transfer Bottleneck

Data must travel between system RAM and GPU VRAM. The CPU orchestrates the transfer, but a DMA (Direct Memory Access) engine performs the actual copy — the CPU does not move bytes through its own registers:

```
CPU (control)
 │
 ▼
System RAM ←──── PCIe 4.0 ────→ GPU VRAM
               (~32 GB/s max)

This transfer can dominate total time!
```

```python
import torch
import time

n = 10000

# Create on CPU
data = torch.randn(n, n)

# Time the transfer
start = time.perf_counter()
data_gpu = data.to('cuda')
torch.cuda.synchronize()
transfer_time = time.perf_counter() - start

# Time the computation
start = time.perf_counter()
result = torch.mm(data_gpu, data_gpu)
torch.cuda.synchronize()
compute_time = time.perf_counter() - start

print(f"Transfer: {transfer_time*1000:.1f} ms")
print(f"Compute:  {compute_time*1000:.1f} ms")
# Often: Transfer: 100ms, Compute: 25ms → Transfer dominates!
```

### Amortizing Transfer Cost

```python
# Bad: Transfer every iteration
for epoch in range(100):
    data_gpu = data.to('cuda')      # Transfer 100x
    result = train_step(data_gpu)
    data = result.to('cpu')         # Transfer 100x

# Good: Keep data on GPU
data_gpu = data.to('cuda')          # Transfer 1x
for epoch in range(100):
    data_gpu = train_step(data_gpu) # Stays on GPU
result = data_gpu.to('cpu')         # Transfer 1x
```

## Hybrid CPU-GPU Computation

Real applications often use both:

```
┌─────────────────────────────────────────────────────────────┐
│                    Hybrid Workflow                          │
│                                                             │
│  CPU                              GPU                       │
│  ┌─────────────────┐             ┌─────────────────┐       │
│  │ Data loading    │────────────▶│ Neural network  │       │
│  │ Preprocessing   │             │ Matrix ops      │       │
│  │ Control flow    │◀────────────│ Convolutions    │       │
│  │ I/O operations  │             │ Batch processing│       │
│  └─────────────────┘             └─────────────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```python
import torch
from torch.utils.data import DataLoader

# CPU: Data loading and preprocessing
dataloader = DataLoader(dataset, num_workers=4)  # CPU workers

# GPU: Model computation
model = model.to('cuda')

for batch in dataloader:  # CPU loads and preprocesses
    inputs, targets = batch
    inputs, targets = inputs.to('cuda'), targets.to('cuda')
    outputs = model(inputs)         # GPU computation
    loss = criterion(outputs, targets)
    loss.backward()                 # GPU backward pass
```

## Decision Framework

```
                    Start
                      │
                      ▼
         ┌───────────────────────┐
         │  Is data large enough  │
         │  to amortize GPU      │
         │  launch and transfer? │
         └───────────────────────┘
                 │         │
                Yes        No
                 │         │
                 ▼         ▼
    ┌─────────────────┐   Use CPU
    │ Is operation    │
    │ data-parallel?  │
    └─────────────────┘
         │         │
        Yes        No
         │         │
         ▼         ▼
    ┌─────────────────┐   Use CPU
    │ Will data stay  │
    │ on GPU for      │
    │ multiple ops?   │
    └─────────────────┘
         │         │
        Yes        No
         │         │
         ▼         ▼
      Use GPU   Consider both
                (profile first)
```

## Summary

| Aspect | CPU | GPU |
|--------|-----|-----|
| **Best for** | Sequential, branching, irregular | Parallel, regular, matrix ops |
| **Data size** | Small to medium | Large |
| **Latency** | Low | Higher (but amortized) |
| **Throughput** | Lower | Much higher |
| **Memory** | System RAM (large) | VRAM (limited) |
| **Transfer** | N/A | Major consideration |

Rules of thumb:

1. **Small data or complex logic** → CPU
2. **Large data, same operation** → GPU
3. **Frequent CPU-GPU transfers** → Reconsider architecture
4. **Deep learning** → GPU (architectures designed for it)
5. **When in doubt** → Profile both
