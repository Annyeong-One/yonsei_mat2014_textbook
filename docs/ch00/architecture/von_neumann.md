# Von Neumann Architecture

## Overview

The **Von Neumann architecture** is the foundational design for nearly all modern computers. It describes a computer that stores both program instructions and data in the same memory space — a concept known as the **stored-program model**.

> **Scope note**: This document describes a simplified conceptual model. Real CPUs include many additional components (branch predictors, reorder buffers, multiple execution units) not shown here.


![von_neumann](./image/von_neumann.png)



## Key Components

### Central Processing Unit (CPU)

In the simplified model, the CPU consists of three main parts:

| Component | Function |
|-----------|----------|
| **Control Unit (CU)** | Fetches instructions from memory, decodes them, coordinates execution |
| **Arithmetic Logic Unit (ALU)** | Performs mathematical and logical operations |
| **Registers** | Small, fast storage locations inside the CPU — includes the **Program Counter (PC)** (address of the next instruction) and the **Instruction Register (IR)** (the instruction currently being decoded) |

### Memory (RAM)

A single memory space that stores both:

- **Instructions** (the program code)
- **Data** (variables, arrays, objects)

This "stored-program" concept was transformative — it made general-purpose computing viable and enabled software to become a commercial product separate from hardware. Earlier computers like ENIAC had programs hardwired or entered via physical switches; changing a program required days of manual rewiring.

### Bus System

The communication pathway connecting CPU and memory, conceptually described as buses (though modern CPUs use complex on-chip interconnect networks rather than literal shared buses):

- **Address Bus**: Specifies which memory location to access
- **Data Bus**: Transfers actual data between CPU and memory
- **Control Bus**: Carries coordination signals including read, write, interrupt request, bus grant, clock, and reset — "read" and "write" are the most commonly cited examples, but the control bus is a collection of many dedicated signaling lines

> **Note**: The control bus signals "read" and "write" are sometimes compared to Unix `rwx` permissions, but the analogy breaks down at **execute** (`x`). Execute is a software/OS abstraction — at the hardware level, the CPU doesn't receive an "execute" signal over the bus. Instead, it simply *fetches* an instruction (a read), and the CPU's internal logic decodes and runs it. There is no separate "execute" bus signal.
>
> The control bus also carries many other signals beyond read/write:
>
> - **Clock** — synchronizes all components
> - **Interrupt request/acknowledge** — peripherals signal the CPU
> - **Bus request/grant** — arbitrates access when multiple devices need the bus (e.g., DMA)
> - **Reset** — forces the system to its initial state
> - **Bus ready/wait** — lets slow devices stall the CPU
>
> "Read" and "write" are the entry-point examples — not an exhaustive list.

Every byte in memory has a numeric **address** — the address bus carries this number so the memory system knows which location to read or write. A 64-bit architecture allows a theoretical address space of $2^{64}$ bytes, though real CPUs implement smaller physical and virtual address ranges (x86-64 currently uses 48–57 bits of virtual address). Instructions themselves contain address references: a `LOAD` instruction includes the address to read from, and a `STORE` includes the address to write to.

### Input/Output

CPUs also communicate with peripherals (keyboard, disk, GPU, network) through I/O controllers connected to the bus system. I/O is not shown in the simplified diagram above but is an essential part of any real system.

## The Fetch-Decode-Execute Cycle

The CPU operates in a continuous loop:

```
┌─────────┐     ┌─────────┐     ┌───────────┐     ┌───────────┐
│  FETCH  │ ──▶ │ DECODE  │ ──▶ │  EXECUTE  │ ──▶ │ WRITEBACK │
└─────────┘     └─────────┘     └───────────┘     └─────────┬─┘
     ▲                                                        │
     └────────────────────────────────────────────────────────┘
```

1. **Fetch**: Read the next instruction from memory (address stored in Program Counter)
2. **Decode**: Control Unit interprets what the instruction means
3. **Execute**: ALU or other components perform the operation
4. **Writeback**: Results are written back to registers or memory
5. **Repeat**: Program Counter increments, cycle continues

