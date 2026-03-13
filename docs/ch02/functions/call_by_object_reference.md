# Call-by-Object-Reference

Python uses a unique parameter passing mechanism often called "call-by-object-reference" or "call-by-sharing." Understanding this model is essential for predicting how functions affect their arguments.


## Neither Call-by-Value nor Call-by-Reference

Python doesn't fit neatly into the traditional categories.

**Call-by-value** (like C with primitives): A copy of the value is passed. Changes inside the function don't affect the original.

**Call-by-reference** (like C with pointers): The memory address is passed. Changes inside the function directly modify the original.

**Call-by-object-reference** (Python): A reference to the object is passed. What happens depends on whether the object is mutable or immutable.


## The Key Insight

When you pass an argument to a function:

1. The parameter becomes a new name bound to the same object
2. Both the original variable and the parameter point to the same object
3. What happens next depends on mutability

```python
def show_id(x):
    print(f"Inside function: id = {id(x)}")

value = [1, 2, 3]
print(f"Outside function: id = {id(value)}")
show_id(value)
```

Output:
```
Outside function: id = 140234567890
Inside function: id = 140234567890
```

Same object, same id—the parameter `x` refers to the same list as `value`.


## Immutable Objects: Appears Like Call-by-Value

With immutable objects (int, str, tuple), you cannot modify the original.

```python
def try_to_modify(x):
    print(f"Before: x = {x}, id = {id(x)}")
    x = x + 10  # Creates a NEW object, rebinds x
    print(f"After:  x = {x}, id = {id(x)}")

n = 5
print(f"Original: n = {n}, id = {id(n)}")
try_to_modify(n)
print(f"After call: n = {n}")
```

Output:
```
Original: n = 5, id = 140234567800
Before: x = 5, id = 140234567800
After:  x = 15, id = 140234567960
After call: n = 5
```

The `x = x + 10` creates a new integer object and rebinds `x` to it. The original `n` is unchanged.


## Mutable Objects: Can Modify In-Place

With mutable objects (list, dict, set), you can modify the original.

```python
def modify_list(lst):
    print(f"Before: {lst}, id = {id(lst)}")
    lst.append(4)  # Modifies the SAME object
    print(f"After:  {lst}, id = {id(lst)}")

my_list = [1, 2, 3]
print(f"Original: {my_list}, id = {id(my_list)}")
modify_list(my_list)
print(f"After call: {my_list}")
```

Output:
```
Original: [1, 2, 3], id = 140234567890
Before: [1, 2, 3], id = 140234567890
After:  [1, 2, 3, 4], id = 140234567890
After call: [1, 2, 3, 4]
```

The `lst.append(4)` mutates the original list. Same id throughout.


## Rebinding vs Mutating

The critical distinction is between **rebinding** (changing what a name points to) and **mutating** (changing the object itself).

### Rebinding: Never Affects the Caller

```python
def rebind(lst):
    lst = [100, 200, 300]  # Rebinds local name to NEW object
    print(f"Inside: {lst}")

my_list = [1, 2, 3]
rebind(my_list)
print(f"Outside: {my_list}")  # [1, 2, 3] - unchanged
```

### Mutating: Affects the Caller (if mutable)

```python
def mutate(lst):
    lst[0] = 100  # Mutates the SAME object
    print(f"Inside: {lst}")

my_list = [1, 2, 3]
mutate(my_list)
print(f"Outside: {my_list}")  # [100, 2, 3] - changed!
```


## Visualizing the Difference

```
# Initial state
my_list ──────► [1, 2, 3]

# After passing to function
my_list ──────► [1, 2, 3] ◄────── lst (parameter)

# After lst.append(4) - MUTATION
my_list ──────► [1, 2, 3, 4] ◄────── lst

# After lst = [100, 200] - REBINDING
my_list ──────► [1, 2, 3]
lst ──────► [100, 200]  (different object)
```


## Common Pitfall: Augmented Assignment

Augmented assignment operators (`+=`, `*=`) behave differently for mutable vs immutable types.

### Immutable (creates new object):

```python
def add_to_tuple(t):
    t += (4,)  # Creates NEW tuple, rebinds t
    return t

my_tuple = (1, 2, 3)
result = add_to_tuple(my_tuple)
print(my_tuple)  # (1, 2, 3) - unchanged
print(result)    # (1, 2, 3, 4)
```

### Mutable (mutates in place):

```python
def add_to_list(lst):
    lst += [4]  # Mutates in place! Equivalent to lst.extend([4])
    return lst

my_list = [1, 2, 3]
result = add_to_list(my_list)
print(my_list)  # [1, 2, 3, 4] - changed!
print(result)   # [1, 2, 3, 4]
```


## Protecting Mutable Arguments

If you don't want a function to modify the original, pass a copy.

```python
def process_data(data):
    data.append("processed")
    return data

original = [1, 2, 3]

# Option 1: Copy when calling
result = process_data(original.copy())
print(original)  # [1, 2, 3] - protected

# Option 2: Copy inside function
def safe_process(data):
    data = data.copy()  # Work on a copy
    data.append("processed")
    return data
```


## Summary Table

| Object Type | Mutation | Rebinding |
|-------------|----------|-----------|
| Immutable (int, str, tuple) | Not possible | Creates new object, doesn't affect caller |
| Mutable (list, dict, set) | Affects caller | Doesn't affect caller |

## Key Takeaways

1. Python passes references to objects, not copies of values
2. Parameters start as aliases pointing to the same objects as arguments
3. Rebinding a parameter never affects the caller's variable
4. Mutating a mutable object affects the caller
5. Use `.copy()` to protect mutable arguments when needed
