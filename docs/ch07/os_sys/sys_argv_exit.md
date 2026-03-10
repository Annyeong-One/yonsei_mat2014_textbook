# sys.argv and sys.exit


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Process command-line arguments with sys.argv and control program termination with sys.exit.

## sys.argv - Command-Line Arguments

Access command-line arguments passed to the script.

```python
import sys

print(f"Script name: {sys.argv[0]}")
print(f"All arguments: {sys.argv}")
print(f"Number of arguments: {len(sys.argv)}")

# Example with arguments
if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")

# Process arguments
def process_args():
    if len(sys.argv) < 2:
        print("Usage: script.py <name>")
        return
    name = sys.argv[1]
    print(f"Hello, {name}")

process_args()
```

```
Script name: script.py
All arguments: ['script.py']
Number of arguments: 1
Usage: script.py <name>
```

## sys.exit - Program Termination

Exit the program with a specific exit code.

```python
import sys

def safe_divide(a, b):
    if b == 0:
        print("Error: division by zero")
        sys.exit(1)  # Exit with error code
    return a / b

# Successful execution
result = safe_divide(10, 2)
print(f"Result: {result}")

# Demonstrate exit code
print("Program completed successfully")
sys.exit(0)  # Exit with success code
```

```
Result: 5.0
Program completed successfully
```

