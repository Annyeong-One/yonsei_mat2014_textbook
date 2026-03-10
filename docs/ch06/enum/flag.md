# Flag and IntFlag


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Flag and IntFlag are specialized enums for bit flags, supporting bitwise operations like OR, AND, and NOT.

---

## Flag Basics

```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4

# Single permission
user1_perms = Permission.READ
print(user1_perms)              # Permission.READ

# Multiple permissions with bitwise OR
user2_perms = Permission.READ | Permission.WRITE
print(user2_perms)              # Permission.READ|WRITE

# Check if permission is set
print(Permission.READ in user2_perms)     # True
print(Permission.EXECUTE in user2_perms)  # False
```

## Practical Flag Example

```python
from enum import Flag, auto

class FileMode(Flag):
    READABLE = auto()    # 1
    WRITABLE = auto()    # 2
    EXECUTABLE = auto()  # 4

def check_permissions(mode: FileMode, required: FileMode) -> bool:
    return required in mode

file_mode = FileMode.READABLE | FileMode.WRITABLE

# Check single permission
print(check_permissions(file_mode, FileMode.READABLE))    # True
print(check_permissions(file_mode, FileMode.EXECUTABLE))  # False

# Check multiple permissions
can_read_write = FileMode.READABLE | FileMode.WRITABLE
print(can_read_write in file_mode)  # True
```

## IntFlag

```python
from enum import IntFlag, auto

class Status(IntFlag):
    RUNNING = auto()     # 1
    PAUSED = auto()      # 2
    STOPPED = auto()     # 4
    ERROR = auto()       # 8

# IntFlag can also use arithmetic
status = Status.RUNNING | Status.ERROR
print(status)           # Status.RUNNING|ERROR
print(status.value)     # 9 (1 + 8)

# Can mix with integers
combined = status | 0x10  # Add raw bits
print(combined.value)     # 25

# Bitwise operations work
print(status & Status.RUNNING)  # Status.RUNNING
print(status & Status.PAUSED)   # Status(0) - empty
```

## Flag Iteration and Checking

```python
from enum import Flag, auto

class Feature(Flag):
    FEATURE_A = auto()
    FEATURE_B = auto()
    FEATURE_C = auto()
    FEATURE_D = auto()

enabled_features = Feature.FEATURE_A | Feature.FEATURE_C

# Iterate over enabled features
print("Enabled features:")
for feature in Feature:
    if feature in enabled_features:
        print(f"  - {feature.name}")

# Count enabled features
count = bin(enabled_features.value).count('1')
print(f"Total enabled: {count}")
```

## Combining Flags

```python
from enum import Flag, auto

class DatabaseOption(Flag):
    CACHE = auto()           # 1
    REPLICATE = auto()       # 2
    COMPRESS = auto()        # 4
    ENCRYPT = auto()         # 8
    VALIDATE = auto()        # 16

def create_connection(options: DatabaseOption):
    if DatabaseOption.ENCRYPT in options:
        print("Enabling encryption")
    if DatabaseOption.CACHE in options:
        print("Enabling cache")
    if DatabaseOption.REPLICATE in options:
        print("Enabling replication")

# Create options combination
conn_options = (DatabaseOption.ENCRYPT | 
                DatabaseOption.CACHE | 
                DatabaseOption.REPLICATE)

create_connection(conn_options)
```

## Removing Flags

```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    ADMIN = auto()

# Start with multiple permissions
perms = Permission.READ | Permission.WRITE | Permission.DELETE

# Remove a permission
perms = perms & ~Permission.DELETE  # Bitwise NOT and AND
print(perms)                        # Permission.READ|WRITE

# Check it's gone
print(Permission.DELETE in perms)   # False
```

## IntFlag Arithmetic

```python
from enum import IntFlag, auto

class Level(IntFlag):
    BASIC = auto()         # 1
    INTERMEDIATE = auto()  # 2
    ADVANCED = auto()      # 4

level = Level.INTERMEDIATE
print(level.value)        # 2

# IntFlag supports arithmetic
next_level = level | Level.ADVANCED
print(next_level.value)   # 6

# Can extract individual flags
remaining = next_level & ~Level.INTERMEDIATE
print(remaining)          # Level.ADVANCED
```

## When to Use Flag

- Permissions and capabilities
- Feature toggles
- Configuration options
- Combination of boolean settings
- Need bitwise operations
