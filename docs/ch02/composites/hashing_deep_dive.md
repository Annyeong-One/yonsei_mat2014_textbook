# Hashability and Hash Tables

## Hashability vs Immutability

These are two distinct concepts that are often confused:

- **Immutability** — about *state*: can the object's value change after creation?
- **Hashability** — about *interface*: does the object have a valid `__hash__` method?

They are independent concepts that happen to correlate by Python's design convention:

```
Immutable → usually hashable    (not always: tuple containing a list)
Mutable   → usually unhashable  (not always: custom class with __hash__)
```

The cleanest one-line rule:

> **Hashable = `__hash__` exists and returns a stable integer. Nothing more, nothing less.**

Immutability is the most natural and common way to guarantee that stability — but it is neither necessary nor sufficient on its own.

```python
# Immutable but NOT hashable
t = (1, [2, 3])
hash(t)          # ✗ TypeError — immutable structure, but unhashable

# Mutable but hashable (custom __hash__)
class Mutable:
    def __hash__(self):
        return 42
    def __eq__(self, other):
        return self is other

m = Mutable(1)
hash(m)    # ✓ works
m.x = 99  # state changes → still mutable
```

---

## What Is a Hash Value?

The hash value is always an **integer** — the raw output of `hash()`:

```python
hash("hello")     # -8522010064543165804  (large integer)
hash(42)          # 42
hash(3.14)        # 322818021289917443
hash((1, 2, 3))   # 2528502973977326415
```

A few key properties:

- **Integers hash to themselves**: `hash(42) == 42`
- **Equal objects must have equal hashes**: `hash(1) == hash(1.0)` because `1 == 1.0`
- **Hash size**: on 64-bit systems, a 64-bit signed integer (~±9.2×10¹⁸)

### Why `1 == 1.0` Is True

Python's `==` compares **mathematical value**, not type. The integer `1` and the float `1.0` represent the same quantity, so Python considers them equal — this is a deliberate design choice consistent with most languages.

```python
1 == 1.0        # True  — same mathematical value
1 is 1.0        # False — different objects, different types
type(1) == type(1.0)  # False
```

Because `1 == 1.0`, it must also be true that `hash(1) == hash(1.0)` — otherwise dict lookups would break.

### Hash Randomization

Not all types produce stable hashes across Python sessions:

```python
hash((1, 2, 3))   # always the same value (given same Python version)
hash("hello")     # different every run  ← randomized by PYTHONHASHSEED
```

This is because `tuple.__hash__` and `str.__hash__` are **different implementations**:

| Type | Algorithm | Randomized? |
|---|---|---|
| `tuple.__hash__` | xxHash-based mixing | ✗ No |
| `str.__hash__` | SipHash-1-3 | ✓ Yes |
| `int.__hash__` | modular arithmetic | ✗ No |
| `frozenset.__hash__` | XOR-based | ✗ No |

String hashing was randomized in Python 3.3 as a **security fix** — without it, an attacker could craft input strings that all hash to the same bucket, causing a hash collision DoS attack on web servers.

---

## How Tuple Hashing Works

The hash of a tuple is computed **recursively from its elements**, combining their hash values using an xxHash-inspired algorithm:

```python
# Pseudocode approximation
def tuple_hash(t):
    acc = 2870177450012600261  # fixed initial seed (not randomized)
    for element in t:
        acc = mix(acc, hash(element))  # needs each element's hash
    return acc
```

This is why `(1, [2, 3])` fails — computing the tuple's hash requires `hash([2, 3])`, but lists are unhashable:

```python
hash((1, [2, 3]))   # ✗ TypeError — fails at runtime when it tries hash([2,3])
```

Order matters in tuples:

```python
hash((1, 2)) == hash((2, 1))               # False — order is part of the computation
hash(frozenset({1,2})) == hash(frozenset({2,1}))  # True  — frozenset is unordered
```

---

## Why Hashability Exists: Hash Table Lookup

Hash values exist primarily to enable **O(1) lookup** in hash tables. Python's `dict` and `set` are both hash tables underneath.

```
key → hash(key) → bucket index → value
bucket index = hash(key) % table_size
```

This is why:

- `dict` keys must be hashable — Python needs a bucket index to store and find them
- `set` members must be hashable — same reason
- `list` has `__hash__ = None` — it was never designed for hash table lookup

```python
# list — no hash table → linear scan
1000 in [0, 1, 2, ..., 999]   # O(n) — checks each element

# set — hash table → direct bucket lookup
1000 in {0, 1, 2, ..., 999}   # O(1) — hash(1000) → bucket → found
```

The hash value is a **large integer** that is a stable property of the key. The **bucket index** is a small integer derived at runtime from the current table size:

```python
hash("hello")          # -8522010064543165804  ← property of the key, stable
hash("hello") % 8      # 4                     ← bucket index, depends on table size
hash("hello") % 16     # 12                    ← different table size → different bucket
```

