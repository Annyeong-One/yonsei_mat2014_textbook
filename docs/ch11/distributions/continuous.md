# Continuous Distributions

SciPy's `scipy.stats` module provides comprehensive implementations of continuous probability distributions with methods for PDF, CDF, sampling, fitting, and statistical analysis, enabling probabilistic modeling and statistical inference in Python.

---

## Common Distributions

### 1. Normal (Gaussian)

**Most important distribution:**

```python
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Create normal distribution (mean=0, std=1)
norm = stats.norm(loc=0, scale=1)

# PDF at x=0
print(norm.pdf(0))  # 0.3989... (1/sqrt(2π))

# CDF at x=1.96
print(norm.cdf(1.96))  # 0.975 (97.5th percentile)

# Generate samples
samples = norm.rvs(size=1000)
print(samples.mean())  # ~0
print(samples.std())   # ~1

# Plot
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x), label='PDF')
plt.plot(x, norm.cdf(x), label='CDF')
plt.legend()
plt.show()
```

**Parameters:**
- `loc`: Mean (μ)
- `scale`: Standard deviation (σ)

### 2. Uniform Distribution

**Equal probability over interval:**

```python
# Uniform on [0, 1]
uniform = stats.uniform(loc=0, scale=1)

# Uniform on [a, b]
a, b = 2, 5
uniform_ab = stats.uniform(loc=a, scale=b-a)

print(uniform_ab.pdf(3))   # 0.333... (1/(b-a))
print(uniform_ab.cdf(3))   # 0.333... ((3-a)/(b-a))

# Generate samples
samples = uniform.rvs(size=1000)
print(samples.min(), samples.max())  # ~0, ~1
```

### 3. Exponential Distribution

**Time between events:**

```python
# Exponential with rate λ=1
expon = stats.expon(scale=1)  # scale = 1/λ

# Rate λ=2 (mean=0.5)
expon_fast = stats.expon(scale=0.5)

print(expon.mean())  # 1.0
print(expon.pdf(0))  # 1.0 (λ)
print(expon.cdf(1))  # 0.632... (1 - e^(-1))

# Memoryless property
t, s = 1, 2
p1 = 1 - expon.cdf(t + s)
p2 = (1 - expon.cdf(t)) * (1 - expon.cdf(s))
print(f"P(X > {t+s}): {p1:.4f}")
print(f"P(X > {t}) * P(X > {s}): {p2:.4f}")
```

### 4. Student's t-Distribution

**Heavy-tailed alternative to normal:**

```python
# t-distribution with df degrees of freedom
df = 5
t_dist = stats.t(df=df)

# Compare to normal
norm = stats.norm()
x = np.linspace(-4, 4, 100)

plt.plot(x, norm.pdf(x), label='Normal')
plt.plot(x, t_dist.pdf(x), label=f't (df={df})')
plt.legend()
plt.title('Heavier tails in t-distribution')
plt.show()

# Critical values
print(t_dist.ppf(0.975))  # 97.5th percentile (two-tailed α=0.05)
# df=5: 2.571
# df=30: 2.042
# Normal: 1.96
```

### 5. Chi-Square Distribution

**Sum of squared normals:**

```python
# Chi-square with k degrees of freedom
k = 3
chi2 = stats.chi2(df=k)

print(chi2.mean())  # k = 3
print(chi2.var())   # 2k = 6

# Relationship to normal
# If Z ~ N(0,1), then Z² ~ χ²(1)
z = np.random.randn(10000)
z_squared = z**2

# Compare
x = np.linspace(0, 10, 100)
plt.hist(z_squared, bins=50, density=True, alpha=0.5, label='Z² samples')
plt.plot(x, stats.chi2(df=1).pdf(x), label='χ²(1) PDF')
plt.legend()
plt.show()
```

### 6. F-Distribution

**Ratio of chi-squares:**

```python
# F-distribution with dfn, dfd degrees of freedom
dfn, dfd = 5, 10
f_dist = stats.f(dfn=dfn, dfd=dfd)

# Critical value (upper tail)
alpha = 0.05
critical = f_dist.ppf(1 - alpha)
print(f"F({dfn}, {dfd}) critical value: {critical:.3f}")

# Used in ANOVA
# F = (variance between groups) / (variance within groups)
```

### 7. Beta Distribution

**Bounded on [0, 1]:**

