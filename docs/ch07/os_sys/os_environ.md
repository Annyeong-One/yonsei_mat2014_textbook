# Environment Variables (os.environ)

Access and modify environment variables through os.environ.

## Reading Environment Variables

Access environment variables.

```python
import os

# Get specific variable
home = os.environ.get('HOME', 'Not set')
print(f"HOME: {home}")

# Check if variable exists
if 'PATH' in os.environ:
    print("PATH is set")

# Get with default
debug = os.environ.get('DEBUG', 'false')
print(f"DEBUG: {debug}")

# List all variables
vars_count = len(os.environ)
print(f"Total env variables: {vars_count}")
```

```
HOME: /home/user
PATH is set
DEBUG: false
Total env variables: 50+
```

## Setting Environment Variables

Set environment variables during program execution.

```python
import os

# Set variable for current process
os.environ['MY_VAR'] = 'hello'
print(f"MY_VAR: {os.environ['MY_VAR']}")

# Set multiple variables
os.environ.update({
    'VAR1': 'value1',
    'VAR2': 'value2'
})

print(f"VAR1: {os.environ.get('VAR1')}")
print(f"VAR2: {os.environ.get('VAR2')}")

# Note: Changes only affect current process
print("Environment updated")
```

```
MY_VAR: hello
VAR1: value1
VAR2: value2
Environment updated
```

