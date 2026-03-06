# C3 Linearization

C3 linearization is the algorithm Python uses to compute the Method Resolution Order (MRO) for classes with multiple inheritance.

---

## Algorithm Overview

### 1. Named After Paper

C3 linearization algorithm from Barrett et al.

### 2. Not Simple Traversal

Not depth-first or breadth-first—a specialized merge algorithm.

### 3. Three Key Properties

- Preserves local precedence order
- Maintains parent MRO consistency  
- Ensures monotonicity

---

## The Formula

For a class `C(B1, B2, ..., Bn)`:

$$

L[C] = [C] + \text{merge}(L[B1], L[B2], \ldots, L[Bn], [B1, B2, \ldots, Bn])

$$

where:

- $L[Bi]$ is the MRO of parent $Bi$
- $[B1, B2, \ldots, Bn]$ is the list of direct parents

---

## Merge Procedure

### 1. Look at Heads

Examine the first element of each list.

### 2. Find Valid Head

Pick the first head that **is not in the tail** of any other list.

### 3. Append and Remove

Append this head to result and remove it from all lists.

### 4. Repeat

Continue until all lists are empty.

---

## Simple Example

### 1. Class Hierarchy

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```

### 2. Compute Base MROs

- $L[A] = [A, \text{object}]$
- $L[B] = [B, A, \text{object}]$
- $L[C] = [C, A, \text{object}]$

### 3. Apply Formula

$$

L[D] = [D] + \text{merge}([B, A, \text{object}], [C, A, \text{object}], [B, C])

$$

---

## Step-by-Step Merge

### 1. Initial Lists

- $[B, A, \text{object}]$ : head $B$, tail $[A, \text{object}]$
- $[C, A, \text{object}]$ : head $C$, tail $[A, \text{object}]$
- $[B, C]$ : head $B$, tail $[C]$

### 2. Pick B

$B$ is a head and not in any tail → append $B$.

Result: $[D, B]$

Updated lists:
- $[A, \text{object}]$
- $[C, A, \text{object}]$
- $[C]$

### 3. Pick C

$C$ is a head and not in any tail → append $C$.

Result: $[D, B, C]$

Updated lists:
- $[A, \text{object}]$
- $[A, \text{object}]$
- $[]$

### 4. Pick A

$A$ is a head and not in any tail → append $A$.

Result: $[D, B, C, A]$

Updated lists:
- $[\text{object}]$
- $[\text{object}]$
- $[]$

### 5. Pick object

$\text{object}$ is a head → append $\text{object}$.

Result: $[D, B, C, A, \text{object}]$

All lists empty—done!

---

## Final MRO

$$

L[D] = [D, B, C, A, \text{object}]

$$

```python
print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

---

## Complex Example

### 1. Multiple Paths

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
class E(D, C): pass
```

### 2. Compute Step-by-Step

- $L[D] = [D, B, C, A, \text{object}]$
- $L[C] = [C, A, \text{object}]$

$$

L[E] = [E] + \text{merge}([D, B, C, A, \text{object}], [C, A, \text{object}], [D, C])

$$

### 3. Merge Process

Following the same merge rules:

$L[E] = [E, D, B, C, A, \text{object}]$

---

## Conflict Detection

### 1. When Merge Fails

If **every head** appears in some tail, merge fails.

### 2. TypeError Raised

```python
class X: pass
class Y: pass
class A(X, Y): pass
class B(Y, X): pass
class C(A, B): pass  # Error!
```

### 3. Error Message

```plaintext
TypeError: Cannot create a consistent method resolution order (MRO)
```

---

## Why It Matters

### 1. Predictability

C3 ensures deterministic method resolution.

### 2. Cooperative Inheritance

Enables `super()` to work correctly.

### 3. Prevents Ambiguity

Guarantees consistency or rejects invalid hierarchies.

---

## Practical Implications

### 1. Left Parents First

Parents listed first have higher priority.

```python
class D(B, C):  # B's methods before C's
    pass
```

### 2. All Ancestors Once

Each class appears exactly once in MRO.

### 3. Monotonic Order

Parent order is preserved throughout the hierarchy.

---

## Key Takeaways

- C3 linearization computes MRO deterministically.
- Uses merge algorithm on parent MROs.
- Picks heads not in any tail.
- Rejects inconsistent hierarchies.
- Enables cooperative multiple inheritance.
