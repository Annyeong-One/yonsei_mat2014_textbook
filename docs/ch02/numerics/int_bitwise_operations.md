# Bitwise Operations

Since integers are stored in binary, Python allows bitwise operations to manipulate individual bits.

---

## Basic Operators

Python provides six bitwise operators for bit-level manipulation.

### 1. AND (&)

Sets each bit to 1 if both bits are 1.

```python
x = 5  # 0b0101
y = 3  # 0b0011

print(x & y)  # Bitwise AND: 1 (0b0101 & 0b0011 = 0b0001)
```

Example: `5 & 3` results in `1` (binary `101 & 011` is `001`).

### 2. OR (|)

Sets each bit to 1 if one of the bits is 1.

```python
x = 5  # 0b0101
y = 3  # 0b0011

print(x | y)  # Bitwise OR: 7  (0b0101 | 0b0011 = 0b0111)
```

Example: `5 | 3` results in `7` (binary `101 | 011` is `111`).

### 3. XOR (^)

Sets each bit to 1 if only one of the bits is 1.

```python
x = 5  # 0b0101
y = 3  # 0b0011

print(x ^ y)  # Bitwise XOR: 6 (0b0101 ^ 0b0011 = 0b0110)
```

Example: `5 ^ 3` results in `6` (binary `101 ^ 011` is `110`).

### 4. NOT (~)

Inverts all the bits.

```python
x = 5  # 0b0101

print(~x)  # Bitwise NOT: -6
```