```python
# Beta(α, β)
alpha, beta = 2, 5
beta_dist = stats.beta(a=alpha, b=beta)

print(beta_dist.mean())  # α/(α+β) = 2/7 ≈ 0.286
print(beta_dist.var())   # αβ/((α+β)²(α+β+1))

# Different shapes
x = np.linspace(0, 1, 100)
for a, b in [(0.5, 0.5), (2, 2), (2, 5), (5, 2)]:
    plt.plot(x, stats.beta(a, b).pdf(x), label=f'α={a}, β={b}')
plt.legend()
plt.title('Beta distributions')
plt.show()

# Used for Bayesian inference on probabilities
```

---

## Distribution Methods

### 1. PDF (Probability Density Function)

**Density at point x:**

```python
norm = stats.norm(0, 1)

# PDF at specific points
print(norm.pdf(0))     # 0.3989 (peak of bell curve)
print(norm.pdf(1))     # 0.2420
print(norm.pdf(-2))    # 0.0540

# PDF for array
x = np.linspace(-3, 3, 7)
print(norm.pdf(x))
# [0.0044, 0.0540, 0.2420, 0.3989, 0.2420, 0.0540, 0.0044]

# PDF properties
# 1. pdf(x) ≥ 0 for all x
# 2. ∫ pdf(x) dx = 1 (area under curve)
# 3. P(a < X < b) = ∫[a,b] pdf(x) dx
```

### 2. CDF (Cumulative Distribution Function)

**Probability X ≤ x:**

```python
norm = stats.norm(0, 1)

# CDF at specific points
print(norm.cdf(0))     # 0.5 (50th percentile)
print(norm.cdf(1))     # 0.8413 (84.13th percentile)
print(norm.cdf(-1.96)) # 0.025 (2.5th percentile)

# Probability between a and b
a, b = -1, 1
prob = norm.cdf(b) - norm.cdf(a)
print(f"P({a} < X < {b}) = {prob:.4f}")  # 0.6827 (68.27%)

# CDF properties
# 1. 0 ≤ cdf(x) ≤ 1
# 2. cdf(-∞) = 0, cdf(∞) = 1
# 3. cdf is non-decreasing
```

### 3. PPF (Percent Point Function)

**Inverse CDF (quantile function):**

```python
norm = stats.norm(0, 1)

# Percentiles
print(norm.ppf(0.5))   # 0.0 (median)
print(norm.ppf(0.025)) # -1.96 (2.5th percentile)
print(norm.ppf(0.975)) # 1.96 (97.5th percentile)

# Confidence interval bounds
alpha = 0.05
lower = norm.ppf(alpha/2)
upper = norm.ppf(1 - alpha/2)
print(f"95% CI: [{lower:.2f}, {upper:.2f}]")  # [-1.96, 1.96]

# Relationship: ppf(cdf(x)) = x
x = 1.5
print(norm.ppf(norm.cdf(x)))  # 1.5
```

### 4. RVS (Random Variates)

**Generate random samples:**

```python
norm = stats.norm(0, 1)

# Single sample
sample = norm.rvs()
print(sample)  # Random value from N(0,1)

# Multiple samples
samples = norm.rvs(size=1000)
print(samples.mean())  # ~0
print(samples.std())   # ~1

# Reproducibility
np.random.seed(42)
samples1 = norm.rvs(size=10)
np.random.seed(42)
samples2 = norm.rvs(size=10)
print(np.allclose(samples1, samples2))  # True

# Different distribution
expon = stats.expon(scale=2)
exp_samples = expon.rvs(size=1000)
print(exp_samples.mean())  # ~2
```

### 5. SF (Survival Function)

**Probability X > x:**

```python
norm = stats.norm(0, 1)

# Survival function (1 - CDF)
print(norm.sf(0))      # 0.5
print(norm.sf(1.96))   # 0.025

# More accurate for extreme tails
x = 10
print(1 - norm.cdf(x))  # 0.0 (underflow)
print(norm.sf(x))       # 7.619...e-24 (accurate)

# Useful for p-values in right-tail tests
z_score = 2.5
p_value = norm.sf(z_score)
print(f"P(Z > {z_score}) = {p_value:.4f}")  # 0.0062
```

### 6. ISF (Inverse Survival Function)

**Inverse of SF:**

