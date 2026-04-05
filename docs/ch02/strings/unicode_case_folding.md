# Unicode Case Folding

Normalization fixes **representation differences**, but not **case differences**.
For case-insensitive Unicode comparison, Python provides `casefold()`.

---

## `lower()` vs `casefold()`

For ASCII text, `lower()` and `casefold()` behave identically. The difference
appears with certain Unicode characters:
```python
print("ß".lower())     # ß   (unchanged)
print("ß".casefold())  # ss  (correct for case-insensitive matching)
```

German `ß` (`U+00DF`) has no uppercase form — `lower()` leaves it alone, but
`casefold()` maps it to `ss` so that `"ß"` and `"SS"` can match after folding.

This makes `casefold()` the correct choice for user-facing, language-aware
case-insensitive comparison.

---

## Combining Normalization and Case Folding

Case folding alone does not solve the representation problem from
[Unicode Normalization](unicode_normalization.md). For fully robust comparison,
combine both steps:
```python
from unicodedata import normalize

def fold_equal(s1, s2):
    return normalize("NFC", s1).casefold() == normalize("NFC", s2).casefold()
```

This handles both sources of mismatch at once:
```python
print(fold_equal("Café", "CAFÉ"))         # True  (case difference)
print(fold_equal("café", "cafe\u0301"))  # True  (representation difference)
print(fold_equal("ß", "SS"))              # True  (language-specific folding)
```

---

## Practical Example: Name Search

User-supplied input rarely arrives in a consistent Unicode form or case.
`fold_equal()` makes search robust against both:
```python
users = [
    {"name": "José",      "email": "jose@example.com"},
    {"name": "Françoise", "email": "francoise@example.com"},
    {"name": "Müller",    "email": "muller@example.com"},
]

def find_user(query):
    return [u for u in users if fold_equal(u["name"], query)]

print(find_user("jose"))       # matches José
print(find_user("JOSÉ"))       # matches José
print(find_user("FRANCOISE"))  # matches Françoise
print(find_user("muller"))     # matches Müller
```

Without `fold_equal()`, none of these queries would match.

---

## Mental Model
```text
bytes
↓ decode
Unicode string
↓ normalize("NFC")
standard representation
↓ casefold()
comparison-ready text
↓ ==
```

---

## When to Use What

| Situation | Approach |
|-----------|----------|
| ASCII or known-normalized strings | `s1 == s2` |
| Unicode-aware, case-sensitive | `normalize("NFC", s1) == normalize("NFC", s2)` |
| Unicode-aware, case-insensitive | `normalize("NFC", s1).casefold() == normalize("NFC", s2).casefold()` |

---

## Key Takeaways

- `casefold()` is more thorough than `lower()` for Unicode-aware case matching.
- For robust user-facing comparison, always combine normalization and case folding:
```python
normalize("NFC", text).casefold()
```

---

## Exercises


**Exercise 1.**
Show the difference between `.lower()` and `.casefold()` using the German character `"\u00df"` (sharp s). Explain why `casefold()` is more suitable for case-insensitive comparison.

??? success "Solution to Exercise 1"

    ```python
    sharp_s = "\u00df"
    print(f"lower():    '{sharp_s.lower()}'")      # ß (unchanged)
    print(f"casefold(): '{sharp_s.casefold()}'")    # ss

    print("SS".casefold() == sharp_s.casefold())  # True
    print("SS".lower() == sharp_s.lower())        # False
    ```

    `lower()` does not change `ß` because it has no uppercase form. `casefold()` maps it to `ss`, enabling correct case-insensitive matching with `"SS"`.

---

**Exercise 2.**
Write a `fold_equal(s1, s2)` function that combines NFC normalization and case folding. Test it with `"Cafe\u0301"` and `"CAFE"`.

??? success "Solution to Exercise 2"

    ```python
    from unicodedata import normalize

    def fold_equal(s1, s2):
        return normalize("NFC", s1).casefold() == normalize("NFC", s2).casefold()

    print(fold_equal("Cafe\u0301", "CAFE"))   # True
    print(fold_equal("\u00df", "SS"))           # True
    print(fold_equal("hello", "HELLO"))         # True
    ```

    NFC normalization handles representation differences, and `casefold()` handles case differences, making this the most robust comparison approach.

---

**Exercise 3.**
Implement a case-insensitive search function `search_users(query, users)` where `users` is a list of name strings. The search should match regardless of case and Unicode representation differences.

??? success "Solution to Exercise 3"

    ```python
    from unicodedata import normalize

    def fold_equal(s1, s2):
        return normalize("NFC", s1).casefold() == normalize("NFC", s2).casefold()

    def search_users(query, users):
        return [u for u in users if fold_equal(u, query)]

    users = ["Jose\u0301", "Fran\u00e7oise", "M\u00fcller", "alice"]
    print(search_users("jose", users))       # ['José']
    print(search_users("ALICE", users))      # ['alice']
    print(search_users("muller", users))     # ['Müller']
    ```

    By normalizing and folding both the query and each user name, the search handles all case and representation variations.
