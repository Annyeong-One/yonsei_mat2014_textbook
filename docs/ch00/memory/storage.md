# Storage (SSD/HDD)

## Storage vs Memory

**Storage** (SSD/HDD) differs fundamentally from RAM:

| Property | RAM | Storage |
|----------|-----|---------|
| **Persistence** | Volatile (lost on power off) | Non-volatile (survives power off) |
| **Latency** | ~80-120 ns | ~20-100 μs (NVMe SSD) to ~5-15 ms (HDD) |
| **Bandwidth** | ~20-50 GB/s per channel (dual-channel ≈ 2×) | ~500 MB/s (SATA) to ~7 GB/s (NVMe) |
| **Cost/GB** | ~\$3-5 (prices fluctuate) | ~\$0.05-0.20 (prices fluctuate) |
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
        │         ↻             │  ← Rotates 5400-7200 RPM (consumer)
        │                       │    10,000-15,000 RPM (enterprise)
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
| **Random Read** | 0.5-2 MB/s |
| **Random IOPS** | 50-200 |
| **Latency** | 5-15 ms |

HDDs excel at sequential access but struggle with random access. Random throughput is limited by IOPS: at 100 IOPS with 4 KB reads, throughput is only 100 × 4 KB = 0.4 MB/s — mechanical seek and rotational delay dominate. Larger request sizes (e.g., 16-64 KB) increase throughput per IOP, which is why the table range extends to 2 MB/s.

## Solid State Drives (SSD)

No moving parts—uses flash memory:

```
SSD Architecture

┌─────────────────────────────────────────────────────┐
│                    SSD Controller                   │
│  ┌─────────────────────────────────────────────┐   │
│  │           DRAM Cache (256 MB - 4 GB)        │   │
│  │         (some budget SSDs are DRAM-less)     │   │
│  └─────────────────────────────────────────────┘   │
│                        │                            │
│  ┌──────────────────────────────────────────────┐  │
│  │              Flash Translation Layer (FTL)    │  │
│  │   Maps logical → physical addresses           │  │
│  │   Handles: wear leveling, garbage collection  │  │
│  │            ECC, over-provisioning             │  │
│  └──────────────────────────────────────────────┘  │
│         │         │         │         │            │
│     ┌───┴───┐ ┌───┴───┐ ┌───┴───┐ ┌───┴───┐      │
│     │ NAND  │ │ NAND  │ │ NAND  │ │ NAND  │      │
│     │ Chip  │ │ Chip  │ │ Chip  │ │ Chip  │      │
│     └───────┘ └───────┘ └───────┘ └───────┘      │
│              (Multiple channels)                   │
└─────────────────────────────────────────────────────┘
```

The SSD controller is far more complex than it appears. **Wear leveling** distributes writes evenly across cells to prevent premature failure. **Garbage collection** reclaims blocks containing stale data in the background. **ECC (Error Correcting Code)** detects and corrects bit errors in NAND cells. **Over-provisioning** reserves extra capacity (typically 7-28%) for these background operations.

### SSD Performance

| Metric | SATA SSD | NVMe SSD |
|--------|----------|----------|
| **Sequential Read** | 500-550 MB/s | 3,000-7,000 MB/s |
| **Sequential Write** | 400-520 MB/s | 2,000-5,000 MB/s |
| **Random Read IOPS (peak)** | 90,000 | 500,000-1,000,000 |
| **Device Latency** | 50-100 μs | 10-30 μs |
| **Application Latency** | 80-200 μs | 20-100 μs |

Application-level latency includes the PCIe/SATA stack, OS driver, filesystem overhead, and I/O queueing — all of which add to the raw device latency. Peak IOPS numbers require high queue depths and parallel I/O; single-threaded workloads typically achieve 50K-150K IOPS on NVMe.

### SATA vs NVMe

```
SATA Interface (legacy)
┌─────┐     ┌─────────────────┐     ┌─────┐
│ CPU │────▶│ Chipset (AHCI)  │────▶│ SSD │
└─────┘     └─────────────────┘     └─────┘
             SATA controller
             (~600 MB/s max)

NVMe Interface (modern)
┌─────┐     ┌───────────────┐     ┌─────┐
│ CPU │────▶│ PCIe Root     │────▶│ SSD │
└─────┘     │ Complex       │     └─────┘
            └───────────────┘
             Bandwidth depends on PCIe generation:
             PCIe 3.0 x4: ~3.5 GB/s
             PCIe 4.0 x4: ~7 GB/s
             PCIe 5.0 x4: ~14 GB/s
```

