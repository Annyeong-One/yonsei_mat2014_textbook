# `str`: Multiline Strings


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python provides several methods to create strings spanning multiple lines.

---

## Triple Quotes

### 1. Basic Syntax

Triple quotes preserve line breaks and allow embedded quotes:

```python
def main():
    a = """On June 1, 1865, Senator Charles Sumner referred to
the most famous speech ever given by President Abraham Lincoln.
In his eulogy on the slain president, he called the Gettysburg Address
a "monumental act." He said Lincoln was mistaken that
"the world will little note, nor long remember what we say here."
"""
    print(a)

if __name__ == "__main__":
    main()
```

### 2. Escape Still Works

Escape sequences function inside triple quotes:

```python
a = """You have to dream before your dreams can come true.
\n-- A. P. J. Abdul Kalam"""
print(a)
```

---

## Line Continuation

### 1. Backslash Method

The backslash joins physical lines into one logical line:

```python
a = "You have to dream before your dreams can come true. \
-- A. P. J. Abdul Kalam"
print(a)
```

For long expressions:

```python
result = 10 + 20 + 30 + 40 + 50 + \
         60 + 70 + 80 + 90 + 100
print(result, type(result))  # 550 <class 'int'>
```

### 2. Parentheses Method

Parentheses allow implicit continuation:

```python
def main():
    a = ( 1 + 2 + 3
        + 4 + 5 + 6
        + 7 + 8 + 9
        + 10 )
    print(a, type(a))  # 55 <class 'int'>

if __name__ == "__main__":
    main()
```

---

## F-String Patterns

### 1. Triple Quote F-String

```python
def main():
    name = "Jaspreet"
    age = 29
    gender = "Male"
    msg = f"""My name is {name}.
              My age is {age}.
              I am a {gender}."""
    print(msg)

if __name__ == "__main__":
    main()
```

### 2. Backslash F-String

```python
def main():
    name = "Jaspreet"
    age = 29
    gender = "Male"
    msg = f"My name is {name}. " \
          f"My age is {age}. " \
          f"I am a {gender}. "
    print(msg)

if __name__ == "__main__":
    main()
```

### 3. Parentheses F-String

```python
def main():
    name = "Jaspreet"
    age = 29
    gender = "Male"
    msg = ( f"My name is {name}. "
            f"My age is {age}. "
            f"I am a {gender}. " )
    print(msg)

if __name__ == "__main__":
    main()
```

---

## Bracket Behavior

### 1. Curly Brackets

Curly brackets create a set, not a multiline int:

```python
def main():
    a = { 1 + 2 + 3
        + 4 + 5 + 6
        + 7 + 8 + 9
        + 10 }
    print(a, type(a))  # {55} <class 'set'>

if __name__ == "__main__":
    main()
```

### 2. Square Brackets

Square brackets create a list:

```python
def main():
    a = [ 1 + 2 + 3
        + 4 + 5 + 6
        + 7 + 8 + 9
        + 10 ]
    print(a, type(a))  # [55] <class 'list'>

if __name__ == "__main__":
    main()
```

---

## Key Takeaways

- Triple quotes preserve formatting and line breaks.
- Backslash (`\`) joins lines without line breaks.
- Parentheses allow implicit line continuation.
- PEP 8 recommends 79-character line limits.