Example: `~5` results in `-6` (binary `~00000101` is `11111010` in two's complement).

### 5. Left Shift (<<)

Shifts the bits to the left, adding zeros on the right.

```python
x = 5  # 0b0101

print(x << 1)  # Left shift: 10 (0b0101 << 1 = 0b1010)
```

Example: `5 << 1` results in `10` (binary `101` becomes `1010`).

### 6. Right Shift (>>)

Shifts the bits to the right, discarding bits shifted off.

```python
x = 5  # 0b0101

print(x >> 1)  # Right shift: 2 (0b0101 >> 1 = 0b0010)
```

Example: `5 >> 1` results in `2` (binary `101` becomes `010`).

---

## Practical Usage

Bitwise operations are useful for bit-level manipulations and optimizations.

### 1. Set Bit

```python
# Set bit at position pos
n |= (1 << pos)
```

### 2. Clear Bit

```python
# Clear bit at position pos
n &= ~(1 << pos)
```

### 3. Toggle Bit

```python
# Toggle bit at position pos
n ^= (1 << pos)
```

### 4. Check Bit

```python
# Check if bit at position pos is set
is_set = n & (1 << pos) != 0
```

### 5. Masking

```python
# Extract the lower 4 bits
lower_4_bits = n & 0b1111
```

---

## AND Examples

Bitwise AND with positive and negative integers.

### 1. Positive AND

What is the output?

```python
print(f"{10 & 5 = }")
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&1010_2&10_{10}\\
\text{b}&101_2&5_{10}\\\hline
\text{a \& b}&0_2&0_{10}\\
\end{array}$$

```python
print(f"{10 & 5 = }")  # Output: 10 & 5 = 0
```

### 2. Negative AND

What is the output?

```python
print(f"{10 & -5 = }")
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&1010_2&10_{10}\\
\text{5_{10} without sign bit}&101_2&5_{10}\\
\text{5_{10} with sign bit}&00101_2&5_{10}\\
\text{one's complement}&11010_2&\\
\text{b}&11011_2&-5_{10}\\
\hline
\text{a \& b}&01010_2&10_{10}\\
\end{array}$$

```python
print(f"{10 & -5 = }")  # Output: 10 & -5 = 10
```

---

## OR Examples

Bitwise OR with positive and negative integers.

### 1. Positive OR

What is the output?

```python
print(f"{10 | 5 = }")
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&1010_2&10_{10}\\
\text{b}&101_2&5_{10}\\\hline
\text{a | b}&1111_2&15_{10}\\
\end{array}$$

```python
print(f"{10 | 5 = }")  # Output: 10 | 5 = 15
```

### 2. Negative OR

What is the output?

```python
print(f"{10 | -5 = }")
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&1010_2&10_{10}\\
\text{b}&11011_2&-5_{10}\\
\hline
\text{a | b}&11011_2&-5_{10}\\
\end{array}$$

```python
print(f"{10 | -5 = }")  # Output: 10 | -5 = -5
```

---

## XOR Examples

Bitwise XOR with positive and negative integers.

### 1. Positive XOR

What is the output?

```python
print(f"{10 ^ 5 = }")
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&1010_2&10_{10}\\
\text{b}&101_2&5_{10}\\\hline
\text{a \^ b}&1111_2&15_{10}\\
\end{array}$$

```python
print(f"{10 ^ 5  = }")  # Output: 10 ^ 5 = 15
```

### 2. Negative XOR

What is the output?

```python
print(f"{10 ^ -5 = }")
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&1010_2&10_{10}\\
\text{b}&11011_2&-5_{10}\\\hline
\text{a \^ b}&10001_2&-15_{10}\\
\end{array}$$

```python
print(f"{10 ^ -5  = }")  # Output: 10 ^ -5 = -15
```

---

## NOT Examples

Bitwise NOT with different integer types.

### 1. Regular NOT

What is the output?

```python
print(f"{~ 10 = }")
```

**Solution:**

$$\begin{array}{ccr}
\text{Expression}&\text{Binary with Sign Bit}&\text{Decimal}\\
\text{a}&01010_2&10_{10}\\\hline
\text{~ a}&10101_2&-11_{10}\\
\end{array}$$

```python
print(f"{~ 10 = }")  # Output: ~ 10 = -11
```

### 2. NumPy uint8

What is the output?

```python
print(f"{~ np.array(10, dtype=np.uint8) = }")
```

**Solution:**

$$\begin{array}{ccr}
\text{Expression}&\text{Binary with np.uint8}&\text{Decimal}\\
\text{a}&00001010_2&10_{10}\\\hline
\text{~ a}&11110101_2&245_{10}\\
\end{array}$$

```python
print(f"{~ np.array(10, dtype=np.uint8) = }")  # Output: 245
```

### 3. NumPy uint16

What is the output?

```python
print(f"{~ np.array(10, dtype=np.uint16) = }")
```

**Solution:**

$$\begin{array}{ccr}
\text{Expression}&\text{Binary with np.uint16}&\text{Decimal}\\
\text{a}&0000000000001010_2&10_{10}\\\hline
\text{~ a}&1111111111110101_2&65525_{10}\\
\end{array}$$

```python
print(f"{~ np.array(10, dtype=np.uint16) = }")  # Output: 65525
```

---

## Right Shift

Right shift discards bits shifted off the right end.

### 1. Positive Shift

What is the output?

```python
print(5 >> 1)
print(5 >> 2)
print(5 >> 3)
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&101_2&5_{10}\\
\hline
\text{a >> 1}&10_2&2_{10}\\
\text{a >> 2}&1_2&1_{10}\\
\text{a >> 3}&0_2&0_{10}\\
\end{array}$$

```python
print(5 >> 1)  # Output: 2
print(5 >> 2)  # Output: 1
print(5 >> 3)  # Output: 0
```

### 2. Negative Shift

What is the output?

```python
print(-5 >> 1)
print(-5 >> 2)
print(-5 >> 3)
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&11011_2&-5_{10}\\
\hline
\text{a >> 1}&11101_2&-3_{10}\\
\text{a >> 2}&11110_2&-2_{10}\\
\text{a >> 3}&11111_2&-1_{10}\\
\end{array}$$

```python
print(-5 >> 1)  # Output: -3
print(-5 >> 2)  # Output: -2
print(-5 >> 3)  # Output: -1
```

---

## Left Shift

Left shift adds zeros on the right, effectively multiplying by powers of 2.

### 1. Positive Shift

What is the output?

```python
print(5 << 1)
print(5 << 2)
print(5 << 3)
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&101_2&5_{10}\\
\hline
\text{a << 1}&1010_2&10_{10}\\
\text{a << 2}&10100_2&20_{10}\\
\text{a << 3}&101000_2&40_{10}\\
\end{array}$$

```python
print(5 << 1)  # Output: 10
print(5 << 2)  # Output: 20
print(5 << 3)  # Output: 40
```

### 2. Negative Shift

What is the output?

```python
print(-5 << 1)
print(-5 << 2)
print(-5 << 3)
```

**Solution:**

$$\begin{array}{crr}
\text{Expression}&\text{Binary}&\text{Decimal}\\
\text{a}&11011_2&-5_{10}\\
\hline
\text{a << 1}&110110_2&-10_{10}\\
\text{a << 2}&1101100_2&-20_{10}\\
\text{a << 3}&11011000_2&-30_{10}\\
\end{array}$$

```python
print(-5 << 1)  # Output: -10
print(-5 << 2)  # Output: -20
print(-5 << 3)  # Output: -30
```

---

## Practical Examples

Real-world applications of bitwise operations.

### 1. Array Sizing

```python
def main():
    for n in range(4):
        memo = [-1] * (1 << (n+1))
        print(memo)

if __name__ == "__main__":
    main()
```

### 2. XOR Swap

Swap two variables without a temporary variable.

What is the output?

```python
a = 4
b = 3
print(f"{a = }, {b = }")

a = a ^ b
b = a ^ b
a = a ^ b
print(f"{a = }, {b = }")
```

**Solution:**

```python
def main():
    a = 4
    b = 3
    print(f"{a = }, {b = }")

    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()
```

### 3. Count Bits

Count the number of bits in an integer.

What is the output?

```python
def func(num):
    count = 0
    while num:
        count += 1
        num >>= 1
    return count

def main():
    print(f"{func(435)}")

if __name__ == "__main__":
    main()   
```

**Solution:**

```python
def func(num):
    count = 0
    while num:
        count += 1
        num >>= 1
    return count

def main():
    print(f"{func(435)}")  # Output: 9

if __name__ == "__main__":
    main()
```

---

## Conclusion

Understanding bitwise operations is essential for low-level programming, optimizing performance, and working with hardware and embedded systems. These operations provide efficient ways to manipulate individual bits for tasks like setting flags, masking, and performing fast arithmetic.
