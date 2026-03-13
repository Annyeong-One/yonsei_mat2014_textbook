# NumPy FFT — Fourier Transforms

The `np.fft` module provides functions for computing the discrete Fourier transform (DFT) and its inverse. Fourier transforms decompose signals into their frequency components.

```python
import numpy as np
```

---

## What is a Fourier Transform?

The Fourier transform converts a signal from the **time domain** to the **frequency domain**:

- **Time domain**: Signal as amplitude vs. time
- **Frequency domain**: Signal as amplitude vs. frequency

```
Time Domain          Fourier Transform       Frequency Domain
    │                      →                      │
 ───┼──▄█▄──           np.fft.fft()         ───┼─█─────
    │                                            │   █
    t                                            f
```

---

## Mathematical Foundations of the DFT

The Discrete Fourier Transform (DFT) converts a length-$N$ sequence $\{x_0, x_1, \ldots, x_{N-1}\}$ in the time domain to a length-$N$ sequence $\{y_0, y_1, \ldots, y_{N-1}\}$ in the frequency domain:

$$y_k = \sum_{n=0}^{N-1} e^{-i\frac{2\pi}{N}nk} x_n, \qquad k = 0, 1, \ldots, N-1$$

The inverse DFT recovers the original sequence:

$$x_n = \frac{1}{N} \sum_{k=0}^{N-1} e^{i\frac{2\pi}{N}nk} y_k, \qquad n = 0, 1, \ldots, N-1$$

### Matrix Form

The DFT can be expressed as a matrix-vector multiplication $\mathbf{y} = W \mathbf{x}$, where $W$ is the DFT matrix with entries $W_{kn} = e^{-i 2\pi kn / N}$. The inverse DFT is $\mathbf{x} = \frac{1}{N} W^* \mathbf{y}$, where $W^*$ is the conjugate of $W$.

### Manual DFT Implementation

Building the DFT from the matrix formula reinforces the linear algebra connection:

```python
import numpy as np
import matplotlib.pyplot as plt

N = 100
time = np.linspace(-2, 2, N)
x = np.zeros_like(time)
x[abs(time) < 1] = time[abs(time) < 1]  # Tent function

# Build the DFT matrix
n = np.arange(N).reshape((N, 1))
k = np.arange(N).reshape((1, N))
nk = n @ k  # (N, N) outer product
W = np.exp(-1j * (2 * np.pi / N) * nk)       # DFT matrix
W_inv = np.exp(1j * (2 * np.pi / N) * nk)    # Inverse DFT matrix

# Forward and inverse transforms
y = W @ x
x_recovered = (W_inv @ y) / N

fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(12, 3))
ax0.plot(x, '--ok', markersize=1, label='Original')
ax1.plot(np.real(y), '--ob', markersize=1, label='Real')
ax1.plot(np.imag(y), '--or', markersize=1, label='Imag')
ax2.plot(x, '--ok', markersize=1, label='Original')
ax2.plot(np.real(x_recovered), '--ob', markersize=1, label='Recovered Real')
for ax, title in zip((ax0, ax1, ax2), ('Time Domain', 'Frequency Domain', 'Time Domain')):
    ax.legend()
    ax.set_title(title)
plt.tight_layout()
plt.show()
```

The manual implementation confirms that `np.fft.fft()` and `np.fft.ifft()` are simply optimized algorithms (the Fast Fourier Transform) for computing this matrix-vector product in $O(N \log N)$ instead of $O(N^2)$.

---

## Basic FFT

### np.fft.fft() — 1D Transform

```python
# Simple signal: sum of two sine waves
t = np.linspace(0, 1, 1000)  # 1 second, 1000 samples
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Compute FFT
fft_result = np.fft.fft(signal)

# Result is complex: contains magnitude and phase
print(fft_result.dtype)  # complex128
print(len(fft_result))   # 1000 (same as input)
```

### Getting Frequencies

```python
# Sample rate
sample_rate = 1000  # Hz (samples per second)
n = len(signal)

# Get frequency bins
frequencies = np.fft.fftfreq(n, d=1/sample_rate)

# Magnitude spectrum
magnitude = np.abs(fft_result)

# Phase spectrum
phase = np.angle(fft_result)
```

### Positive Frequencies Only

FFT output is symmetric for real signals. Usually we only want positive frequencies:

```python
# Use only first half (positive frequencies)
n_half = n // 2
freq_positive = frequencies[:n_half]
magnitude_positive = magnitude[:n_half]

# Or use rfft for real input (more efficient)
fft_real = np.fft.rfft(signal)
freq_real = np.fft.rfftfreq(n, d=1/sample_rate)
```

---

## Inverse FFT

### np.fft.ifft() — Reconstruct Signal

```python
# Original signal
signal = np.sin(2 * np.pi * 5 * t)

# Forward FFT
fft_result = np.fft.fft(signal)

# Inverse FFT (reconstruct)
reconstructed = np.fft.ifft(fft_result)

# Should match original (within floating point precision)
print(np.allclose(signal, reconstructed.real))  # True
```

---

## 2D FFT (Images)

### np.fft.fft2() — 2D Transform

