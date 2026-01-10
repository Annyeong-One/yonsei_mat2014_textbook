# Discrete Distributions

Discrete probability distributions model countable outcomes with scipy.stats providing binomial, Poisson, geometric, and other discrete distributions for modeling events, counts, and categorical data.

---

## Common Distributions

### 1. Binomial

**n independent trials, p success probability:**

```python
from scipy import stats

# Binomial(n=10, p=0.3)
n, p = 10, 0.3
binom = stats.binom(n=n, p=p)

# PMF: P(X = k)
print(binom.pmf(3))  # P(exactly 3 successes)

# CDF: P(X ≤ k)
print(binom.cdf(3))  # P(at most 3 successes)

# Mean and variance
print(binom.mean())  # n*p = 3.0
print(binom.var())   # n*p*(1-p) = 2.1

# Samples
samples = binom.rvs(size=1000)
```

### 2. Poisson

**Count of events in fixed interval:**

```python
# Poisson(λ=5)
lam = 5
poisson = stats.poisson(mu=lam)

print(poisson.pmf(5))  # P(X = 5)
print(poisson.mean())  # λ = 5
print(poisson.var())   # λ = 5

# Applications: arrivals, defects, rare events
```

### 3. Geometric

**Trials until first success:**

```python
# Geometric(p=0.3)
p = 0.3
geom = stats.geom(p=p)

print(geom.pmf(1))    # P(success on 1st trial) = p
print(geom.mean())    # 1/p = 3.33...
print(geom.var())     # (1-p)/p² = 7.78...

# Memoryless property
```

### 4. Negative Binomial

**Trials until r successes:**

```python
# NegBinom(r=5, p=0.3)
r, p = 5, 0.3
nbinom = stats.nbinom(n=r, p=p)

print(nbinom.mean())  # r*(1-p)/p = 11.67
print(nbinom.var())   # r*(1-p)/p² = 38.89
```

### 5. Hypergeometric

**Sampling without replacement:**

```python
# Hypergeometric(M=50, n=10, N=20)
# M: population size
# n: number of success states
# N: number of draws
M, n, N = 50, 10, 20
hypergeom = stats.hypergeom(M=M, n=n, N=N)

print(hypergeom.mean())  # N*n/M = 4.0
```

### 6. Multinomial

**Multiple categories:**

```python
# Multinomial(n=10, p=[0.2, 0.3, 0.5])
n = 10
p = [0.2, 0.3, 0.5]
multinom = stats.multinomial(n=n, p=p)

# Sample outcome
sample = multinom.rvs(size=1)
print(sample)  # e.g., [[2, 3, 5]]
```

### 7. Uniform Discrete

**Equal probabilities:**

```python
# Discrete uniform on {a, ..., b}
low, high = 1, 6  # Die roll
discrete_unif = stats.randint(low=low, high=high+1)

print(discrete_unif.pmf(3))  # 1/6
print(discrete_unif.mean())  # (low+high)/2 = 3.5
```

---

## Methods

### 1. PMF

```python
binom = stats.binom(n=10, p=0.5)

# Single value
print(binom.pmf(5))  # P(X=5)

# Multiple values
k = range(11)
pmf_vals = binom.pmf(k)
print(sum(pmf_vals))  # 1.0 (sums to 1)
```

### 2. CDF

```python
print(binom.cdf(5))  # P(X ≤ 5)

# Probability range
p_range = binom.cdf(7) - binom.cdf(2)  # P(3 ≤ X ≤ 7)
```

### 3. PPF

```python
# Quantile (smallest k where P(X ≤ k) ≥ q)
print(binom.ppf(0.5))  # Median

# Confidence interval
lower = binom.ppf(0.025)
upper = binom.ppf(0.975)
```

### 4. RVS

```python
samples = binom.rvs(size=1000, random_state=42)
print(samples.mean())  # ~5.0
```

### 5. Stats

```python
mean, var = binom.stats(moments='mv')
print(f"Mean: {mean}, Var: {var}")
```

### 6. Interval

```python
# Support of distribution
a, b = binom.support()
print(f"X ∈ [{a}, {b}]")  # [0, 10]
```

### 7. Expect

```python
# E[g(X)]
expected = binom.expect(lambda x: x**2)
print(expected)  # E[X²]
```

---

## Applications

### 1. Quality Control

```python
# 5% defect rate, sample 100 items
n, p = 100, 0.05
binom = stats.binom(n=n, p=p)

# P(at most 3 defects)
print(binom.cdf(3))

# P(more than 10 defects) - warning threshold
print(1 - binom.cdf(10))
```

### 2. A/B Testing

```python
# Control: 100 trials, 23 conversions
# Treatment: 100 trials, 28 conversions
n = 100
p_control = 23/100
p_treatment = 28/100

# Confidence intervals
from scipy import stats
ci_control = stats.binom.interval(0.95, n, p_control)
ci_treatment = stats.binom.interval(0.95, n, p_treatment)

print(f"Control: {ci_control}")
print(f"Treatment: {ci_treatment}")
```

### 3. Poisson Process

```python
# Customer arrivals: λ=5 per hour
lam = 5
poisson = stats.poisson(mu=lam)

# P(exactly 3 arrivals)
print(poisson.pmf(3))

# P(at least 8 arrivals)
print(1 - poisson.cdf(7))
```

### 4. Rare Events

```python
# Disease prevalence: 0.1% in population of 10,000
n, p = 10000, 0.001
binom = stats.binom(n=n, p=p)

# Poisson approximation (n large, p small)
lam = n * p  # np = 10
poisson = stats.poisson(mu=lam)

# Compare
k = 15
print(f"Binomial: {binom.pmf(k):.6f}")
print(f"Poisson: {poisson.pmf(k):.6f}")  # Very close!
```

### 5. Waiting Times

```python
# Geometric: trials until success
p = 0.2
geom = stats.geom(p=p)

# Expected wait
print(f"Average trials: {geom.mean()}")  # 5.0

# P(success within 10 trials)
print(geom.cdf(10))
```

### 6. Inventory

```python
# Daily demand: Poisson(λ=20)
lam = 20
poisson = stats.poisson(mu=lam)

# Stock level for 95% service level
stock_level = poisson.ppf(0.95)
print(f"Stock level: {stock_level}")

# Expected stockouts
prob_stockout = 1 - poisson.cdf(stock_level)
print(f"Stockout probability: {prob_stockout:.2%}")
```

### 7. Simulations

```python
# Monte Carlo: estimate π
n_trials = 10000
inside_circle = 0

for _ in range(n_trials):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1

pi_estimate = 4 * inside_circle / n_trials
print(f"π ≈ {pi_estimate:.4f}")

# Confidence interval using binomial
p = inside_circle / n_trials
se = np.sqrt(p * (1-p) / n_trials)
ci = stats.norm.interval(0.95, loc=4*p, scale=4*se)
print(f"95% CI: {ci}")
```

---

## Summary

| Distribution | Parameters | Mean | Use Case |
|--------------|------------|------|----------|
| **Binomial** | n, p | np | Fixed trials |
| **Poisson** | λ | λ | Event counts |
| **Geometric** | p | 1/p | First success |
| **NegBinom** | r, p | r(1-p)/p | r-th success |
| **Hypergeom** | M, n, N | Nn/M | Without replacement |

**Key insight:** Discrete distributions model countable outcomes with probability mass functions (PMF), providing exact probabilities for specific values rather than densities over continuous ranges.