> **What "fetch" means**: The CPU retrieves the instruction stored at the memory address pointed to by the Program Counter (PC), loads it into the Instruction Register (IR), then advances the PC to the next instruction. Normally the PC advances sequentially, though branches and jumps can change it. Think of the PC as a bookmark — fetch is literally fetching the next instruction from that bookmark location.

Conceptually, instructions execute one at a time in sequence. In practice, modern CPUs use **pipelining** to overlap stages of different instructions:

```
Cycle:          1        2        3        4        5
Instruction A:  Fetch    Decode   Execute  Write
Instruction B:           Fetch    Decode   Execute  Write
Instruction C:                    Fetch    Decode   Execute ...
```

Combined with **superscalar execution** (issuing multiple instructions per cycle through parallel execution units, typically 2–6) and **out-of-order execution** (reordering instructions to avoid stalls), modern CPUs process many instructions simultaneously — but the programmer-visible model remains sequential.

## The Von Neumann Bottleneck

The defining limitation of the architecture: instructions and data ultimately compete for access to the same memory system.

```
CPU  ◀════════════════════▶  Memory
     (instructions AND data
      share the same path)
```

This creates a bottleneck because the CPU must wait for memory transfers, and instruction fetches compete with data loads for the same bus. In early designs the bottleneck was literally a single shared bus. In modern systems the physical interconnect is far more complex (crossbar switches, mesh networks, multiple memory channels), but the fundamental constraint remains: CPU speed has grown far faster than memory speed (the "memory wall"), and the bottleneck manifests as memory latency and bandwidth limits rather than a single wire.

## Memory Hierarchy

To bridge this speed gap, systems use a hierarchy of progressively smaller, faster storage between the CPU and main memory. The following are approximate orders of magnitude — exact values vary by CPU model and workload:

```
CPU Memory Hierarchy (approximate)
Registers       ~1 cycle
L1 cache        ~3–5 cycles
L2 cache        ~12 cycles
L3 cache        ~40 cycles
RAM             ~100+ cycles

Storage
SSD / Disk      ~100,000+ cycles
```

Each level acts as a buffer, keeping frequently used data close to the CPU. Data moves between levels in **cache lines** — fixed-size blocks, typically 64 bytes. When the CPU requests a single byte, the entire cache line containing it is fetched. This is why sequential array access is fast (nearby data arrives for free) and why pointer chasing through scattered objects is slow (each pointer may trigger a new cache line fetch).

