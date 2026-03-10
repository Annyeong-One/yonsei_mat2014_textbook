
# System Bus

## What is a Bus?

A **bus** is a communication pathway that transfers data between computer components. Think of it as a highway system connecting different parts of the computer.

```

┌─────────────────────────────────────────────────────────────┐
│ System Bus │
│ ═══════════════════════════════════════════════════════ │
│ │ │ │ │ │
│ ┌───┴───┐ ┌───┴───┐ ┌───┴───┐ ┌───┴───┐ │
│ │ CPU │ │ RAM │ │ GPU │ │ I/O │ │
│ └───────┘ └───────┘ └───────┘ └───────┘ │
└─────────────────────────────────────────────────────────────┘

```

## Bus Components

A bus consists of three types of lines:

### 1. Address Bus

Specifies **where** to read/write data.

### 2. Data Bus

Transfers **actual data** between components.

### 3. Control Bus

Carries **command signals** such as:

- Read / Write
- Clock
- Interrupt
- Bus Request / Grant

---

# Bus Operation

### Read Operation

```

CPU wants to read from address 0x1000:

1. CPU places 0x1000 on Address Bus
2. CPU sets Read signal
3. Memory retrieves data
4. Memory places data on Data Bus
5. CPU reads data

```

### Write Operation

```

CPU writes value to memory:

1. Address placed on Address Bus
2. Data placed on Data Bus
3. Write signal asserted
4. Memory stores value

```

---

# Bus Hierarchy

Modern computers use **multiple buses at different speeds**.

```

CPU Internal Bus (registers ↔ ALU ↔ cache)

↓
CPU Interconnect / Fabric

↓
Memory Bus (DDR4 / DDR5)

↓
PCIe Bus (GPU, SSD, devices)

```

The closer the bus is to the CPU, the **higher the bandwidth and lower the latency**.

---

# Bus Speed and Bandwidth

Bandwidth depends on bus width and clock speed.

Example:

```

Bandwidth = Bus Width × Clock Speed × Transfers per Clock

Example DDR4-3200:
Width = 64 bits = 8 bytes
Clock = 1600 MHz
DDR transfers = 2 per clock

Bandwidth ≈ 25 GB/s per channel

```

---

# PCIe: Modern Expansion Bus

PCIe is the main **device communication bus** used for GPUs, SSDs, and high-speed peripherals.

Example lane configurations:

```

x1  ≈ 2 GB/s
x4  ≈ 8 GB/s
x8  ≈ 16 GB/s
x16 ≈ 32 GB/s

```

---

# Bus Contention

Only **one device can use a shared bus at a time**.

If multiple devices request the bus simultaneously:

```

Device A: request → transfer
Device B: request → wait
Device C: request → wait

```

This situation is called **bus contention**.

---

# Bus Arbitration

To resolve contention, hardware uses **bus arbitration**.

A **bus arbiter** decides which device gains control of the bus.

Common strategies include:

| Method | Description |
|------|-------------|
| Priority-based | Higher priority devices win |
| Round-robin | Devices take turns |
| First-come-first-served | Queue-based |

Arbitration ensures orderly communication between components.

---

# Bus Mastering

In early computers, **only the CPU controlled the bus**.

Modern systems allow other devices to temporarily become **bus masters**.

A bus master can initiate transfers directly.

Examples:

- GPUs
- network cards
- disk controllers
- DMA controllers

These devices can move data without CPU involvement.

---

# Direct Memory Access (DMA)

**Direct Memory Access (DMA)** allows devices to transfer data **directly to or from RAM** without continuous CPU intervention.

Without DMA:

```

Device → CPU → RAM

```

With DMA:

```

Device → RAM

```

Example disk read operation with DMA:

```

1. CPU configures DMA controller
2. Disk reads data
3. DMA transfers data directly into RAM
4. CPU receives interrupt when transfer completes

````

Advantages:

- reduces CPU workload
- allows parallel CPU computation
- improves overall system throughput

DMA is heavily used by:

- disk controllers
- network cards
- GPUs
- high-speed storage devices

---

# Python Perspective

### Memory Bandwidth Limits

Large array operations are often limited by **memory bus bandwidth**, not CPU speed.

```python
import numpy as np
import time

arr = np.random.rand(125_000_000)

start = time.perf_counter()
np.sum(arr)
elapsed = time.perf_counter() - start

bandwidth = arr.nbytes / elapsed / 1e9
print(f"Bandwidth: {bandwidth:.1f} GB/s")
````

Typical systems achieve **30–40 GB/s**.

---

# Summary

| Concept         | Description                          |
| --------------- | ------------------------------------ |
| Address Bus     | Specifies memory location            |
| Data Bus        | Transfers actual data                |
| Control Bus     | Command signals                      |
| Bus Arbitration | Determines which device uses the bus |
| Bus Mastering   | Devices initiating transfers         |
| DMA             | Direct device ↔ memory transfers     |
| PCIe            | High-speed device bus                |

Key insights:

* Only one device uses a bus at a time
* Arbitration resolves competing requests
* DMA allows devices to bypass the CPU
* Bus bandwidth can limit system performance

