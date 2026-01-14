# Brownian Motion

Visualize stochastic processes with Matplotlib.

---

## Brownian Motion Class

```python
import matplotlib.pyplot as plt
import numpy as np

class BrownianMotion:

    def __init__(self, T=1):
        self.T = T

    def run_MC(self, num_paths=1, num_steps=None, seed=None):
        """
        Generate Brownian motion sample paths.
        
        Parameters
        ----------
        num_paths : int
            Number of paths to generate
        num_steps : int
            Number of time steps
        seed : int
            Random seed for reproducibility
            
        Returns
        -------
        t : array
            Time points
        dt : float
            Time step size
        sqrt_dt : float
            Square root of time step
        B : array
            Brownian motion paths (num_paths x num_steps+1)
        dB : array
            Increments (num_paths x num_steps)
        """
        if num_steps is None:
            num_steps = int(self.T * 12 * 21)  # Daily steps for 1 year
        if seed is not None:
            np.random.seed(seed)

        t = np.linspace(0, self.T, num_steps + 1)
        dt = t[1] - t[0]
        sqrt_dt = np.sqrt(dt)

        Z = np.random.standard_normal((num_paths, num_steps))
        if num_paths > 1:
            Z = (Z - Z.mean(axis=0)) / Z.std(axis=0)

        dB = Z * sqrt_dt
        B = np.concatenate([np.zeros((num_paths, 1)), dB.cumsum(axis=1)], axis=1)
        
        return t, dt, sqrt_dt, B, dB
```

---

## Plotting Sample Paths

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    num_paths = 10
    num_steps = 1000

    bm = BrownianMotion()
    t, _, _, B, _ = bm.run_MC(num_paths, num_steps, seed=0)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_title('Ten Sample Paths of Brownian Motion $B_t$')
    
    for i in range(num_paths):
        ax.plot(t, B[i], alpha=0.7)
    
    ax.set_xlabel('Time $t$')
    ax.set_ylabel('$B_t$')
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.grid(True, alpha=0.3)
    
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Distribution at Terminal Time

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def main():
    num_paths = 10000
    num_steps = 1000
    T = 1

    bm = BrownianMotion(T=T)
    t, _, _, B, _ = bm.run_MC(num_paths, num_steps, seed=42)

    # Terminal values
    terminal_values = B[:, -1]

    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Histogram
    ax.hist(terminal_values, bins=50, density=True, alpha=0.7, label='Simulated')
    
    # Theoretical distribution: N(0, T)
    x = np.linspace(-4, 4, 100)
    ax.plot(x, stats.norm(0, np.sqrt(T)).pdf(x), 'r-', lw=2, label=f'$N(0, {T})$')
    
    ax.set_xlabel('$B_T$')
    ax.set_ylabel('Density')
    ax.set_title(f'Distribution of $B_T$ at $T={T}$')
    ax.legend()
    
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Geometric Brownian Motion

Stock price model:

```python
import matplotlib.pyplot as plt
import numpy as np

def simulate_gbm(S0, mu, sigma, T, num_paths, num_steps, seed=None):
    """
    Simulate Geometric Brownian Motion.
    
    S_t = S_0 * exp((mu - sigma^2/2)*t + sigma*B_t)
    """
    if seed is not None:
        np.random.seed(seed)
    
    dt = T / num_steps
    t = np.linspace(0, T, num_steps + 1)
    
    # Generate standard normal increments
    dW = np.random.randn(num_paths, num_steps) * np.sqrt(dt)
    W = np.concatenate([np.zeros((num_paths, 1)), dW.cumsum(axis=1)], axis=1)
    
    # GBM formula
    drift = (mu - 0.5 * sigma**2) * t
    diffusion = sigma * W
    S = S0 * np.exp(drift + diffusion)
    
    return t, S

def main():
    S0 = 100       # Initial price
    mu = 0.10      # Drift (10% annual return)
    sigma = 0.20   # Volatility (20%)
    T = 1          # Time horizon (1 year)
    num_paths = 20
    num_steps = 252  # Trading days

    t, S = simulate_gbm(S0, mu, sigma, T, num_paths, num_steps, seed=42)

    fig, ax = plt.subplots(figsize=(12, 5))
    
    for i in range(num_paths):
        ax.plot(t * 252, S[i], alpha=0.6)
    
    ax.axhline(S0, color='black', linestyle='--', label=f'$S_0={S0}$')
    ax.axhline(S0 * np.exp(mu * T), color='red', linestyle='--', 
               label=f'Expected: ${S0 * np.exp(mu * T):.1f}$')
    
    ax.set_xlabel('Trading Days')
    ax.set_ylabel('Stock Price')
    ax.set_title('Geometric Brownian Motion - Stock Price Simulation')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Confidence Bands

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    num_paths = 1000
    num_steps = 252
    T = 1

    bm = BrownianMotion(T=T)
    t, _, _, B, _ = bm.run_MC(num_paths, num_steps, seed=42)

    # Calculate statistics
    mean = B.mean(axis=0)
    std = B.std(axis=0)
    
    # Theoretical standard deviation
    theoretical_std = np.sqrt(t)

    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Plot a few sample paths
    for i in range(5):
        ax.plot(t, B[i], alpha=0.3, color='blue')
    
    # Confidence bands
    ax.fill_between(t, mean - 2*std, mean + 2*std, 
                    alpha=0.2, color='blue', label='±2σ (empirical)')
    ax.plot(t, 2*theoretical_std, 'r--', label='±2σ (theoretical)')
    ax.plot(t, -2*theoretical_std, 'r--')
    
    ax.set_xlabel('Time $t$')
    ax.set_ylabel('$B_t$')
    ax.set_title('Brownian Motion with Confidence Bands')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Key Takeaways

- Brownian motion is the foundation of stochastic calculus
- Use NumPy for efficient path generation
- Plot multiple paths to show distribution of outcomes
- GBM models stock prices with log-normal distribution
- Confidence bands show expected variation over time