This separation is deliberate:

- `__hash__` is responsible for producing a **good, stable, large integer**
- The hash table maps that integer to a bucket via `%`

---

## Hash Table Internals

### Load Factor and Memory Overhead

Python's `dict` keeps the **load factor** (entries / table size) below **2/3**:

```
table size = 8
max entries before resize = 5   (8 × 2/3 ≈ 5)
```

The used area grows from 1/3 to 2/3, then resize kicks in:

```
used area 1/3 ────────────> used area 2/3 ──> resize ──> used area 1/3
```

This means at any time, at least **1/3 of the table is intentionally empty**. The memory overhead oscillates:

| Moment | Used | Empty (wasted) |
|---|---|---|
| Just after resize | ~1/3 | ~2/3 |
| Just before resize | ~2/3 | ~1/3 |
| Average | ~1/2 | ~1/2 |

In practice each empty slot is just 8 bytes (a null pointer), so the real memory cost is small. The O(1) lookup benefit far outweighs the memory overhead.

### Resize: Like List Resize, Plus Rehashing

When the 6th entry is inserted into a size-8 table, Python resizes:

```
List resize:  allocate new array → memcopy        → done   O(n)
Dict resize:  allocate new table → rehash + reinsert → done   O(n)
```

The extra step is necessary because bucket indices change with table size:

```python
hash("hello") % 8  = 3   # old table
hash("hello") % 16 = 11  # new table — different bucket!
```

Every key must be recomputed and repositioned. Both list and dict resize are **O(1) amortized** for the same reason — table size doubles each time, so resizes become exponentially rare.

### Collision Resolution: Open Addressing

When two keys land in the same bucket, Python uses **open addressing** — it probes for the next available slot rather than chaining a linked list.

**Simple linear probing** (not what Python does):
```
collision at bucket 3 → try 4 → try 5 → try 6 ...
```

Problem: this causes **clustering** — long occupied runs that make future collisions worse.

**Python's actual probing formula** (from CPython source):
```python
j = (5 * j + 1 + perturb) % table_size
perturb >>= 5
```

Here `j` on the right is the **current (occupied) bucket**, and `j` on the left is the **next bucket to probe**.

This jumps pseudo-randomly around the table:
```
simple linear:  3 → 4 → 5 → 6        # clustering
Python actual:  3 → 11 → 6 → 14      # spread out
```

The table is logically a **circular buffer** — the `%` operation causes wrap-around so no index ever goes out of bounds:

```
(7 + 1) % 8 = 0   ← wraps back to start
```

### The `perturb` Variable

`perturb` starts as the **full hash value** (before `% table_size`) and decays toward zero:

```python
perturb = hash(key)           # large integer — full hash value
j = perturb % table_size      # initial bucket

# each collision step:
j = (5 * j + 1 + perturb) % table_size
perturb >>= 5                  # right shift by 5: divide by 32
```

`>>=` is a compound bitwise shift — `perturb >>= 5` means `perturb = perturb >> 5`, dropping the 5 rightmost bits each step:

```
step 0: perturb = 12345678          (64 bits of randomness)
step 1: perturb = 385802            (÷ 32)
step 2: perturb = 12056             (÷ 32 again)
step 3: perturb = 376
step 4: perturb = 11
step 5: perturb = 0                 ← effectively dead
```

Once `perturb` reaches 0, the formula reduces to `j = (5*j + 1) % table_size` — a deterministic cycle guaranteed to visit every bucket, ensuring insertion always succeeds.

**Why use the full hash value instead of just the bucket index?**

Two keys can share the same initial bucket but have different full hash values:

```python
hash("hello") % 8 = 3    # full hash = -8522010064543165804
hash("world") % 8 = 3    # full hash =  1234567890123456789
# same bucket → collision!
```

Using the full hash in `perturb` gives them **different probe sequences**, resolving collisions quickly. Using only the bucket index (3) would send both down the same path.

### Deletion: Tombstones

You cannot simply empty a slot on deletion — it would break ongoing probe sequences:

```
delete "hello" at bucket 3 → empty slot

lookup "world": bucket 3 → empty → stop! → not found ✗  WRONG
```

Python uses a **tombstone** marker instead:

```
delete "hello" → bucket 3 → mark DELETED (tombstone)

lookup "world": bucket 3 → tombstone → keep probing
               → bucket 4 → found "world" ✓
```

---

## Summary

```
__hash__ exists
    → hash(key) returns a large integer
        → hash(key) % table_size returns bucket index
            → O(1) lookup is possible
                → can be used as dict key / set member

list has no __hash__
    → no bucket index computable
        → only linear O(n) scan possible
            → cannot be dict key / set member
```

People often say "dict keys must be immutable" — but the correct term is **hashable**. Immutability is just the most common way to guarantee a stable hash value. The actual technical requirement is always hashability.
