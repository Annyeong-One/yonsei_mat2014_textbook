# Distribution Methods

SciPy distributions provide a unified interface with methods for computing probabilities (pdf/pmf, cdf), generating samples (rvs), calculating quantiles (ppf), and performing statistical inference.

---

## Core Methods

### 1. PDF/PMF

**Probability density/mass function:**

```python
from scipy import stats

# Continuous: PDF
norm = stats.norm(0, 1)
print(norm.pdf(0))  # Density at x=0

# Discrete: PMF  
binom = stats.binom(n=10, p=0.5)
print(binom.pmf(5))  # P(X = 5)

# Vector input
x = np.linspace(-3, 3, 7)
print(norm.pdf(x))
```

### 2. Log PDF/PMF

**For numerical stability:**

```python
# Log probability (more stable)
print(norm.logpdf(0))  # log(pdf(0))

# Useful for large deviations
x = 10
print(norm.pdf(x))     # Very small, may underflow
print(norm.logpdf(x))  # log scale, stable

# Product of probabilities → Sum of log probabilities
data = [1, 2, 3, 4, 5]
log_likelihood = np.sum(norm.logpdf(data))
```

### 3. CDF

**Cumulative probability:**

```python
# P(X ≤ x)
print(norm.cdf(1.96))  # 0.975

# Probability interval
a, b = -1, 1
prob = norm.cdf(b) - norm.cdf(a)  # P(a < X ≤ b)
```

### 4. SF (Survival Function)

**Complement of CDF:**

```python
# P(X > x) = 1 - CDF(x)
print(norm.sf(1.96))  # 0.025

# More accurate for tail probabilities
x = 10
print(1 - norm.cdf(x))  # May have rounding error
print(norm.sf(x))       # More accurate
```

### 5. PPF (Percent Point Function)

**Inverse CDF (quantiles):**

```python
# Find x where CDF(x) = q
print(norm.ppf(0.975))  # 1.96

# Confidence intervals
alpha = 0.05
lower = norm.ppf(alpha/2)
upper = norm.ppf(1 - alpha/2)
print(f"95% CI bounds: [{lower:.2f}, {upper:.2f}]")
```

### 6. ISF (Inverse Survival Function)

**Inverse of SF:**

```python
# Find x where SF(x) = q
print(norm.isf(0.025))  # 1.96

# Equivalent to ppf(1-q)
q = 0.05
print(norm.isf(q))      # Same as norm.ppf(1-q)
```

### 7. RVS (Random Variates)

**Generate samples:**

```python
# Single sample
sample = norm.rvs()

# Multiple samples
samples = norm.rvs(size=1000)

# Reproducible
samples = norm.rvs(size=100, random_state=42)

# Different shapes
samples_2d = norm.rvs(size=(10, 5))  # 10×5 array
```

---

## Statistical Methods

### 1. Stats

**Summary statistics:**

```python
# Mean, variance, skewness, kurtosis
m, v, s, k = norm.stats(moments='mvsk')
print(f"Mean: {m}, Var: {v}, Skew: {s}, Kurt: {k}")

# Just mean and variance
m, v = norm.stats(moments='mv')

# Different distribution
expon = stats.expon(scale=2)
print(expon.stats(moments='mv'))  # (2.0, 4.0)
```

### 2. Mean

```python
print(norm.mean())  # 0.0
print(expon.mean()) # 1/λ

# Computed from moments
```

### 3. Median

```python
print(norm.median())  # 0.0 (50th percentile)
print(expon.median()) # ln(2)/λ

# Equivalent to ppf(0.5)
print(norm.ppf(0.5))
```

### 4. Variance/Std

```python
print(norm.var())  # 1.0
print(norm.std())  # 1.0 (sqrt of var)
```

### 5. Interval

**Confidence/credible intervals:**

```python
# Central interval containing α probability
alpha = 0.95
interval = norm.interval(alpha)
print(f"{alpha*100}% interval: {interval}")

# For different distributions
interval = stats.t(df=5).interval(0.95)
```

### 6. Support

**Range of distribution:**

