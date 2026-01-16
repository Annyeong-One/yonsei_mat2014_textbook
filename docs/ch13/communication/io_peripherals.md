# I/O and Peripherals

## Input/Output Overview

**I/O (Input/Output)** refers to communication between the computer and external devices:

```
┌─────────────────────────────────────────────────────────────┐
│                         Computer                            │
│                                                             │
│  ┌─────────┐    ┌──────────────────┐    ┌───────────────┐  │
│  │   CPU   │◀══▶│   I/O Controller │◀══▶│  Peripherals  │  │
│  └─────────┘    │   (Chipset/PCH)  │    │               │  │
│                 └──────────────────┘    │ - Keyboard    │  │
│                         ▲               │ - Mouse       │  │
│                         │               │ - Storage     │  │
│  ┌─────────┐            │               │ - Network     │  │
│  │   RAM   │◀═══════════╯               │ - Display     │  │
│  └─────────┘                            └───────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## I/O Methods

### 1. Programmed I/O (Polling)

CPU actively checks device status:

```
CPU Polling Loop:

while True:
    status = read_device_status()
    if status == READY:
        data = read_device_data()
        break
    # CPU wastes cycles waiting!
```

**Pros**: Simple
**Cons**: Wastes CPU cycles

### 2. Interrupt-Driven I/O

Device signals CPU when ready:

```
Interrupt Flow:

1. CPU initiates I/O operation
2. CPU continues other work
3. Device completes → sends interrupt
4. CPU pauses current work
5. CPU handles interrupt (reads data)
6. CPU resumes previous work

┌─────────────────────────────────────────────────────────────┐
│ CPU: [Work][Work][Work][Int][Work][Work][Work][Int][Work]   │
│                         ▲                     ▲             │
│                     Keyboard              Network           │
│                     interrupt             interrupt         │
└─────────────────────────────────────────────────────────────┘
```

### 3. Direct Memory Access (DMA)

Device transfers data directly to memory:

```
DMA Transfer:

┌─────┐                              ┌─────────┐
│ CPU │ 1. Setup DMA                 │ Device  │
│     │────────────────────────────▶ │         │
└─────┘                              └────┬────┘
                                          │
   2. CPU does other work                 │ 3. Device transfers
                                          │    directly to RAM
┌─────────┐                               │
│   RAM   │◀──────────────────────────────┘
└─────────┘
                                     4. DMA complete interrupt
```

**Pros**: CPU free during transfer, high throughput
**Cons**: Complex setup, memory contention

## Common I/O Interfaces

### USB (Universal Serial Bus)

```
USB Speed Comparison:
┌──────────────┬────────────┬────────────────────┐
│   Version    │  Speed     │   Common Use       │
├──────────────┼────────────┼────────────────────┤
│ USB 2.0      │ 480 Mbps   │ Keyboards, mice    │
│ USB 3.0      │ 5 Gbps     │ External drives    │
│ USB 3.1      │ 10 Gbps    │ Fast storage       │
│ USB 3.2      │ 20 Gbps    │ Docks, displays    │
│ USB4         │ 40 Gbps    │ High-speed I/O     │
└──────────────┴────────────┴────────────────────┘
```

### SATA vs NVMe

```
Storage Interface Comparison:

SATA III:
┌─────┐                    ┌─────────┐
│ CPU │──── SATA ─────────▶│  SSD    │
└─────┘   (~600 MB/s)      └─────────┘

NVMe (PCIe):
┌─────┐                    ┌─────────┐
│ CPU │──── PCIe ─────────▶│  SSD    │
└─────┘   (~7,000 MB/s)    └─────────┘
```

### Network Interfaces

```
Network Speed Comparison:
┌──────────────┬────────────┬────────────────────┐
│   Type       │  Speed     │   Bandwidth        │
├──────────────┼────────────┼────────────────────┤
│ 1 GbE        │ 1 Gbps     │ ~125 MB/s          │
│ 10 GbE       │ 10 Gbps    │ ~1.25 GB/s         │
│ 25 GbE       │ 25 Gbps    │ ~3.1 GB/s          │
│ 100 GbE      │ 100 Gbps   │ ~12.5 GB/s         │
└──────────────┴────────────┴────────────────────┘
```

## I/O in Python

### File I/O (Storage)

```python
import time

# Buffered I/O (default)
start = time.perf_counter()
with open('large_file.bin', 'rb') as f:
    data = f.read()  # OS handles buffering
read_time = time.perf_counter() - start

size_mb = len(data) / 1e6
bandwidth = size_mb / read_time