```python
norm = stats.norm(0, 1)

# ISF (inverse of survival function)
print(norm.isf(0.5))    # 0.0
print(norm.isf(0.025))  # 1.96

# Relationship: isf(p) = ppf(1-p)
p = 0.05
print(norm.isf(p))      # 1.645
print(norm.ppf(1-p))    # 1.645

# Critical values for one-tailed tests
alpha = 0.05
critical = norm.isf(alpha)
print(f"Critical value (α={alpha}): {critical:.3f}")
```

### 7. Stats Method

**Summary statistics:**

```python
norm = stats.norm(0, 1)

# Mean, variance, skewness, kurtosis
mean, var, skew, kurt = norm.stats(moments='mvsk')
print(f"Mean: {mean}")      # 0.0
print(f"Variance: {var}")   # 1.0
print(f"Skewness: {skew}")  # 0.0 (symmetric)
print(f"Kurtosis: {kurt}")  # 0.0 (mesokurtic)

# Just mean and variance
m, v = norm.stats(moments='mv')

# Different distribution
expon = stats.expon(scale=2)
m, v, s, k = expon.stats(moments='mvsk')
print(f"Exponential: mean={m}, var={v}, skew={s:.2f}, kurt={k:.2f}")
# mean=2, var=4, skew=2.0, kurt=6.0 (heavy right tail)
```

---

## Special Distributions

### 1. Log-Normal Distribution

**Exponentiated normal:**

```python
# If log(X) ~ N(μ, σ²), then X ~ LogNormal(μ, σ²)
mu, sigma = 0, 1
lognorm = stats.lognorm(s=sigma, scale=np.exp(mu))

print(lognorm.mean())   # exp(μ + σ²/2) = exp(0.5) ≈ 1.649
print(lognorm.median()) # exp(μ) = 1.0

# Generate samples
samples = lognorm.rvs(size=1000)

# Verify: log(samples) should be normal
log_samples = np.log(samples)
print(log_samples.mean())  # ~0
print(log_samples.std())   # ~1

# Used for: stock prices, income distributions, particle sizes
```

### 2. Gamma Distribution

**Sum of exponentials:**

```python
# Gamma(α, β)
alpha, beta = 2, 0.5  # shape, scale
gamma = stats.gamma(a=alpha, scale=beta)

print(gamma.mean())  # α*β = 1.0
print(gamma.var())   # α*β² = 0.5

# Relationship to exponential
# Exponential(λ) = Gamma(1, 1/λ)
lam = 2
expon = stats.expon(scale=1/lam)
gamma_equiv = stats.gamma(a=1, scale=1/lam)
print(expon.mean(), gamma_equiv.mean())  # Both 0.5

# Used for: waiting times, insurance claims
```

### 3. Weibull Distribution

**Reliability analysis:**

```python
# Weibull with shape parameter c
c = 1.5
weibull = stats.weibull_min(c=c)

# Different shapes
x = np.linspace(0, 3, 100)
for shape in [0.5, 1, 1.5, 5]:
    w = stats.weibull_min(c=shape)
    plt.plot(x, w.pdf(x), label=f'c={shape}')
plt.legend()
plt.title('Weibull distributions')
plt.show()

# c < 1: Decreasing hazard (early failures)
# c = 1: Constant hazard (exponential)
# c > 1: Increasing hazard (wear-out failures)

# Used for: failure times, wind speed, survival analysis
```

### 4. Cauchy Distribution

**Heavy-tailed, no mean:**

```python
# Cauchy (location=0, scale=1)
cauchy = stats.cauchy()

# Undefined mean and variance!
try:
    print(cauchy.mean())
except:
    print("Mean is undefined")

# But median exists
print(cauchy.median())  # 0.0

# Very heavy tails
print(cauchy.pdf(0))     # 0.3183 (1/π)
print(cauchy.pdf(10))    # 0.0031 (still notable)
print(stats.norm().pdf(10))  # ~0 (negligible)

# Sample mean doesn't converge!
samples = cauchy.rvs(size=10000)
print(samples.mean())  # Unstable, no convergence
```

### 5. Pareto Distribution

**Power law distribution:**

```python
# Pareto with shape parameter b
b = 2.5
pareto = stats.pareto(b=b)

print(pareto.mean())  # b/(b-1) = 2.5/1.5 ≈ 1.667 (if b > 1)

# 80-20 rule: 80% of effects from 20% of causes
# Probability of top 20%
x = pareto.ppf(0.8)
top_20_pct_value = pareto.mean() - pareto.expect(lambda t: t, lb=x)
total_value = pareto.mean()
print(f"Top 20% owns {top_20_pct_value/total_value*100:.0f}% of value")

# Used for: wealth distribution, city sizes, word frequency
```

