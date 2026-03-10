
# Time vs Space


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Efficient programs balance **time complexity** and **space complexity**. Understanding this trade-off is essential for writing performant Python code.

---

## Time complexity

Time complexity measures how execution time grows with input size.

Common classes:

- O(1): constant time
- O(log n): logarithmic
- O(n): linear
- O(n log n), O(n²): increasingly expensive

In Python, constant factors also matter.

---

## Space complexity

Space complexity measures memory usage:

- stack usage (call frames),
- heap usage (objects, containers),
- temporary allocations.

Faster algorithms often use more memory.

---

## Trade-offs in practice

Examples:

- caching results speeds up computation but uses memory,
- precomputing arrays avoids recomputation,
- vectorization trades memory for speed.

```python
# trade memory for speed
cache = {}
````

These techniques shift work from **computation time** to **memory usage**.

---

## Hardware trade-offs: prefetching and speculation

Modern CPUs also make trade-offs between **time and wasted work**.

Because main memory is much slower than the CPU, processors try to predict what data or instructions will be needed next.

Two important techniques are **prefetching** and **speculative execution**.

### Prefetching

Memory latency is high compared to CPU speed:

```
L1 cache   ~4 cycles
L2 cache   ~12 cycles
L3 cache   ~40 cycles
RAM        ~100+ cycles
```

To hide this delay, CPUs attempt to **prefetch data before it is needed**.

Example sequential access pattern:

```python
for i in range(n):
    total += arr[i]
```

The hardware detects the sequential pattern and loads upcoming cache lines into the cache ahead of time.

This means that when the CPU needs the data, it is **already waiting in cache**.

However, prefetching is a trade-off:

* Correct predictions reduce latency.
* Incorrect predictions waste memory bandwidth and cache space.

---

### Speculative execution

CPUs also try to predict **future instructions**, especially around conditional branches.

Example:

```python
if price > threshold:
    execute_trade()
else:
    log_event()
```

The CPU may predict which branch will execute and start running those instructions **before the condition is fully evaluated**.

If the prediction is correct:

* execution continues without delay.

If the prediction is wrong:

* the speculative work is discarded and the pipeline is restarted.

This improves average performance but occasionally performs **wasted work**.

---

## Why this matters for Python

Python programs do not directly control hardware features like speculation or prefetching, but program structure still affects how well the CPU can use them.

Examples:

* **Sequential memory access** benefits from hardware prefetching.
* **Vectorized NumPy operations** allow the CPU to process predictable streams of data.
* **Random memory access** defeats prefetching and slows programs.

Designing algorithms with predictable memory access patterns often leads to better performance.

---

## Financial computing

In quantitative finance:

* latency matters in trading,
* memory matters in simulations,
* robustness matters more than micro-optimizations.

Choosing the right trade-offs depends on the application.

---

## Key takeaways

* Faster algorithms often use more memory.
* Hardware also makes performance trade-offs internally.
* Prefetching hides memory latency by predicting future accesses.
* Speculative execution predicts future instructions.
* Optimize only after correctness.

