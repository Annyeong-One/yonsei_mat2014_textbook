# io.StringIO and io.BytesIO

StringIO and BytesIO create in-memory file-like objects for text and binary data respectively. They are useful for testing, temporary buffers, and situations where file system I/O should be avoided.

---

## StringIO for Text

### In-Memory Text Buffer

```python
from io import StringIO

buffer = StringIO()
buffer.write("Hello ")
buffer.write("World!")

contents = buffer.getvalue()
print(contents)
```

Output:
```
Hello World!
```

### Reading from StringIO

```python
from io import StringIO

buffer = StringIO("line1\nline2\nline3")

for line in buffer:
    print(line.strip())
```

Output:
```
line1
line2
line3
```

## BytesIO for Binary

### In-Memory Binary Buffer

```python
from io import BytesIO

buffer = BytesIO()
buffer.write(b"Hello ")
buffer.write(b"World!")

contents = buffer.getvalue()
print(contents)
```

Output:
```
b'Hello World!'
```

### Binary Data Processing

```python
from io import BytesIO

image_data = BytesIO()
image_data.write(b'\x89PNG\r\n\x1a\n')
image_data.write(b'mock_image_data')

image_data.seek(0)
header = image_data.read(8)
print(f"PNG Header: {header}")
```

Output:
```
PNG Header: b'\x89PNG\r\n\x1a\n'
```

## Testing and Mocking

### Testing File Operations

```python
from io import StringIO
import sys

buffer = StringIO()
sys.stdout = buffer
print("Captured output")
sys.stdout = sys.__stdout__

result = buffer.getvalue()
print(f"Result: {result}")
```

Output:
```
Result: Captured output
```

### CSV Processing

```python
from io import StringIO
import csv

csv_data = StringIO()
writer = csv.writer(csv_data)
writer.writerow(['name', 'age'])
writer.writerow(['Alice', 30])
writer.writerow(['Bob', 25])

csv_data.seek(0)
reader = csv.reader(csv_data)
for row in reader:
    print(row)
```

Output:
```
['name', 'age']
['Alice', '30']
['Bob', '25']
```
