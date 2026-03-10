# `str`: Slicing


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Slicing extracts substrings using a flexible `[start:end:step]` syntax.

---

## Basic Syntax

### 1. Slice Notation

$$\begin{array}{ccccccccccccccccccc}
\text{a}&[&1&:&7&:&2&]\\
&&\uparrow&&\uparrow&&\uparrow&\\
&&\text{start}&&\text{end}&&\text{step}&\\
&&&&\text{(exclusive)}&&\text{(default 1)}&\\
\end{array}$$

### 2. Simple Slice

Extract characters from start to end (exclusive):

```python
def main():
    a = "Hello Pi"
    #    01234567
    print(a[1:7])   # ello P
    print(a[-8:-2]) # ello P (same result)

if __name__ == "__main__":
    main()
```

---

## Step Parameter

### 1. Custom Step Size

Skip characters using the step value:

```python
def main():
    a = "Hello Pi"
    #    01234567
    print(a[1:7:2])   # elP (every 2nd char)
    print(a[-8:-2:2]) # elP (same result)

if __name__ == "__main__":
    main()
```

### 2. Default Step

Step defaults to 1 when omitted:

```python
a = "Hello Pi"
print(a[1:7])    # ello P
print(a[1:7:1])  # ello P (same)
```

---

## Omitting Parameters

### 1. Omit End

Go to the end of the string:

```python
def main():
    a = "Hello Pi"
    print(f"{a[1:] = }")  # a[1:] = 'ello Pi'
    print(a[-8:])         # Hello Pi

if __name__ == "__main__":
    main()
```

### 2. Omit Start

Start from the beginning:

```python
a = "Hello Pi"
print(a[:5])  # Hello
print(a[:-3]) # Hello
```

### 3. With Step

Combine omissions with step:

```python
def main():
    a = "Hello Pi"
    print(f"{a[1::2] = }")   # a[1::2] = 'el i'
    print(f"{a[1:-1:2] = }") # a[1:-1:2] = 'el '

if __name__ == "__main__":
    main()
```

---

## Negative Step

### 1. Reverse String

Use `[::-1]` to reverse:

```python
def main():
    a = "Hello Pi"
    print(a[::-1])  # iP olleH

if __name__ == "__main__":
    main()
```

### 2. Reverse Slice

Combine range with negative step:

```python
a = "Hello Pi"
print(a[7:0:-1])  # iP olle
print(a[7::-1])   # iP olleH
```

---

## Mixed Indexing

### 1. Positive and Negative

Mix positive start with negative end:

```python
def main():
    a = "Hello Pi"
    print(f"{a[1:-1] = }")    # a[1:-1] = 'ello P'
    print(f"{a[1:-1:2] = }")  # a[1:-1:2] = 'el '

if __name__ == "__main__":
    main()
```

---

## Key Takeaways

- Syntax: `a[start:end:step]`.
- End index is exclusive.
- Step defaults to 1.
- `[::-1]` reverses the string.
