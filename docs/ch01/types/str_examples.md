
# str Examples

This section gathers practical examples showing how string operations work together.

---

## 1. Greeting Message

```python
name = "Alice"
message = f"Hello, {name}!"

print(message)
````

Output:

```text
Hello, Alice!
```

---

## 2. Username Validation

```python
username = "user123"

if username.isalnum():
    print("valid username")
else:
    print("invalid username")
```

---

## 3. Word Count

```python
sentence = "Python is fun"
words = sentence.split()

print(len(words))
```

Output:

```text
3
```

---

## 4. Reverse a String

```python
text = "Python"
print(text[::-1])
```

Output:

```text
nohtyP
```

---

## 5. CSV-Like Parsing

```python
line = "red,green,blue"
colors = line.split(",")

print(colors)
```

Output:

```text
['red', 'green', 'blue']
```

---

## 6. Rebuilding Text

```python
words = ["Python", "is", "readable"]
sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is readable
```

---

## 7. Case Normalization

```python
a = "PYTHON"
b = "python"

if a.lower() == b.lower():
    print("same word")
```

---

## 8. Path Example with Raw String

```python
path = r"C:\Users\student\notes.txt"
print(path)
```

---

## 9. Summary

These examples show that strings are used for:

* storing text
* formatting messages
* validating input
* parsing data
* transforming textual information

String processing is one of the most important programming skills in Python.