NVMe connects via PCIe lanes, which may go directly to the CPU's root complex or through the chipset depending on the motherboard. The key advantage is that NVMe bypasses the SATA protocol's bottleneck and supports deeper command queues (up to 64K queues vs SATA's single queue).

## Storage in the Memory Hierarchy

Storage sits at the bottom of the memory hierarchy — the slowest but largest and most persistent level:

```
Registers   ~128 B       ~1 cycle       │
L1 Cache    ~32 KB       ~4 cycles      │ CPU (per core)
L2 Cache    ~256 KB      ~12 cycles     │
L3 Cache    ~8-32 MB     ~40 cycles     │ (shared across cores)
────────────────────────────────────────────
RAM         8-128 GB     ~80-120 ns     │ Memory
────────────────────────────────────────────
NVMe SSD    256 GB-4 TB  ~20-100 μs     │
SATA SSD    256 GB-4 TB  ~80-200 μs     │ Storage
HDD         1-20 TB     ~5-15 ms        │

One HDD access ≈ 40 million CPU cycles!
```

The latencies above are **application-level** values, which include OS driver, filesystem, and queueing overhead — not just raw device latency. Raw NVMe device latency can be as low as ~10 μs, but applications rarely see that.

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

!!! warning "OS Page Cache"
    File I/O benchmarks can be misleading. The OS maintains a **page cache** — recently read or written file data kept in RAM. A second `f.read()` of the same file often reads from the page cache (RAM speed), not from disk. To measure true storage speed, you must either clear the OS cache between runs or use files larger than available RAM. Write benchmarks are similarly affected: the OS may accept writes into the page cache and flush to disk asynchronously, making writes appear faster than the actual storage device.

### Buffered vs Unbuffered I/O

Python uses buffered I/O by default. There are actually **two levels of buffering** between your code and the storage device:

```
Python code
    ↓
Python I/O buffer (user-space, controlled by buffering= parameter)
    ↓
OS page cache (kernel-space, always present unless O_DIRECT)
    ↓
Storage device
```

```python
# Buffered (default) - batches small writes in Python's user-space buffer
with open('file.txt', 'w') as f:
    for i in range(10000):
        f.write('line\n')  # Batched in Python's memory buffer

# Unbuffered - bypasses Python's buffer, but still goes through OS page cache
with open('file.bin', 'wb', buffering=0) as f:
    f.write(b'data')  # Each write() call → syscall, but OS may cache in RAM
    # unbuffered mode is only available for binary files
```

Even with `buffering=0`, writes still pass through the OS page cache unless the application uses special flags like `O_DIRECT` (not exposed by Python's built-in `open`). The OS flushes the page cache to disk asynchronously. Use `f.flush()` followed by `os.fsync(f.fileno())` to force data to the storage device.

### Memory-Mapped Files

Access files as if they were memory. When you memory-map a file, the OS maps the file's contents into the process's virtual address space — but does **not** load the file immediately. Data is loaded on demand via **page faults**: when you access a page that is not yet in RAM, the OS pauses execution, loads that page from disk into the page cache, and resumes. Frequently accessed pages stay in RAM for subsequent accesses.

```python
import mmap
import numpy as np

# Memory-map for random access
with open('data.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    # First access to this region triggers a page fault (disk read)
    # Subsequent accesses to the same page hit the page cache (RAM speed)
    value = mm[1000000:1000008]  # Read 8 bytes at offset 1M
    mm.close()

# NumPy memmap
arr = np.memmap('array.dat', dtype='float64', mode='r',
                shape=(1000000,))
# Access elements without loading entire array
print(arr[500000])
```

## Storage for Data Science

File format choice directly affects storage performance. The differences come from two factors: **I/O volume** (how many bytes must be read from disk) and **CPU cost** (how much parsing is needed after reading). Columnar formats like Parquet also enable reading only the needed columns, reducing I/O.

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

For datasets larger than RAM, chunked reading keeps the **working set** small enough to fit in memory. Instead of loading the entire file (which would cause a `MemoryError` or trigger swap), only one chunk is in RAM at a time:

```python
import pandas as pd

# Process in chunks — only one chunk (~100K rows) in RAM at a time
total_rows = 0
for chunk in pd.read_csv('huge.csv', chunksize=100000):
    total_rows += len(chunk)
    # Process chunk, then it can be garbage collected
print(f"Total rows: {total_rows}")
```

## SSD Write Considerations

### Write Amplification

NAND flash has an asymmetry: you can write to individual **pages** (~4-16 KB) but can only erase entire **blocks** (~256 KB - 4 MB). Data cannot be overwritten in place — the old page must eventually be erased as part of a whole block.

The naive approach would require read-modify-write of the entire block (256 KB / 4 KB = 64x amplification). Modern SSD controllers avoid this through **log-structured writes**:

```
How modern SSDs handle writes:

1. Write new data to a fresh page (no erase needed)
2. Mark old page as stale ("invalid")
3. Later, garbage collection reclaims blocks with many stale pages:
   a. Copy valid pages from partially-stale block to a new block
   b. Erase the old block
   c. Add erased block to the free pool

This reduces write amplification dramatically.
```

Real-world write amplification is typically **1.2x-3x**, not the theoretical 64x worst case. The actual ratio depends on workload randomness, over-provisioning ratio, and how full the drive is — a nearly full SSD has fewer free blocks and higher amplification.

### SSD Endurance

Flash cells wear out after many writes:

| SSD Type | P/E Cycles | Typical Endurance |
|----------|------------|-------------------|
| SLC | 50,000-100,000 | Very High |
| MLC | 3,000-10,000 | High |
| TLC | 1,000-3,000 | Medium |
| QLC | 100-1,000 | Lower |

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

| Storage Type | App. Latency | Seq. Bandwidth | Best For |
|--------------|--------------|----------------|----------|
| **HDD** | 5-15 ms | 100-200 MB/s | Archival, bulk storage |
| **SATA SSD** | 80-200 μs | 500 MB/s | General purpose |
| **NVMe SSD** | 20-100 μs | 3,000-7,000 MB/s | Performance workloads |

Key points for Python:

- Storage is 1000-100,000x slower than RAM
- Use appropriate file formats (Parquet > CSV)
- Memory-map files for random access patterns
- Buffer writes to avoid many small operations
- NVMe SSDs dramatically improve data loading times
- Keep working datasets in RAM when possible
