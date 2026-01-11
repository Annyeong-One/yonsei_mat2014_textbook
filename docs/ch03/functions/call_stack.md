# Call Stack

## Stack Frames

### 1. Function Calls

```python
def a():
    print("In a")
    b()
    print("Back in a")

def b():
    print("In b")
    c()
    print("Back in b")

def c():
    print("In c")

a()
```

**Stack during execution:**
```
[c frame]
[b frame]
[a frame]
[main]
```

## Frame Inspection

### 1. View Stack

```python
import inspect

def show_stack():
    for frame_info in inspect.stack():
        print(f"{frame_info.function} at line {frame_info.lineno}")

def outer():
    middle()

def middle():
    show_stack()

outer()
```

## Stack Overflow

### 1. Too Deep

```python
import sys

print(sys.getrecursionlimit())  # 1000

def infinite():
    return infinite()

# infinite()  # RecursionError
```

## Summary

- Each call creates frame
- Frames stack up
- Limited depth
- Unwind on return