### 6. Triangular Distribution

**Simple bounded distribution:**

```python
# Triangular(left, mode, right)
left, mode, right = 0, 2, 4
c = (mode - left) / (right - left)  # Normalized mode
triang = stats.triang(c=c, loc=left, scale=right-left)

print(triang.mean())    # (left + mode + right) / 3 = 2.0
print(triang.median())  # Depends on mode position

# Used for: simple uncertainty modeling, PERT estimation
```

### 7. Laplace Distribution

**Double exponential:**

```python
# Laplace (location=0, scale=1)
laplace = stats.laplace()

# Peaked at center, exponential tails
x = np.linspace(-5, 5, 100)
plt.plot(x, stats.norm().pdf(x), label='Normal')
plt.plot(x, laplace.pdf(x), label='Laplace')
plt.legend()
plt.title('Laplace vs Normal')
plt.show()

print(laplace.pdf(0))    # 0.5 (peak)
print(stats.norm().pdf(0))  # 0.399 (lower peak)

# Used for: robust statistics, signal processing
```

---

## Parameter Estimation

### 1. Method of Moments

**Match sample moments:**

```python
# Generate data
true_mu, true_sigma = 5, 2
data = np.random.normal(true_mu, true_sigma, size=1000)

# Estimate parameters
estimated_mu = data.mean()
estimated_sigma = data.std(ddof=1)  # Unbiased estimator

print(f"True: μ={true_mu}, σ={true_sigma}")
print(f"Estimated: μ={estimated_mu:.2f}, σ={estimated_sigma:.2f}")

# Create fitted distribution
fitted_norm = stats.norm(loc=estimated_mu, scale=estimated_sigma)
```

### 2. Maximum Likelihood Estimation

**Using fit() method:**

```python
# Generate data
true_params = (2, 5)  # shape, loc for gamma
data = stats.gamma.rvs(a=2, loc=5, scale=1, size=500)

# Fit distribution
shape, loc, scale = stats.gamma.fit(data)
print(f"Estimated: shape={shape:.2f}, loc={loc:.2f}, scale={scale:.2f}")

# Create fitted distribution
fitted = stats.gamma(a=shape, loc=loc, scale=scale)

# Compare
x = np.linspace(data.min(), data.max(), 100)
plt.hist(data, bins=30, density=True, alpha=0.5, label='Data')
plt.plot(x, fitted.pdf(x), 'r-', label='Fitted')
plt.legend()
plt.show()
```

### 3. Fix Parameters

**Fit with fixed parameters:**

```python
# Generate normal data
data = np.random.normal(0, 2, size=1000)

# Fit with fixed location
loc, scale = stats.norm.fit(data, floc=0)  # Fix μ=0, estimate σ
print(f"Fixed μ=0, estimated σ={scale:.2f}")

# Fit with fixed scale
loc, scale = stats.norm.fit(data, fscale=1)  # Estimate μ, fix σ=1
print(f"Estimated μ={loc:.2f}, fixed σ=1")
```

### 4. Goodness of Fit

**Check fit quality:**

```python
from scipy import stats

# Generate data
data = np.random.normal(0, 1, size=100)

# Fit normal distribution
loc, scale = stats.norm.fit(data)
fitted = stats.norm(loc=loc, scale=scale)

# Kolmogorov-Smirnov test
statistic, p_value = stats.kstest(data, fitted.cdf)
print(f"K-S test: statistic={statistic:.4f}, p-value={p_value:.4f}")
# High p-value (>0.05): Good fit

# Anderson-Darling test
result = stats.anderson(data, dist='norm')
print(f"A-D statistic: {result.statistic:.4f}")
print("Critical values:", result.critical_values)
# statistic < critical → Good fit
```

### 5. Q-Q Plot

**Visual fit assessment:**

```python
import matplotlib.pyplot as plt
from scipy import stats

# Generate data
data = np.random.normal(0, 1, size=100)

# Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot")
plt.show()

# Points on line → Good fit
# Deviations → Poor fit

# For different distributions
data_exp = np.random.exponential(2, size=100)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
stats.probplot(data_exp, dist="norm", plot=axes[0])
axes[0].set_title("Exponential data vs Normal")
stats.probplot(data_exp, dist="expon", plot=axes[1])
axes[1].set_title("Exponential data vs Exponential")
plt.show()
```

