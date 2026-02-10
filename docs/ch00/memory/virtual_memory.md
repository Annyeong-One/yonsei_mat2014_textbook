# Virtual Memory

## The Problem Virtual Memory Solves

Without virtual memory:

- Programs must know exact physical memory addresses
- One program can corrupt another's memory
- Programs limited to available physical RAM
- Memory fragmentation wastes space

Virtual memory solves all of these.

## What is Virtual Memory?

**Virtual memory** creates an abstraction where each process thinks it has its own private, contiguous address space.

```
Process A sees:              Process B sees:
┌─────────────────┐          ┌─────────────────┐
│ 0x0000 - Code   │          │ 0x0000 - Code   │
│ 0x1000 - Data   │          │ 0x1000 - Data   │
│ 0x2000 - Heap   │          │ 0x2000 - Heap   │
│      ...        │          │      ...        │
│ 0xFFFF - Stack  │          │ 0xFFFF - Stack  │
└─────────────────┘          └─────────────────┘
     │                            │
     │    Virtual → Physical      │
     │        Translation         │
     ▼                            ▼
┌─────────────────────────────────────────────┐
│              Physical RAM                   │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │
│  │ A's │ │ B's │ │ A's │ │ OS  │ │ B's │  │
│  │code │ │heap │ │data │ │     │ │code │  │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘  │
│         (scattered, but that's OK)         │
└─────────────────────────────────────────────┘
```

## Address Translation

The CPU's **Memory Management Unit (MMU)** translates virtual addresses to physical:

```
Virtual Address (from CPU)
         │
         ▼
    ┌─────────┐
    │   MMU   │ ◀── Uses Page Table
    └────┬────┘
         │
         ▼
Physical Address (to RAM)
```

### Page Tables

Memory is divided into **pages** (typically 4 KB). The page table maps virtual to physical pages:

```
Page Table (simplified)
┌─────────────┬─────────────┬─────────────┐
│ Virtual Page│Physical Page│   Flags     │
├─────────────┼─────────────┼─────────────┤
│      0      │     42      │ R/W/Present │
│      1      │    107      │ R/W/Present │
│      2      │     --      │ Not Present │ ← Page fault if accessed
│      3      │     89      │ Read-Only   │
│     ...     │    ...      │    ...      │
└─────────────┴─────────────┴─────────────┘
```

### Address Breakdown

A 64-bit virtual address is split:

```
Virtual Address (48 bits used on x86-64)
┌────────────────────────────────────────────────┐
│ Page Index (36 bits)  │  Page Offset (12 bits) │
└────────────────────────────────────────────────┘
         │                        │
         │                        └── Position within page (0-4095)
         │
         └── Which page (looked up in page table)
```

## Page Faults

When accessing a page not in RAM:

```
Program accesses address 0x12345678
              │
              ▼
        ┌──────────┐
        │   MMU    │
        └────┬─────┘
              │
              ▼
    ┌────────────────────┐
    │ Page in RAM?       │
    └────────────────────┘
         │           │
        Yes          No
         │           │
         ▼           ▼
    Return data   PAGE FAULT
                      │
                      ▼
              ┌──────────────┐
              │ OS Handler   │
              │ - Load from  │
              │   swap/disk  │
              │ - Update     │
              │   page table │
              └──────────────┘
                      │
                      ▼
                Retry access
```

### Types of Page Faults

| Type | Cause | Resolution |
|------|-------|------------|
| **Minor** | Page in memory but not mapped | Update page table |
| **Major** | Page on disk (swapped out) | Read from swap |
| **Invalid** | Illegal access | Segmentation fault |

## Swap Space

**Swap** extends virtual memory to disk:

```
┌──────────────────────────────────────────────────────┐
│                Virtual Address Space                 │
│  ┌─────────────────────────────────────────────┐    │
│  │          Process sees 16 GB                  │    │
│  └─────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────┘
                          │
           ┌──────────────┴──────────────┐
           ▼                             ▼
┌──────────────────┐          ┌──────────────────┐
│    Physical RAM   │          │   Swap (Disk)    │
│      (8 GB)       │          │     (16 GB)      │
│                   │          │                  │
│ Active pages live │◀────────▶│ Inactive pages   │
│ here              │  swap    │ moved here       │
└──────────────────┘          └──────────────────┘
```

When RAM fills up:

1. OS identifies least-recently-used pages
2. Writes them to swap
3. Frees RAM for active pages
4. If swapped page needed again → major page fault

### Swap Thrashing

When working set exceeds RAM, constant swapping destroys performance:

