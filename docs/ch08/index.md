# Chapter 8: NumPy

This chapter covers NumPy, the foundational library for numerical computing in Python, including array creation, indexing, broadcasting, vectorization, linear algebra, random number generation, and Fourier transforms.

## 8.1 Getting Started

- [Installation](setup/installation.md)
- [Import Convention](setup/import_convention.md)
- [Version Check](setup/version_check.md)

## 8.2 Overview

- [Lists vs Arrays](overview/lists_vs_arrays.md)
- [NumPy Constants](overview/numpy_constants.md)

## 8.3 Array Creation

- [np.array and Dimensions](generation/np_array.md)
- [np.zeros, np.ones, np.empty](generation/zeros_ones_empty.md)
- [np.full and np.eye](generation/full_eye_identity.md)
- [np.arange and np.linspace](generation/arange_linspace.md)
- [np.diag and Diagonal Matrices](generation/diag_matrices.md)

## 8.4 Array Attributes

- [Shape and ndim](attributes/shape_ndim.md)
- [Reshaping Arrays](attributes/reshape.md)
- [Expanding Dimensions](attributes/expand_dims.md)
- [np.newaxis](attributes/numpy_newaxis.md)
- [Squeezing Dimensions](attributes/squeeze.md)
- [Dtype Basics](attributes/dtype_basics.md)
- [Changing Dtype](attributes/dtype_conversion.md)

## 8.5 Indexing and Slicing

- [Basic Indexing](indexing/basic_indexing.md)
- [Slicing Arrays](indexing/slicing.md)
- [Shape After Indexing](indexing/shape_after_indexing.md)
- [Image Manipulation](indexing/image_manipulation.md)
- [Fancy Indexing](indexing/fancy_indexing.md)
- [Boolean Masking](indexing/boolean_masking.md)

## 8.6 Views and Copies

- [View vs Copy](memory/numpy_views_copies.md)
- [Operations That Return Views](memory/view_operations.md)
- [Operations That Return Copies](memory/copy_operations.md)
- [ravel vs flatten](memory/ravel_flatten.md)
- [Memory Contiguity](memory/contiguity.md)
- [Stride Tricks](memory/strides.md)

## 8.7 Element-wise Operations

- [Arithmetic Operations](operations/arithmetic.md)
- [Power Exp Log](operations/power_exp_log.md)
- [Rounding Functions](operations/rounding.md)
- [Comparison Operators](operations/comparison.md)
- [Universal Functions](operations/ufuncs.md)

## 8.8 Broadcasting

- [Broadcasting Rules](broadcasting/broadcasting.md)
- [Broadcasting with Different ndims](broadcasting/different_ndims.md)
- [Common Broadcasting Patterns](broadcasting/common_patterns.md)
- [Broadcasting Failures and Debugging](broadcasting/failures_debugging.md)
- [Performance Implications](broadcasting/performance.md)

## 8.9 Vectorization

- [Performance vs Loops](vectorization/performance.md)
- [Vectorization Basics](vectorization/vectorization_basics.md)
- [Summation Benchmark](vectorization/summation_benchmark.md)
- [Numerical Integration](vectorization/numerical_integration.md)
- [Loop Hoisting](vectorization/loop_hoisting.md)
- [Memory Preallocation](vectorization/preallocation.md)
- [In-Place Operations](vectorization/inplace_operations.md)
- [Profiling Tools](vectorization/profiling_tools.md)
- [Einsum Operations](vectorization/einsum.md)
- [Acceleration Libraries](vectorization/acceleration_libs.md)
- [np.vectorize](vectorization/numpy_vectorize.md)

## 8.10 Array Manipulation

- [Transpose and Swapaxes](manipulation/transpose.md)
- [Concatenation](manipulation/concatenation.md)
- [Splitting Arrays](manipulation/splitting.md)
- [Array Iteration](manipulation/iteration.md)
- [Roll](manipulation/roll.md)

## 8.11 Array Methods

- [Reductions with axis](methods/reductions.md)
- [Min Max Argmin Argmax](methods/minmax.md)
- [Sum Prod Cumsum](methods/sum_prod.md)
- [Element-wise Min Max](methods/elementwise_minmax.md)
- [Statistics Methods](methods/statistics.md)
- [Covariance Correlation](methods/cov_corr.md)
- [Sorting Arrays](methods/sorting.md)
- [Searching Arrays](methods/searching.md)
- [Filtering with where](methods/where.md)
- [Utility Functions](methods/utility.md)

## 8.12 Array Utilities

- [clip, unique, diff, gradient](utilities/numpy_utilities.md)

## 8.13 Random Arrays

- [Random Seed and Reproducibility](random/seed.md)
- [Normal Distributions](random/normal.md)
- [Uniform Distributions](random/uniform.md)
- [Binomial Distribution](random/binomial.md)
- [Poisson Distribution](random/poisson.md)
- [Exponential Distribution](random/exponential.md)
- [Discrete Distributions](random/discrete.md)
- [Random Permutations](random/permutations.md)

## 8.14 Mesh Grids

- [np.meshgrid](meshgrid/meshgrid.md)
- [np.mgrid and np.ogrid](meshgrid/mgrid_ogrid.md)
- [Surface Plotting](meshgrid/surface_plotting.md)

## 8.15 Linear Algebra

- [Matrix Multiplication](linalg/matrix_multiply.md)
- [Determinant and Inverse](linalg/det_inv.md)
- [Solving Linear Systems](linalg/solve_systems.md)
- [Eigenvalues](linalg/eigenvalues.md)
- [Singular Value Decomposition](linalg/svd.md)
- [Matrix Norms](linalg/norms.md)
- [Cholesky Decomposition](linalg/cholesky.md)
- [QR Decomposition](linalg/qr.md)

## 8.16 Polynomial and Curve Fitting

- [np.polyfit and np.poly1d](fitting/numpy_polyfit.md)
- [np.polynomial Module (Modern API)](fitting/numpy_polynomial.md)
- [Polynomial Class](fitting/polynomial_class.md)
- [Least Squares Connection](fitting/least_squares.md)
- [scipy.interpolate — Spline Interpolation](fitting/scipy_interpolation.md)

## 8.17 Fourier Transforms

- [np.fft Module](fft/numpy_fft.md)
- [Spectrogram and STFT](fft/spectrogram_stft.md)
- [Window Functions](fft/windowing.md)
- [2D FFT for Images](fft/fft_2d_image.md)

## 8.18 Array I/O

- [save, load, savez](io/numpy_io.md)

## 8.19 Structured Arrays

- [Record Arrays](structured/numpy_structured.md)

## 8.20 NumPy OOP Design

- [NumPy ndarray Design](oop/numpy_ndarray.md)
- [NumPy dtype and Shape](oop/numpy_dtype_shape.md)
- [NumPy UFuncs](oop/numpy_ufuncs.md)
- [NumPy vs C Arrays](oop/numpy_vs_c.md)
- [PIL vs NumPy Images](oop/pil_vs_numpy.md)

## 8.21 scipy.ndimage

- [Convolution and Filtering](ndimage/convolution_filtering.md)
- [Generic Filters](ndimage/generic_filter.md)
- [Binary Structure and Morphology](ndimage/binary_structure.md)
