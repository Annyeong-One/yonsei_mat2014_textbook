# Installation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## pip Install

### 1. Basic Install

Install NumPy using Python's package manager.

```bash
pip install numpy
```

### 2. Specific Version

Install a specific version if needed.

```bash
pip install numpy==1.26.0
```

### 3. Upgrade Existing

Upgrade to the latest version.

```bash
pip install --upgrade numpy
```

## conda Install

### 1. Basic Install

Install NumPy using Anaconda/Miniconda.

```bash
conda install numpy
```

### 2. From conda-forge

Install from the conda-forge channel.

```bash
conda install -c conda-forge numpy
```

### 3. Specific Version

```bash
conda install numpy=1.26.0
```

## Virtual Environment

### 1. Create Environment

Isolate NumPy installation in a virtual environment.

```bash
# Using venv
python -m venv myenv

# Activate (Linux/macOS)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate
```

### 2. Install in venv

```bash
# After activation
pip install numpy
```

### 3. conda Environment

```bash
# Create with NumPy
conda create -n myenv numpy

# Activate
conda activate myenv
```

## Platform Support

### 1. Cross-Platform

NumPy works on all major operating systems.

```python
import numpy as np
import platform

def main():
    print(f"OS: {platform.system()}")
    print(f"NumPy version: {np.__version__}")

if __name__ == "__main__":
    main()
```

### 2. Supported Systems

- **Windows**: Windows 10/11, x64
- **macOS**: Intel and Apple Silicon (M1/M2/M3)
- **Linux**: Most distributions, x64 and ARM

### 3. Python Versions

NumPy supports recent Python versions. Check compatibility:

```bash
# Check your Python version
python --version

# NumPy 1.26+ requires Python 3.9+
```
