
# Practice Examples

These exercises demonstrate common loop patterns.

---

## Fibonacci Sequence

```python
def fibonacci(n):

    a,b = 0,1

    for _ in range(n):

        a,b = b,a+b

        print(a)
````

---

## Prime Numbers

```python
for num in range(2,100):

    for i in range(2,int(num**0.5)+1):

        if num%i==0:
            break

    else:
        print(num)
```

---

## Armstrong Numbers

```python
for num in range(100,1000):

    a = num//100
    b = num//10%10
    c = num%10

    if num == a**3 + b**3 + c**3:

        print(num)
```

