# Memory Overview

## The Memory Problem

Modern CPUs can execute billions of instructions per second, but memory cannot deliver data that fast. This fundamental mismatch shapes all of computing.

```
The Speed Gap

CPU Speed:     ████████████████████████████████  (4 GHz = 0.25 ns/cycle)
L1 Cache:      ████████████                      (~1 ns)
L2 Cache:      ██████████████                    (~4 ns)
L3 Cache:      ████████████████████              (~12 ns)
RAM:           ████████████████████████████████████████████████  (~80-120 ns)
SSD:           ████████████████████████████████████████████████████  (~100,000 ns)

A RAM access takes ~200-300 cycles, 400,000 cycles for SSD!
(Modern CPUs use out-of-order execution to do other work while waiting)
```

## The Memory Hierarchy

To bridge this gap, computers use a **hierarchy** of memory types—each level trades capacity for speed:

```
                    ┌─────────────┐
                    │  Registers  │  ← Fastest, smallest
                    │   (~1 KB)   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  L1 Cache   │
                    │  (~32 KB)   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  L2 Cache   │
                    │  (~256 KB)  │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  L3 Cache   │
                    │  (~8 MB)    │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │    RAM      │
                    │  (~16 GB)   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │   Storage   │  ← Slowest, largest
                    │  (~1 TB)    │
                    └─────────────┘
```

## The Hierarchy in Action: Booting Your Computer

The best way to understand why the memory hierarchy exists is to watch it come alive the moment you press the power button.

### Who Is in Charge of Booting?

The **BIOS** (Basic Input/Output System) or its modern successor **UEFI** (Unified Extensible Firmware Interface) is in charge of booting. It lives on a **flash memory chip** (typically SPI flash) soldered directly onto the motherboard — completely separate from your RAM and SSD.

| Component | Type | Role at Boot |
|-----------|------|--------------|
| **BIOS/UEFI chip** | Flash memory (on motherboard) | First code to run |
| **RAM** | Volatile DRAM | Where the OS gets loaded into |
| **SSD** | Non-volatile Flash | Where OS files are stored |

### The Hardwired Start Address

The moment power hits the CPU, it begins executing from a fixed **reset vector** — a hardwired address mapped to the system firmware. This behavior is not software, not configurable, not stored in a file. It is literally baked into the CPU's circuit logic — a reflex.

But RAM is empty at boot. So what is at that address?

The motherboard is wired so that the reset vector is **mapped to the BIOS/UEFI chip**, not RAM. When the CPU "goes to" that address, it is transparently reading from the flash chip:

```
Address Space (what the CPU sees):
┌─────────────────────┐ 0xFFFFFFFF  (top)
│   BIOS/UEFI chip    │ ← Reset vector: CPU always starts here
├─────────────────────┤
│        ...          │
├─────────────────────┤
│        RAM          │ ← OS gets loaded here later
└─────────────────────┘ 0x00000000  (bottom)
```

This is the key insight: **"memory address" does not mean RAM**. It is just a number the CPU uses to refer to a location. The motherboard decides which physical chip actually responds to that number.

### The Full Boot Sequence

```
Power On
    │
    ▼
┌─────────────────────────┐
│ CPU jumps to reset      │  ← hardwired reflex
│ vector (→ BIOS/UEFI)    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   POST (Self-Test)      │  ← checks RAM, CPU, GPU, keyboard
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Find Boot Device       │  ← checks boot order (SSD, USB, ...)
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Load Bootloader        │  ← reads MBR or EFI partition from SSD
│  (GRUB / Windows BM)    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  OS Kernel → RAM        │  ← SSD → RAM: the hierarchy in motion
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  OS takes over          │  ← drivers, services, login screen
└─────────────────────────┘
```

The boot sequence touches nearly every tier of the memory hierarchy in order — firmware flash → RAM → SSD → RAM — making it a perfect map of why each tier exists.

### Why Flash Memory for Firmware?

The firmware chip stores the BIOS/UEFI — a small program whose sole job is to get the computer to the point where the OS can take over. But why flash memory and not any other storage?

- **Non-volatile** — retains its contents without power. The instructions are always there the instant power arrives, before anything else has been initialized.
- **Immediately readable by the CPU** — unlike an SSD, which requires a whole driver stack to be set up before you can read from it. The flash chip just sits in the address space, ready to go.
- **Updatable but protected** — modern flash memory can be updated (that is what a "BIOS update" is), but requires deliberate effort and typically hardware-level write protection. Historically, true ROM (read-only memory) was used and could not be modified at all.

