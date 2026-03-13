# IDE Debugging Overview

Overview of debugging capabilities in popular Python IDEs.

## IDE Debugging Features

Most IDEs provide visual debuggers.

```python
# IDE debugging typically provides:
# - Breakpoints (click on line number)
# - Variable inspection in watch window
# - Call stack visualization
# - Step through code visually
# - Conditional breakpoints
# - Debug console for expressions

def factorial(n):
    if n <= 1:
        return 1
    # Set breakpoint on next line in IDE
    return n * factorial(n - 1)

result = factorial(5)
print(f"5! = {result}")
```

```
5! = 120
```

## Remote Debugging

Debug applications running on remote servers.

```python
# Python debuggers support remote debugging
# Example: debugpy for VS Code

# In application (server-side):
import debugpy

debugpy.listen(('0.0.0.0', 5678))
debugpy.wait_for_client()

def remote_function():
    x = 10
    return x * 2

result = remote_function()
print(result)

# In IDE, connect to localhost:5678 to debug
```

```
Waiting for debugger to attach...
```

