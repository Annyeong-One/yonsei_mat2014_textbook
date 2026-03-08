# Memory Overview

## The Memory Problem

Modern CPUs can execute billions of instructions per second, but memory cannot deliver data that fast. This fundamental mismatch shapes all of computing.

```
The Speed Gap

CPU Speed:     ████████████████████████████████  (4 GHz = 0.25 ns/cycle)
L1 Cache:      ████████████                      (~1 ns)
L2 Cache:      ██████████████                    (~3 ns)
L3 Cache:      ████████████████████              (~10 ns)
RAM:           ████████████████████████████████████████████████  (~60 ns)
SSD:           ████████████████████████████████████████████████████  (~100,000 ns)

CPU waits 240 cycles for RAM, 400,000 cycles for SSD!
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
                    │  (~64 KB)   │
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

The **BIOS** (Basic Input/Output System) or its modern successor **UEFI** (Unified Extensible Firmware Interface) is in charge of booting. It lives on a **Flash ROM chip** soldered directly onto the motherboard — completely separate from your RAM and SSD.

| Component | Type | Role at Boot |
|-----------|------|--------------|
| **BIOS/UEFI chip** | Flash ROM (on motherboard) | First code to run |
| **RAM** | Volatile DRAM | Where the OS gets loaded into |
| **SSD** | Non-volatile Flash | Where OS files are stored |

### The Hardwired Start Address

The moment power hits the CPU, it always begins executing from one specific memory address — `0xFFFFFFF0` on x86 processors. This behavior is not software, not configurable, not stored in a file. It is literally baked into the CPU's circuit logic — a reflex.

But RAM is empty at boot. So what is at that address?

The motherboard is wired so that `0xFFFFFFF0` is **mapped to the BIOS/UEFI chip**, not RAM. When the CPU "goes to" that address, it is transparently reading from the ROM chip:

```
Address Space (what the CPU sees):
┌─────────────────────┐ 0xFFFFFFFF  (top)
│   BIOS/UEFI chip    │ ← 0xFFFFFFF0  CPU always starts here
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
│ CPU jumps to 0xFFFFFFF0 │  ← hardwired reflex
│ (mapped to BIOS/UEFI)   │
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

The boot sequence touches nearly every tier of the memory hierarchy in order — ROM → RAM → SSD → RAM — making it a perfect map of why each tier exists.

### Why ROM Specifically?

ROM stores the BIOS/UEFI firmware — a small program whose sole job is to get the computer to the point where the OS can take over. But why ROM and not any other storage?

- **Non-volatile** — retains its contents without power. The instructions are always there the instant power arrives, before anything else has been initialized.
- **Immediately readable by the CPU** — unlike an SSD, which requires a whole driver stack to be set up before you can read from it. ROM just sits in the address space, ready to go.
- **Read-only (historically)** — the instructions cannot be accidentally overwritten by a crashed OS or malicious software. Modern Flash ROM can be updated (that is what a "BIOS update" is), but it requires deliberate effort.

Think of ROM as the **"always-on, always-ready" first responder**. At the moment of power-on, nothing else is ready yet — RAM is empty, the SSD needs initialization, the OS does not exist yet. ROM is the only thing the CPU can trust to be there unconditionally.

## Hierarchy Properties

Each level has distinct characteristics:

| Level | Size | Latency | Bandwidth | Managed By |
|-------|------|---------|-----------|------------|
| **Registers** | ~1 KB | 0.25 ns | N/A | Compiler |
| **L1 Cache** | 32-64 KB | 1 ns | ~1 TB/s | Hardware |
| **L2 Cache** | 256-512 KB | 3 ns | ~500 GB/s | Hardware |
| **L3 Cache** | 4-32 MB | 10 ns | ~200 GB/s | Hardware |
| **RAM** | 8-128 GB | 60 ns | ~50 GB/s | OS |
| **SSD** | 256 GB-4 TB | 100 μs | ~5 GB/s | OS |
| **HDD** | 1-20 TB | 10 ms | ~200 MB/s | OS |

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
│ Fetch from RAM    │──────────→ Return data (60 ns)
└───────────────────┘
        │
        ▼
  Also load into L1, L2, L3 (for next access)
```

### Why Load into All Three Levels?

When data is fetched from RAM after a full cache miss, the hardware loads it into **all three cache levels simultaneously** as it passes through on its way up to the CPU:

```
RAM → L3 → L2 → L1 → CPU
       ↑     ↑     ↑
    stored stored stored
```

The reasoning is straightforward. You just made an expensive 60 ns trip to RAM — so you leave copies at every level as a safety net:

- **L1** gets it because the CPU just asked for it and will likely need it again soon
- **L2 and L3** act as fallbacks — if L1 evicts it (L1 is tiny, ~64 KB), the data is still in L2; if L2 evicts it, still in L3; only then is another RAM fetch required

Think of it like going to the library basement for a book. Since you made that expensive trip, you leave a copy on your desk (L1), the floor bookshelf (L2), and the hallway shelf (L3) — so next time you never need to go back down.

### Cache Eviction

Each cache level has a fixed size, so when it is full and new data arrives, something must be **evicted**. The most common policy is **LRU (Least Recently Used)**:

```
L1 Cache (tiny, ~64 KB) — example with 4 slots:

