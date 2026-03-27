# enumerate() and zip()

Both functions wrap an existing iterable and yield tuples. `enumerate()` pairs each element with its index; `zip()` pairs elements from two or more iterables.

## enumerate()

`enumerate()` adds an index counter to any iterable. It is the idiomatic replacement for `range(len(sequence))`:

```python
fruits = ["apple", "banana", "cherry"]

# Avoid this
for i in range(len(fruits)):
    print(i, fruits[i])

# Prefer this
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

Output:

```text
0 apple
1 banana
2 cherry
```

The default counter starts at 0. Use `start=` to begin at a different value:

```python
tasks = ["Buy groceries", "Call mom", "Finish homework"]
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
```

Output:

```text
1. Buy groceries
2. Call mom
3. Finish homework
```

## zip()

`zip()` combines elements from multiple iterables into tuples, stopping at the shortest:

```python
names = ["Alice", "Bob", "Charlie"]
ages  = [25, 30, 35]

for name, age in zip(names, ages):
    print(name, age)
```

Output:

```text
Alice 25
Bob 30
Charlie 35
```

Three iterables at once:

```python
names  = ["Alice", "Bob", "Charlie"]
ages   = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} and lives in {city}")
```

Output:

```text
Alice is 25 and lives in NYC
Bob is 30 and lives in LA
Charlie is 35 and lives in Chicago
```

### Converting zip output

`zip()` is lazy — wrap it in `list()` to materialise the pairs:

```python
pairs = list(zip(names, ages))
print(pairs)   # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

### Building a dictionary from two lists

```python
keys   = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = dict(zip(keys, values))
print(person)   # {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

### Unzipping

The `*` operator unpacks a list of pairs back into separate sequences:

```python
pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names, ages = zip(*pairs)
print(names)   # ('Alice', 'Bob', 'Charlie')
print(ages)    # (25, 30, 35)
```

## Key Ideas

`enumerate()` is the idiomatic way to iterate with an index — prefer it over `range(len(seq))`.
`zip()` is the idiomatic way to iterate over two or more sequences in parallel — prefer it over indexing both manually.
Both functions are lazy: they produce one tuple at a time without building the full result in memory.
