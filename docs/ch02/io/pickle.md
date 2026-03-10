# pickle and Serialization


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The pickle module serializes Python objects into bytes for storage or transmission. While convenient for Python-specific data, pickle has security implications and limitations compared to other formats.

---

## Basic Pickling

### Serializing Objects

```python
import pickle

data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

pickled = pickle.dumps(data)
print(f"Pickled: {type(pickled)}")

restored = pickle.loads(pickled)
print(restored)
```

Output:
```
Pickled: <class 'bytes'>
{'name': 'Alice', 'age': 30, 'scores': [95, 87, 92]}
```

### File Persistence

```python
import pickle
import io

data = [1, 2, 3, 4, 5]
buffer = io.BytesIO()

pickle.dump(data, buffer)

buffer.seek(0)
restored = pickle.load(buffer)
print(restored)
```

Output:
```
[1, 2, 3, 4, 5]
```

## Custom Objects

### Pickling Classes

```python
import pickle
import io

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age})"

dog = Dog("Buddy", 5)
buffer = io.BytesIO()

pickle.dump(dog, buffer)
buffer.seek(0)
restored = pickle.load(buffer)
print(restored)
```

Output:
```
Dog(name=Buddy, age=5)
```

## Protocols and Versions

### Protocol Versions

```python
import pickle
import io

data = {"key": "value"}

for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
    buffer = io.BytesIO()
    pickle.dump(data, buffer, protocol=protocol)
    size = buffer.tell()
    print(f"Protocol {protocol}: {size} bytes")
```

Output:
```
Protocol 0: 27 bytes
Protocol 1: 17 bytes
Protocol 2: 17 bytes
Protocol 3: 16 bytes
Protocol 4: 15 bytes
Protocol 5: 10 bytes
```

## Security Considerations

### Pickle Security Warning

```python
import pickle
import json

data = {"name": "Alice", "age": 30}
safe_json = json.dumps(data)
restored = json.loads(safe_json)
print(restored)
```

Output:
```
{'name': 'Alice', 'age': 30}
```
