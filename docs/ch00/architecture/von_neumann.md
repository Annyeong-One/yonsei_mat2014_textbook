
# Von Neumann Architecture


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

The **Von Neumann architecture** is the foundational design for nearly all modern computers.  
It describes a system where **program instructions and data share the same memory space**.

This idea is called the **stored-program model**.

In this model, a computer consists of:

- a **Central Processing Unit (CPU)**
- **memory**
- **input/output devices**
- a **communication system (bus)** connecting them

![Von Neumann architecture](image/von_neumann.png)

*Figure: Simplified Von Neumann architecture showing the CPU, memory,
system bus, and I/O devices.*

The key innovation was that **program instructions are stored in the same memory as data and encoded as binary numbers** representing operations defined by the processor's **instruction set architecture (ISA)**, allowing programs to be loaded, modified, and executed dynamically.

---

# Key Components

## Central Processing Unit (CPU)

The CPU executes program instructions.

In simplified models, the CPU is often described as consisting of three main parts.
Modern CPUs contain many additional components (such as pipelines, caches, and branch predictors), but the CU–ALU–register model captures the essential structure.

| Component | Function |
|----------|----------|
| **Control Unit (CU)** | Fetches, decodes, and coordinates the execution of instructions |
| **Arithmetic Logic Unit (ALU)** | Performs basic integer arithmetic and logical operations |
| **Registers** | Small, fast storage inside the CPU |

Two important registers are:

| Register | Purpose |
|--------|--------|
| **Program Counter (PC)** | Address of the next instruction; normally increments sequentially but changes on jumps, branches, or function calls |
| **Instruction Register (IR)** | The instruction currently being executed |

Registers are the **fastest storage accessible to the CPU**.

---

## Memory (RAM)

Main memory stores both:

- **program instructions**
- **program data**

Each memory location has a unique **numeric address**.

For example, assuming 4-byte instructions:

```
Address      Content
0x1000       LOAD A
0x1004       ADD B
0x1008       STORE C
```

The CPU reads instructions from memory and executes them sequentially.

Early machines such as **ENIAC initially required manual rewiring or plugboard configuration**, which made reprogramming slow and cumbersome.
The stored-program concept allowed software to be loaded directly into memory.

---

## Bus System

In simplified models, the connection between components is called the **system bus**.

A bus consists of multiple signal lines grouped into three categories.

### Address Bus

Specifies **which memory location** is accessed. The address bus is **unidirectional** (CPU to memory).

```
CPU ───── Address Bus ─────▶ Memory
```

### Data Bus

Transfers **actual data**. The data bus is **bidirectional** (CPU can read from or write to memory).

```
CPU ◀──── Data Bus ────▶ Memory
```

### Control Bus

Carries **timing and control signals** that coordinate memory reads, writes, and other operations.

Examples:

- read
- write
- interrupt
- clock

Together these buses allow the CPU, memory, and I/O devices to communicate.

---

# The Fetch–Decode–Execute Cycle

Programs execute through a repeating loop called the **instruction cycle**.

```
Fetch → Decode → Execute → Writeback
```

### 1. Fetch

The CPU **fetches** the instruction at the address stored in the **Program Counter**.
During the fetch stage, the CPU places the instruction address on the address bus and reads the instruction through the data bus.

### 2. Decode

The Control Unit **decodes** the instruction.

### 3. Execute

The ALU or other hardware performs the operation.

### 4. Writeback

The result is stored in registers or memory.

### 5. Repeat

The Program Counter moves to the next instruction.

This process continues until the program terminates.

---

# The Von Neumann Bottleneck

The Von Neumann bottleneck arises because both instructions and data must travel between the CPU and memory over the same communication channel.

```
CPU  ◀════════════════════▶  Memory
(instructions and data
share the same path)
```

As CPUs became faster than memory systems, the processor **often stalls waiting for data from memory** rather than performing computations.

The CPU stalls because:

- **memory bandwidth** is limited relative to CPU speed
- **memory latency** adds delay to every access
- instruction fetches **compete** with data accesses for the same channel

Early computers used a single memory interface for both instructions and data, forcing them to compete for the same bandwidth.
This growing gap between processor speed and memory speed is called the **memory wall**.

Modern processors mitigate the bottleneck using techniques such as caching, prefetching, and pipelining.

---

# Memory Hierarchy

To reduce memory delays, modern computers use a **hierarchy of storage layers**.
The memory hierarchy forms a pyramid: smaller, faster memories are closer to the CPU, while larger, slower memories are farther away.

