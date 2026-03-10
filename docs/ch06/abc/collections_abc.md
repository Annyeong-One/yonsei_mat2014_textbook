# collections.abc


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `collections.abc` module provides abstract base classes for container types. These help you create classes that work with Python's built-in operations.

---

## Common Abstract Base Classes

```python
from collections.abc import Sequence, Mapping, Set

# Check if object is a Sequence
list_obj = [1, 2, 3]
print(isinstance(list_obj, Sequence))  # True

tuple_obj = (1, 2, 3)
print(isinstance(tuple_obj, Sequence))  # True

dict_obj = {'a': 1}
print(isinstance(dict_obj, Mapping))    # True

set_obj = {1, 2, 3}
print(isinstance(set_obj, Set))         # True
```

## Creating a Custom Sequence

```python
from collections.abc import Sequence

class CustomList(Sequence):
    def __init__(self, data):
        self._data = list(data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __len__(self):
        return len(self._data)

custom = CustomList([10, 20, 30])
print(custom[0])           # 10
print(len(custom))         # 3
print(20 in custom)        # True
print(list(custom))        # [10, 20, 30]

# Supports iteration
for item in custom:
    print(item)
```

## Creating a Custom Mapping

```python
from collections.abc import Mapping

class DictWrapper(Mapping):
    def __init__(self, data):
        self._data = dict(data)
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)

wrapper = DictWrapper({'a': 1, 'b': 2})
print(wrapper['a'])        # 1
print(len(wrapper))        # 2
print('b' in wrapper)      # True
print(dict(wrapper))       # {'a': 1, 'b': 2}
```

## Creating a Custom Set

```python
from collections.abc import Set

class UniqueList(Set):
    def __init__(self, data):
        self._data = set(data)
    
    def __contains__(self, item):
        return item in self._data
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)

unique = UniqueList([1, 2, 2, 3, 3, 3])
print(len(unique))                    # 3
print(2 in unique)                    # True
print(unique & UniqueList([2, 3, 4])) # {2, 3} - set operations work!
```

## Iterator and Iterable

```python
from collections.abc import Iterator, Iterable

class CountUp(Iterable):
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        return CountUpIterator(self.max)

class CountUpIterator(Iterator):
    def __init__(self, max):
        self.current = 1
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.max:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

counter = CountUp(3)
for num in counter:
    print(num)  # 1, 2, 3
```

## Callable

```python
from collections.abc import Callable

# Check if something is callable
print(callable(print))           # True
print(callable(int))             # True
print(callable([]))              # False

def my_function():
    pass

print(isinstance(my_function, Callable))  # True

class CallableClass:
    def __call__(self):
        return "Called!"

obj = CallableClass()
print(isinstance(obj, Callable))  # True
print(obj())                       # Called!
```

## Container

```python
from collections.abc import Container

class AllowList(Container):
    def __init__(self, allowed_items):
        self._allowed = set(allowed_items)
    
    def __contains__(self, item):
        return item in self._allowed

allowlist = AllowList(['admin', 'moderator', 'user'])
print('admin' in allowlist)    # True
print('guest' in allowlist)    # False
```

## Sized and Hashable

```python
from collections.abc import Sized, Hashable

# String is both Sized and Hashable
text = "hello"
print(isinstance(text, Sized))     # True
print(isinstance(text, Hashable))  # True

# List is Sized but not Hashable
lst = [1, 2, 3]
print(isinstance(lst, Sized))      # True
print(isinstance(lst, Hashable))   # False
```

## Practical Example: LRU Cache Using ABC

```python
from collections.abc import MutableMapping

class SimpleLRUCache(MutableMapping):
    def __init__(self, max_size=10):
        self._cache = {}
        self._access_order = []
        self.max_size = max_size
    
    def __getitem__(self, key):
        self._access_order.remove(key)
        self._access_order.append(key)
        return self._cache[key]
    
    def __setitem__(self, key, value):
        if len(self._cache) >= self.max_size and key not in self._cache:
            oldest = self._access_order.pop(0)
            del self._cache[oldest]
        
        if key in self._cache:
            self._access_order.remove(key)
        self._cache[key] = value
        self._access_order.append(key)
    
    def __delitem__(self, key):
        del self._cache[key]
        self._access_order.remove(key)
    
    def __iter__(self):
        return iter(self._cache)
    
    def __len__(self):
        return len(self._cache)

cache = SimpleLRUCache(3)
cache['a'] = 1
cache['b'] = 2
cache['c'] = 3
cache['d'] = 4  # Evicts 'a'
print(dict(cache))  # {'b': 2, 'c': 3, 'd': 4}
```
