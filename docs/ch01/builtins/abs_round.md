# abs() and round()

The abs() function returns absolute values, while round() rounds numbers to a specified precision. Both are fundamental for numeric operations and data processing.

---

## abs() Function

### Basic Absolute Value

```python
print(abs(-5))
print(abs(5))
print(abs(-3.14))
```

Output:
```
5
5
3.14
```

### With Complex Numbers

```python
z = 3 + 4j
magnitude = abs(z)
print(f"Magnitude of {z}: {magnitude}")
```

Output:
```
Magnitude of 3+4j: 5.0
```

### Practical Usage

```python
readings = [10, -5, 8, -3, 12, -7]
deviations = [abs(x) for x in readings]
print(f"Absolute deviations: {deviations}")
```

Output:
```
Absolute deviations: [10, 5, 8, 3, 12, 7]
```

## round() Function

### Basic Rounding

```python
print(round(3.14159))
print(round(3.14159, 2))
print(round(3.14159, 4))
```

Output:
```
3
3.14
3.1416
```

### Rounding to Nearest Even

```python
# Python uses banker's rounding (round half to even)
print(round(0.5))
print(round(1.5))
print(round(2.5))
```

Output:
```
0
2
2
```

### Negative Decimal Places

```python
# Round to nearest 10, 100, etc.
print(round(1234, -1))
print(round(1234, -2))
print(round(1234, -3))
```

Output:
```
1230
1200
1000
```

## Combined Examples

### Price Rounding

```python
prices = [19.99, 25.50, 12.345]
discounted = [price * 0.9 for price in prices]
final = [round(p, 2) for p in discounted]

for original, rounded in zip(discounted, final):
    print(f"{original:.4f} -> ${rounded:.2f}")
```

Output:
```
17.9910 -> $17.99
22.9500 -> $22.95
11.1105 -> $11.11
```

### Statistical Analysis

```python
measurements = [10.1, -5.3, 8.7, -3.2, 12.5, -7.1]

mean = sum(measurements) / len(measurements)
rounded_mean = round(mean, 2)
abs_mean = round(abs(mean), 2)

print(f"Mean: {rounded_mean}")
print(f"Absolute mean: {abs_mean}")
```

Output:
```
Mean: 2.43
Absolute mean: 2.43
```
