# Indentation and Blocks

Python uses indentation to define code blocks, making visual structure and logical structure identical. This is enforced by the interpreter, not just a style convention.

## Definition

**Indentation** is the leading whitespace at the start of a line. In Python, indentation is syntax: it groups statements into **blocks** (the bodies of `if`, `for`, `while`, `def`, `class`, `with`, and `try`). A colon (`:`) introduces a new block, and all statements in that block must share the same indentation level. PEP 8 prescribes **4 spaces** per level.

## Explanation

**Core rules**: (1) Every statement in a block must be indented identically. (2) Mixing tabs and spaces in the same file raises `TabError` in Python 3. (3) Blank lines inside a block need no indentation. (4) A block must contain at least one statement (use `pass` if empty).

**Continuation lines**: Expressions inside parentheses `()`, brackets `[]`, or braces `{}` can span multiple lines without extra syntax. Outside brackets, use a backslash `\` for explicit continuation (prefer parentheses when possible).

**Avoiding deep nesting**: Use guard clauses (early `return`, `continue`, or `raise`) to keep nesting shallow. Deeply nested code is harder to read and maintain.

## Examples

```python
# Colon introduces a block; body indented 4 spaces
if temperature > 30:
    print("Hot")
    print("Stay hydrated")

# Nested blocks add another 4 spaces each level
for i in range(3):
    for j in range(3):
        if i == j:
            print(f"diagonal: ({i}, {j})")
```

```python
# Guard clauses reduce nesting
def process(data):
    if data is None:
        return None
    if not validate(data):
        return None
    return transform(data)
```

```python
# Implicit continuation inside parentheses
result = (
    first_value
    + second_value
    + third_value
)

# Hanging indent for function definitions
def create_user(
        name,
        email,
        role="viewer"):
    return {"name": name, "email": email, "role": role}
```

```python
# Common errors
if True:
print("missing indent")   # IndentationError

if True:
    print("4 spaces")
  print("2 spaces")       # IndentationError: unindent does not match
```
