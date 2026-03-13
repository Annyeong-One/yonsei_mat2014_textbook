# Built-in Names

## View Built-ins

### 1. List All

```python
# Access built-in namespace
print(dir(__builtins__))

# Count
print(len(dir(__builtins__)))
```

### 2. Check Built-in

```python
import builtins

print(hasattr(builtins, 'list'))    # True
print(hasattr(builtins, 'myvar'))   # False
```

## Don't Shadow

### 1. Type Constructors

```python
# Don't shadow these!
# int = 42        
# float = 3.14    
# str = "text"    
# list = []       
# dict = {}       
# tuple = ()      
# set = set()     
# bool = True     
```

### 2. Common Functions

```python
# Don't shadow
# len = 5       # Very bad!
# range = []    
# print = "x"   # Very bad!
# input = 42    
# sum = 0       # Common mistake!
# max = 10      # Common mistake!
# min = 1       # Common mistake!
```

### 3. Iteration

```python
# Don't shadow
# iter = []     
# next = 1      
# filter = []   
# map = {}      
# sorted = []   # Very common!
# reversed = [] 
```

## Recovery

### 1. Delete Shadow

```python
# Shadowed
list = [1, 2, 3]

# Recover
del list
list(range(5))  # Works
```

### 2. Access builtins

```python
import builtins

# Even if shadowed
len = 42
builtins.len([1, 2, 3])  # Works
```

## Safe Alternatives

| Don't Use | Use Instead |
|-----------|-------------|
| `sum` | `total` |
| `list` | `items`, `data_list` |
| `dict` | `mapping` |
| `type` | `kind`, `data_type` |
| `id` | `identifier` |
| `max` | `maximum` |
| `min` | `minimum` |
| `sorted` | `ordered` |
