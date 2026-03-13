# Command Line Arguments

The `argparse` module provides a way to parse command-line arguments passed to Python scripts.


## Basic Usage

```python
import argparse

parser = argparse.ArgumentParser(description='A simple calculator')
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")

args = parser.parse_args()
print(f"Sum: {args.num1 + args.num2}")
```

Run:
```bash
python script.py 5 3
# Sum: 8.0
```


## Positional Arguments

Positional arguments are required and parsed in order.

```python
import argparse

def calculate(x, y, op):
    if op == "+": return x + y
    if op == "-": return x - y
    if op == "*": return x * y
    if op == "/": return x / y

parser = argparse.ArgumentParser(description='Calculator')
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("op", help="Operation: +, -, *, /")

args = parser.parse_args()
result = calculate(args.num1, args.num2, args.op)
print(f"Result: {result}")
```

Run:
```bash
python script.py 10 5 +
# Result: 15.0
```


## Keyword (Optional) Arguments

Use `-` or `--` prefix for optional arguments.

```python
import argparse

parser = argparse.ArgumentParser(description='Calculator')
parser.add_argument("-x", "--num1", type=float, default=0, help="First number")
parser.add_argument("-y", "--num2", type=float, default=0, help="Second number")
parser.add_argument("-o", "--op", default="+", help="Operation")

args = parser.parse_args()
```

Run:
```bash
python script.py                    # Uses defaults
python script.py -x 10 -y 5         # num1=10, num2=5, op="+"
python script.py --num1 10 --num2 5 # Same as above
python script.py -x 10 -y 5 -o "*"  # Multiplication
```


## Default Values

```python
parser.add_argument("-n", "--name", default="World", help="Name to greet")
```

If not provided, `args.name` will be `"World"`.


## Type Conversion

By default, arguments are strings. Use `type=` to convert:

```python
parser.add_argument("count", type=int)
parser.add_argument("--rate", type=float, default=0.1)
```


## Boolean Flags

Use `action="store_true"` for boolean flags:

```python
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
```

Run:
```bash
python script.py           # args.verbose = False
python script.py -v        # args.verbose = True
python script.py --verbose # args.verbose = True
```


## Help Text

argparse automatically generates help:

```bash
python script.py --help
```

Output:
```
usage: script.py [-h] [-x NUM1] [-y NUM2] [-o OP]

Calculator

optional arguments:
  -h, --help            show this help message and exit
  -x NUM1, --num1 NUM1  First number
  -y NUM2, --num2 NUM2  Second number
  -o OP, --op OP        Operation
```


## Complete Example

```python
import argparse

def calculate(x, y, op):
    operations = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y if y != 0 else None
    }
    return operations.get(op)

def main():
    parser = argparse.ArgumentParser(description='Simple calculator')
    
    # Optional arguments with defaults
    parser.add_argument("-x", "--num1", type=float, default=1.0,
                        help="First number (default: 1.0)")
    parser.add_argument("-y", "--num2", type=float, default=2.0,
                        help="Second number (default: 2.0)")
    parser.add_argument("-o", "--op", default="+",
                        help="Operation: +, -, *, / (default: +)")
    
    args = parser.parse_args()
    
    result = calculate(args.num1, args.num2, args.op)
    if result is not None:
        print(f"{args.num1} {args.op} {args.num2} = {result}")
    else:
        print("Error: Division by zero")

if __name__ == "__main__":
    main()
```


## The args Namespace

`parse_args()` returns a `Namespace` object:

```python
args = parser.parse_args()
print(args)  # Namespace(num1=10.0, num2=5.0, op='+')

# Access as attributes
print(args.num1)  # 10.0
print(args.op)    # '+'
```


## Common Patterns

### Required Optional Argument

```python
parser.add_argument("-f", "--file", required=True, help="Input file")
```

### Choices

```python
parser.add_argument("-o", "--op", choices=["+", "-", "*", "/"],
                    default="+", help="Operation")
```

### Multiple Values

```python
parser.add_argument("files", nargs="+", help="Input files")
# Usage: python script.py file1.txt file2.txt file3.txt
```


## Summary

| Feature | Syntax |
|---------|--------|
| Positional | `parser.add_argument("name")` |
| Optional | `parser.add_argument("-n", "--name")` |
| Type | `type=int`, `type=float` |
| Default | `default=value` |
| Required | `required=True` |
| Boolean | `action="store_true"` |
| Choices | `choices=["a", "b", "c"]` |
| Help | `help="Description"` |
