# CPU Basics

## What is a CPU?

The **Central Processing Unit (CPU)** is the primary component that executes program instructions. Often called the "brain" of the computer, it performs arithmetic, logic, and control operations.

```
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

## Core Components

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
| **Arithmetic** | Addition, subtraction, multiplication, division |
| **Logic** | AND, OR, NOT, XOR |
| **Comparison** | Equal, greater than, less than |
| **Bit Shifting** | Left shift, right shift |

### Registers

Registers are the fastest storage in a computer—small memory cells inside the CPU itself:

```
┌─────────────────────────────────────────┐
│              CPU Registers              │
├─────────────────────────────────────────┤
│  Program Counter (PC)  │ Next instruction address  │
│  Instruction Register  │ Current instruction       │
│  Accumulator          │ Computation results       │
│  General Purpose (R0-R15) │ Temporary data        │
│  Stack Pointer        │ Top of call stack         │
│  Flags/Status         │ Comparison results        │
└─────────────────────────────────────────┘
```

Registers are measured in bits (32-bit or 64-bit), which determines:

- Maximum addressable memory
- Size of numbers that can be processed in one operation
- Overall architecture designation (x86 vs x86-64)

## Instruction Execution

### Machine Instructions

At the lowest level, CPUs execute **machine instructions**—binary patterns that specify operations:

```
Example x86 instruction (simplified):

ADD EAX, EBX    ; Add register EBX to EAX

Binary: 01 D8   ; The actual bytes the CPU sees
```

Each instruction type has an **opcode** (operation code) that tells the CPU what to do.

### Instruction Categories

| Category | Purpose | Example |
|----------|---------|---------|
| **Data Movement** | Move data between locations | `MOV`, `LOAD`, `STORE` |
| **Arithmetic** | Mathematical operations | `ADD`, `SUB`, `MUL`, `DIV` |
| **Logic** | Boolean operations | `AND`, `OR`, `XOR`, `NOT` |
| **Control Flow** | Change execution order | `JMP`, `CALL`, `RET` |
| **Comparison** | Set flags for branching | `CMP`, `TEST` |

### The Execution Pipeline

Modern CPUs overlap instruction stages for efficiency:

```
Time ──────────────────────────────────────▶

Instruction 1:  [Fetch][Decode][Execute][Write]
Instruction 2:        [Fetch][Decode][Execute][Write]
Instruction 3:              [Fetch][Decode][Execute][Write]
Instruction 4:                    [Fetch][Decode][Execute][Write]
```

This **pipelining** allows multiple instructions to be in-flight simultaneously.

## CPU and Memory Interaction

### The Memory Hierarchy

CPUs access data through a hierarchy of increasingly slower (but larger) storage:

```
Speed                              Size
  ▲                                  ▲
  │   ┌──────────┐                   │
  │   │ Registers│  ~100 bytes       │
  │   ├──────────┤                   │
  │   │ L1 Cache │  ~64 KB           │
  │   ├──────────┤                   │
  │   │ L2 Cache │  ~256 KB          │
  │   ├──────────┤                   │
  │   │ L3 Cache │  ~8 MB            │
  │   ├──────────┤                   │
  │   │   RAM    │  ~16 GB           │
  │   ├──────────┤                   │
  │   │   SSD    │  ~500 GB          │
  │   └──────────┘                   │
  │                                  │
```

### Access Latency

Approximate cycles to access different levels:

| Level | Latency (cycles) | Latency (nanoseconds) |
|-------|-----------------|----------------------|
| Register | 1 | ~0.3 ns |
| L1 Cache | 4 | ~1 ns |
| L2 Cache | 12 | ~3 ns |
| L3 Cache | 40 | ~10 ns |
| RAM | 200+ | ~60 ns |

This explains why cache-friendly code is dramatically faster.

## Python's Perspective

### Python Bytecode vs Machine Code

Python code doesn't run directly on the CPU. Instead:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Python Code │ ──▶ │  Bytecode   │ ──▶ │ Machine Code│
│   (.py)     │     │  (.pyc)     │     │   (CPU)     │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                    CPython Interpreter
                    (executes bytecode)
```

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

### Why Python is "Slow"

Each Python operation involves:

- **Dynamic type checking** at runtime
- **Dictionary lookups** for variable names
- **Object allocation** on the heap
- **Reference counting** updates

Compare to C, where `x = a + b` might be a single `ADD` instruction.

### NumPy's Advantage

NumPy bypasses Python's overhead by:

```python
import numpy as np

# Single Python call, millions of CPU operations
result = np.add(arr1, arr2)
```

The actual computation happens in compiled C code that directly uses CPU instructions, operating on contiguous memory.

## Key CPU Metrics

| Metric | Description | Typical Value |
|--------|-------------|---------------|
| **Clock Speed** | Cycles per second | 3-5 GHz |
| **IPC** | Instructions per cycle | 2-6 |
| **Core Count** | Independent processors | 4-16 |
| **Cache Size** | Fast on-chip memory | 8-32 MB |
| **TDP** | Power consumption | 65-125W |

## Summary

The CPU executes programs through:

1. **Fetch**: Get instruction from memory
2. **Decode**: Determine what operation to perform
3. **Execute**: ALU performs the computation
4. **Write Back**: Store results

Key points for Python programmers:

- Python adds layers of abstraction above raw CPU operations
- This abstraction costs performance but provides flexibility
- Understanding CPU basics explains why vectorized NumPy code is fast
- Memory access patterns significantly impact performance

The CPU's speed is ultimately limited by memory bandwidth—a constraint that shapes how we write efficient code.
