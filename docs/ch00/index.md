

# Chapter 0: Computer Fundamentals

This chapter introduces the fundamental hardware and data concepts that underpin modern computing systems. Although many programmers interact primarily with high-level languages such as Python, all software ultimately executes on physical hardware.

Understanding the structure of computer systems helps explain:

* why some programs run faster than others
* how memory and storage influence performance
* how data is represented at the machine level
* how modern CPUs and GPUs execute programs

These topics provide the conceptual foundation required to reason about **performance, numerical computation, and large-scale data processing**.

This chapter is organized into three major sections:

1. **Computer Architecture** — how processors execute programs
2. **Memory Hierarchy** — how data moves through the system
3. **Data Representation** — how information is encoded in binary

Together these ideas form the conceptual model needed to understand the behavior of real-world computing systems.

---

## 0.1 Computer Architecture

Computer architecture describes how processors execute instructions and coordinate computation.

Although modern processors contain billions of transistors and highly complex microarchitectures, their operation can still be understood using a few core abstractions.

This section introduces the architectural concepts that explain how programs interact with hardware.

Topics include:

* the **von Neumann architecture**, which defines the stored-program model
* the structure and operation of modern **CPUs**
* how processors execute instructions and schedule work across **cores and threads**
* how **clock speed and instruction throughput** influence performance
* the design principles behind **GPUs**, which enable massive parallel computation

The goal of this section is to provide a mental model for how hardware executes software.

---

### Topics

* [Von Neumann Architecture](architecture/von_neumann.md)
  Introduces the stored-program model and the fundamental structure of modern computers, including the CPU, memory, and system bus.

* [CPU Basics](architecture/cpu_basics.md)
  Explains how processors execute instructions, including instruction pipelines, registers, caches, and vector instructions.

* [CPU Cores and Threads](architecture/cpu_cores_threads.md)
  Describes how modern processors execute multiple threads simultaneously and how operating systems schedule work across cores.

* [Clock Speed and Instructions](architecture/clock_instructions.md)
  Explains the relationship between clock frequency, instructions per cycle, and overall processor throughput.

* [GPU Architecture](architecture/gpu_architecture.md)
  Introduces the massively parallel design of GPUs and explains why they are effective for machine learning and scientific computing.

---

## 0.2 Memory Hierarchy

Memory systems determine how quickly data can move through a computer.

Although CPUs can execute billions of instructions per second, accessing main memory or storage is significantly slower. To mitigate this difference, computers organize memory into a **hierarchy of storage layers**.

Each level of the hierarchy trades off:

* capacity
* latency
* bandwidth
* cost

This section examines how data moves between these layers and how memory access patterns influence performance.

Understanding the memory hierarchy is essential for explaining:

* cache behavior
* memory locality
* data movement costs
* performance bottlenecks in numerical programs

---

### Topics

* [Memory Overview](memory/memory_overview.md)
  Introduces the layered structure of computer memory systems and the trade-offs between speed, capacity, and cost.

* [Registers and Cache](memory/registers_cache.md)
  Explains how the fastest levels of the memory hierarchy store frequently accessed data close to the CPU.

* [RAM (Main Memory)](memory/ram.md)
  Describes the structure and performance characteristics of dynamic random-access memory.

* [Virtual Memory](memory/virtual_memory.md)
  Explains how operating systems provide processes with the illusion of large continuous memory spaces.

* [Storage (SSD/HDD)](memory/storage.md)
  Introduces persistent storage technologies and explains their performance characteristics.

* [Memory Access Patterns](memory/access_patterns.md)
  Explores how the order of memory access affects cache efficiency and program performance.

---

## 0.3 Data Representation

At the lowest level, computers represent all information as **binary data**.

Numbers, text, images, and program instructions are ultimately stored as sequences of bits. Understanding how these representations work is essential for reasoning about numerical precision, data formats, and system behavior.

This section introduces the core ideas behind binary representation and the encoding schemes used in modern computing.

Topics include:

* binary number systems
* integer encoding
* floating-point arithmetic
* character encoding

These concepts form the foundation for understanding how computers process numerical and symbolic information.

---

### Topics

* [Bits and Bytes](data/bits_bytes.md)
  Introduces binary digits and the basic units used to store digital information.

* [Binary and Hexadecimal](data/binary_hexadecimal.md)
  Explains positional number systems and the relationship between binary, hexadecimal, and decimal representations.

* [Integer Representation](data/integer_representation.md)
  Describes how signed integers are stored using two’s complement representation.

* [Floating Point (IEEE 754 Preview)](data/floating_point_representation.md)
  Introduces floating-point numbers and the IEEE 754 standard used for real-number computation.

* [Character Encoding Preview](data/character_encoding.md)
  Explains how text is represented digitally using encoding schemes such as ASCII and Unicode.

---

## Chapter Summary

This chapter establishes the foundational concepts needed to understand modern computing systems.

We examined three major components of computer systems:

* **Architecture**, which describes how processors execute programs
* **Memory systems**, which determine how data moves through the machine
* **Data representation**, which explains how information is encoded digitally

Together these concepts provide the framework necessary to understand performance, numerical computation, and large-scale data processing in modern software systems.

Subsequent chapters will build upon these foundations to explore **numerical algorithms, performance optimization, and scientific computing techniques** in greater depth.
