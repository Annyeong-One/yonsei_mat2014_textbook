# Chapter 15: Systems and Networking

Python abstracts away the hardware — you write `x = 42` without thinking about how the CPU stores that integer in memory or how data travels between devices. Yet understanding these layers explains why some Python code is fast and some is slow, why `NumPy` outperforms pure Python loops, and why distributed computing requires different patterns than single-machine code. This chapter pulls back the curtain on hardware communication, networking, and distributed systems, then reconnects each concept to Python's execution model.

The chapter moves from the lowest level (how the CPU talks to memory and peripherals) through networking and distributed systems, and ends by connecting everything back to Python's runtime behavior.

## 15.1 Bus and Communication

- [System Bus](communication/system_bus.md)
- [CPU-Memory Communication](communication/cpu_memory.md)
- [CPU-GPU Communication](communication/cpu_gpu.md)
- [I/O and Peripherals](communication/io_peripherals.md)

## 15.2 Networking Fundamentals

- [Network Basics](networking/network_basics.md)
- [Client-Server Model](networking/client_server.md)
- [Protocols (TCP/IP, HTTP)](networking/protocols.md)
- [Latency and Bandwidth](networking/latency_bandwidth.md)
- [Local vs Remote Computation](networking/local_vs_remote.md)

## 15.3 Distributed Systems Preview

- [Single Machine vs Cluster](distributed/single_vs_cluster.md)
- [GPU Clusters](distributed/gpu_clusters.md)
- [Cloud Computing Basics](distributed/cloud_basics.md)

## 15.4 Connecting to Python

- [Hardware and Interpreted Languages](python_connection/interpreted_languages.md)
- [Why Python is Slow](python_connection/why_python_slow.md)
- [How NumPy Bridges the Gap](python_connection/numpy_bridge.md)
- [GIL and Hardware](python_connection/gil_hardware.md)
