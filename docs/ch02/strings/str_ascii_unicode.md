# `str`: ASCII and Unicode

Python strings support the full Unicode character set, building upon the ASCII foundation.

---

## ASCII Basics

### 1. What is ASCII?

ASCII (American Standard Code for Information Interchange) maps characters to numbers 0-127:

| Character | Decimal |
|-----------|---------|
| `'0'` | 48 |
| `'A'` | 65 |
| `'a'` | 97 |

### 2. The `ord()` Function

Convert characters to their numeric code:

```python
def main():
    print(f"{ord('0') = }")  # ord('0') = 48
    print(f"{ord('1') = }")  # ord('1') = 49
    print(f"{ord('A') = }")  # ord('A') = 65
    print(f"{ord('B') = }")  # ord('B') = 66
    print(f"{ord('a') = }")  # ord('a') = 97
    print(f"{ord('b') = }")  # ord('b') = 98

if __name__ == "__main__":
    main()
```

### 3. The `chr()` Function

Convert numeric codes back to characters:

```python
def main():
    print(f"{chr(48) = }")  # chr(48) = '0'
    print(f"{chr(49) = }")  # chr(49) = '1'
    print(f"{chr(65) = }")  # chr(65) = 'A'
    print(f"{chr(66) = }")  # chr(66) = 'B'
    print(f"{chr(97) = }")  # chr(97) = 'a'
    print(f"{chr(98) = }")  # chr(98) = 'b'

if __name__ == "__main__":
    main()
```

---

## Unicode Extension

### 1. Beyond ASCII

Unicode extends to over 1.1 million code points:

```python
def main():
    print(f"{ord('ה') = }")   # ord('ה') = 1492 (Hebrew)
    print(f"{ord('ち') = }")  # ord('ち') = 12385 (Japanese)
    print(f"{ord('好') = }")  # ord('好') = 22909 (Chinese)
    print(f"{ord('안') = }")  # ord('안') = 50504 (Korean)

if __name__ == "__main__":
    main()
```

### 2. Reverse Conversion

```python
def main():
    print(f"{chr(1492) = }")   # chr(1492) = 'ה'
    print(f"{chr(12385) = }")  # chr(12385) = 'ち'
    print(f"{chr(22909) = }")  # chr(22909) = '好'
    print(f"{chr(50504) = }")  # chr(50504) = '안'

if __name__ == "__main__":
    main()
```

---

## Code Points

### 1. What is a Code Point?

A code point is a unique number assigned to each Unicode character:

| Character | Code Point | Hex |
|-----------|------------|-----|
| `'A'` | 65 | U+0041 |
| `'ñ'` | 241 | U+00F1 |
| `'好'` | 22909 | U+597D |

### 2. Unicode Escapes

Represent characters using escape sequences:

```python
# 4-digit Unicode escape
char1 = '\u03A9'      # Omega (Ω)
char2 = '\u5B57'      # Chinese 字

# 8-digit Unicode escape
char3 = '\U0001F600'  # Emoji 😀

print(char1, char2, char3)  # Ω 字 😀
```

### 3. Plus-Minus Example

Print the ± symbol:

```python
def main():
    print('\u00B1 1')  # ± 1

if __name__ == "__main__":
    main()
```

---

## Encoding Diagram

$$\begin{array}{ccccc}
&\text{Encoding}&&\text{Decoding}\\
\text{"A"}&\longrightarrow&\text{65}&\longrightarrow&\text{"A"}\\
&\text{ord}&&\text{chr}\\
\end{array}$$

---

## Key Takeaways

- `ord()` converts characters to numeric codes.
- `chr()` converts codes back to characters.
- Unicode extends ASCII to global characters.
- Use `\uXXXX` for 4-digit Unicode escapes.
