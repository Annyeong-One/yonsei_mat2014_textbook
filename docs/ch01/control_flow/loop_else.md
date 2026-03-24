
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
