# Storage (SSD/HDD)

Storage is persistent but 1,000-100,000x slower than RAM. Choosing the right storage technology and file format directly determines data loading times in Python workflows.

## Definition

**Storage** refers to non-volatile devices (SSDs and HDDs) that retain data without power. **HDDs** use spinning magnetic platters with mechanical read/write heads (~5-15 ms latency). **SSDs** use NAND flash memory with no moving parts (~20-100 us for NVMe, ~80-200 us for SATA).

## Explanation

| Type | App. Latency | Seq. Bandwidth | Random IOPS |
|------|-------------|----------------|-------------|
| HDD | 5-15 ms | 100-200 MB/s | 50-200 |
| SATA SSD | 80-200 us | 500 MB/s | ~90,000 |
| NVMe SSD | 20-100 us | 3,000-7,000 MB/s | 500K-1M |

NVMe connects directly via PCIe lanes, bypassing SATA's protocol bottleneck. SSDs internally use a Flash Translation Layer (FTL) that handles wear leveling, garbage collection, and error correction transparently.

**File format matters for Python**: Parquet (binary, columnar) loads 5-10x faster than CSV (text, row-oriented) because it requires less I/O and parsing. For datasets larger than RAM, use chunked reading (`pd.read_csv(..., chunksize=100000)`) or memory-mapped files (`np.memmap`).

**OS page cache caveat**: The OS caches file data in RAM. Benchmarks of file I/O may measure page cache speed rather than actual storage speed unless files exceed available RAM.

## Examples

```python
import pandas as pd
import time

# CSV vs Parquet: binary columnar format is dramatically faster
start = time.perf_counter()
df = pd.read_csv('large_data.csv')
print(f"CSV:     {time.perf_counter() - start:.1f}s")

start = time.perf_counter()
df = pd.read_parquet('large_data.parquet')
print(f"Parquet: {time.perf_counter() - start:.1f}s")
```

```python
import numpy as np

# Memory-mapped files: work with data larger than RAM
arr = np.memmap('huge.dat', dtype='float64', mode='w+',
                shape=(100_000_000,))  # 800 MB on disk
arr[0] = 3.14  # OS pages data in/out transparently
print(arr[0])  # 3.14
```

```python
import pandas as pd

# Chunked reading: process data larger than RAM
total = 0
for chunk in pd.read_csv('huge.csv', chunksize=100_000):
    total += chunk['value'].sum()
print(f"Total: {total}")
```