```python
# Continuous
print(norm.support())  # (-inf, inf)
print(stats.uniform().support())  # (0, 1)

# Discrete  
print(binom.support())  # (0, 10)
```

### 7. Expect

**Expected value of function:**

```python
# E[g(X)]
def g(x):
    return x**2

expected = norm.expect(g)
print(f"E[X²] = {expected}")  # Should equal var + mean²

# With bounds
expected_bounded = norm.expect(g, lb=-1, ub=1)
```

---

## Fitting Methods

### 1. Fit

**Maximum likelihood estimation:**

```python
# Generate data
data = np.random.normal(5, 2, size=1000)

# Fit parameters
loc, scale = stats.norm.fit(data)
print(f"μ̂ = {loc:.2f}, σ̂ = {scale:.2f}")

# Create fitted distribution
fitted = stats.norm(loc=loc, scale=scale)
```

### 2. Fit with Fixed Parameters

```python
# Fix location, estimate scale
loc, scale = stats.norm.fit(data, floc=5)
print(f"Fixed μ=5, σ̂ = {scale:.2f}")

# Fix scale, estimate location
loc, scale = stats.norm.fit(data, fscale=1)
print(f"μ̂ = {loc:.2f}, fixed σ=1")
```

### 3. Fit Method Parameter

```python
# Different fitting methods
loc, scale = stats.norm.fit(data, method='MLE')  # Maximum likelihood
loc, scale = stats.norm.fit(data, method='MM')   # Method of moments
```

### 4. Fit_loc_scale

**Fit location-scale family:**

```python
# For location-scale distributions
from scipy.stats import distributions

loc, scale = distributions.fit_loc_scale(data, norm)
```

### 5. NLLf (Negative Log-Likelihood)

```python
# Evaluate fit quality
params = (5, 2)  # (loc, scale)
nll = norm.nnlf(params, data)
print(f"Negative log-likelihood: {nll:.2f}")

# Lower is better
```

### 6. Freeze

**Create distribution with fixed parameters:**

```python
# Instead of passing parameters every time
dist = stats.norm(loc=5, scale=2)

# Use like any distribution
print(dist.pdf(5))
print(dist.cdf(7))
samples = dist.rvs(size=100)

# Useful for repeated operations
```

### 7. Moment

**Raw moments:**

```python
# n-th moment: E[X^n]
print(norm.moment(1))  # E[X] = 0
print(norm.moment(2))  # E[X²] = 1
print(norm.moment(3))  # E[X³] = 0
print(norm.moment(4))  # E[X⁴] = 3
```

---

## Advanced Methods

### 1. Entropy

**Differential entropy:**

```python
# Continuous entropy
print(norm.entropy())  # 0.5*log(2πe)

# Higher entropy = more uncertainty
print(stats.norm(0, 1).entropy())   # 1.42
print(stats.norm(0, 2).entropy())   # 2.11 (wider, more uncertain)

# Discrete entropy
binom = stats.binom(n=10, p=0.5)
print(binom.entropy())
```

### 2. Median Absolute Deviation

```python
# Not a method, but useful statistic
from scipy import stats

data = np.random.normal(0, 1, 1000)
mad = stats.median_abs_deviation(data)
print(f"MAD: {mad:.3f}")  # Robust measure of spread
```

### 3. Fit Goodness

```python
# K-S test for fit quality
data = np.random.normal(0, 1, 100)
loc, scale = stats.norm.fit(data)
fitted = stats.norm(loc=loc, scale=scale)

ks_stat, p_value = stats.kstest(data, fitted.cdf)
print(f"K-S statistic: {ks_stat:.4f}, p-value: {p_value:.4f}")
# High p-value indicates good fit
```

### 4. Anderson-Darling Test

```python
result = stats.anderson(data, dist='norm')
print(f"A-D statistic: {result.statistic:.4f}")
print(f"Critical values: {result.critical_values}")
print(f"Significance levels: {result.significance_level}")

# If statistic < critical value, distribution fits
```

### 5. Probability Plot

```python
# Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot")
plt.show()

# Points on line → good fit
```

### 6. CDF Distance