Think of the firmware chip as the **"always-on, always-ready" first responder**. At the moment of power-on, nothing else is ready yet — RAM is empty, the SSD needs initialization, the OS does not exist yet. The firmware chip is the only thing the CPU can trust to be there unconditionally.

## Hierarchy Properties

Each level has distinct characteristics:

| Level | Size | Latency | Managed By |
|-------|------|---------|------------|
| **Registers** | ~1 KB | 0.25 ns | Compiler |
| **L1 Cache** | ~32 KB (data) | ~1 ns | Hardware |
| **L2 Cache** | 256-512 KB | ~4 ns | Hardware |
| **L3 Cache** | 4-32 MB | ~12 ns | Hardware |
| **RAM** | 8-128 GB | ~80-120 ns | OS |
| **SSD** | 256 GB-4 TB | ~100 μs | OS |
| **HDD** | 1-20 TB | ~10 ms | OS |

Latencies are approximate and vary by CPU model and generation. L1 caches are typically split into separate instruction and data caches (e.g., 32 KB each).

## Why Hierarchy Works: Locality

The hierarchy exploits two types of **locality**:

### Temporal Locality

Recently accessed data is likely to be accessed again soon.

```python
# Temporal locality: 'total' accessed repeatedly
total = 0
for i in range(1000000):
    total += i  # 'total' stays in register/cache
```

### Spatial Locality

Data near recently accessed data is likely to be accessed soon.

```python
# Spatial locality: array elements are adjacent in memory
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(arr)):
    print(arr[i])  # Sequential access → prefetching works
```

## Cache Mechanics

When the CPU needs data:

```
CPU requests address X
        │
        ▼
┌───────────────────┐
│ Check L1 Cache    │──── Hit? ──→ Return data (1 ns)
└───────────────────┘
        │ Miss
        ▼
┌───────────────────┐
│ Check L2 Cache    │──── Hit? ──→ Return data (3 ns)
└───────────────────┘
        │ Miss
        ▼
┌───────────────────┐
│ Check L3 Cache    │──── Hit? ──→ Return data (10 ns)
└───────────────────┘
        │ Miss
        ▼
┌───────────────────┐
│ Fetch from RAM    │──────────→ Return data (~100 ns)
└───────────────────┘
        │
        ▼
  Load into cache hierarchy (for next access)
```

### How Data Fills the Cache

When data is fetched from RAM after a full cache miss, it is installed in L1 (where the CPU needs it). Whether lower levels (L2, L3) also keep a copy depends on the CPU's **cache inclusion policy**:

- **Inclusive caches** — L1 data is always also present in L2 and L3. Used in some older Intel designs.
- **Non-inclusive / exclusive caches** — data may exist in only one level at a time. Used in modern AMD Zen and recent Intel designs.

```
RAM → cache hierarchy → L1 → CPU
      (exact behavior depends on inclusion policy)
```

The result is the same from a programmer's perspective: after a cache miss, the data is available in L1 for fast subsequent access, and the cache hierarchy as a whole retains recently used data so that eviction from L1 does not always require a full trip back to RAM.

### Cache Eviction

Each cache level has a fixed size, so when it is full and new data arrives, something must be **evicted**. Most CPUs approximate **LRU (Least Recently Used)** using simpler hardware heuristics (pseudo-LRU, tree-PLRU), because true LRU tracking is too expensive to implement in hardware for highly associative caches:

```
L1 Cache (tiny, ~32 KB) — example with 4 slots:

Initial state:
┌─────┬─────┬─────┬─────┐
│  A  │  B  │  C  │  D  │   (A is oldest, D is newest)
└─────┴─────┴─────┴─────┘

New data E arrives → L1 is full → evict A (least recently used)
┌─────┬─────┬─────┬─────┐
│  B  │  C  │  D  │  E  │
└─────┴─────┴─────┴─────┘
```

When data is evicted from a cache level, it is **discarded** — unless the data has been modified (is "dirty"), in which case it is **written back** to the next level of memory. Caches at each level operate independently; eviction from L1 does not automatically place the data into L2.

```
L1 evicts data → discarded (or written back if dirty)
L2 evicts data → discarded (or written back if dirty)
L3 evicts data → discarded (or written back to RAM if dirty)
```

