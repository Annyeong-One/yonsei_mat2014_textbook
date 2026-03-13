
# break and continue

Loop control statements modify the execution flow inside loops.

---

## break

`break` exits the loop immediately.

```python
numbers = [1,5,8,3]

for num in numbers:
    if num == 8:
        break
    print(num)
````

Output:

```
1
5
```

Execution stops when `8` is found.

---

## continue

`continue` skips the rest of the current iteration.

```python
for i in range(10):

    if i % 2 == 0:
        continue

    print(i)
```

Output:

```
1
3
5
7
9
```

Even numbers are skipped.

---

## break vs continue

| Statement | Effect                  |
| --------- | ----------------------- |
| break     | exits the loop entirely |
| continue  | skips to next iteration |

---

## Nested Loops

`break` affects only the **innermost loop**.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i,j)
```
