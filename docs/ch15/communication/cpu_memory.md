
# CPU-Memory Communication

## The Memory Controller

Modern CPUs have an integrated **memory controller** that manages communication with RAM:

```

┌─────────────────────────────────────────────────────────────┐
│ CPU │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ CPU Cores │ │
│ │ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ │ │
│ │ │Core 0│ │Core 1│ │Core 2│ │Core 3│ │ │
│ │ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ │ │
│ │ └────────┼────────┼────────┘ │ │
│ │ ▼ │ │
│ │ ┌─────────────┐ │ │
│ │ │ L3 Cache │ │ │
│ │ └──────┬──────┘ │ │
│ └───────────────┼──────────────────────────────────────┘ │
│ ▼ │
│ ┌───────────────────────────────────┐ │
│ │ Integrated Memory Controller │ │
│ │ ┌─────────┐ ┌─────────┐ │ │
│ │ │Channel A│ │Channel B│ │ │
│ │ └────┬────┘ └────┬────┘ │ │
│ └───────┼─────────────────┼────────┘ │
└──────────┼─────────────────┼────────────────────────────────┘
│ │
▼ ▼
┌────────┐ ┌────────┐
│ DIMM 1 │ │ DIMM 2 │
└────────┘ └────────┘

```

---

# CPU Interconnect Fabric

Inside the processor, cores, caches, and memory controllers must communicate through an **internal interconnect network**.

This on-chip network is sometimes called the **CPU fabric** or **core interconnect**.

```

CPU Package

┌───────────────────────────────────────────────┐
│ Core │ Core │ Core │ Core │
│ │ │ │ │
│ └───────┬──────────┬──────────┬──────────┘
│ │
│ ▼
│ Shared Cache (L3)
│ │
│ ▼
│ On-Chip Interconnect Fabric
│ │
│ ▼
│ Memory Controller
└───────────────────────────────────────────────┘

```

The interconnect fabric allows communication between:

- CPU cores
- shared caches
- memory controllers
- I/O controllers

Modern processors no longer use a single shared bus internally because many cores must communicate simultaneously.

---

## Types of Interconnect Designs

Different processors use different internal topologies.

| Topology | Description |
|--------|-------------|
| **Ring** | Components connected in a circular loop |
| **Mesh** | Grid network allowing multiple simultaneous paths |
| **Crossbar** | Direct connections between many components |

Examples:

| CPU Vendor | Interconnect |
|-----------|--------------|
| Intel | Ring Bus or Mesh |
| AMD | Infinity Fabric |
| Apple | High-bandwidth on-chip fabric |

These interconnects move data between cores, caches, and memory controllers.

---

## Chiplet-Based Processors

Many modern CPUs are built from **chiplets** rather than one large chip.

Example architecture:

```

CPU Package

┌─────────────┐ ┌─────────────┐
│ Core Chiplet│ │ Core Chiplet│
│ (Cores + L3)│ │ (Cores + L3)│
└──────┬──────┘ └──────┬──────┘
│ │
└───────┬──────────┬──────────┘
▼
I/O Chiplet
(Memory controllers, PCIe, etc.)
│
▼
RAM

```

Chiplet designs allow:

- better manufacturing yield
- more cores per processor
- scalable multi-core designs

The chiplets communicate through the **interconnect fabric**.

---

# Memory Access Flow

### Read Request

```

1. CPU Core needs data at address X
   │
   ▼
2. Check L1 Cache ──── Hit? ──→ Return data (1 ns)
   │ Miss
   ▼
3. Check L2 Cache ──── Hit? ──→ Return data (3 ns)
   │ Miss
   ▼
4. Check L3 Cache ──── Hit? ──→ Return data (10 ns)
   │ Miss
   ▼
5. Memory Controller receives request
   │
   ▼
6. Controller sends address to RAM via memory bus
   │
   ▼
7. RAM retrieves data (Row → Column activation)
   │
   ▼
8. Data returns to CPU (~60 ns total from request)
   │
   ▼
9. Data cached in L1/L2/L3 for future access

```

---

# Memory Channels

Multiple channels allow parallel access:

```

Single Channel:
┌─────────────────┐
│ Memory Controller│
│ ┌──────┐ │
│ │Chan A│ │
│ └──┬───┘ │
└───────┼─────────┘
│
┌────┴────┐
│ DIMM │ Bandwidth: ~25 GB/s
└─────────┘

Dual Channel:
┌─────────────────┐
│ Memory Controller│
│ ┌──────┐ ┌──────┐│
│ │Chan A│ │Chan B││
│ └──┬───┘ └──┬───┘│
└────┼────────┼────┘
│ │
┌────┴────┐┌────┴────┐
│ DIMM ││ DIMM │ Bandwidth: ~50 GB/s
└─────────┘└─────────┘

```

---

# Channel Interleaving

Data is striped across channels for parallelism:

```

Address 0x0000 → Channel A
Address 0x0040 → Channel B
Address 0x0080 → Channel A
Address 0x00C0 → Channel B

```

Sequential access automatically uses both channels.

---

# Memory Timing

### DDR SDRAM Timing

Important parameters:

```

tCL – CAS Latency
tRCD – Row to Column Delay
tRP – Row Precharge
tRAS – Row Active Time

```

Example DDR4-3200 CL16 memory.

Total latency for a DRAM access is typically **~60–100 ns**.

---

# Cache Coherency

When multiple cores access the same memory location, caches must remain consistent.

The **MESI protocol** tracks cache states:

| State | Meaning |
|------|--------|
| Modified | Only copy, changed |
| Exclusive | Only copy, clean |
| Shared | Multiple copies |
| Invalid | Not valid |

---

# False Sharing

False sharing occurs when two threads modify data in the **same cache line**.

Even if the variables are unrelated, the cache line must bounce between cores.

This creates unnecessary coherency traffic and reduces performance.

---

# NUMA: Non-Uniform Memory Access

Multi-socket systems have local and remote memory.

```

Socket 0 ─── RAM 0
│
Inter-CPU Link
│
Socket 1 ─── RAM 1

```

Access times:

```

Local memory ~60 ns
Remote memory ~100 ns

```

Operating systems try to allocate memory close to the CPU that uses it.

---

# Summary

| Concept | Description |
|--------|-------------|
| Memory Controller | Manages CPU-RAM communication |
| CPU Interconnect | Internal network linking cores and memory |
| Channels | Parallel memory paths |
| Interleaving | Distributing addresses across channels |
| Cache Coherency | Maintaining consistent cache data |
| False Sharing | Performance loss from shared cache lines |
| NUMA | Different access times to local vs remote memory |

Key insights for Python:

- Large array operations are often **memory-bandwidth limited**
- Sequential access enables **prefetching and channel interleaving**
- Random access incurs **full DRAM latency**
- False sharing can hurt multi-threaded programs