```python
import numpy as np

# If this exceeds RAM, you'll experience thrashing
huge_array = np.random.rand(10_000_000_000)  # 80 GB

# Every access might cause a page fault
for i in range(len(huge_array)):
    _ = huge_array[i]  # Potentially 1 page fault per access
```

## Memory Protection

Virtual memory enables **process isolation**:

```
Process A's Page Table          Process B's Page Table
┌─────────┬──────────┐          ┌─────────┬──────────┐
│ VA 0x100│ PA 0x5000│          │ VA 0x100│ PA 0x8000│
└─────────┴──────────┘          └─────────┴──────────┘

Same virtual address maps to DIFFERENT physical addresses
→ Processes cannot access each other's memory
```

### Protection Bits

Each page has permission flags:

| Flag | Meaning |
|------|---------|
| **R** | Readable |
| **W** | Writable |
| **X** | Executable |
| **U** | User accessible (vs kernel only) |

```
Code pages:   R-X (read, execute, not write)
Data pages:   RW- (read, write, not execute)
Stack:        RW- (read, write, not execute)
```

Violating permissions causes **segmentation fault**.

## Python and Virtual Memory

### Process Memory Layout

```
Python Process Virtual Address Space
┌─────────────────────────────────────────┐ High addresses
│              Stack                      │
│    (function calls, local variables)    │
├─────────────────────────────────────────┤
│                 ↓                       │
│           (grows down)                  │
│                                         │
│           (grows up)                    │
│                 ↑                       │
├─────────────────────────────────────────┤
│              Heap                       │
│    (Python objects, NumPy arrays)       │
├─────────────────────────────────────────┤
│         Memory-mapped files             │
│    (shared libraries, mmap)             │
├─────────────────────────────────────────┤
│              Data                       │
│    (global variables)                   │
├─────────────────────────────────────────┤
│              Code                       │
│    (Python interpreter, libraries)      │
└─────────────────────────────────────────┘ Low addresses
```

### Checking Process Memory

```python
import psutil
import os

process = psutil.Process(os.getpid())
mem_info = process.memory_info()

print(f"RSS (Resident Set Size): {mem_info.rss / 1e6:.1f} MB")
print(f"VMS (Virtual Memory Size): {mem_info.vms / 1e6:.1f} MB")
```

- **RSS**: Physical memory actually used
- **VMS**: Total virtual address space (can exceed physical RAM)

### Memory-Mapped Files

Python can map files directly into virtual memory:

```python
import mmap
import os

# Create a file
with open('data.bin', 'wb') as f:
    f.write(b'\x00' * 1000000)  # 1 MB

# Memory-map it
with open('data.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    
    # Access like a byte array
    mm[0] = 65  # Write 'A'
    print(mm[0:10])  # Read bytes
    
    mm.close()
```

NumPy's memmap uses this:

```python
import numpy as np

# Array backed by file - can exceed RAM
arr = np.memmap('huge.dat', dtype='float64', mode='w+',
                shape=(1_000_000_000,))  # 8 GB

# OS pages in/out as needed
arr[0] = 3.14
arr[999_999_999] = 2.71
```

## TLB: Translation Lookaside Buffer

Page table lookups are slow. The **TLB** caches recent translations:

```
Virtual Address
      │
      ▼
┌─────────────┐
│  Check TLB  │──── Hit ───▶ Physical Address (fast!)
└─────────────┘
      │ Miss
      ▼
┌─────────────┐
│ Page Table  │──── Walk ──▶ Physical Address (slow)
│   Walk      │              + Update TLB
└─────────────┘
```

TLB misses hurt performance on random access patterns:

```python
import numpy as np

n = 100_000_000
arr = np.random.rand(n)
indices = np.random.permutation(n)

# Sequential: TLB friendly
for i in range(n):
    _ = arr[i]  # Same page for ~500 consecutive accesses

# Random: TLB hostile
for i in indices:
    _ = arr[i]  # Different page nearly every access → TLB misses
```

## Summary

| Concept | Description |
|---------|-------------|
| **Virtual Memory** | Abstraction giving each process isolated address space |
| **Page** | Unit of memory (typically 4 KB) |
| **Page Table** | Maps virtual pages to physical pages |
| **Page Fault** | Access to unmapped page triggers OS handler |
| **Swap** | Disk space extending virtual memory beyond RAM |
| **TLB** | Cache for page table entries |
| **Protection** | Permissions (R/W/X) per page |

Key implications for Python:

- Each Python process has isolated memory space
- Large allocations may trigger page faults (slow first access)
- Memory-mapped files enable working with data exceeding RAM
- Random access patterns cause TLB misses
- Swap thrashing destroys performance—keep working set in RAM
