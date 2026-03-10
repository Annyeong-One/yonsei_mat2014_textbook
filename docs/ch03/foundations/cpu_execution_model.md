
# CPU Execution Model


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

The **Von Neumann model** describes a computer executing instructions sequentially:

```

Fetch → Decode → Execute → Writeback

```

Conceptually, the CPU performs one instruction at a time.

However, **modern CPUs do not literally execute instructions sequentially**.  
Instead, they use a set of techniques that allow **many instructions to be processed simultaneously** while preserving the illusion of sequential execution.

These techniques include:

- **Pipelining**
- **Superscalar execution**
- **Out-of-order execution**
- **Register renaming**

Together they form the **modern CPU execution model**.

---

# 1. Instruction Pipelining

The simplest performance improvement is **pipelining**.

Instead of completing one instruction before starting the next, the CPU overlaps the stages of different instructions.

### Without Pipelining

```

Instruction A: Fetch → Decode → Execute → Write
Instruction B:                     Fetch → Decode → Execute → Write
Instruction C:                                      Fetch → Decode → Execute → Write

```

Each instruction must finish before the next begins.

---

### With Pipelining

```

Cycle:          1        2        3        4        5
Instruction A:  Fetch    Decode   Execute  Write
Instruction B:           Fetch    Decode   Execute  Write
Instruction C:                    Fetch    Decode   Execute ...

````

Multiple instructions are now **in different stages simultaneously**.

The pipeline behaves like an **assembly line**: each stage works on a different instruction.

---

### Pipeline Hazards

Pipelines can stall due to dependencies.

Example:

```python
x = a + b
y = x * c
````

The second instruction cannot execute until `x` is computed.

Modern CPUs include mechanisms such as:

* **forwarding**
* **stall detection**
* **branch prediction**

to reduce these delays.

---

# 2. Superscalar Execution

A **superscalar CPU** can issue **multiple instructions per cycle**.

Instead of one execution unit, the CPU contains several:

```
Execution Units
----------------
ALU 1
ALU 2
Floating Point Unit
Load/Store Unit
Vector Unit
```

If instructions are independent, they can execute simultaneously.

Example:

```
a = b + c
d = e + f
g = h * i
```

All three operations may execute in parallel.

Modern CPUs typically issue **2–6 instructions per cycle**.

---

# 3. Out-of-Order Execution

Programs are written sequentially, but CPUs may execute instructions **in a different order** to avoid stalls.

Example instruction sequence:

```
1. LOAD A
2. LOAD B
3. ADD C
```

If instruction 2 waits on memory, instruction 3 may execute first.

```
Original order:   1 → 2 → 3
Execution order:  1 → 3 → 2
```

The CPU ensures that the **final result remains identical to sequential execution**.

This is called **out-of-order execution**.

---

### Why Out-of-Order Execution Exists

Memory operations are slow.

Typical latencies:

```
Registers   ~1 cycle
L1 cache    ~4 cycles
L2 cache    ~12 cycles
L3 cache    ~40 cycles
RAM         ~100+ cycles
```

If the CPU waited for every memory access, most of its time would be idle.

Out-of-order execution allows the CPU to **keep working on other instructions while waiting**.

---

# 4. Register Renaming

Out-of-order execution introduces a problem: **false dependencies**.

Example:

```
1. r1 = a + b
2. r1 = c + d
```

Both instructions write to `r1`, so the CPU might think they must execute sequentially.

However, these instructions are actually independent.

To solve this, CPUs use **register renaming**.

---

### Architectural vs Physical Registers

The programmer sees a small set of registers.

Example (x86-64):

```
rax
rbx
rcx
rdx
...
```

These are **architectural registers**.

Internally, the CPU maintains many more **physical registers**.

Example:

```
architectural registers: 16
physical registers: ~150–200
```

The CPU dynamically maps architectural names to physical registers.

```
r1 → p37
r1 → p84
```

This allows instructions to execute independently.

---

# 5. Speculative Execution

Modern CPUs attempt to **predict future instructions**.

Example:

```
if (x > 0):
    do_A()
else:
    do_B()
```

The CPU predicts which branch will execute and **speculatively runs those instructions early**.

If the prediction is correct:

* execution continues normally.

If the prediction is wrong:

* the CPU discards the speculative work and corrects the pipeline.

This process relies on **branch prediction hardware**.

---

# 6. Preserving the Sequential Illusion

Even though the CPU executes instructions in complex ways internally, it guarantees that the program behaves **as if instructions executed sequentially**.

This is called **precise execution**.

Key mechanisms include:

* **reorder buffers**
* **commit stages**
* **instruction retirement**

These ensure that results become visible **in the original program order**.

---

# 7. Why This Matters for Python

Most Python code does not interact directly with CPU instructions.

However, the CPU execution model explains several performance behaviors.

### Independent Operations Run Faster

Independent calculations allow the CPU to use multiple execution units.

Example:

```python
a = x + y
b = u + v
c = p + q
```

These operations may execute in parallel at the hardware level.

---

### Memory Latency Dominates Performance

Many programs spend more time waiting for memory than performing computation.

This is why **cache-friendly data structures** and **vectorized libraries (NumPy)** are often much faster than Python loops.

---

### Sequential Dependencies Limit Performance

Code with strong dependencies cannot benefit from parallel execution.

Example:

```python
x = 0
for i in range(n):
    x += i
```

Each iteration depends on the previous value of `x`, limiting instruction-level parallelism.

---

# Summary

| Technique                  | Purpose                                       |
| -------------------------- | --------------------------------------------- |
| **Pipelining**             | Overlap instruction stages                    |
| **Superscalar execution**  | Execute multiple instructions per cycle       |
| **Out-of-order execution** | Avoid stalls by reordering instructions       |
| **Register renaming**      | Remove false dependencies                     |
| **Speculation**            | Predict and execute future instructions early |

Together, these mechanisms allow modern CPUs to execute **hundreds of instructions simultaneously internally**, while preserving the **simple sequential model** seen by programmers.