### 6. AIC/BIC Criteria

**Compare model fit:**

```python
# Generate mixed data
data = np.concatenate([
    np.random.normal(0, 1, 500),
    np.random.normal(5, 1.5, 500)
])

# Fit different distributions
norm_fit = stats.norm.fit(data)
norm_dist = stats.norm(*norm_fit)

# Log-likelihood
log_lik = np.sum(np.log(norm_dist.pdf(data)))

# AIC = -2*log_lik + 2*k (k = number of parameters)
k = 2  # μ, σ
aic = -2 * log_lik + 2 * k
print(f"AIC: {aic:.2f}")

# BIC = -2*log_lik + k*log(n)
n = len(data)
bic = -2 * log_lik + k * np.log(n)
print(f"BIC: {bic:.2f}")

# Lower AIC/BIC → Better fit
```

### 7. Bootstrap Confidence Intervals

**Uncertainty in estimates:**

```python
# Generate data
data = np.random.normal(5, 2, size=100)

# Bootstrap
n_bootstrap = 1000
estimates = []

for _ in range(n_bootstrap):
    sample = np.random.choice(data, size=len(data), replace=True)
    loc, scale = stats.norm.fit(sample)
    estimates.append((loc, scale))

estimates = np.array(estimates)

# Confidence intervals
ci_mu = np.percentile(estimates[:, 0], [2.5, 97.5])
ci_sigma = np.percentile(estimates[:, 1], [2.5, 97.5])

print(f"μ: {estimates[:, 0].mean():.2f} [{ci_mu[0]:.2f}, {ci_mu[1]:.2f}]")
print(f"σ: {estimates[:, 1].mean():.2f} [{ci_sigma[0]:.2f}, {ci_sigma[1]:.2f}]")
```

---

## Practical Applications

### 1. Confidence Intervals

**Normal-based CI:**

```python
from scipy import stats

# Sample data
data = [23, 25, 27, 24, 26, 22, 28, 25, 24, 26]
n = len(data)

# Sample statistics
mean = np.mean(data)
se = stats.sem(data)  # Standard error

# 95% confidence interval
confidence = 0.95
ci = stats.t.interval(confidence, df=n-1, loc=mean, scale=se)

print(f"Mean: {mean:.2f}")
print(f"95% CI: [{ci[0]:.2f}, {ci[1]:.2f}]")
```

### 2. Hypothesis Testing

**z-test for mean:**

```python
# Null hypothesis: μ = μ0
mu0 = 25
data = [27, 28, 26, 29, 25, 30, 27, 26, 28, 27]

# Test statistic
mean = np.mean(data)
se = stats.sem(data)
z = (mean - mu0) / se

# p-value (two-tailed)
p_value = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"z = {z:.3f}, p-value = {p_value:.4f}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print(f"Reject H0 (p={p_value:.4f} < α={alpha})")
else:
    print(f"Fail to reject H0 (p={p_value:.4f} ≥ α={alpha})")
```

### 3. Sample Size Calculation

**Power analysis:**

```python
from scipy import stats

# Parameters
mu0 = 100  # Null hypothesis mean
mu1 = 105  # Alternative hypothesis mean
sigma = 10  # Population standard deviation
alpha = 0.05
power = 0.80  # Desired power (1 - β)

# Critical value
z_alpha = stats.norm.ppf(1 - alpha/2)

# Required sample size (two-tailed test)
z_beta = stats.norm.ppf(power)
n = ((z_alpha + z_beta) * sigma / (mu1 - mu0))**2
print(f"Required sample size: {int(np.ceil(n))}")

# Verify power with this n
se = sigma / np.sqrt(n)
critical_value = mu0 + z_alpha * se
power_actual = 1 - stats.norm.cdf(critical_value, loc=mu1, scale=se)
print(f"Actual power: {power_actual:.3f}")
```

### 4. Tolerance Intervals

**Prediction intervals:**

```python
# Data
data = np.random.normal(100, 15, size=50)

# Fit distribution
mu, sigma = stats.norm.fit(data)

# 95% tolerance interval covering 99% of population
# P(interval contains 99% of population) = 95%
confidence = 0.95
coverage = 0.99

# Using normal quantiles
z = stats.norm.ppf((1 + coverage) / 2)
k = z * np.sqrt((1 + 1/len(data)))  # Correction factor

lower = mu - k * sigma
upper = mu + k * sigma

print(f"Tolerance interval: [{lower:.2f}, {upper:.2f}]")
print(f"With {confidence*100}% confidence, {coverage*100}% of population in this range")
```

