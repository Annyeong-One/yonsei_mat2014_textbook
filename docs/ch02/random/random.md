# Random Numbers and

Random number generation is essential for Monte Carlo simulation, risk analysis, and stochastic modeling.

---

## Random number

NumPy provides a modern random API:

```python
import numpy as np

rng = np.random.default_rng(seed=42)
```

Using an explicit generator is preferred over global state.

---

## Common distributions

```python
rng.standard_normal(size=1000)
rng.uniform(0.0, 1.0, size=1000)
rng.normal(loc=0.0, scale=1.0, size=1000)
```

Many distributions are available.

---

## Reproducibility

Setting a seed ensures reproducible results:

```python
rng = np.random.default_rng(123)
```

This is essential for debugging and research.

---

## Monte Carlo

```python
Z = rng.standard_normal(1_000_000)
estimate = Z.mean()
```

Law of large numbers ensures convergence.

---

## Financial context

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
