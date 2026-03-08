# CPU Basics

## What is a CPU?

The **Central Processing Unit (CPU)** is the hardware component responsible for executing machine instructions. It performs arithmetic, logic, and control operations.

> **Scope note**: The following diagram is a simplified conceptual model — not a representation of modern CPU architecture. Modern CPUs include instruction decoders, branch predictors, load/store units, reorder buffers, and multiple execution units, and distribute control logic across many pipeline stages rather than using a single centralized control unit.

```
Conceptual CPU Model (Simplified)
┌─────────────────────────────────────────────────────────────┐
│                          CPU                                │
│                                                             │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│   │   Control    │    │     ALU      │    │   Registers  │ │
│   │    Unit      │◀──▶│              │◀──▶│              │ │
│   └──────────────┘    └──────────────┘    └──────────────┘ │
│          │                   │                    │        │
│          └───────────────────┼────────────────────┘        │
│                              │                             │
│                       ┌──────┴──────┐                      │
│                       │    Cache    │                      │
│                       │  (L1, L2)   │                      │
│                       └──────┬──────┘                      │
└──────────────────────────────┼──────────────────────────────┘
                               │
                          To Memory
```

Modern CPUs distribute control across many pipeline stages and execution units rather than relying on a single centralized control unit.

## The Instruction Cycle

Before examining each component, it helps to understand the fundamental cycle that drives everything:

```
┌─────────┐     ┌─────────┐     ┌───────────┐     ┌───────────┐
│  FETCH  │ ──▶ │ DECODE  │ ──▶ │  EXECUTE  │ ──▶ │ WRITEBACK │
└─────────┘     └─────────┘     └───────────┘     └─────────┬─┘
     ▲                                                        │
     └────────────────────────────────────────────────────────┘
```

1. **Fetch**: Read the next instruction from memory (address stored in Program Counter)
2. **Decode**: Determine what operation the instruction specifies
3. **Execute**: Perform the operation (arithmetic, logic, memory access, etc.)
4. **Writeback**: Store results back to registers or memory

This cycle repeats continuously. Modern CPUs expand this conceptual cycle into many pipeline stages (often 10–20) and execute instructions out of order, with hundreds of instructions in flight simultaneously. Modern pipelines also include stages such as register renaming, instruction scheduling, and retirement. Every component described below plays a role in one or more of these stages.

## Conceptual CPU Components

### Control Unit (CU)

The control unit orchestrates CPU operations:

- **Fetches** instructions from memory
- **Decodes** instructions to determine what operation to perform
- **Signals** other components to execute the operation
- **Manages** the program counter (tracks which instruction is next)

### Arithmetic Logic Unit (ALU)

The ALU performs actual computations:

| Operation Type | Examples |
|---------------|----------|
| **Arithmetic** | Addition, subtraction, multiplication, division (multiplication and division often use separate execution units) |
| **Logic** | AND, OR, NOT, XOR |
| **Comparison** | Equal, greater than, less than |
| **Bit Shifting** | Left shift, right shift |

### Registers

Registers are the fastest storage in a computer—small memory cells inside the CPU itself:

```
┌─────────────────────────────────────────┐
│              CPU Registers              │
├─────────────────────────────────────────┤
│  Program Counter (PC)    │ Next instruction address │
│  Instruction Register    │ Current instruction      │
│  General Purpose         │ Data and computation     │
│  Stack Pointer           │ Top of call stack        │
│  Flags/Status            │ Comparison results       │
└─────────────────────────────────────────┘
```

Registers typically have a fixed width (e.g., 32-bit or 64-bit), which influences:

- Maximum addressable memory
- Size of numbers that can be processed in one operation

The architecture designation (e.g., x86 vs x86-64) is determined by the ISA design as a whole — including register width, address space, and instruction encoding — not by register size alone.

## Instruction Execution

### Machine Instructions

At the lowest level, CPUs execute **machine instructions**—binary patterns that specify operations:

```
Example x86 instruction (simplified):

ADD EAX, EBX    ; Add register EBX to EAX

Binary: 01 D8   ; The actual bytes the CPU sees
```

Each instruction type has an **opcode** (operation code) that tells the CPU what to do. Note that x86 instructions are **variable length** — different instructions may occupy different numbers of bytes. Not all architectures work this way; ARM, for example, uses fixed-length instructions.

### Instruction Categories

| Category | Purpose | Example |
|----------|---------|---------|
| **Data Movement** | Move data between locations | `MOV`, `LOAD`, `STORE` |
| **Arithmetic/Logic** | Mathematical and boolean operations, comparisons | `ADD`, `SUB`, `MUL`, `AND`, `CMP` |
| **Control Flow** | Change execution order | `JMP`, `CALL`, `RET` |

### The Execution Pipeline

Modern CPUs overlap instruction stages for efficiency:

```
Time ──────────────────────────────────────▶

Instruction 1:  [Fetch][Decode][Execute][Write]
Instruction 2:        [Fetch][Decode][Execute][Write]
Instruction 3:              [Fetch][Decode][Execute][Write]
Instruction 4:                    [Fetch][Decode][Execute][Write]
```

This **pipelining** allows multiple instructions to be in-flight simultaneously — different stages of different instructions overlap in time. This is distinct from **superscalar execution**, which issues multiple instructions per cycle through parallel execution units. Together they provide two forms of parallelism:

- **Pipeline parallelism**: Different stages of different instructions execute simultaneously
- **Superscalar parallelism**: Multiple instructions are issued and executed per cycle

Pipelining introduces **hazards** — situations where the next instruction cannot proceed immediately:

