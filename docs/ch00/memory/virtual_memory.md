# Virtual Memory

## The Problem Virtual Memory Solves

Without virtual memory:

- Programs must know exact physical memory addresses
- One program can corrupt another's memory
- Programs limited to available physical RAM
- Memory fragmentation wastes space

Virtual memory solves all of these.

## Who Controls Virtual Memory: OS or CPU?

Both — they play different roles and neither can do it alone.

```
Virtual Memory = OS (policy) + CPU/MMU (mechanism)
```

The **CPU/MMU** handles the mechanical part — actual address translation at hardware speed:

```
Every single memory access:

Virtual address
      │
      ▼
   MMU (hardware)
      │  looks up page table
      ▼
Physical address → RAM

This happens billions of times per second
→ must be hardware, no time for OS involvement
```

The **OS** handles the policy part — decisions and setup:

```
OS is responsible for:

- Creating page tables when a process starts
- Deciding which pages to swap out when RAM is full
- Handling page faults (loading pages back from disk)
- Setting permissions (R/W/X) on each page
- Destroying page tables when process exits
```

| Responsibility | Who |
|---|---|
| Building and maintaining page tables | OS |
| Actually translating addresses | MMU (CPU) |
| Deciding what to swap out | OS |
| Catching invalid accesses | MMU raises exception → OS handles it |
| TLB caching of translations | MMU (CPU) |
| Loading swapped pages back | OS |

Neither works without the other — the MMU needs the OS to set up the page tables it reads from, and the OS needs the MMU to enforce the isolation it designed.

### The Broader Pattern: OS as Stage, CPU as Performer

This division generalizes to the entire relationship between OS and CPU:

```
Virtual Memory:
  OS  → builds page tables, sets permissions
  MMU → does every address translation

Cache:
  OS  → allocates memory regions
  Cache Controller → does every promotion/eviction

Interrupts:
  OS  → registers interrupt handlers
  CPU → detects the interrupt, jumps to handler

Process Scheduling:
  OS  → decides which process runs next
  CPU → actually executes the instructions

Boot:
  BIOS/UEFI → sets up the working environment
  CPU        → executes every instruction
```

The OS is a **configuration and coordination layer** — it makes decisions, sets up tables, registers handlers, and manages resources, but only runs when something needs to be decided or handled. The vast majority of actual work — billions of operations per second — is done by the CPU running autonomously within the environment the OS prepared.

```
OS  = rulebook + referee
      (runs occasionally, when decisions needed)

CPU = player
      (runs constantly, does the actual work)
```

The OS is in control in the sense that it *defines the rules*. The CPU is in control in the sense that it *does everything*. They are complementary, not competing.

### Every Modern OS Uses Virtual Memory

Virtual memory is considered a fundamental requirement of any modern OS — Windows, Linux, macOS, iOS, Android all use it without exception. It became standard in the 1980s–90s as multitasking OSes took over, and today the MMU is built directly into CPU silicon because the hardware assumes virtual memory will always be in use.

The only exceptions are bare-metal embedded systems and some real-time OSes (RTOS) where there is barely an "OS" in the traditional sense — programs run directly on hardware with no abstraction layer.



**Virtual memory** creates an abstraction where each process thinks it has its own private, contiguous address space.

On x86-64, only 48 of 64 address bits are used, creating two **canonical** halves separated by a large non-canonical hole (any address in the gap causes a fault). The **lower canonical half** is user space, and the **upper canonical half** is kernel space:

```
Process A sees:              Process B sees:
┌─────────────────┐          ┌─────────────────┐
│  Kernel space   │          │  Kernel space   │  (shared, inaccessible
│  (upper half)   │          │  (upper half)   │   to user code)
├─────────────────┤          ├─────────────────┤
│ 0x0000 - Code   │          │ 0x0000 - Code   │
│ 0x1000 - Data   │          │ 0x1000 - Data   │
│ 0x2000 - Heap   │          │ 0x2000 - Heap   │
│      ...        │          │      ...        │
│ 0x7FFF - Stack  │          │ 0x7FFF - Stack  │
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

Memory is divided into **pages** (typically 4 KB on x86-64; ARM64 also supports 16 KB and 64 KB default pages). Modern systems additionally support **huge pages** (2 MB or 1 GB on x86-64) which reduce TLB pressure for large working sets — each TLB entry covers more memory. The page table maps virtual to physical pages. Conceptually, each entry maps one virtual page to one physical page:

```
Page Table Entry (simplified)
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

