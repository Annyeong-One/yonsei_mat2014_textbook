# Character Encoding

Computers store bits, not characters. Character encoding defines the rules for converting between human-readable text and binary data, and getting it wrong produces garbled output.

## Definition

A **character encoding** is a mapping from characters to byte sequences. **Unicode** is a character set that assigns a unique **code point** (e.g., U+0041 for 'A') to every character in every language. **UTF-8** is the dominant encoding that converts Unicode code points to 1-4 bytes, with ASCII compatibility for the first 128 characters.

## Explanation

**ASCII** (1963) defined 128 characters using 7 bits -- sufficient for English but nothing else. Incompatible 8-bit extensions (Latin-1, Windows-1252) caused widespread compatibility problems where the same byte meant different characters in different encodings.

**Unicode** solved this by creating a universal character set. The key distinction: Unicode defines *which characters exist* and their code points; encodings like UTF-8, UTF-16, and UTF-32 define *how those code points are stored as bytes*.

**UTF-8** dominates because it is ASCII-compatible (1 byte for English), compact, self-synchronizing (you can find character boundaries from any position), and has no byte-order issues. It uses 1-4 bytes per character: 1 for ASCII, 2 for accented Latin, 3 for CJK, 4 for emoji.

**Python 3 strings** are sequences of Unicode code points. `len()` counts code points, not bytes. Converting between strings and bytes requires explicit encoding/decoding.

## Examples

```python
# Character to code point and back
print(ord('A'))   # 65
print(chr(65))    # 'A'
print(hex(ord('中')))  # '0x4e2d'
```

```python
# Encoding: str -> bytes (UTF-8 uses variable-width bytes)
text = "Hello, 世界!"
encoded = text.encode('utf-8')
print(len(text))     # 10  (code points)
print(len(encoded))  # 14  (bytes: CJK chars use 3 bytes each)

# Decoding: bytes -> str
decoded = encoded.decode('utf-8')
print(decoded)  # Hello, 世界!
```

```python
# Always specify encoding for file I/O
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('café ☕')

with open('data.txt', 'r', encoding='utf-8') as f:
    print(f.read())  # café ☕
```

```python
# Handling encoding errors
invalid = b'\xff\xfe'
try:
    invalid.decode('utf-8')
except UnicodeDecodeError as e:
    print(f"Error: {e}")

print(invalid.decode('utf-8', errors='replace'))  # ��
```
