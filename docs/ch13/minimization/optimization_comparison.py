"""
Comparing SciPy Optimization Methods - A Comprehensive Tutorial
Exploring scipy.optimize.minimize with multiple algorithms, callback functions,
Jacobians, Hessians, and convergence analysis. See optimization in action!
Run this file to compare different optimization strategies!
"""

import numpy as np
from scipy import optimize
import sys

print("=" * 70)
print("COMPARING SCIPY OPTIMIZATION METHODS")
print("=" * 70)

# ============================================================================
# EXAMPLE 1: The Rosenbrock Function - A Classic Optimization Benchmark
# ============================================================================
print("\n1. THE ROSENBROCK FUNCTION: A CHALLENGING TEST CASE")
print("-" * 70)

def rosenbrock_f(a, b):
    """
    Return the Rosenbrock function, Jacobian, and Hessian.

    The Rosenbrock function is a classic test case for optimization:
    f(x, y) = (a - x)^2 + b*(y - x^2)^2

    It has a minimum value of 0 at (a, a^2).
    The function is easy to evaluate but has a narrow curved valley,
    making it challenging for gradient-free methods.

    Parameters
    ----------
    a, b : float
        Parameters defining the surface. Typical values are a=1, b=100.
        Higher b makes the valley narrower and harder to navigate.
    """
    def f(x, y):
        return (a - x)**2 + b * (y - x**2) ** 2

    def J(x, y):
        # Jacobian (gradient) of the Rosenbrock function
        # df/dx = -2(a - x) - 4*b*x*(y - x^2)
        # df/dy = 2*b*(y - x^2)
        return np.array([
            -2 * (a - x) - 4 * b * x * (y - x**2),
            2 * b * (y - x ** 2)
        ])

    def H(x, y):
        # Hessian (matrix of second derivatives)
        # Used by Newton-CG and trust region methods
        # [d²f/dx²  d²f/dxdy]
        # [d²f/dydx d²f/dy²]
        return np.array([
            [2 + 8*b*x**2 - 4*b*(y - x**2), -4*b*x],
            [-4*b*x, 2*b]
        ])

    return f, J, H

# Set up Rosenbrock with typical parameters
a, b = 1.0, 100.0
rosenbrock, rosenbrock_J, rosenbrock_H = rosenbrock_f(a=a, b=b)

# Test evaluation
x0_test, y0_test = -0.5, 2.5
f_val = rosenbrock(x0_test, y0_test)
print(f"Rosenbrock function at ({x0_test}, {y0_test}): {f_val:.4f}")
print(f"True minimum is at ({a}, {a**2}) with value 0.0")
print(f"Starting point is {f_val:.0f} units away from optimum")

# Evaluate gradient and Hessian
grad = rosenbrock_J(x0_test, y0_test)
hess = rosenbrock_H(x0_test, y0_test)
print(f"\nGradient at start: {grad}")
print(f"Hessian at start:\n{hess}")

# ============================================================================
# EXAMPLE 2: Nelder-Mead Method - Gradient-Free Optimization
# ============================================================================
print("\n2. NELDER-MEAD METHOD: NO GRADIENTS NEEDED")
print("-" * 70)

print("Nelder-Mead is a simplex-based method requiring only function values.")
print("Advantages: robust, no gradients needed, handles non-smooth functions")
print("Disadvantages: slower convergence, more function evaluations\n")

x0 = np.array([-0.5, 2.5])
result_nm = optimize.minimize(
    lambda p: rosenbrock(*p),
    x0=x0,
    method='Nelder-Mead',
    options={'disp': False}
)

print("Nelder-Mead Results:")
print(f"  Optimal point: ({result_nm.x[0]:.6f}, {result_nm.x[1]:.6f})")
print(f"  Function value: {result_nm.fun:.2e}")
print(f"  Iterations: {result_nm.nit}")
print(f"  Function evaluations: {result_nm.nfev}")
print(f"  Success: {result_nm.success}")

# ============================================================================
# EXAMPLE 3: BFGS Method - Quasi-Newton with Gradient
# ============================================================================
print("\n3. BFGS METHOD: QUASI-NEWTON WITH GRADIENT")
print("-" * 70)

print("BFGS is a quasi-Newton method that approximates the Hessian.")
print("Advantages: faster than gradient-free, uses only gradients (no Hessian)")
print("Disadvantages: needs accurate gradients, may fail on non-smooth functions\n")

result_bfgs = optimize.minimize(
    lambda p: rosenbrock(*p),
    x0=x0,
    jac=lambda p: rosenbrock_J(*p),
    method='BFGS',
    options={'disp': False}
)

print("BFGS Results:")
print(f"  Optimal point: ({result_bfgs.x[0]:.6f}, {result_bfgs.x[1]:.6f})")
print(f"  Function value: {result_bfgs.fun:.2e}")
print(f"  Iterations: {result_bfgs.nit}")
print(f"  Function evaluations: {result_bfgs.nfev}")
print(f"  Gradient evaluations: {result_bfgs.njev}")

