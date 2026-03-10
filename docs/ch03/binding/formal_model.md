# Formal Model


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Environment

### 1. Name-Value Mapping

Environment (Γ) maps names to values:

```python
# Environment example:
# Γ = {x: 42, y: "hello", z: [1, 2, 3]}

x = 42
y = "hello"
z = [1, 2, 3]
```

### 2. Notation

Formal notation:

```
Γ[x ↦ v]  # Bind x to value v in Γ
Γ(x)      # Lookup x in Γ
```

## Binding Rules

### 1. Simple Binding

```python
# Before: Γ = {}
x = 42
# After: Γ = {x: 42}

# Before: Γ = {x: 42}
y = "hello"
# After: Γ = {x: 42, y: "hello"}
```

### 2. Rebinding

```python
# Before: Γ = {x: 42}
x = 100
# After: Γ = {x: 100}
```

## Evaluation

### 1. Expression Eval

```
Γ ⊢ e ⇓ v
```

Means: "In environment Γ, expression e evaluates to value v"

### 2. Example

```python
# Γ = {x: 10, y: 20}
# Γ ⊢ x + y ⇓ 30

x = 10
y = 20
result = x + y  # 30
```

## Scope Chain

### 1. Nested Environments

```python
# Global: Γ_global = {x: 10}
x = 10

def f():
    # Local: Γ_local = {y: 20}
    # Parent: Γ_global
    y = 20
    return x + y
```

### 2. Lookup Chain

```
Γ_local → Γ_enclosing → Γ_global → Γ_builtin
```

## Assignment Semantics

### 1. Create Binding

```python
# Γ ⊢ x = e ⇓ Γ[x ↦ v]
# where Γ ⊢ e ⇓ v

x = 42
# Evaluates 42, binds x
```

### 2. Multiple Assignment

```python
# Γ ⊢ x, y = e1, e2 ⇓ Γ[x ↦ v1, y ↦ v2]

x, y = 1, 2
```

## Function Application

### 1. Environment Extension

```python
def f(x, y):
    return x + y

# Call: f(10, 20)
# Creates: Γ_f = Γ_global[x ↦ 10, y ↦ 20]
```

### 2. Formal Rule

```
Γ ⊢ f(e1, e2) ⇓ v
where:
  Γ ⊢ e1 ⇓ v1
  Γ ⊢ e2 ⇓ v2
  Γ' = Γ[x ↦ v1, y ↦ v2]
  Γ' ⊢ body ⇓ v
```

## Summary

### 1. Core Concepts

- Environment: name → value mapping
- Binding: Γ[x ↦ v]
- Lookup: Γ(x)
- Evaluation: Γ ⊢ e ⇓ v

### 2. Operations

- Create binding
- Update binding
- Lookup value
- Extend environment