In practice, modern CPUs use **multi-level page tables** — not a flat table. A flat table for 48-bit addresses would require billions of entries. Instead, the page table is a tree:

```
x86-64 Four-Level Page Table

Virtual address bits: | 9 bits | 9 bits | 9 bits | 9 bits | 12 bits |
                       PML4     PDPT      PD       PT      offset

  PML4 (level 4)
    └── PDPT (level 3)
          └── PD (Page Directory, level 2)
                └── PT (Page Table, level 1)
                      └── Physical page + offset
```

Each level is a table with 512 entries (2^9). The MMU performs a **page walk** — following pointers through up to 4 levels of tables — to resolve a virtual address. Without TLB caching, this requires 4 memory reads just for translation, before the actual data access.

The tree structure is sparse: only branches that correspond to actually mapped memory need to exist, saving enormous amounts of memory compared to a flat table.

### Address Breakdown

A 64-bit virtual address (48 bits used on x86-64):

```
Virtual Address (48 bits used on x86-64)
┌────────┬────────┬────────┬────────┬──────────────┐
│ PML4   │ PDPT   │  PD    │  PT    │ Page Offset  │
│ 9 bits │ 9 bits │ 9 bits │ 9 bits │   12 bits    │
└────────┴────────┴────────┴────────┴──────────────┘
  │         │         │         │           │
  │         │         │         │           └── Byte within page (0-4095)
  │         │         │         └── Entry in Page Table
  │         │         └── Entry in Page Directory
  │         └── Entry in Page Directory Pointer Table
  └── Entry in Page Map Level 4

Each 9-bit index selects 1 of 512 entries at that level.
4 KB page = 2^12 bytes → 12-bit offset
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
| **Minor** | Page already in memory (e.g., in page cache) but not yet mapped into this process's page table | Update page table — no disk I/O |
| **Major** | Page not in memory — either swapped out or never loaded (**demand paging**: executables and mmap'd files are loaded page-by-page on first access, not all at once) | Read from disk (swap or file) |
| **Invalid** | Illegal access (unmapped address, permission violation) | Segmentation fault |

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

1. OS identifies infrequently-used pages (using approximated LRU — true LRU would require tracking every memory access, which is impractical)
2. Writes them to swap (or compresses them in RAM first — macOS does this before swapping)
3. Frees RAM for active pages
4. If swapped page needed again → major page fault

Different OSes handle memory pressure differently:

| OS | Strategy |
|----|----------|
| **Linux** | Approximate LRU (clock variants) + page cache reclaim |
| **macOS** | Memory compression first, then swap |
| **Windows** | Working set trimming |

Many modern systems avoid swapping unless memory pressure is extreme — compression and page cache reclaim are preferred because they avoid slow disk I/O.

### Swap Thrashing

When working set exceeds RAM, constant swapping destroys performance:

```python
import numpy as np

# Allocating beyond RAM typically causes MemoryError or OOM kill,
# not thrashing. Thrashing occurs when multiple processes or
# data structures collectively exceed RAM:
arrays = []
for _ in range(20):
    arrays.append(np.random.rand(100_000_000))  # 800 MB each = 16 GB total

# Random access across all arrays forces constant page faults
# if total exceeds physical RAM
for arr in arrays:
    _ = arr[np.random.randint(len(arr))]
```

!!! note "OOM Killer vs Thrashing"
    In practice, most modern systems will kill the offending process (Linux OOM killer) rather than thrash indefinitely. Thrashing is more commonly seen when many smaller processes collectively exceed RAM, not from a single massive allocation.

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
│    (C-level call frames; Python locals  │
│     live on the heap, not here)         │
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

Python can map files directly into virtual memory. Memory mapping does **not** load the file immediately — it maps the file into the process's virtual address space. When you access a region for the first time, a **page fault** occurs: the OS loads that page from disk into the page cache and maps it into the process. Subsequent accesses to the same page hit the page cache at RAM speed.

```python
import mmap
import os

