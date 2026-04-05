
# Loop Else

Python loops support an optional `else` clause.

The `else` block runs **only if the loop completes normally**.

If a `break` statement occurs, the `else` block is skipped.

## Example

```python
numbers = [1,3,5,7]

for num in numbers:

    if num == 4:
        print("Found")
        break

else:
    print("4 not found")
```

Output:

```
4 not found
```

## Practical Pattern: Searching

```python
def find_number(nums,target):

    for num in nums:

        if num == target:
            return True

    else:
        return False
```

This pattern cleanly expresses **search logic**.

---

## Exercises

**Exercise 1.**
The `else` clause on a loop runs when the loop completes "normally" (without `break`). Predict the output:

```python
for i in range(5):
    if i == 10:
        break
else:
    print("no break")

for i in range(5):
    if i == 3:
        break
else:
    print("no break")
```

Why does the name `else` confuse many programmers? What would be a more intuitive name for this feature?

??? success "Solution to Exercise 1"
    Output:

    ```text
    no break
    ```

    Only the first `"no break"` prints. In the first loop, `i` never equals `10`, so `break` never executes, and the `else` clause runs. In the second loop, `i == 3` triggers `break`, so the `else` clause is **skipped**.

    The name `else` confuses programmers because they read it as "else if the loop condition is false" (by analogy with `if/else`). A more intuitive name would be `nobreak` or `then` -- "do this if the loop completed without breaking." Raymond Hettinger (Python core developer) has suggested thinking of it as "if no break."

---

**Exercise 2.**
`while` loops also support `else`. Predict the output:

```python
n = 5
while n > 0:
    n -= 1
else:
    print(f"ended with n={n}")

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
else:
    print(f"ended with n={n}")
```

Explain when the `else` clause executes in each case. Is it possible for the `else` block to run if the `while` condition was never `True`?

??? success "Solution to Exercise 2"
    Output:

    ```text
    ended with n=0
    ```

    Only the first `else` clause runs. The first `while` loop runs until `n` reaches `0`, at which point `n > 0` is `False` and the loop exits normally. The `else` clause executes.

    The second `while` loop hits `break` when `n == 2`, so the `else` clause is skipped.

    Yes, the `else` block runs even if the `while` condition was never `True`:

    ```python
    while False:
        pass
    else:
        print("runs!")  # This prints!
    ```

    The `else` clause runs whenever `break` was NOT hit. If the loop body never executes (because the condition was initially false), `break` was certainly not hit, so `else` runs.

---

**Exercise 3.**
The classic use case for loop `else` is primality testing:

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
```

Explain how this works. Then explain: could you write this function without `for...else`? What is the equivalent code without using `else`? Is the `else` version actually clearer?

??? success "Solution to Exercise 3"
    The function works as follows: it loops through potential divisors from 2 to sqrt(n). If any divisor is found (`n % i == 0`), it returns `False` immediately via `break`-like behavior (actually `return`, which also exits the loop). If no divisor is found, the loop completes normally, and the `else` clause returns `True`.

    Without `for...else`:

    ```python
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    ```

    This is actually **simpler and more readable**. When the function returns inside the loop, the `else` clause is unnecessary -- `return True` at the end naturally means "we checked all divisors and found none." The `for...else` pattern is most useful when you need to distinguish "break happened" from "loop completed" and you are **not** inside a function that can use `return`. In practice, many Pythonistas find `for...else` confusing and prefer explicit alternatives.
