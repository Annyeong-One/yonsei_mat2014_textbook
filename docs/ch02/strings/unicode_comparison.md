# Unicode Comparison Strategies

Python provides three levels of string comparison, each appropriate for
different situations.

---

## Level 1: Exact Comparison

Use `==` when both strings are known to be in the same Unicode form and
case matters:
```python
s1 = "café"
s2 = "café"

print(s1 == s2)  # True
```

This is the fastest approach but fails silently if the strings come from
different sources with different internal representations.

---

## Level 2: Unicode-Aware Case-Sensitive Comparison

Use `normalize()` when strings may have different internal representations
but case still matters:
```python
from unicodedata import normalize

def nfc_equal(s1, s2):
    return normalize("NFC", s1) == normalize("NFC", s2)

print(nfc_equal("café", "cafe\u0301"))  # True
print(nfc_equal("Café", "café"))        # False  (case-sensitive)
```

Typical use cases: comparing database keys, filenames, identifiers.

---

## Level 3: Unicode-Aware Case-Insensitive Comparison

Use `normalize()` combined with `casefold()` when strings may differ in
both representation and case:
```python
def fold_equal(s1, s2):
    return normalize("NFC", s1).casefold() == normalize("NFC", s2).casefold()

print(fold_equal("Café", "CAFÉ"))         # True
print(fold_equal("café", "cafe\u0301"))  # True
print(fold_equal("ß", "SS"))              # True
```

Typical use cases: user authentication, search queries, international names.

---

## Summary

| Level | Approach | Use When |
|-------|----------|----------|
| 1 | `s1 == s2` | Strings are ASCII or already normalized |
| 2 | `nfc_equal(s1, s2)` | Case matters, but representation may vary |
| 3 | `fold_equal(s1, s2)` | User-facing input, case and representation may vary |

Each level adds robustness at a small performance cost. For user-facing
comparison, always prefer Level 3.

---

## See Also

- [Unicode Normalization](unicode_normalization.md)
- [Unicode Case Folding](unicode_case_folding.md)