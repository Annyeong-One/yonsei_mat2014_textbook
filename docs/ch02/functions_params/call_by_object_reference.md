# Call-by-Object-Reference

Consider this: you assign a list to two variables, then modify through one of them.

```python
a = ["Hi Bob", "Hi Alice"]
b = a

a[0] = 0
print(a)  # [0, 'Hi Alice']
print(b)  # [0, 'Hi Alice'] — b changed too!
```

Both `a` and `b` point to the same list object. Python doesn't copy values into variables — it binds names to objects. The same principle governs how arguments are passed to functions.


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

Output (actual addresses vary between runs):
```
Outside function: id = 0x...A
Inside function: id = 0x...A
```

Same object, same id — the parameter `x` refers to the same list as `value`.

```
# Initial state
my_list ──────► [1, 2, 3]

# After passing to function
my_list ──────► [1, 2, 3] ◄────── lst (parameter)

# After lst.append(4) — MUTATION
my_list ──────► [1, 2, 3, 4] ◄────── lst

# After lst = [100, 200] — REBINDING
my_list ──────► [1, 2, 3]
lst ──────► [100, 200]  (different object)
```

Mutation changes the object itself — all names that reference it see the change. Rebinding makes the local name point to a different object, leaving the original untouched.


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

Output (actual addresses vary between runs):
```
Original: n = 5, id = 0x...A
Before: x = 5, id = 0x...A
After:  x = 15, id = 0x...B
After call: n = 5
```

The `x = x + 10` creates a new integer object and rebinds `x` to it. The original `n` is unchanged. The key observation is that `0x...A` and `0x...B` differ — a new object was created.


## Mutable Objects: Can Modify In-Place

With mutable objects (list, dict, set), you can modify the original through the parameter.

```python
def modify_list(lst):
    lst.append(4)  # Modifies the SAME object

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]
```

Compare this with creating two separate objects that happen to hold equal values:

```python
a = [1, 2, 3]
b = [1, 2, 3]  # Different object, same contents

a[0] = 0
print(a)  # [0, 2, 3]
print(b)  # [1, 2, 3] — unaffected, different object
```

Whether two names share an object or merely hold equal values determines whether mutation through one name is visible through the other.

The detailed consequences of this mechanism — rebinding vs mutating, defensive copying patterns, and the augmented assignment gotcha (`+=`) — are covered in [Parameter Passing](parameter_passing.md) and [Default Parameter Gotcha](default_parameter_gotcha.md).