# ============================================================================
# EXAMPLE 4: Newton-CG Method - Using Exact Hessian
# ============================================================================
print("\n4. NEWTON-CG METHOD: USING EXACT HESSIAN")
print("-" * 70)

print("Newton-CG uses exact Hessian information for rapid convergence.")
print("Advantages: fewest iterations, most accurate near minimum")
print("Disadvantages: must compute and provide Hessian matrix\n")

result_ncg = optimize.minimize(
    lambda p: rosenbrock(*p),
    x0=x0,
    jac=lambda p: rosenbrock_J(*p),
    hess=lambda p: rosenbrock_H(*p),
    method='Newton-CG',
    options={'disp': False}
)

print("Newton-CG Results:")
print(f"  Optimal point: ({result_ncg.x[0]:.6f}, {result_ncg.x[1]:.6f})")
print(f"  Function value: {result_ncg.fun:.2e}")
print(f"  Iterations: {result_ncg.nit}")
print(f"  Function evaluations: {result_ncg.nfev}")

# ============================================================================
# EXAMPLE 5: L-BFGS-B Method - Bounded Optimization
# ============================================================================
print("\n5. L-BFGS-B METHOD: HANDLE BOUNDS ON VARIABLES")
print("-" * 70)

print("L-BFGS-B handles box constraints (lower and upper bounds per variable).")
print("Advantages: efficient for bounded problems, limited memory use")
print("Disadvantages: requires bounds, doesn't use Hessian\n")

# Add box constraints: -0.8 <= x <= 0.8, 0 <= y <= 3.0
bounds = [(-0.8, 0.8), (0, 3.0)]
result_lbfgs = optimize.minimize(
    lambda p: rosenbrock(*p),
    x0=x0,
    jac=lambda p: rosenbrock_J(*p),
    method='L-BFGS-B',
    bounds=bounds,
    options={'disp': False}
)

print("L-BFGS-B Results (with bounds: x in [-0.8, 0.8], y in [0, 3]):")
print(f"  Optimal point: ({result_lbfgs.x[0]:.6f}, {result_lbfgs.x[1]:.6f})")
print(f"  Function value: {result_lbfgs.fun:.2e}")
print(f"  Iterations: {result_lbfgs.nit}")
print(f"  Note: optimum would be (1, 1) but y=1 is outside x-bound")

# ============================================================================
# EXAMPLE 6: Callback Functions - Tracking Optimization Path
# ============================================================================
print("\n6. TRACKING OPTIMIZATION PROGRESS WITH CALLBACKS")
print("-" * 70)

print("Callback functions execute during optimization to monitor progress.")
print("Track iteration count, function values, or record the optimization path.\n")

path = [x0.copy()]  # Record starting point
iteration_count = [0]  # Use list to modify in nested function

def callback_function(xk):
    """
    Called after each iteration.
    xk: current parameter values
    """
    iteration_count[0] += 1
    path.append(xk.copy())

result_with_callback = optimize.minimize(
    lambda p: rosenbrock(*p),
    x0=x0,
    jac=lambda p: rosenbrock_J(*p),
    method='BFGS',
    callback=callback_function,
    options={'disp': False}
)

path = np.array(path)
print("Optimization path (first 5 steps):")
for i in range(min(5, len(path))):
    f_val = rosenbrock(path[i, 0], path[i, 1])
    print(f"  Step {i}: x={path[i, 0]:7.4f}, y={path[i, 1]:7.4f}, f={f_val:10.4f}")

print(f"\n  ... (total {len(path)-1} steps)")
print(f"  Final: x={path[-1, 0]:7.4f}, y={path[-1, 1]:7.4f}, f={result_with_callback.fun:.2e}")

# ============================================================================
# EXAMPLE 7: Convergence Comparison - Method Efficiency
# ============================================================================
print("\n7. COMPARING CONVERGENCE RATES AND EFFICIENCY")
print("-" * 70)

# Compare different methods
methods_to_compare = [
    ('Nelder-Mead', {'method': 'Nelder-Mead', 'options': {'disp': False}}),
    ('BFGS', {'method': 'BFGS',
              'jac': lambda p: rosenbrock_J(*p), 'options': {'disp': False}}),
    ('Newton-CG', {'method': 'Newton-CG',
                   'jac': lambda p: rosenbrock_J(*p),
                   'hess': lambda p: rosenbrock_H(*p),
                   'options': {'disp': False}}),
    ('L-BFGS-B', {'method': 'L-BFGS-B',
                  'jac': lambda p: rosenbrock_J(*p),
                  'options': {'disp': False}}),
    ('CG', {'method': 'CG',
            'jac': lambda p: rosenbrock_J(*p),
            'options': {'disp': False}}),
]

print("\nMethod Comparison (starting from [-0.5, 2.5]):")
print("-" * 70)
print(f"{'Method':<15} {'Iterations':<12} {'Func Evals':<12} {'Final Value':<15} {'Success':<10}")
print("-" * 70)