### 5. Extreme Value Analysis

**Modeling extremes:**

```python
# Annual maximum temperatures
maxima = np.array([38, 41, 39, 43, 37, 40, 44, 38, 42, 39])

# Fit Generalized Extreme Value (GEV) distribution
from scipy.stats import genextreme

# Fit (shape, loc, scale)
c, loc, scale = genextreme.fit(maxima)
gev = genextreme(c=c, loc=loc, scale=scale)

# 100-year return level (exceeded once per 100 years on average)
return_period = 100
prob = 1 - 1/return_period  # 0.99
return_level = gev.ppf(prob)

print(f"100-year return level: {return_level:.1f}°C")

# Probability of exceeding 45°C
prob_exceed = 1 - gev.cdf(45)
print(f"P(T > 45°C) = {prob_exceed:.4f}")
```

### 6. Mixture Models

**Combining distributions:**

```python
# Two-component Gaussian mixture
weights = [0.3, 0.7]
means = [0, 5]
stds = [1, 1.5]

# Generate mixture samples
n = 1000
components = np.random.choice([0, 1], size=n, p=weights)
samples = np.array([
    np.random.normal(means[c], stds[c]) for c in components
])

# PDF of mixture
def mixture_pdf(x):
    return (weights[0] * stats.norm(means[0], stds[0]).pdf(x) +
            weights[1] * stats.norm(means[1], stds[1]).pdf(x))

# Plot
x = np.linspace(-5, 10, 200)
plt.hist(samples, bins=50, density=True, alpha=0.5, label='Samples')
plt.plot(x, mixture_pdf(x), 'r-', linewidth=2, label='True mixture')
plt.legend()
plt.show()
```

### 7. Monte Carlo Simulation

**Risk analysis:**

```python
# Project cost estimation
# Fixed cost: $100k
# Variable cost: Normal($50k, $10k)
# Revenue: Lognormal(median=$200k, σ=0.3)

n_sim = 10000

fixed_cost = 100
variable_cost = np.random.normal(50, 10, n_sim)
revenue = np.random.lognormal(np.log(200), 0.3, n_sim)

profit = revenue - fixed_cost - variable_cost

# Risk metrics
print(f"Mean profit: ${profit.mean():.2f}k")
print(f"Std profit: ${profit.std():.2f}k")
print(f"P(profit > 0): {(profit > 0).mean():.2%}")
print(f"5th percentile (VaR): ${np.percentile(profit, 5):.2f}k")
print(f"95th percentile: ${np.percentile(profit, 95):.2f}k")

# Plot distribution
plt.hist(profit, bins=50, density=True, alpha=0.5)
plt.axvline(0, color='r', linestyle='--', label='Break-even')
plt.xlabel('Profit ($k)')
plt.legend()
plt.show()
```

---

## Summary

| Distribution | Parameters | Mean | Use Cases |
|--------------|------------|------|-----------|
| **Normal** | μ, σ | μ | General measurements, errors |
| **Uniform** | a, b | (a+b)/2 | Random selection |
| **Exponential** | λ | 1/λ | Time between events |
| **t** | df | 0 (if df>1) | Small samples, heavy tails |
| **Chi-square** | df | df | Variance tests, goodness of fit |
| **F** | df1, df2 | df2/(df2-2) | ANOVA, variance ratios |
| **Beta** | α, β | α/(α+β) | Probabilities, proportions |
| **Gamma** | α, β | αβ | Waiting times, claims |
| **Lognormal** | μ, σ | exp(μ+σ²/2) | Income, prices |
| **Weibull** | c | Γ(1+1/c) | Reliability, survival |

**Key methods:**
- `pdf()`: Probability density at x
- `cdf()`: Cumulative probability P(X ≤ x)
- `ppf()`: Inverse CDF (quantiles)
- `rvs()`: Random samples
- `fit()`: Parameter estimation
- `stats()`: Summary statistics

**Key insight:** Continuous distributions provide mathematical models for real-world phenomena, enabling probabilistic reasoning, uncertainty quantification, and statistical inference through a rich set of analytical and computational tools.
