# yield from


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The yield from statement delegates to a sub-generator, combining value iteration and exception handling. It's a powerful tool for building complex generator hierarchies and simplifying generator composition.

---

## Basic yield from

### Delegating to Sub-generator

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

def delegating_generator():
    yield from simple_generator()
    yield 4

for value in delegating_generator():
    print(value)
```

Output:
```
1
2
3
4
```

### vs yield in a Loop

```python
def with_loop(g):
    for value in g:
        yield value

def with_yield_from(g):
    yield from g

g = (i for i in range(3))
print(list(with_loop(g)))

g = (i for i in range(3))
print(list(with_yield_from(g)))
```

Output:
```
[0, 1, 2]
[0, 1, 2]
```

## Nested Generators

### Tree Traversal

```python
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

tree = [1, [2, 3, [4, 5]], 6]
result = list(flatten(tree))
print(result)
```

Output:
```
[1, 2, 3, 4, 5, 6]
```

## Exception Handling

### Propagating Exceptions

```python
def sub_gen():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        yield "caught error"

def delegating():
    yield from sub_gen()

gen = delegating()
print(next(gen))
print(next(gen))
```

Output:
```
1
2
```

## Return Values

### Capturing Sub-generator Return

```python
def sub_generator():
    yield 1
    yield 2
    return "done"

def delegating():
    result = yield from sub_generator()
    yield f"Got: {result}"

for value in delegating():
    print(value)
```

Output:
```
1
2
Got: done
```