Caches only hold **copies** of data that permanently lives lower in the hierarchy. If evicted clean data is needed again, it is simply re-fetched. Programs never need to worry about eviction — the hardware manages it invisibly.

### Data Survival: Temporal Locality in Action

Every time data is accessed again and found in cache, the hardware marks it as recently used, making it less likely to be evicted. Frequently used data naturally stays close to the CPU:

```
Timeline of data A being accessed repeatedly:

Access 1: A fetched from RAM → loaded into L1
                                           ↑
                                     marked as recent

Access 2: A found in L1 (hit!) → still marked recent, stays in L1
Access 3: A found in L1 (hit!) → still marked recent, stays in L1

... time passes, other data fills L1 ...

A gets evicted from L1 (no longer recent enough)

Access 4: A re-fetched from lower level → back in L1, marked recent
```

The survival of data in cache depends entirely on how frequently it is used relative to competing data:

| Data behavior | Cache fate |
|---|---|
| Accessed repeatedly | Stays in L1 indefinitely |
| Accessed occasionally | May be evicted and re-fetched |
| Accessed rarely | Evicted, requires longer re-fetch |
| Accessed once and never again | Evicted quickly |

This is temporal locality in action — and exactly why NumPy arrays accessed in tight loops are so much faster than scattered Python objects. The array keeps hitting L1; the Python objects keep missing and triggering fresh RAM fetches.

### Who Is in Charge of Promotion and Eviction?

The **CPU hardware itself** — specifically the **cache controller**, a dedicated circuit built into the CPU chip — manages eviction, replacement, and cache line fills. Not the OS, not software, not you.

```
Who manages each level:

Registers        ← Compiler
                      (decides which values go in registers)
                         │
L1 / L2 / L3    ← Cache Controller (built into CPU)
    Cache              - eviction and replacement decisions
                       - cache line fills
                       - hardware prefetchers
                       - coherence protocols (multicore)
                       - all automatic, all in hardware
                         │
RAM              ← OS
                      (allocates memory to processes,
                       manages virtual memory)
                         │
SSD              ← OS
                      (swap / page file when RAM is full)
```

The cache controller operates at CPU speed — it has to, because the whole point of L1 is to return data in ~1 ns. There is simply no time to consult the OS or any software. Every eviction and replacement decision is made in hardware, in nanoseconds, completely invisibly to any program running on the machine.

This is why caches are called **transparent** — no program ever asks "please put this in L1." The hardware watches all memory accesses and silently decides what to keep, promote, and evict. Your Python code has no idea the cache even exists.

### Cache Lines

Caches don't transfer single bytes—they move **cache lines** (typically 64 bytes):

```
Memory:
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ a0 │ a1 │ a2 │ a3 │ a4 │ a5 │ a6 │ a7 │ b0 │ b1 │ b2 │ b3 │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
└──────────────────────────────────────┘
              Cache Line (64 bytes)

Access a0 → entire cache line loaded
Access a1, a2, ... a7 → already in cache (free!)
```

### The Cache Line as Transfer Unit

The "whole house moves together" rule is the primary mechanism for CPU cache transfers.

When you ask for a single byte, the hardware never fetches just that byte. It finds the aligned 64-byte block containing it and moves the entire block:

```
You ask for byte at address 130 (which is a2)

RAM:
address:  128  129  130  131  132  ... 191
data:      a0   a1   a2   a3   a4  ... a63
           └─────────────────────────────┘
                  one cache line (64 bytes)

→ entire line (a0 through a63) is fetched into cache
→ not just a2
```

Cache lines are the **primary unit of transfer** for CPU caches. Some hardware mechanisms (prefetchers, memory controllers) may fetch larger units, but from the programmer's perspective, the 64-byte cache line is the fundamental granularity.

This is exactly why spatial locality is so powerful. When you access `a2` and pay the expensive RAM fetch cost (~100 ns), you automatically get `a0` through `a63` for free in cache. If your next accesses are `a3`, `a4`, `a5` — they are already there. You paid once for the whole house, and everyone benefits.

### Latency vs Throughput: Memory-Level Parallelism

The latency numbers above (~100 ns for RAM) might suggest that every cache miss completely stalls the CPU. In practice, modern CPUs can issue **multiple memory requests simultaneously** while continuing to execute other instructions out of order:

