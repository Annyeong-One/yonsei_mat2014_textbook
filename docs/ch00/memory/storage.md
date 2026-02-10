# Storage (SSD/HDD)

## Storage vs Memory

**Storage** (SSD/HDD) differs fundamentally from RAM:

| Property | RAM | Storage |
|----------|-----|---------|
| **Persistence** | Volatile (lost on power off) | Non-volatile (survives power off) |
| **Latency** | ~60 ns | ~100 μs (SSD) to ~10 ms (HDD) |
| **Bandwidth** | ~50 GB/s | ~500 MB/s to ~5 GB/s |
| **Cost/GB** | ~$3-5 | ~$0.05-0.20 |
| **Capacity** | 8-128 GB | 256 GB - 20 TB |

## Hard Disk Drives (HDD)

Traditional spinning magnetic disks:

```
HDD Physical Structure

        ┌───────────────────────┐
        │     Spinning Platter   │
        │    ┌───────────────┐  │
        │    │               │  │
        │    │   Magnetic    │◀─┼── Read/Write Head
        │    │   Surface     │  │   (moves in/out)
        │    │               │  │
        │    └───────────────┘  │
        │         ↻             │  ← Rotates 5400-7200 RPM
        └───────────────────────┘
```

### HDD Latency Components

```
Total HDD Access Time
= Seek Time + Rotational Latency + Transfer Time

Seek Time:        ~5-10 ms   (move head to track)
Rotational Delay: ~4-8 ms    (wait for sector to rotate under head)
Transfer:         ~0.1 ms    (read the data)
─────────────────────────────
Total:            ~10-20 ms  (per random access!)
```

### HDD Performance

| Metric | Value |
|--------|-------|
| **Sequential Read** | 100-200 MB/s |
| **Random Read** | 0.5-2 MB/s (IOPS limited) |
| **Random IOPS** | 50-200 |
| **Latency** | 5-15 ms |

HDDs excel at sequential access but struggle with random access.

## Solid State Drives (SSD)

No moving parts—uses flash memory:

```
SSD Architecture

┌─────────────────────────────────────────────────────┐
│                    SSD Controller                   │
│  ┌─────────────────────────────────────────────┐   │
│  │           DRAM Cache (1-4 GB)               │   │
│  └─────────────────────────────────────────────┘   │
│                        │                            │
│  ┌──────────────────────────────────────────────┐  │
│  │              Flash Translation Layer          │  │
│  └──────────────────────────────────────────────┘  │
│         │         │         │         │            │
│     ┌───┴───┐ ┌───┴───┐ ┌───┴───┐ ┌───┴───┐      │
│     │ NAND  │ │ NAND  │ │ NAND  │ │ NAND  │      │
│     │ Chip  │ │ Chip  │ │ Chip  │ │ Chip  │      │
│     └───────┘ └───────┘ └───────┘ └───────┘      │
│              (Multiple channels)                   │
└─────────────────────────────────────────────────────┘
```

### SSD Performance

| Metric | SATA SSD | NVMe SSD |
|--------|----------|----------|
| **Sequential Read** | 500-550 MB/s | 3,000-7,000 MB/s |
| **Sequential Write** | 400-520 MB/s | 2,000-5,000 MB/s |
| **Random Read IOPS** | 90,000 | 500,000-1,000,000 |
| **Latency** | 50-100 μs | 10-20 μs |

### SATA vs NVMe

```
SATA Interface (legacy)
┌─────┐                    ┌─────┐
│ CPU │──── SATA ────────▶│ SSD │
└─────┘    (~600 MB/s max) └─────┘

NVMe Interface (modern)
┌─────┐                    ┌─────┐
│ CPU │──── PCIe ────────▶│ SSD │
└─────┘    (~7 GB/s+)      └─────┘
```

## Storage Latency in Perspective

```
CPU cycle (4 GHz):           0.25 ns     │
L1 Cache:                    1 ns        │ CPU time scale
L2 Cache:                    3 ns        │
L3 Cache:                    10 ns       │
────────────────────────────────────────────
RAM:                         60 ns       │
────────────────────────────────────────────
NVMe SSD:                    10,000 ns   │
SATA SSD:                    100,000 ns  │ Storage time scale
HDD:                         10,000,000 ns │

One HDD access = 40 million CPU cycles!
```

## Python File I/O

### Basic File Operations

```python
import time

# Writing
start = time.perf_counter()
with open('test.bin', 'wb') as f:
    f.write(b'\x00' * 100_000_000)  # 100 MB
print(f"Write: {time.perf_counter() - start:.2f} s")

# Reading
start = time.perf_counter()
with open('test.bin', 'rb') as f:
    data = f.read()
print(f"Read: {time.perf_counter() - start:.2f} s")
```