Initial state:
┌─────┬─────┬─────┬─────┐
│  A  │  B  │  C  │  D  │   (A is oldest, D is newest)
└─────┴─────┴─────┴─────┘

New data E arrives → L1 is full → evict A (least recently used)
┌─────┬─────┬─────┬─────┐
│  B  │  C  │  D  │  E  │
└─────┴─────┴─────┴─────┘
```

Importantly, **eviction does not mean the data is gone** — it just falls down to the next level:

```
L1 full → evict to L2
               │
          L2 full → evict to L3
                        │
                   L3 full → evicted from cache entirely
                                    │
                               (still exists in RAM or SSD)
```

Caches only hold **copies** of data that permanently lives lower in the hierarchy. Programs never need to worry about eviction — the hardware manages it invisibly.

### Data Survival: Multiple Chances to Stay in Cache

Every time data gets accessed again, it gets **promoted back up** and its eviction clock resets. LRU rewards frequently used data by keeping it close to the CPU:

```
Timeline of data A being accessed repeatedly:

Access 1: A fetched from RAM → loaded into L3, L2, L1
                                                    ↑
                                              eviction clock starts

Access 2: A found in L1 (hit!) → clock resets, A stays in L1
Access 3: A found in L1 (hit!) → clock resets, A stays in L1

... time passes, other data fills L1 ...

A gets evicted from L1 → falls to L2 (still safe)

Access 4: A found in L2 (hit!) → promoted back to L1, clock resets
```

The survival of data in cache depends entirely on how frequently it is used relative to competing data — the cache is a scoreboard where frequently accessed data naturally floats to the top:

| Data behavior | Cache fate |
|---|---|
| Accessed repeatedly | Stays in L1 indefinitely |
| Accessed occasionally | Bounces between L1 and L2 |
| Accessed rarely | Drifts down to L3 or evicted entirely |
| Accessed once and never again | Evicted quickly |

This is temporal locality in action — and exactly why NumPy arrays accessed in tight loops are so much faster than scattered Python objects. The array keeps hitting L1; the Python objects keep missing and triggering fresh RAM fetches.

### Who Is in Charge of Promotion and Eviction?

The **CPU hardware itself** — specifically the **cache controller**, a dedicated circuit built into the CPU chip — manages all promotion, eviction, and LRU tracking. Not the OS, not software, not you.

```
Who manages each level:

Registers        ← Compiler
                      (decides which values go in registers)
                         │
L1 / L2 / L3    ← Cache Controller (built into CPU)
    Cache              - promotion, eviction, LRU tracking
                       - cache line fills
                       - all automatic, all in hardware
                         │
RAM              ← OS
                      (allocates memory to processes,
                       manages virtual memory)
                         │
SSD              ← OS
                      (swap / page file when RAM is full)
```

The cache controller operates at CPU speed — it has to, because the whole point of L1 is to return data in 1 ns. There is simply no time to consult the OS or any software. Every promotion and eviction decision is made in hardware, in nanoseconds, completely invisibly to any program running on the machine.

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

### The Cache Line Is Always the Atomic Unit

The "whole house moves together" rule applies consistently at **every level** of the hierarchy — including the initial fetch from RAM.

When you ask for a single byte, the hardware never fetches just that byte. It finds the aligned 64-byte block containing it and moves the entire block:

```
You ask for byte at address 130 (which is a2)

RAM:
address:  128  129  130  131  132  ... 191
data:      a0   a1   a2   a3   a4  ... a63
           └─────────────────────────────┘
                  one cache line (64 bytes)

→ entire line (a0 through a63) moves from RAM into L3, L2, L1
→ not just a2
```

The same rule holds at every transition:

```
RAM → L3 → L2 → L1      always in 64-byte houses
       ↑     ↑     ↑
  whole     whole  whole
  line      line   line
```

The hardware has one simple rule throughout: **the cache line is the atomic unit of transfer, always, everywhere.** No level ever breaks the house apart — not on the way up (promotion), not on the way down (eviction).

This is exactly why spatial locality is so powerful. When you access `a2` and pay the expensive RAM fetch cost (60 ns), you automatically get `a0` through `a63` for free in cache. If your next accesses are `a3`, `a4`, `a5` — they are already there. You paid once for the whole house, and everyone benefits.



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
  0.01 MB: 150.0 GB/s  ← Fits in L2, very fast
  0.10 MB: 120.0 GB/s  ← Fits in L3
  1.00 MB: 80.0 GB/s   ← Mostly L3
 10.00 MB: 45.0 GB/s   ← Spills to RAM
100.00 MB: 35.0 GB/s   ← RAM-limited
```

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