results_comparison = {}
for method_name, options in methods_to_compare:
    result = optimize.minimize(lambda p: rosenbrock(*p), x0=x0, **options)
    results_comparison[method_name] = result
    print(f"{method_name:<15} {result.nit:<12} {result.nfev:<12} {result.fun:<15.2e} {str(result.success):<10}")

print("\nInterpretation:")
print("  Iterations: fewer iterations = faster algorithm")
print("  Func Evals: evaluations of objective function")
print("  Final Value: lower is better (should be ~0)")
print("  Success: did optimization converge?")

# ============================================================================
# EXAMPLE 8: Effect of Starting Point on Convergence
# ============================================================================
print("\n8. STARTING POINT SENSITIVITY")
print("-" * 70)

print("Optimization can be sensitive to initial conditions.\n")

starting_points = [
    (-0.5, 2.5),
    (0.0, 0.0),
    (2.0, 2.0),
    (-1.0, 3.0),
]

print(f"{'Starting Point':<20} {'BFGS Iters':<15} {'Newton-CG Iters':<15}")
print("-" * 50)

for x0_point in starting_points:
    x0_array = np.array(x0_point)

    result_bfgs_var = optimize.minimize(
        lambda p: rosenbrock(*p),
        x0=x0_array,
        jac=lambda p: rosenbrock_J(*p),
        method='BFGS',
        options={'disp': False}
    )

    result_ncg_var = optimize.minimize(
        lambda p: rosenbrock(*p),
        x0=x0_array,
        jac=lambda p: rosenbrock_J(*p),
        hess=lambda p: rosenbrock_H(*p),
        method='Newton-CG',
        options={'disp': False}
    )

    print(f"{str(x0_point):<20} {result_bfgs_var.nit:<15} {result_ncg_var.nit:<15}")

# ============================================================================
# EXAMPLE 9: Visualization of Convergence Patterns
# ============================================================================
print("\n9. DETAILED CONVERGENCE ANALYSIS")
print("-" * 70)

print("Track function values throughout optimization process:\n")

# Track function values with BFGS
function_values = [rosenbrock(*x0)]
iteration_num = [0]

def callback_tracking(xk):
    function_values.append(rosenbrock(*xk))
    iteration_num.append(iteration_num[-1] + 1)

result_track = optimize.minimize(
    lambda p: rosenbrock(*p),
    x0=x0,
    jac=lambda p: rosenbrock_J(*p),
    method='BFGS',
    callback=callback_tracking,
    options={'disp': False}
)

print("Function value reduction in BFGS method:")
print(f"{'Iteration':<12} {'Function Value':<20} {'Reduction':<20}")
print("-" * 52)
for i in range(min(10, len(function_values))):
    fval = function_values[i]
    if i == 0:
        reduction = "-"
    else:
        reduction = f"{function_values[i-1] - fval:.4e}"
    print(f"{i:<12} {fval:<20.6e} {str(reduction):<20}")

if len(function_values) > 10:
    print(f"... ({len(function_values)-10} more steps)")
    print(f"{len(function_values)-1:<12} {function_values[-1]:<20.6e}")

# ============================================================================
# EXAMPLE 10: Gradient Accuracy and Optimization Quality
# ============================================================================
print("\n10. IMPORTANCE OF ACCURATE GRADIENTS")
print("-" * 70)

# Compare with numerical gradient approximation
def numerical_gradient(func, x, eps=1e-8):
    """Approximate gradient using finite differences"""
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += eps
        x_minus[i] -= eps
        grad[i] = (func(x_plus) - func(x_minus)) / (2 * eps)
    return grad

print("Comparing analytical vs numerical gradients:\n")
x_test = np.array([0.5, 0.5])
analytical_grad = rosenbrock_J(*x_test)
numerical_grad = numerical_gradient(lambda p: rosenbrock(*p), x_test)

print(f"Analytical gradient: {analytical_grad}")
print(f"Numerical gradient:  {numerical_grad}")
print(f"Difference: {np.linalg.norm(analytical_grad - numerical_grad):.2e}")

# Optimize with analytical gradient
result_analytical = optimize.minimize(
    lambda p: rosenbrock(*p),
    x0=x0,
    jac=lambda p: rosenbrock_J(*p),
    method='BFGS',
    options={'disp': False}
)

print(f"\nWith analytical gradient: {result_analytical.nit} iterations")
print(f"Final value: {result_analytical.fun:.2e}")

print("\n" + "=" * 70)
print("Key takeaways:")
print("- Nelder-Mead: robust, no gradients, but slower")
print("- BFGS: good balance, needs gradient, no Hessian")
print("- Newton-CG: fastest, needs exact Hessian")
print("- L-BFGS-B: for bounded optimization problems")
print("- Callbacks: track optimization progress in real-time")
print("- Accurate gradients/Hessians = faster convergence")
print("- Starting point can affect convergence speed")
print("=" * 70)
