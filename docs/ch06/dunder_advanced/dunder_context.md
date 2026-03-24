# Context Managers

Resource management is a recurring challenge in programming: files must be closed, locks must be released, and database connections must be returned to the pool — even when an exception interrupts normal flow. Python's `with` statement and the context manager protocol guarantee that cleanup code runs no matter what. Any object that implements `__enter__` and `__exit__` can be used with `with`.

## With Statement Support

### 1. The __enter__ Method

The `__enter__` method is called when execution enters the `with` block. It performs any setup work (opening a file, acquiring a lock) and returns the resource that will be bound to the variable after the `as` keyword. If no resource needs to be returned, it typically returns `self`.

### 2. The __exit__ Method

The `__exit__` method is called when execution leaves the `with` block, whether normally or because of an exception. It receives three arguments — `exc_type`, `exc_val`, and `exc_tb` — that describe the exception, or are all `None` if the block completed successfully. After performing cleanup, `__exit__` can suppress the exception by returning `True`, or let it propagate by returning `False` (or `None`).

### 3. Usage

The following class wraps a filename and ensures the underlying file handle is always closed, even if an error occurs inside the `with` block.

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # Do not suppress exceptions

with ManagedFile("example.txt") as f:
    contents = f.read()
# f is guaranteed to be closed here
```

When the `with` block begins, `__enter__` opens the file and returns the file handle. When the block ends — normally or via exception — `__exit__` closes the file.

## Summary

- Context managers guarantee resource cleanup by pairing setup (`__enter__`) with teardown (`__exit__`).
- The `__exit__` method always runs, even when an exception occurs inside the `with` block.
- Implement `__enter__` and `__exit__` on any class to make its instances usable with the `with` statement.
