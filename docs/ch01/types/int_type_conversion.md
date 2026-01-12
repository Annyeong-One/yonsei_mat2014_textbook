# Type Conversion

Python provides flexible type conversion and checking for integers.

---

## Type Checking

Check and verify integer types at runtime.

### 1. type() Function

```python
num = 42
print(type(num))  # <class 'int'>
```

### 2. isinstance()

```python
x = 10
print(isinstance(x, int))  # True
```

---

## Conversion

Python allows conversion between integers and other numeric types.

### 1. To Float

```python
num = 42
float_num = float(num)  # Convert to float
print(float_num)  # Output: 42.0
```

### 2. To String

```python
num = 42
str_num = str(num)      # Convert to string
print(str_num, type(str_num))  # Output: 42 <class 'str'>
```

### 3. Type Checking

```python
num = 42
print(type(num))  # <class 'int'>

float_num = float(num)  # Convert to float
str_num = str(num)      # Convert to string
```

---

## From float

Converting floating-point numbers to integers.

### 1. float to int

```python
def main():
    print(int(3.64))   # Output: 3
    print(int(-3.64))  # Output: -3

if __name__ == "__main__":
    main()
```

Note: `int()` truncates toward zero, not floor division.

---

## From String

Converting strings to integers.

### 1. Basic Conversion

```python
def main():
    print(int("20"))
    print(int("   20"))
    print(int("20     "))
    print(int("   20     "))

if __name__ == "__main__":
    main()
```

### 2. Invalid String

What is the output?

```python
print( int( "10.7" ) )
```

**Solution:**

```python
def main():
    print( int( "10.7" ) )  # Raises ValueError

if __name__ == "__main__":
    main()
```

This raises a `ValueError` because `"10.7"` is not a valid integer string. Use `int(float("10.7"))` instead.

---

## Conclusion

Type conversion and checking are essential for ensuring correct data types and preventing type-related errors in Python programs.