### Buffered vs Unbuffered I/O

Python uses buffered I/O by default:

```python
# Buffered (default) - batches small writes
with open('file.txt', 'w') as f:
    for i in range(10000):
        f.write('line\n')  # Batched in memory buffer

# Unbuffered - each write goes to disk
with open('file.txt', 'w', buffering=0) as f:  # Only for binary
    # Would be very slow for many small writes
    pass
```

### Memory-Mapped Files

Access files as if they were memory:

```python
import mmap
import numpy as np

# Memory-map for random access
with open('data.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    # Random access without reading entire file
    value = mm[1000000:1000008]  # Read 8 bytes at offset 1M
    mm.close()

# NumPy memmap
arr = np.memmap('array.dat', dtype='float64', mode='r', 
                shape=(1000000,))
# Access elements without loading entire array
print(arr[500000])
```

## Storage for Data Science

### Loading Large Datasets

```python
import pandas as pd
import time

# CSV (text, slow to parse)
start = time.perf_counter()
df = pd.read_csv('large_data.csv')
print(f"CSV: {time.perf_counter() - start:.1f} s")

# Parquet (binary, columnar, fast)
start = time.perf_counter()
df = pd.read_parquet('large_data.parquet')
print(f"Parquet: {time.perf_counter() - start:.1f} s")

# Typically Parquet is 5-10x faster
```

### File Format Comparison

| Format | Read Speed | Write Speed | Compression | Random Access |
|--------|------------|-------------|-------------|---------------|
| **CSV** | Slow | Medium | None | No |
| **Parquet** | Fast | Medium | Good | Yes (by column) |
| **HDF5** | Fast | Fast | Optional | Yes |
| **Pickle** | Fast | Fast | None | No |
| **NumPy .npy** | Very Fast | Very Fast | None | No |

### Chunked Reading

For datasets larger than RAM:

```python
import pandas as pd

# Process in chunks
total_rows = 0
for chunk in pd.read_csv('huge.csv', chunksize=100000):
    total_rows += len(chunk)
    # Process chunk...
print(f"Total rows: {total_rows}")
```

## SSD Write Considerations

### Write Amplification

SSDs can only erase in large blocks. Writing small amounts causes extra work:

```
Write 4 KB to SSD:
1. Read entire 256 KB block
2. Modify 4 KB within block
3. Erase entire block
4. Write entire 256 KB back

Write amplification = 256/4 = 64x!
```

### SSD Endurance

Flash cells wear out after many writes:

| SSD Type | Writes per Cell | Typical Endurance |
|----------|-----------------|-------------------|
| SLC | 100,000 | Very High |
| MLC | 10,000 | High |
| TLC | 3,000 | Medium |
| QLC | 1,000 | Lower |

For data science:

- Reading is essentially unlimited
- Heavy write workloads (temp files, checkpoints) accumulate wear
- Enterprise SSDs have higher endurance

## Practical Guidelines

### When to Use Each Storage Type

```
Use HDD:
- Archival/backup
- Sequential access workloads
- Maximum capacity per dollar

Use SATA SSD:
- General purpose
- Boot drive
- Application storage

Use NVMe SSD:
- Data science workloads
- Database storage
- Maximum performance
```

### Optimizing Storage Access

```python
# Bad: Many small random reads
for i in random_indices:
    with open('data.bin', 'rb') as f:
        f.seek(i * 8)
        value = f.read(8)

# Good: Batch reads, sequential when possible
with open('data.bin', 'rb') as f:
    data = f.read()  # Read all at once
values = [data[i*8:(i+1)*8] for i in random_indices]

# Best: Use memory-mapped files for random access
arr = np.memmap('data.bin', dtype='float64', mode='r')
values = arr[random_indices]
```

## Summary

| Storage Type | Latency | Seq. Bandwidth | Best For |
|--------------|---------|----------------|----------|
| **HDD** | 10 ms | 150 MB/s | Archival, bulk storage |
| **SATA SSD** | 100 μs | 500 MB/s | General purpose |
| **NVMe SSD** | 20 μs | 5,000 MB/s | Performance workloads |

Key points for Python:

- Storage is 1000-100,000x slower than RAM
- Use appropriate file formats (Parquet > CSV)
- Memory-map files for random access patterns
- Buffer writes to avoid many small operations
- NVMe SSDs dramatically improve data loading times
- Keep working datasets in RAM when possible