Other techniques include **prefetching** (predicting what data will be needed next) and **speculative execution** (executing instructions before knowing if they're needed).

### Harvard Architecture: The Contrast

The **Harvard architecture** separates instruction memory from data memory, eliminating the competition between the two. Most microcontrollers — small, independent computers dedicated to a single specific task — use a pure Harvard design. Modern desktop CPUs use a **modified Harvard architecture**: physically they follow Von Neumann (unified RAM), but the L1 cache is split into separate instruction and data caches, recovering much of Harvard's benefit.

The three designs can be compared as a spectrum:

```
Pure Von Neumann          Modified Harvard           Pure Harvard
(unified everything)      (modern CPUs)              (separate everything)

CPU                       CPU chip                   CPU
 └── one bus               ├── L1i (separate)         ├── instr bus
      └── RAM              ├── L1d (separate)         │    └── instr RAM
    (instr + data)         ├── L2  (unified)          └── data bus
                           └── L3  (unified)               └── data RAM
                          Outside CPU chip
                           └── RAM (unified)
```

> **Important**: L1, L2, and L3 caches are all **inside the CPU chip**. Only RAM sits outside. The distinction between levels is not inside vs outside the CPU, but rather:
> - **L1** — split (Harvard-style), per-core, directly feeds the decoder and ALU
> - **L2** — unified, per-core, slightly further from execution units
> - **L3** — unified, shared across all cores

**Why the L1 split is enough**: The benefit of separate L1 caches goes beyond parallelism:

- **Simultaneous access** — the decoder reads from L1i while the ALU reads from L1d, recovering Harvard's parallelism
- **Different access patterns** — instruction streams are highly sequential with strong locality; data access is less predictable
- **No cache pollution** — data loads cannot evict hot instructions, and vice versa

L2 and L3 remain unified because the CPU has already captured the key benefits at L1, and unifying the deeper levels simplifies design without meaningful cost. Since the CPU spends the vast majority of its time talking to cache rather than RAM, the L1 split is sufficient — RAM remains shared; only the "desk drawers" (L1 instruction and data caches) are separate.

### Data Flow: The Train Model

The following is a **conceptual model**, not a literal description of hardware data flow. In practice, caches refill in 64-byte cache lines, hardware prefetchers may bypass levels, and out-of-order cores request data long before execution reaches that instruction. The hierarchy behaves *as if* data moves forward through these layers — like a train pulling cargo forward, carriage by carriage:

```
RAM          L3       L2       L1       Registers    CPU
(original) → (copy) → (copy) → (copy) → (copy)    → execute
```

> **Fetch = Copy**: At every stage, "fetching" means copying forward — the original always stays in RAM. Nothing is moved or destroyed.

> **Registers are the last stop**: The ALU can only operate on data sitting in registers — not directly from L1 cache. Registers are the smallest and fastest storage, holding only what the ALU needs right now. The programmer sees ~16 **architectural** general-purpose registers (in x86-64), but internally the CPU maintains ~150–200 **physical** registers and uses **register renaming** to map architectural names to physical locations, enabling out-of-order execution.

Each cache level holds a **copy**, pulled forward from the level behind it. When the CPU needs data:

1. Checks **Registers** first — if found, ~1 cycle (already loaded)
2. Not there? Checks **L1** — ~3–5 cycles (cache hit)
3. Not there? Checks **L2** — ~12 cycles
4. Not there? Checks **L3** — ~40 cycles
5. Not there? Goes to **RAM** — ~100+ cycles (cache miss cascade)

When a cache miss occurs, data is copied up the chain and cached at each level for future reuse. If the same data is needed again soon (**temporal locality**), it's already waiting in L1.

Refilling also works level by level:

```
RAM ←————————————————————————————————————
          L3 ←——————————————————————————   (refills from RAM)
                   L2 ←—————————————————  (refills from L3)
                            L1 ←—————————  (refills from L2)
                            Registers ←——  (refills from L1)
                                 CPU executes here
```

### CPU Package and Internal Buses

On most modern CPUs, L3 is on the same die as the CPU cores. In chiplet-based designs (e.g., AMD Zen), L3 may reside on the same chiplet as a group of cores. Either way, all cache levels are packaged together as one unit you install on the motherboard:

```
CPU Package (what you buy & install)
┌─────────────────────────────────────┐
│  Core 0          Core 1             │
│  ┌──────────┐  ┌──────────┐         │
│  │ L1, L2   │  │ L1, L2   │         │
│  └────┬─────┘  └─────┬────┘         │
│       └──────┬────────┘             │
│         ┌────▼─────┐                │
│         │    L3    │ (shared,        │
│         │ same die │  on-chip)      │
│         └──────────┘                │
└─────────────────────────────────────┘
                ↕
              RAM (separate sticks on motherboard)
```

Each connection is a bus — different names and speeds depending on what is connected:

| Connection | Interconnect | Speed |
|---|---|---|
| L1 ↔ L2 | internal core bus | fastest |
| L2 ↔ L3 | vendor-specific on-chip interconnect (ring bus, mesh, Infinity Fabric, etc.) | fast |
| L3 ↔ RAM | memory bus (DDR5 etc.) | slower |
| RAM ↔ GPU | PCIe | slower still |

### Cache Behavior

#### Eviction

Each cache level has a **fixed size** — copies accumulate until the cache is full, at which point an **eviction policy** decides what to discard to make room for new data:

```
Typical ranges (modern CPUs):
L1  32–64 KB    per core
L2  512 KB–2 MB per core
L3  tens of MB  shared across cores
```

Common eviction policies:

| Policy | Description |
|--------|-------------|
| **LRU** (Least Recently Used) | Evict whatever was used longest ago |
| **LFU** (Least Frequently Used) | Evict whatever was used least often |
| **Random** | Evict a random entry (simpler hardware) |

Hardware caches typically use approximations of LRU (pseudo-LRU) because exact LRU is too expensive to implement in hardware at high associativity.

The cache is effectively a **fixed-size sliding window** of the most recently used data — constantly filling up and discarding stale copies to stay relevant to what the CPU needs next.

#### Coherency

In a multi-core system, each core has its own L1 and L2 caches, so the same memory address may exist as copies in multiple caches simultaneously. If one core modifies its copy, the other cores' copies become stale. Hardware **cache coherency protocols** (such as MESI) ensure that all cores see a consistent view of memory by tracking which caches hold copies of each line and invalidating or updating them when a write occurs. This happens automatically in hardware — the programmer does not manage it directly — but it has performance implications: frequent writes to shared data force cross-core invalidation traffic, which is one reason why concurrent programming benefits from minimizing shared mutable state.

## Python Connection

Understanding Von Neumann architecture explains several Python behaviors.

### Why Python Objects Have Overhead

Every Python object lives in memory with metadata:

```python
import sys

x = 42
print(sys.getsizeof(x))  # 28 bytes, not 4!
```

The 28 bytes include a reference count, type pointer, and the integer value — all stored in the same memory space. Note that `sys.getsizeof()` reports the object's own size; objects that reference other objects (like lists) consume additional memory not counted here.

### Why Memory Access Patterns Matter

NumPy arrays are faster than Python lists for several compounding reasons:

```python
import numpy as np

# Contiguous memory - CPU cache can work efficiently
arr = np.zeros(1_000_000)  # One block in memory

# Scattered objects - unpredictable access patterns
lst = [0.0] * 1_000_000    # Million separate objects
```

NumPy's speed comes from: contiguous memory layout (cache-friendly), vectorized C loops (no Python interpreter overhead per element), and SIMD instructions that process multiple values in a single CPU operation. Memory locality is one contributing factor, but not the whole story.

## Historical Context

The architecture is named after mathematician John von Neumann, who described the stored-program concept in the 1945 "First Draft of a Report on the EDVAC." The ideas were developed collaboratively with J. Presper Eckert and John Mauchly, among others — the attribution to Von Neumann alone is a historical simplification.

| Era | Approach |
|-----|----------|
| **Before (e.g. ENIAC, 1945)** | Programs hardwired via physical switches and cables; changing a program took days |
| **EDVAC report (1945)** | Von Neumann's "First Draft" described the stored-program concept |
| **EDSAC (1949)** | One of the first machines to run a stored program in practice |
| **Modern CPUs** | Still fundamentally Von Neumann, with Harvard-style caches mitigating the bottleneck |

## Summary

| Concept | Description |
|---------|-------------|
| **Stored Program** | Instructions and data share the same memory |
| **Sequential Model** | Programmer-visible execution is sequential; hardware optimizations happen underneath |
| **Shared Memory Path** | CPU and memory communicate through a shared pathway |
| **Bottleneck** | Shared instruction/data path limits throughput; mitigated by caches and Harvard-style L1 split |
| **Memory Hierarchy** | Registers → L1/L2/L3 cache → RAM → Disk bridges the speed gap |

The Von Neumann architecture remains the dominant model for CPUs today. Understanding it — and its bottleneck — explains why cache-friendly programming patterns (like vectorization and contiguous array access) matter, and why the gap between CPU speed and memory speed is a fundamental constraint in computing.
