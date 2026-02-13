# Encoding Issues

Text encoding mismatches are a common source of errors. Understanding character encodings and Python text handling prevents encoding-related bugs.

---

## UTF-8 Basics

### Default Encoding

```python
import sys

print(f"Default: {sys.getdefaultencoding()}")

text = "Hello 世界 🌍"
print(f"Text: {text}")
print(f"Bytes (UTF-8): {text.encode('utf-8')}")
```

Output:
```
Default: utf-8
Text: Hello 世界 🌍
Bytes (UTF-8): b'Hello \xe4\xb8\x96\xe7\x95\x8c \xf0\x9f\x8c\x8d'
```

## Encoding/Decoding

### Encoding Text to Bytes

```python
text = "café"

utf8 = text.encode('utf-8')
latin1 = text.encode('latin-1')
ascii_err = text.encode('ascii', errors='replace')

print(f"UTF-8: {utf8}")
print(f"Latin-1: {latin1}")
print(f"ASCII (replace): {ascii_err}")
```

Output:
```
UTF-8: b'caf\xc3\xa9'
Latin-1: b'caf\xe9'
ASCII (replace): b'caf?'
```

### Decoding Bytes to Text

```python
utf8_bytes = b'caf\xc3\xa9'
latin1_bytes = b'caf\xe9'

print(f"UTF-8: {utf8_bytes.decode('utf-8')}")
print(f"UTF-8 as Latin-1: {utf8_bytes.decode('latin-1')}")
```

Output:
```
UTF-8: café
UTF-8 as Latin-1: cafÃ©
```

## File Encoding

### Specifying File Encoding

```python
import io
import tempfile
import os

with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
    f.write("Hello 世界")
    temp_file = f.name

with open(temp_file, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"Read: {content}")

os.unlink(temp_file)
```

Output:
```
Read: Hello 世界
```

## Error Handling

### Encoding Error Strategies

```python
text = "café"

replace = text.encode('ascii', errors='replace')
ignore = text.encode('ascii', errors='ignore')

print(f"Replace: {replace}")
print(f"Ignore: {ignore}")
```

Output:
```
Replace: b'caf?'
Ignore: b'caf'
```
