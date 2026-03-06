"""
Manual DFT Implementation Using Matrix Algebra
================================================
Level: Intermediate
Topics: Discrete Fourier Transform, matrix-vector multiplication,
        complex exponentials, frequency domain analysis

This module implements the DFT from first principles using the matrix
formulation, then verifies against scipy.fft for correctness.
"""

import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt

# =============================================================================
# SECTION 1: Build the DFT Matrix
# =============================================================================

if __name__ == "__main__":
    """
    The DFT of a length-N sequence x is y = W @ x, where:

        W[k, n] = exp(-i * 2π * k * n / N)

    The inverse DFT is x = (1/N) * W* @ y, where W* is the conjugate.
    """


    def build_dft_matrix(N):
        """Build the N×N DFT matrix W and its conjugate W*."""
        n = np.arange(N).reshape((N, 1))
        k = np.arange(N).reshape((1, N))
        nk = n @ k  # (N, N) outer product of indices
        W = np.exp(-1j * (2 * np.pi / N) * nk)
        W_conj = np.exp(1j * (2 * np.pi / N) * nk)
        return W, W_conj


    def manual_fft(x, W):
        """Forward DFT: y = W @ x."""
        return W @ x


    def manual_ifft(y, W_conj, N):
        """Inverse DFT: x = (1/N) * W* @ y."""
        return (W_conj @ y) / N


    # =============================================================================
    # SECTION 2: Test Signal — Tent Function
    # =============================================================================

    N = 100
    time = np.linspace(-2, 2, N)
    x = np.zeros_like(time)
    x[abs(time) < 1] = time[abs(time) < 1]

    # =============================================================================
    # SECTION 3: Manual DFT vs scipy.fft
    # =============================================================================

    W, W_conj = build_dft_matrix(N)

    # Manual DFT
    y_manual = manual_fft(x, W)
    x_recovered_manual = manual_ifft(y_manual, W_conj, N)

    # scipy.fft for comparison
    y_scipy = fft.fft(x)
    x_recovered_scipy = fft.ifft(y_scipy)

    # Verify they match
    print("Manual vs scipy.fft agreement:")
    print(f"  Forward: {np.allclose(y_manual, y_scipy)}")
    print(f"  Inverse: {np.allclose(x_recovered_manual, x_recovered_scipy)}")
    print(f"  Roundtrip error: {np.max(np.abs(x - np.real(x_recovered_manual))):.2e}")

    # =============================================================================
    # SECTION 4: Visualization
    # =============================================================================

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    # Time domain (original)
    axes[0].plot(x, '--ok', markersize=2, label='Original')
    axes[0].set_title('Time Domain')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Frequency domain
    axes[1].plot(np.real(y_manual), '--ob', markersize=1, label='Real')
    axes[1].plot(np.imag(y_manual), '--or', markersize=1, label='Imag')
    axes[1].set_title('Frequency Domain (Manual DFT)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # Recovered signal
    axes[2].plot(x, '--ok', markersize=2, label='Original')
    axes[2].plot(np.real(x_recovered_manual), '--ob', markersize=1, label='Recovered')
    axes[2].set_title('Time Domain (Recovered)')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # =============================================================================
    # SECTION 5: Performance Comparison
    # =============================================================================
    """
    The manual DFT using matrix multiplication is O(N²).
    The FFT algorithm (Cooley-Tukey) is O(N log N).
    For N = 100, this is 10000 vs ~664 — a ~15x difference.
    For N = 10000, it's 100,000,000 vs ~132,877 — a ~750x difference.
    """

    import time

    for N_test in [100, 1000]:
        W_test, _ = build_dft_matrix(N_test)
        x_test = np.random.randn(N_test)

        t0 = time.perf_counter()
        for _ in range(100):
            _ = W_test @ x_test
        t_manual = time.perf_counter() - t0

        t0 = time.perf_counter()
        for _ in range(100):
            _ = fft.fft(x_test)
        t_fft = time.perf_counter() - t0

        print(f"\nN={N_test}:")
        print(f"  Manual (matrix):  {t_manual:.4f} sec")
        print(f"  scipy.fft:        {t_fft:.4f} sec")
        print(f"  Speedup:          {t_manual / t_fft:.1f}x")
