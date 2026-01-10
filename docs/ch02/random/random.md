# Random Numbers and Simulation

Random number generation is essential for Monte Carlo simulation, risk analysis, and stochastic modeling.

---

## 1. Random number generators

NumPy provides a modern random API:

```python
import numpy as np

rng = np.random.default_rng(seed=42)
```

Using an explicit generator is preferred over global state.

---

## 2. Common distributions

```python
rng.standard_normal(size=1000)
rng.uniform(0.0, 1.0, size=1000)
rng.normal(loc=0.0, scale=1.0, size=1000)
```

Many distributions are available.

---

## 3. Reproducibility

Setting a seed ensures reproducible results:

```python
rng = np.random.default_rng(123)
```

This is essential for debugging and research.

---

## 4. Monte Carlo simulation example

```python
Z = rng.standard_normal(1_000_000)
estimate = Z.mean()
```

Law of large numbers ensures convergence.

---

## 5. Financial context

Random simulation is used for:
- option pricing,
- risk estimation,
- stress testing,
- scenario analysis.

---

## Key takeaways

- Use `default_rng`.
- Control seeds for reproducibility.
- Random simulation underpins Monte Carlo methods.
