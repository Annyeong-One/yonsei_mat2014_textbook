# Review Quiz

## Question 1

What happens here?

```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)
```

Answer: [1, 2, 3, 4]
Reason: b references same object

## Question 2

What's printed?

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
```

Answer: [2, 2, 2]
Reason: Late binding captures i

## Question 3

What's the output?

```python
def function(x=[]):
    x.append(1)
    return x

print(function())
print(function())
```

Answer:
[1]
[1, 1]
Reason: Mutable default

## Question 4

What does this print?

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)
print(x == y)
```

Answer:
False
True
Reason: Different objects, same value

## Question 5

What's x after this?

```python
def outer():
    x = 10
    def inner():
        x = 20
    inner()
    return x

print(outer())
```

Answer: 10
Reason: inner() creates local x

## Summary

Test your understanding:
- Reference model
- Late binding
- Mutable defaults
- Identity vs equality
- Variable scope