```
            ┌─────────────┐
            │  Registers  │
            │  ~1 cycle   │
            └─────────────┘
                   ▲
            ┌─────────────┐
            │   L1 Cache  │
            │   3–5 cyc   │
            └─────────────┘
                   ▲
            ┌─────────────┐
            │   L2 Cache  │
            │  10–15 cyc  │
            └─────────────┘
                   ▲
            ┌─────────────┐
            │   L3 Cache  │
            │  30–50 cyc  │
            └─────────────┘
                   ▲
            ┌─────────────┐
            │     RAM     │
            │ 100–300 cyc │
            └─────────────┘
                   ▲
            ┌─────────────┐
            │  SSD / Disk │
            └─────────────┘

   ↑ Faster, smaller
   ↓ Larger, slower
```

### Typical Memory Latencies

The difference between storage layers is dramatic.
The following approximate values illustrate the gap between CPU and memory speeds.

| Operation | Approximate Latency |
|---|---|
| CPU register access | ~1 cycle |
| L1 cache access | ~1 ns |
| L2 cache access | ~3–5 ns |
| L3 cache access | ~10–20 ns |
| Main memory (RAM) | ~100 ns |
| SSD access | ~100 µs |
| Disk seek (HDD) | ~5–10 ms |

These differences explain why caches and memory locality are critical for performance.

Each layer stores a **temporary copy of frequently used data**.
Upper levels are smaller but faster; lower levels are larger but slower.

The memory hierarchy works because programs exhibit two key patterns:

- **Temporal locality**: programs tend to reuse recently accessed data
- **Spatial locality**: programs tend to access nearby memory locations

Caches exploit these patterns to keep the most relevant data close to the CPU.

Disk and SSD are included in the hierarchy because operating systems use **virtual memory**, allowing programs to access storage as if it were memory.

---

# Harvard Architecture: A Contrast

The **Harvard architecture** separates instruction memory from data memory.

```
Harvard Architecture

Instruction Memory ──▶ CPU ◀── Data Memory
```

This removes the competition between instruction fetches and data accesses.

Most modern CPUs use a **modified Harvard architecture**:

- instructions and data share main memory
- but the CPU uses **separate instruction and data caches**

This provides many of Harvard's advantages while keeping a unified memory model.

### Harvard Architecture in Practice

Some systems implement a true Harvard architecture. Many microcontrollers
(such as AVR and PIC devices) use separate instruction and data memories,
allowing instructions and data to be accessed simultaneously.

Modern desktop and server CPUs typically use a **modified Harvard architecture**.
Main memory remains unified, but the processor uses separate instruction and
data caches, often called **L1I (instruction cache)** and **L1D (data cache)**.
L2 and L3 caches are usually unified.

```
        CPU
       /   \
   L1I      L1D
    |        |
      L2 (Unified)
         |
      L3 Cache
         |
      RAM
```

This design allows the CPU to fetch instructions and access data in parallel,
reducing the effects of the Von Neumann bottleneck while preserving a unified
memory model for software.

---

# Why Architecture Matters for Python

Understanding Von Neumann architecture explains key Python performance behaviors.

## Memory Locality

Python lists store **contiguous pointers**, but the objects those pointers reference are scattered across memory.
Each access requires an additional level of **indirection**, following a pointer to a different memory location. This pattern, called **pointer chasing**, defeats spatial locality and causes frequent cache misses, which slows down sequential iteration.

NumPy arrays store values in **contiguous memory**, which aligns with how caches work.

```python
import numpy as np

arr = np.zeros(1_000_000)     # contiguous memory block
lst = [0.0] * 1_000_000       # many separate objects scattered in memory
```

NumPy arrays are faster because:

- data is contiguous, exploiting **spatial locality**
- fewer objects means less memory overhead
- the CPU cache can prefetch sequential data efficiently

---

## Object Memory Overhead

Every Python object carries metadata beyond its value.

```python
import sys

x = 42
print(sys.getsizeof(x))
```

The memory size includes:

- reference count
- type information
- stored value

This larger memory footprint increases cache pressure and memory bandwidth usage.
A Python list of integers uses far more memory than a NumPy array of the same numbers, because each integer is a full object stored separately in memory.

---

# Historical Context

The architecture is named after **John von Neumann**, who formally documented the stored-program concept in the 1945 *First Draft of a Report on the EDVAC*.

The ideas were developed with contributions from:

* J. Presper Eckert
* John Mauchly
* other early computer scientists

Early machines such as **EDSAC (1949)** implemented the stored-program model in practice.

Modern processors still follow the same fundamental architecture.

---

# Summary

| Concept                | Description                        |
| ---------------------- | ---------------------------------- |
| Stored Program         | Instructions and data share memory |
| CPU Components         | Control unit, ALU, registers       |
| Bus System             | Connects CPU, memory, and devices  |
| Instruction Cycle      | Fetch → Decode → Execute → Writeback |
| Von Neumann Bottleneck | Shared memory path limits speed    |
| Memory Hierarchy       | Registers → Cache → RAM → Storage  |
| Modified Harvard       | Split instruction and data caches  |

The Von Neumann architecture remains the dominant model for general-purpose computers.
Understanding it provides the foundation for reasoning about performance, memory behavior, and program execution.