```python
# Create simple 2D pattern
image = np.zeros((100, 100))
image[40:60, 40:60] = 1  # White square

# 2D FFT
fft_2d = np.fft.fft2(image)

# Shift zero frequency to center (for visualization)
fft_shifted = np.fft.fftshift(fft_2d)

# Magnitude spectrum
magnitude_2d = np.abs(fft_shifted)
```

### Inverse 2D FFT

```python
# Reconstruct image
reconstructed = np.fft.ifft2(fft_2d)
print(np.allclose(image, reconstructed.real))  # True
```

---

## Common Operations

### fftshift / ifftshift

Shift zero-frequency component to center (useful for visualization):

```python
fft_result = np.fft.fft(signal)

# Shift: zero frequency to center
shifted = np.fft.fftshift(fft_result)

# Unshift: back to original layout
unshifted = np.fft.ifftshift(shifted)
```

### rfft / irfft (Real Input)

More efficient for real-valued signals:

```python
# Real signal → use rfft (half the output)
signal = np.random.randn(1000)

fft_complex = np.fft.fft(signal)     # Length: 1000
fft_real = np.fft.rfft(signal)       # Length: 501

# Inverse
reconstructed = np.fft.irfft(fft_real)
```

---

## Practical Examples

### Find Dominant Frequency

```python
# Signal with unknown frequency
sample_rate = 1000
t = np.linspace(0, 1, sample_rate)
signal = np.sin(2 * np.pi * 50 * t) + np.random.randn(sample_rate) * 0.5

# FFT
fft = np.fft.rfft(signal)
freqs = np.fft.rfftfreq(len(signal), 1/sample_rate)
magnitudes = np.abs(fft)

# Find peak frequency
peak_idx = np.argmax(magnitudes)
dominant_freq = freqs[peak_idx]
print(f"Dominant frequency: {dominant_freq} Hz")  # ~50 Hz
```

### Low-Pass Filter

```python
def low_pass_filter(signal, sample_rate, cutoff_freq):
    """Remove frequencies above cutoff."""
    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), 1/sample_rate)
    
    # Zero out high frequencies
    fft[freqs > cutoff_freq] = 0
    
    # Reconstruct
    return np.fft.irfft(fft)

# Apply 100 Hz low-pass filter
filtered = low_pass_filter(signal, sample_rate=1000, cutoff_freq=100)
```

### Remove Specific Frequency (Notch Filter)

```python
def notch_filter(signal, sample_rate, remove_freq, bandwidth=2):
    """Remove specific frequency band."""
    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), 1/sample_rate)
    
    # Zero out target frequency band
    mask = (freqs > remove_freq - bandwidth) & (freqs < remove_freq + bandwidth)
    fft[mask] = 0
    
    return np.fft.irfft(fft)

# Remove 60 Hz hum
clean_signal = notch_filter(signal, 1000, 60)
```

### Power Spectrum

```python
def power_spectrum(signal, sample_rate):
    """Compute power spectral density."""
    n = len(signal)
    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n, 1/sample_rate)
    
    # Power = |FFT|² / n
    power = np.abs(fft) ** 2 / n
    
    return freqs, power

freqs, power = power_spectrum(signal, 1000)
```

---

## FFT Functions Summary

| Function | Purpose |
|----------|---------|
| `fft(a)` | 1D FFT |
| `ifft(a)` | Inverse 1D FFT |
| `fft2(a)` | 2D FFT |
| `ifft2(a)` | Inverse 2D FFT |
| `fftn(a)` | N-dimensional FFT |
| `rfft(a)` | 1D FFT for real input |
| `irfft(a)` | Inverse of rfft |
| `fftfreq(n, d)` | Frequency bins for fft |
| `rfftfreq(n, d)` | Frequency bins for rfft |
| `fftshift(a)` | Shift zero-freq to center |
| `ifftshift(a)` | Inverse of fftshift |

---

## Performance Tips

```python
# FFT is fastest when length is power of 2
n = 1024  # 2^10 — fast
n = 1000  # not power of 2 — slower

# Pad to next power of 2
def next_power_of_2(x):
    return 1 << (x - 1).bit_length()

signal_padded = np.pad(signal, (0, next_power_of_2(len(signal)) - len(signal)))
```

---

## scipy.fft Module

The `scipy.fft` module provides the same FFT functions as `np.fft` but with additional features such as multithreading support via the `workers` parameter:

```python
import scipy.fft as fft

y = fft.fft(x)
x_recovered = fft.ifft(y)

# Parallel computation with multiple workers
y_parallel = fft.fft(x, workers=-1)  # Use all available CPU cores
```

For most use cases, `np.fft` and `scipy.fft` produce identical results. Use `scipy.fft` when you need the extra performance from multithreading or access to additional transform types.

---

## Key Takeaways

- FFT converts time domain → frequency domain
- `np.fft.fft()` for complex/general signals
- `np.fft.rfft()` for real signals (more efficient)
- `fftfreq()` / `rfftfreq()` get frequency bins
- `fftshift()` centers zero frequency (for visualization)
- Use `np.abs()` for magnitude, `np.angle()` for phase
- Power of 2 lengths are fastest
- Common applications: filtering, spectrum analysis, image processing