# Create a file
with open('data.bin', 'wb') as f:
    f.write(b'\x00' * 1000000)  # 1 MB

# Memory-map it
with open('data.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)

    # First access to each page triggers a page fault (disk read)
    mm[0] = 65  # Write 'A'
    print(mm[0:10])  # Read bytes — same page, no page fault

    mm.close()
```

NumPy's memmap uses this:

```python
import numpy as np

# Array backed by file - can exceed RAM
arr = np.memmap('huge.dat', dtype='float64', mode='w+',
                shape=(1_000_000_000,))  # 8 GB

# OS pages in/out as needed — each first access triggers a page fault
arr[0] = 3.14
arr[999_999_999] = 2.71
```

## TLB: Translation Lookaside Buffer

Page table walks are slow — up to 4 memory reads per translation on x86-64. The **TLB** caches recent translations to avoid this cost:

```
Virtual Address
      │
      ▼
┌─────────────┐
│  Check TLB  │──── Hit ───▶ Physical Address (fast, ~1 cycle)
└─────────────┘
      │ Miss
      ▼
┌─────────────┐
│ Page Table  │──── Walk ──▶ Physical Address (slow, ~10-100 cycles
│   Walk      │              typical; up to ~200-400 if page table
│             │              entries miss all caches) + Update TLB
└─────────────┘
```

Typical TLB sizes are small:

| Level | Entries | Coverage (4 KB pages) |
|-------|---------|----------------------|
| **L1 TLB** | 64-128 | 256-512 KB |
| **L2 TLB** | 1,000-2,000 | 4-8 MB |

This is why huge pages matter for TLB coverage — with 2 MB pages, 128 TLB entries cover 256 MB instead of just 512 KB. Performance-sensitive workloads with large working sets (databases, scientific computing) often use huge pages to reduce TLB miss rates.

!!! note "TLB Miss ≠ Page Fault"
    A **TLB miss** triggers a hardware **page walk** through the multi-level page table — this is slow but stays entirely in RAM. A **page fault** occurs only when the page table indicates the page is not in physical RAM at all (e.g., swapped to disk or never loaded). Most TLB misses are resolved by the page walk without involving the OS.

TLB misses hurt performance on random access patterns:

```python
import numpy as np

n = 100_000_000
arr = np.random.rand(n)
indices = np.random.permutation(n)

# Sequential: TLB friendly (Python loop overhead dominates here;
# use NumPy vectorized operations to observe real TLB effects)
for i in range(n):
    _ = arr[i]  # Same page for ~500 consecutive accesses

# Random: TLB hostile
for i in indices:
    _ = arr[i]  # Different page nearly every access → TLB misses
```

## Copy-on-Write (COW)

When a process forks (creates a child process), the OS does not immediately copy all memory pages. Instead, both processes share the same physical pages, marked as **read-only**. Only when one process tries to **write** to a shared page does the OS copy that specific page — hence "copy on write":

```
After fork (before any writes):

Parent page table          Child page table
┌──────────┐               ┌──────────┐
│ VA → PA 1│               │ VA → PA 1│ ← Same physical page
│ VA → PA 2│               │ VA → PA 2│ ← Same physical page
└──────────┘               └──────────┘
                (both marked read-only)

After child writes to page 1:

Parent page table          Child page table
┌──────────┐               ┌──────────┐
│ VA → PA 1│               │ VA → PA 3│ ← New copy of page 1
│ VA → PA 2│               │ VA → PA 2│ ← Still shared
└──────────┘               └──────────┘
```

COW is important for Python's `multiprocessing` module — forked workers initially share the parent's memory (including loaded data), and only pages that are modified get duplicated. However, CPython's reference counting increments and decrements `ob_refcnt` in object headers on INCREF/DECREF operations (which happen frequently during normal execution), which can trigger COW copies even when the Python code only *reads* data.

## Summary

| Concept | Description |
|---------|-------------|
| **Virtual Memory** | Abstraction giving each process isolated address space |
| **Page** | Unit of memory (4 KB standard; 2 MB/1 GB huge pages for performance) |
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
