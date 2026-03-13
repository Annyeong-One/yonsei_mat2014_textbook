# `str`: UTF-8 Encoding

UTF-8 is a variable-length encoding that efficiently represents all Unicode characters.

---

## Why UTF-8?

### 1. ASCII Limitations

ASCII only supports 128 characters (0-127), insufficient for non-English text:

```python
# ASCII works for English
char = 'A'  # 65 in ASCII

# But not for other scripts
char = '好'  # Requires Unicode
```

### 2. UTF-8 Advantages

UTF-8 provides:

- Backward compatibility with ASCII
- Compact storage for common characters
- Full Unicode support (1.1M+ code points)
- Self-synchronizing byte sequences

---

## Encoding Structure

### 1. Byte Patterns

UTF-8 uses 1-4 bytes depending on the character:

| Code Point Range | Byte Pattern | Bytes |
|------------------|--------------|-------|
| U+0000 – U+007F | `0xxxxxxx` | 1 |
| U+0080 – U+07FF | `110xxxxx 10xxxxxx` | 2 |
| U+0800 – U+FFFF | `1110xxxx 10xxxxxx 10xxxxxx` | 3 |
| U+10000 – U+10FFFF | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` | 4 |

### 2. Leading Bits

The first byte indicates sequence length:

- `0xxxxxxx` → Single byte (ASCII)
- `110xxxxx` → Start of 2-byte sequence
- `1110xxxx` → Start of 3-byte sequence
- `11110xxx` → Start of 4-byte sequence
- `10xxxxxx` → Continuation byte

---

## Examples

### 1. ASCII Character

The letter 'A' uses 1 byte:

```
'A' → U+0041 → 0100 0001 (1 byte)
```

### 2. Accented Character

The letter 'ñ' uses 2 bytes:

```
'ñ' → U+00F1 → 11000011 10110001 (2 bytes)
```

### 3. Chinese Character

The character '世' uses 3 bytes:

```
'世' → U+4E16 → 11100100 10111000 10010110 (3 bytes)
                   \xe4     \xb8     \x96
```

### 4. Emoji

The musical symbol '𝄞' uses 4 bytes:

```
'𝄞' → U+1D11E → 11110000 10010000 10000000 10111110 (4 bytes)
```

---

## Binary Encoding

### 1. Full Conversion

```python
def main():
    print(f"{bin(ord('0')) = :>9}")  # '0b110000'
    print(f"{bin(ord('1')) = :>9}")  # '0b110001'
    print(f"{bin(ord('A')) = :>9}")  # '0b1000001'
    print(f"{bin(ord('B')) = :>9}")  # '0b1000010'
    print(f"{bin(ord('a')) = :>9}")  # '0b1100001'
    print(f"{bin(ord('b')) = :>9}")  # '0b1100010'

if __name__ == "__main__":
    main()
```

### 2. Round Trip

```python
def main():
    print(f"{chr(int(bin(ord('A')),2)) = }")  # 'A'
    print(f"{chr(int(bin(ord('B')),2)) = }")  # 'B'

if __name__ == "__main__":
    main()
```

---

## Comparison

### 1. Other Encodings

| Encoding | Bytes/Char | Use Case |
|----------|------------|----------|
| UTF-8 | 1-4 | Web, general |
| UTF-16 | 2-4 | Windows, Java |
| UTF-32 | 4 | Fast indexing |
| ASCII | 1 | English only |

### 2. Why UTF-8 Dominates

- No endianness issues
- ASCII files are valid UTF-8
- Minimal storage for English text
- Web standard (HTML, XML)

---

## Key Takeaways

- UTF-8 uses 1-4 bytes per character.
- ASCII characters remain single-byte.
- Leading bits identify sequence length.
- Most widely adopted encoding today.