```python
# Compare two distributions
dist1 = stats.norm(0, 1)
dist2 = stats.norm(0, 1.5)

# Kolmogorov-Smirnov distance
x = np.linspace(-5, 5, 1000)
ks_distance = np.max(np.abs(dist1.cdf(x) - dist2.cdf(x)))
print(f"K-S distance: {ks_distance:.4f}")
```

### 7. Custom Distributions

```python
# Create custom distribution
class MyDist(stats.rv_continuous):
    def _pdf(self, x):
        return np.exp(-x**2/2) / np.sqrt(2*np.pi)

my_dist = MyDist(name='my_dist')
print(my_dist.pdf(0))  # Works like built-in
```

---

## Practical Examples

### 1. Confidence Intervals

```python
data = [23, 25, 27, 24, 26, 22, 28, 25, 24, 26]
n = len(data)

mean = np.mean(data)
se = stats.sem(data)

# 95% CI using t-distribution
ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)
print(f"95% CI: [{ci[0]:.2f}, {ci[1]:.2f}]")
```

### 2. Hypothesis Testing

```python
# One-sample t-test against μ₀=25
mu0 = 25
t_stat = (mean - mu0) / se
p_value = 2 * stats.t.sf(abs(t_stat), df=n-1)
print(f"t = {t_stat:.3f}, p = {p_value:.4f}")
```

### 3. Power Analysis

```python
# Required sample size for power=0.8
from statsmodels.stats.power import tt_solve_power

n_required = tt_solve_power(
    effect_size=0.5,
    alpha=0.05,
    power=0.8,
    alternative='two-sided'
)
print(f"Required n: {int(np.ceil(n_required))}")
```

### 4. Bootstrap

```python
# Bootstrap confidence interval
n_bootstrap = 1000
means = []

for _ in range(n_bootstrap):
    sample = np.random.choice(data, size=len(data), replace=True)
    means.append(np.mean(sample))

ci_boot = np.percentile(means, [2.5, 97.5])
print(f"Bootstrap 95% CI: {ci_boot}")
```

### 5. Monte Carlo

```python
# Simulate option payoff
S0 = 100  # Current price
K = 105   # Strike price
T = 1     # Time to expiration
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility

n_sim = 10000
ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*np.random.randn(n_sim))
payoff = np.maximum(ST - K, 0)
option_price = np.exp(-r*T) * np.mean(payoff)
print(f"Call option price: ${option_price:.2f}")
```

### 6. Tolerance Interval

```python
# 95% confidence, 99% coverage
data = np.random.normal(100, 15, 50)
mean, std = np.mean(data), np.std(data, ddof=1)

# Using tolerance interval formula
from scipy.stats import chi2, norm
n = len(data)
gamma = 0.95  # Confidence
p = 0.99      # Coverage

k = norm.ppf((1+p)/2) * np.sqrt((n+1)/n) * np.sqrt((n-1)/chi2.ppf(gamma, n-1))
lower = mean - k*std
upper = mean + k*std

print(f"Tolerance interval: [{lower:.2f}, {upper:.2f}]")
```

### 7. Probability Calibration

```python
# Check if probabilities are calibrated
predicted_probs = np.array([0.1, 0.3, 0.6, 0.8, 0.9])
outcomes = np.array([0, 0, 1, 1, 1])

# Brier score (lower is better)
brier = np.mean((predicted_probs - outcomes)**2)
print(f"Brier score: {brier:.4f}")

# Log loss
from sklearn.metrics import log_loss
print(f"Log loss: {log_loss(outcomes, predicted_probs):.4f}")
```

---

## Summary

**Core methods:**
- `pdf()/pmf()`: Density/mass at x
- `cdf()`: Cumulative probability P(X ≤ x)
- `ppf()`: Inverse CDF (quantiles)
- `rvs()`: Random samples
- `fit()`: Parameter estimation

**Statistical methods:**
- `stats()`: Summary statistics (mean, var, skew, kurt)
- `interval()`: Confidence intervals
- `entropy()`: Information content

**Key insight:** SciPy's unified distribution interface provides consistent methods across all distributions, enabling seamless probability calculations, sampling, and statistical inference with minimal code changes when switching between distributions.
