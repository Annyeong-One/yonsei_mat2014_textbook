# Virtual Memory

Virtual memory gives each process its own isolated address space, protects processes from each other, and allows programs to use more memory than physically available. It is fundamental to how every modern OS works.

## Definition

**Virtual memory** is an abstraction where the OS and CPU's Memory Management Unit (MMU) translate virtual addresses to physical RAM addresses via **page tables**. Memory is divided into **pages** (typically 4 KB). Each process has its own page table, making the same virtual address map to different physical locations in different processes.

## Explanation

The **MMU** (hardware) performs address translation billions of times per second. The **OS** (software) builds page tables, handles page faults, and decides what to swap. Neither works without the other.

**Page faults** occur when a process accesses a page not currently in RAM: *minor* faults just update the page table (no disk I/O), *major* faults require loading data from disk, and *invalid* faults (unmapped or permission violation) cause segmentation faults.

**TLB (Translation Lookaside Buffer)** caches recent translations to avoid the expensive 4-level page walk. With only 64-128 L1 TLB entries covering 256-512 KB, random access across large data causes TLB misses that significantly degrade performance.

**Swap** extends virtual memory to disk. When RAM fills, the OS moves inactive pages to swap. If the working set exceeds RAM, constant swapping (**thrashing**) destroys performance.

**Copy-on-Write (COW)**: After `fork()`, parent and child share physical pages until one writes, triggering a copy. Important for `multiprocessing` -- but CPython's reference counting can trigger COW copies even on read-only access.

## Examples

```python
import psutil
import os

# RSS = physical memory used; VMS = virtual address space (can exceed RAM)
p = psutil.Process(os.getpid())
mem = p.memory_info()
print(f"RSS: {mem.rss / 1e6:.1f} MB")
print(f"VMS: {mem.vms / 1e6:.1f} MB")
```

```python
import numpy as np

# Memory-mapped array: uses virtual memory to work with data larger than RAM
arr = np.memmap('huge.dat', dtype='float64', mode='w+',
                shape=(1_000_000_000,))  # 8 GB virtual
arr[0] = 3.14            # page fault loads this page from disk
arr[999_999_999] = 2.71  # page fault for a different page
```

```python
import mmap

# Direct memory mapping of a file
with open('data.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    # First access triggers page fault (disk read)
    # Subsequent accesses to same page hit OS page cache (RAM speed)
    value = mm[1000000:1000008]
    mm.close()
```
