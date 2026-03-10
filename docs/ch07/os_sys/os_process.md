# Process Management (os)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Create and manage processes using os module functions.

## Process Information

Get information about the current process.

```python
import os

# Process ID
pid = os.getpid()
print(f"Process ID: {pid}")

# Parent process ID
ppid = os.getppid()
print(f"Parent Process ID: {ppid}")

# User ID
uid = os.getuid()
print(f"User ID: {uid}")

# Environment
print(f"Process name: python")
```

```
Process ID: 12345
Parent Process ID: 1234
User ID: 1000
Process name: python
```

## Running External Commands

Execute system commands (use subprocess for most cases).

```python
import os
import sys

# For simple commands, use os.system (deprecated, prefer subprocess)
# os.system returns exit code

# Get directory listing
exit_code = os.system('ls -la /tmp > /dev/null 2>&1')
print(f"ls exit code: {exit_code}")

# More reliable: use subprocess
import subprocess
result = subprocess.run(['echo', 'Hello'], capture_output=True, text=True)
print(f"Output: {result.stdout}")
```

```
ls exit code: 0
Output: Hello
```