print(f"Read: {bandwidth:.0f} MB/s")
```

### Network I/O

```python
import socket
import time

def measure_network_latency(host, port):
    """Measure round-trip time to server."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    message = b'ping'
    
    start = time.perf_counter()
    sock.send(message)
    response = sock.recv(1024)
    latency = time.perf_counter() - start
    
    sock.close()
    return latency * 1000  # ms

# Example
# latency = measure_network_latency('example.com', 80)
# print(f"RTT: {latency:.1f} ms")
```

### Asynchronous I/O

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    """Non-blocking HTTP request."""
    async with session.get(url) as response:
        return await response.text()

async def fetch_many(urls):
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# All requests happen concurrently, not sequentially
# results = asyncio.run(fetch_many(urls))
```

## I/O Latency Comparison

```
┌────────────────────────────────────────────────────────────┐
│                    I/O Latency Scale                       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ L1 cache:          │                            1 ns       │
│ RAM:               │████                       60 ns       │
│ NVMe SSD:          │████████████████      20,000 ns       │
│ SATA SSD:          │██████████████████   100,000 ns       │
│ HDD:               │████████████████████████████████████  │
│                                          10,000,000 ns    │
│ Network (local):   │████████████████████   100,000 ns     │
│ Network (internet):│████████████████████████████████████  │
│                                          50,000,000 ns    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## I/O-Bound vs CPU-Bound

### I/O-Bound Operations

```python
import time

# I/O-bound: waiting for external device
def io_bound_task():
    # CPU sits idle while waiting for disk/network
    with open('large_file.bin', 'rb') as f:
        data = f.read()  # CPU waits for disk
    return data

# Threading helps I/O-bound tasks
from concurrent.futures import ThreadPoolExecutor

def fetch_multiple_files(file_list):
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Threads wait in parallel for I/O
        results = list(executor.map(io_bound_task, file_list))
    return results
```

### CPU-Bound Operations

```python
import numpy as np

# CPU-bound: computation keeps CPU busy
def cpu_bound_task(data):
    # CPU actively computing
    return np.sum(data ** 2)

# Multiprocessing helps CPU-bound tasks
from multiprocessing import Pool

def process_multiple_arrays(arrays):
    with Pool(processes=4) as pool:
        # Different processes on different cores
        results = pool.map(cpu_bound_task, arrays)
    return results
```

## Optimizing I/O

### Strategy 1: Buffering

```python
# Bad: Many small writes
with open('output.txt', 'w') as f:
    for i in range(1000000):
        f.write(f"{i}\n")  # Each write may hit disk

# Better: Write larger chunks
buffer = []
with open('output.txt', 'w') as f:
    for i in range(1000000):
        buffer.append(f"{i}\n")
        if len(buffer) >= 10000:
            f.write(''.join(buffer))
            buffer = []
    if buffer:
        f.write(''.join(buffer))
```

### Strategy 2: Memory Mapping

```python
import mmap
import numpy as np

# Memory-map large file
with open('huge_data.bin', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    
    # Access like memory, OS handles I/O
    data = mm[1000:2000]
    
    mm.close()

# NumPy memmap
arr = np.memmap('huge_array.dat', dtype='float64', mode='r',
                shape=(1000000000,))
# Access elements without loading entire file
subset = arr[::1000]  # Every 1000th element
```

### Strategy 3: Async I/O

```python
import asyncio

async def main():
    # Concurrent I/O operations
    results = await asyncio.gather(
        async_read_file('file1.txt'),
        async_read_file('file2.txt'),
        async_fetch_url('http://example.com'),
    )
    return results

# All three I/O operations overlap
# asyncio.run(main())
```

## Summary

| Method | How It Works | Best For |
|--------|-------------|----------|
| **Polling** | CPU checks device | Simple, low-speed |
| **Interrupts** | Device signals CPU | General purpose |
| **DMA** | Direct memory transfer | High-speed, bulk data |

| Interface | Bandwidth | Typical Use |
|-----------|-----------|-------------|
| USB 3.0 | 625 MB/s | Peripherals, storage |
| SATA III | 600 MB/s | Legacy storage |
| NVMe | 7,000 MB/s | Fast storage |
| 10 GbE | 1.25 GB/s | Networking |

Key points for Python:

- I/O operations often dominate execution time
- Use threading for I/O-bound tasks (GIL released during I/O)
- Use multiprocessing for CPU-bound tasks
- Buffering and batching reduce I/O overhead
- Async I/O enables concurrent operations
- Memory mapping avoids loading entire files
