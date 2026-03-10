# Common pdb Commands


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Master the most useful pdb commands for effective debugging.

## Navigation Commands

Commands for stepping through code.

```python
# Common pdb navigation:
# l - list current code section
# n (next) - execute next line
# s (step) - step into function
# c (continue) - resume execution
# u (up) - go up one frame
# d (down) - go down one frame
# j lineno (jump) - jump to line

def example():
    x = 1  # Breakpoint here, then n to next
    y = 2  # n again
    z = x + y  # s into any function calls
    return z

# In pdb session:
# (Pdb) l
# (Pdb) n
# (Pdb) s
# (Pdb) c
```

```
Commands accepted and executed in pdb
```

## Inspection Commands

Commands for examining variables and state.

```python
# Inspection commands in pdb:
# p expression - print value
# pp object - pretty print object
# whatis variable - show type
# h - help
# h command - help on specific command

def inspect_example(data):
    result = sum(data)
    count = len(data)
    # Breakpoint and inspect
    import pdb; pdb.set_trace()
    
    # In pdb:
    # (Pdb) p result
    # (Pdb) pp data
    # (Pdb) whatis count
    
    return result

print("Inspection commands available")
```

```
Inspection commands available
```

