"""
Sparse Matrix Operations for Information Theory - Variation of Information
Exploring sparse matrix formats (COO, CSR), sparse diagonal matrices, and
information-theoretic computations using SciPy's sparse module.
Run this file to see practical examples of sparse matrices in action!
"""

import numpy as np
from scipy import sparse

print("=" * 70)
print("SPARSE MATRIX OPERATIONS FOR INFORMATION-THEORETIC COMPUTATIONS")
print("=" * 70)

# ============================================================================
# EXAMPLE 1: Building Sparse Matrices from Data - COO Format
# ============================================================================
print("\n1. BUILDING SPARSE MATRICES IN COORDINATE (COO) FORMAT")
print("-" * 70)

# The COO (Coordinate) format is efficient when you have (row, col, data) tuples
# Perfect for constructing sparse matrices from raw data
x = np.array([1, 0, 2, 1, 1, 2])  # row indices
y = np.array([0, 1, 1, 2, 0, 2])  # column indices
data = np.ones(len(x))             # values at (x, y) positions

# Create a COO matrix: this represents a 3x3 sparse matrix with counts
coo = sparse.coo_matrix((data, (x, y)), shape=(3, 3))
print("COO matrix (raw format):")
print(coo)
print("\nDensity: {:.2%} non-zero elements".format(coo.nnz / (3 * 3)))

# ============================================================================
# EXAMPLE 2: Converting Between Sparse Formats
# ============================================================================
print("\n2. CONVERTING BETWEEN SPARSE FORMATS: COO -> CSR")
print("-" * 70)

# Convert COO to CSR (Compressed Sparse Row) for efficient arithmetic
csr = coo.tocsr()
print("Converted to CSR format (better for row operations):")
print(csr)
print("CSR data:", csr.data)
print("CSR indptr:", csr.indptr)
print("CSR indices:", csr.indices)

# Normalize the matrix to represent a probability distribution
pxy = csr.copy()
pxy.data /= np.sum(pxy.data)
print("\nNormalized to sum to 1.0 (probability distribution):")
print("Sum of all elements:", pxy.sum())

# ============================================================================
# EXAMPLE 3: Computing Marginal Probabilities from Sparse Joint Distribution
# ============================================================================
print("\n3. COMPUTING MARGINAL PROBABILITIES")
print("-" * 70)

# From joint distribution p(x,y), compute marginals p(x) and p(y)
# sum(axis=1) gives row sums, sum(axis=0) gives column sums
px = np.array(pxy.sum(axis=1)).ravel()  # p(x): sum over y
py = np.array(pxy.sum(axis=0)).ravel()  # p(y): sum over x

print("p(x) - marginal probability over x:", px)
print("p(y) - marginal probability over y:", py)
print("Both marginals sum to 1.0: p(x)={:.3f}, p(y)={:.3f}".format(px.sum(), py.sum()))

# ============================================================================
# EXAMPLE 4: Creating Sparse Diagonal Matrices
# ============================================================================
print("\n4. CREATING SPARSE DIAGONAL MATRICES WITH sparse.diags()")
print("-" * 70)

# sparse.diags creates diagonal matrices efficiently
# Input: diagonals as list, offsets as list
diag_values = np.array([0.1, 0.3, 0.4, 0.2])  # diagonal elements
diag_matrix = sparse.diags([diag_values], [0], shape=(4, 4))

print("Sparse diagonal matrix created from diagonal values:")
print(diag_matrix.todense())
print("Non-zero elements:", diag_matrix.nnz)

# Computing inverses is safe with sparse.diags even with zeros
# For elements with value v, the inverse is 1/v
def safe_inverse(arr):
    """Safely invert array, leaving zeros as zeros"""
    arr_inv = arr.copy()
    nz = np.nonzero(arr)  # find non-zero indices
    arr_inv[nz] = 1 / arr[nz]  # invert only non-zero elements
    return arr_inv

px_inv_values = safe_inverse(px)
px_inv = sparse.diags([px_inv_values], [0])  # diagonal matrix of 1/p(x)
print("\nDiagonal matrix of 1/p(x):")
print(px_inv.todense())

# ============================================================================
# EXAMPLE 5: Element-wise Operations on Sparse Matrices
# ============================================================================
print("\n5. ELEMENT-WISE OPERATIONS: x*log(x) IN SPARSE MATRICES")
print("-" * 70)

def xlogx(arr):
    """Compute x*log(x) safely, treating 0*log(0) = 0"""
    result = arr.copy()
    nz = np.nonzero(arr)
    result[nz] = arr[nz] * np.log2(arr[nz])
    return result

