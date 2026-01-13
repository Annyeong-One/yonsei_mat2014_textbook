# Installing Python

Python is the primary language used throughout this book. This section explains common ways to install Python reliably on different systems.

---

## System Python vs

Most operating systems ship with a system Python, but:
- it may be outdated,
- modifying it can break system tools.

It is strongly recommended to install a separate Python distribution.

---

## Installing with

On macOS, Homebrew is a popular package manager.

Steps:
1. Install Homebrew from https://brew.sh
2. Run:
```bash
brew install python
```

This installs the latest stable Python and `pip`.

---

## Installing with

Conda provides:
- Python,
- package management,
- isolated environments.

Steps:
1. Download Anaconda or Miniconda.
2. Create an environment:
```bash
conda create -n quant python=3.11
conda activate quant
```

Conda is especially convenient for scientific computing.

---

## Installing with pip

Advanced users may prefer `pyenv` to manage Python versions.

Typical workflow:
```bash
pyenv install 3.11.6
pyenv global 3.11.6
pip install --upgrade pip
```

This gives fine-grained control over Python versions.

---

## Verification

### Command Line

Check installation with:

```bash
python --version
pip --version
```

You should see Python 3.10+.

### From Python

```python
from platform import python_version
print(python_version())  # e.g., '3.11.6'

import sys
print(sys.version)       # Full version info
print(sys.executable)    # Path to Python interpreter
```

---

## Key takeaways

- Avoid modifying system Python.
- Use Homebrew or Conda for simplicity.
- Use virtual environments for projects.