```
Simple model:       request → wait 100 ns → request → wait 100 ns
                    (serial, slow)

Reality (MLP):      request ─────────────────→ data arrives
                    request ─────────────────→ data arrives
                    request ─────────────────→ data arrives
                    (overlapped, much higher throughput)
```

This is why **latency and throughput are different**: a single access costs ~100 ns, but the CPU can have many in flight at once. Sequential access patterns benefit most from this because the prefetcher can issue requests far ahead of the CPU's current position.

## Python Memory Layout

Python objects live in RAM, managed by the interpreter:

```python
import sys

# Every Python object has overhead
x = 1
print(sys.getsizeof(x))  # 28 bytes (not 4 or 8!)

# Lists store references, not values
lst = [1, 2, 3]
print(sys.getsizeof(lst))  # 80 bytes (just the list object)
# Plus 28 bytes × 3 for the integers = 164 bytes total
```

### NumPy's Memory Advantage

NumPy arrays use contiguous memory, enabling cache efficiency:

```python
import numpy as np

# NumPy: contiguous block of raw values
arr = np.array([1, 2, 3], dtype=np.int64)
print(arr.nbytes)  # 24 bytes (8 bytes × 3, no overhead per element)

# Python list: scattered objects
lst = [1, 2, 3]
# ~164 bytes, objects may not be contiguous
```

```
Python List Memory Layout:
┌─────────┐     ┌─────────┐
│  List   │────▶│ Ref[0]  │────▶ [PyObject: 1] (somewhere in heap)
│ Object  │     │ Ref[1]  │────▶ [PyObject: 2] (somewhere else)
└─────────┘     │ Ref[2]  │────▶ [PyObject: 3] (somewhere else)
                └─────────┘
                 ↑ contiguous pointers (some spatial locality)
                   but objects themselves are scattered (pointer chasing)

NumPy Array Memory Layout:
┌─────────┐     ┌───────────────────────┐
│ ndarray │────▶│  1  │  2  │  3  │     │  ← Contiguous data buffer
│ Object  │     └───────────────────────┘
└─────────┘
```

## Measuring Memory Hierarchy Effects

```python
import numpy as np
import time

def measure_access_pattern(size_mb):
    """Measure time to sum array of given size."""
    n = size_mb * 1024 * 1024 // 8  # Number of float64 elements
    arr = np.random.rand(n)
    
    # Warm up cache
    _ = np.sum(arr)
    
    # Measure
    start = time.perf_counter()
    for _ in range(10):
        _ = np.sum(arr)
    elapsed = time.perf_counter() - start
    
    bandwidth = (n * 8 * 10) / elapsed / 1e9  # GB/s
    return bandwidth

# Test different sizes
for size in [0.01, 0.1, 1, 10, 100]:
    bw = measure_access_pattern(size)
    print(f"{size:6.2f} MB: {bw:.1f} GB/s")
```

Expected pattern:

```
  0.01 MB: 150.0 GB/s  ← Roughly fits in L2
  0.10 MB: 120.0 GB/s  ← Roughly fits in L3
  1.00 MB: 80.0 GB/s   ← Mostly L3
 10.00 MB: 45.0 GB/s   ← Spills to RAM
100.00 MB: 35.0 GB/s   ← RAM-limited
```

Exact boundaries between cache levels are fuzzy in practice due to hardware prefetchers, cache sharing between cores, and OS background activity.

## Key Concepts Summary

| Concept | Description |
|---------|-------------|
| **Memory Hierarchy** | Multiple levels of storage trading speed for capacity |
| **Cache** | Small, fast memory that stores recently used data |
| **Cache Line** | Unit of transfer between cache levels (typically 64 bytes) |
| **Cache Hit** | Data found in cache (fast) |
| **Cache Miss** | Data not in cache, must fetch from lower level (slow) |
| **Temporal Locality** | Recently used data likely to be used again |
| **Spatial Locality** | Nearby data likely to be used together |

## Why This Matters for Python

Understanding the memory hierarchy explains:

- Why NumPy is faster than Python lists (contiguous memory → cache efficiency)
- Why accessing array elements sequentially is faster than randomly
- Why small, hot loops are fast (fit in cache)
- Why memory-bound operations don't benefit from faster CPUs
- Why data layout matters for performance

The hierarchy is invisible to most Python code, but its effects are everywhere.