- **Data hazards**: An instruction depends on the result of a previous instruction (often mitigated using forwarding — bypassing intermediate results directly between stages)
- **Control hazards**: A branch instruction makes the next instruction uncertain
- **Structural hazards**: Two instructions need the same hardware resource

Modern CPUs address these with **out-of-order execution** (reordering instructions to avoid stalls) and **branch prediction** (speculatively executing the likely path of a branch).

## CPU and Memory Interaction

### The Memory and Storage Hierarchy

CPUs access data through a hierarchy of increasingly slower (but larger) storage:

```
Speed                              Size
  ▲    Memory Hierarchy               ▲
  │   ┌──────────┐                   │
  │   │ L1 Cache │  tens of KB        │
  │   ├──────────┤                   │
  │   │ L2 Cache │  hundreds of KB   │
  │   ├──────────┤    to a few MB    │
  │   │ L3 Cache │  tens of MB       │
  │   ├──────────┤                   │
  │   │   RAM    │  GBs              │
  │   ├──────────┤                   │
  │    Secondary storage             │
  │   ├──────────┤                   │
  │   │ SSD/Disk │  hundreds of GB+  │
  │   └──────────┘                   │
  │                                  │
```

CPUs contain dozens of architectural registers plus additional vector and floating-point registers. Registers are part of the CPU datapath rather than the memory hierarchy proper — they are where the ALU operates directly on data. L3 cache is typically shared across multiple cores.

### Access Latency

Approximate cycles to access different levels:

| Level | Latency (order-of-magnitude cycles) |
|-------|--------------------------------------|
| Register | ~1 cycle |
| L1 Cache | ~4 cycles |
| L2 Cache | ~12 cycles |
| L3 Cache | ~40 cycles |
| RAM | ~200 cycles |

Exact latency varies by CPU model and workload. Cycles are more stable than nanoseconds for comparison because nanoseconds depend on clock speed. Two aspects of memory performance matter:

- **Latency**: Time to access a single value
- **Bandwidth**: How much data can be transferred per second

Both constrain performance, especially in scientific computing. Many data-intensive workloads (such as large matrix operations) are limited by memory bandwidth rather than latency.

This is why cache-friendly memory access patterns can dramatically improve performance. When the CPU loads a value from memory, it fetches the entire **cache line** (typically 64 bytes) containing that value. Two forms of locality exploit this:

- **Spatial locality**: Nearby data is likely to be accessed soon (sequential array traversal)
- **Temporal locality**: Recently accessed data is likely to be accessed again (loop variables)

Sequential memory access therefore performs much better than random access, because nearby data is already in cache. In parallel code, multiple threads modifying data in the same cache line can cause performance problems known as **false sharing**.

## Python's Perspective

### Python Bytecode vs Machine Code

Most Python implementations (like CPython) execute bytecode via an interpreter rather than running directly on the CPU:

```
┌─────────────┐     ┌─────────────┐     ┌──────────────────┐
│ Python Code │ ──▶ │  Bytecode   │ ──▶ │   Interpreter    │
│   (.py)     │     │  (.pyc)     │     │   Loop (C code)  │
└─────────────┘     └─────────────┘     └────────┬─────────┘
                                                 │
                                        Machine Instructions
                                           (on CPU)
```

CPython **interprets** bytecode rather than compiling it to native machine code. The interpreter is itself a compiled C program that reads each bytecode instruction and dispatches the corresponding C routine, which in turn executes as machine instructions on the CPU.

A simple Python operation becomes many machine instructions:

```python
x = a + b
```

This triggers:

1. Look up `a` in namespace dictionary
2. Look up `b` in namespace dictionary
3. Check types of both objects
4. Call appropriate `__add__` method
5. Allocate memory for result
6. Store result and bind to `x`

### Why Python is Slower Per Operation

Each Python operation involves:

- **Dynamic type checking** at runtime
- **Dictionary lookups** for variable names
- **Object allocation** on the heap
- **Reference counting** updates

Compare to C, where `x = a + b` might be a single `ADD` instruction.

> **Note**: Some Python implementations (e.g., PyPy) use JIT compilation instead of pure interpretation, significantly reducing this overhead for long-running code.

### NumPy's Advantage

NumPy bypasses Python's overhead by:

```python
import numpy as np

# Single Python call, millions of CPU operations
result = np.add(arr1, arr2)
```

The actual computation happens in compiled C code that directly uses CPU instructions — including SIMD vector instructions (e.g., AVX, SSE, NEON) that process multiple data elements simultaneously (e.g., adding 8 numbers in one instruction) — operating on contiguous memory. Many scientific Python libraries follow this same pattern, moving computation into compiled C or C++ extensions.

## Key CPU Metrics

| Metric | Description | Typical Value |
|--------|-------------|---------------|
| **Clock Speed** | Cycles per second | 3-5 GHz |
| **IPC** | Instructions per cycle; peak may reach ~4–6 on wide superscalar CPUs, but real workloads typically achieve far less | 2-6 |
| **Core Count** | Independent processors | 4-16 |
| **Cache Size** | Fast on-chip memory | 8-32 MB |
| **TDP** | Power consumption | 65-125W |

## Summary

Key points for Python programmers:

- The CPU executes programs through a continuous **fetch-decode-execute-writeback** cycle
- Python adds layers of abstraction above raw CPU operations — this costs performance but provides flexibility
- Vectorized libraries like NumPy exploit SIMD and cache locality to achieve high performance
- Memory access patterns significantly impact performance

Performance is often limited either by computation or by memory access — understanding which constraint dominates shapes how we write efficient code.
