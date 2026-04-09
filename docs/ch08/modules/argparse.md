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


## The args Namespace

`parse_args()` returns a `Namespace` object:

```python
args = parser.parse_args()
print(args)  # Namespace(num1=10.0, num2=5.0, op='+')

# Access as attributes
print(args.num1)  # 10.0
print(args.op)    # '+'
```

Use `args.num1`, `args.num2`, and `args.op` to access values safely.

