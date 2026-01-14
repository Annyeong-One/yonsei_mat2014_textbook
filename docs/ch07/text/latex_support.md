# LaTeX Support

Matplotlib supports LaTeX-style math rendering for professional mathematical notation.

---

## Basic Math Mode

Use dollar signs for inline math:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('$y = \\sin(x)$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.show()
```

---

## Raw Strings

Use raw strings to avoid escaping backslashes:

```python
# Without raw string (need double backslashes)
ax.set_title('$y = \\sin(x)$')

# With raw string (single backslashes)
ax.set_title(r'$y = \sin(x)$')
```

---

## Common Math Symbols

**Greek letters:**
```python
ax.set_xlabel(r'$\alpha, \beta, \gamma, \delta, \theta, \phi, \pi$')
ax.set_xlabel(r'$\Alpha, \Beta, \Gamma, \Delta, \Theta, \Phi, \Pi$')
```

**Superscripts and subscripts:**
```python
ax.set_title(r'$x^2$')           # x squared
ax.set_title(r'$x_i$')           # x subscript i
ax.set_title(r'$x^{2n}$')        # x to the 2n
ax.set_title(r'$x_{ij}$')        # x subscript ij
```

**Fractions:**
```python
ax.set_title(r'$\frac{a}{b}$')
ax.set_title(r'$\frac{dy}{dx}$')
```

**Square roots:**
```python
ax.set_title(r'$\sqrt{x}$')
ax.set_title(r'$\sqrt[3]{x}$')   # Cube root
```

**Summation and integrals:**
```python
ax.set_title(r'$\sum_{i=1}^{n} x_i$')
ax.set_title(r'$\int_0^\infty e^{-x} dx$')
```

---

## Complex Equations

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Normal distribution formula
ax.text(0.5, 0.8, 
        r'$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$',
        fontsize=16, ha='center')

# Schrödinger equation
ax.text(0.5, 0.5,
        r'$i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi$',
        fontsize=16, ha='center')

# Euler's identity
ax.text(0.5, 0.2,
        r'$e^{i\pi} + 1 = 0$',
        fontsize=16, ha='center')

ax.axis('off')
plt.show()
```

---

## Matrices

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Matrix
matrix_text = r'''$\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}$'''

ax.text(0.5, 0.5, matrix_text, fontsize=14, ha='center', va='center')
ax.axis('off')
plt.show()
```

---

## Using Full LaTeX

For full LaTeX rendering (requires LaTeX installation):

```python
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

fig, ax = plt.subplots()
ax.set_title(r'\textbf{Bold Title}')
ax.set_xlabel(r'\textit{Italic Label}')
plt.show()
```

---

## Math in Tick Labels

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels([r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])

plt.show()
```

---

## Math Font Styles

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Different styles
ax.text(0.5, 0.9, r'$\mathrm{Roman}$', ha='center', fontsize=14)
ax.text(0.5, 0.7, r'$\mathit{Italic}$', ha='center', fontsize=14)
ax.text(0.5, 0.5, r'$\mathbf{Bold}$', ha='center', fontsize=14)
ax.text(0.5, 0.3, r'$\mathcal{CALLIGRAPHY}$', ha='center', fontsize=14)
ax.text(0.5, 0.1, r'$\mathbb{BLACKBOARD}$', ha='center', fontsize=14)

ax.axis('off')
plt.show()
```

---

## Reference Table

| Symbol | Code | Result |
|--------|------|--------|
| Greek | `\alpha, \beta, \gamma` | α, β, γ |
| Superscript | `x^2` | x² |
| Subscript | `x_i` | xᵢ |
| Fraction | `\frac{a}{b}` | a/b |
| Square root | `\sqrt{x}` | √x |
| Summation | `\sum_{i}^{n}` | Σ |
| Integral | `\int_a^b` | ∫ |
| Infinity | `\infty` | ∞ |
| Partial | `\partial` | ∂ |
| Nabla | `\nabla` | ∇ |

---

## Key Takeaways

- Use `$...$` for math mode
- Raw strings (`r'...'`) avoid escape issues
- Common symbols: Greek letters, fractions, integrals
- Use `\mathrm{}`, `\mathbf{}`, etc. for font styles
- Full LaTeX requires `text.usetex = True` and LaTeX installation