# This is used in entropy calculations: H = -sum(p * log(p))
test_probs = np.array([0.0, 0.25, 0.5, 0.25])
xlogx_result = xlogx(test_probs)
print("Input probabilities:", test_probs)
print("x*log2(x) values:", xlogx_result)
print("Entropy contribution (-sum): {:.4f}".format(-np.sum(xlogx_result)))

# ============================================================================
# EXAMPLE 6: Computing Variation of Information (VI)
# ============================================================================
print("\n6. INFORMATION-THEORETIC METRIC: VARIATION OF INFORMATION")
print("-" * 70)

def variation_of_information(x, y):
    """
    Compute Variation of Information between two clusterings.

    VI(X;Y) = H(X|Y) + H(Y|X)
    where H(X|Y) is conditional entropy of X given Y

    Parameters:
    x, y: array-like cluster assignments (same length)

    Returns:
    VI score (lower is better, 0 means identical clustering)
    """
    # Build joint probability matrix from cluster assignments
    pxy = sparse.coo_matrix(
        (np.ones(x.size), (x.ravel(), y.ravel())),
        dtype=float
    ).tocsr()

    # Normalize to probability distribution
    pxy.data /= np.sum(pxy.data)

    # Compute marginals
    px = np.array(pxy.sum(axis=1)).ravel()
    py = np.array(pxy.sum(axis=0)).ravel()

    # Create inverse diagonal matrices
    px_inv = sparse.diags([safe_inverse(px)], [0])
    py_inv = sparse.diags([safe_inverse(py)], [0])

    # Compute H(Y|X) = -sum_x p(x) * sum_y p(y|x) * log(p(y|x))
    # where p(y|x) = p(x,y) / p(x)
    hygx = -(px * xlogx(py_inv.dot(pxy)).sum(axis=1)).sum()

    # Compute H(X|Y) = -sum_y p(y) * sum_x p(x|y) * log(p(x|y))
    hxgy = -(py * xlogx(pxy.dot(px_inv)).sum(axis=1)).sum()

    return hygx + hxgy

# Test VI with example clusterings
clustering1 = np.array([0, 0, 1, 1, 2, 2])  # first clustering
clustering2 = np.array([0, 0, 1, 1, 2, 2])  # identical clustering
clustering3 = np.array([0, 1, 0, 1, 0, 1])  # completely different

vi_same = variation_of_information(clustering1, clustering2)
vi_diff = variation_of_information(clustering1, clustering3)

print("Clustering 1:", clustering1)
print("Clustering 2 (identical):", clustering2)
print("VI(identical) = {:.4f} (should be ~0)".format(vi_same))
print("\nClustering 3 (different):", clustering3)
print("VI(different) = {:.4f}".format(vi_diff))
print("\nVI metric: lower values indicate more similar clusterings")
print("VI = 0 means identical clusterings")

# ============================================================================
# EXAMPLE 7: Practical Sparse Computation Patterns
# ============================================================================
print("\n7. PRACTICAL PATTERNS: EFFICIENT SPARSE COMPUTATIONS")
print("-" * 70)

# Pattern 1: Element-wise multiplication with diagonal matrices
print("\nPattern 1: Left-multiply matrix by diagonal")
test_matrix = np.array([[1, 2], [3, 4]], dtype=float)
test_sparse = sparse.csr_matrix(test_matrix)
scaling_diag = sparse.diags([2.0, 0.5])  # scale rows
result = scaling_diag @ test_sparse
print("Original:\n", test_matrix)
print("After scaling first row by 2.0, second by 0.5:")
print(result.todense())

# Pattern 2: Handling division in sparse matrices
print("\nPattern 2: Safe division in sparse contexts")
values = np.array([1.0, 2.0, 0.0, 4.0])
inv_values = safe_inverse(values)
print("Original values:", values)
print("After safe inversion:", inv_values)
print("(zeros remain zero, others inverted)")

# Pattern 3: Computing with conditional probabilities
print("\nPattern 3: Computing matrix products for conditional probabilities")
joint = sparse.csr_matrix(np.array([[0.1, 0.2], [0.3, 0.4]]))
normalizer = sparse.diags([1/0.4, 1/0.7])  # normalize by column sums
conditional = joint @ normalizer
print("Joint distribution shape:", joint.shape)
print("After normalization (columns sum to 1):")
print(conditional.todense())

print("\n" + "=" * 70)
print("Key takeaways:")
print("- COO format: good for construction from coordinate data")
print("- CSR format: efficient for arithmetic and row operations")
print("- sparse.diags(): creates diagonal matrices efficiently")
print("- Safe operations: handle zeros carefully in log/inverse operations")
print("- Application: VI measures clustering similarity via sparse matrix ops")
print("=" * 70)
