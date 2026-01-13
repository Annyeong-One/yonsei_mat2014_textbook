# pip and PyPI

`pip` is Python's default package manager. It installs packages from the **Python Package Index (PyPI)**.

---

## What is PyPI?

**PyPI** (Python Package Index) at https://pypi.org is the official repository for Python packages.

- Over 500,000 packages available
- Anyone can publish packages
- `pip` downloads from PyPI by default

---

## Basic Commands

### Install a Package

```bash
pip install numpy
pip install pandas matplotlib scikit-learn
```

### Install Specific Version

```bash
pip install numpy==1.24.0        # Exact version
pip install numpy>=1.20.0        # Minimum version
pip install numpy>=1.20,<2.0     # Version range
```

### Upgrade a Package

```bash
pip install --upgrade numpy
pip install -U numpy             # Short form
```

### Uninstall a Package

```bash
pip uninstall numpy
pip uninstall -y numpy           # Skip confirmation
```

---

## Information Commands

### Show Package Info

```bash
pip show numpy
```

Output:
```
Name: numpy
Version: 1.24.0
Summary: Fundamental package for array computing
Home-page: https://numpy.org
Author: Travis E. Oliphant et al.
Location: /usr/lib/python3.11/site-packages
Requires: 
Required-by: pandas, scipy, matplotlib
```

### List Installed Packages

```bash
pip list                         # All packages
pip list --outdated              # Packages with newer versions
pip list --format=freeze         # In requirements format
```

### Search (Deprecated)

```bash
# pip search is deprecated
# Use PyPI website or:
pip index versions numpy         # Show available versions
```

---

## Requirements Files

### Create requirements.txt

```bash
pip freeze > requirements.txt
```

Example `requirements.txt`:
```
numpy==1.24.0
pandas==2.0.0
matplotlib==3.7.0
scikit-learn==1.2.0
```

### Install from requirements.txt

```bash
pip install -r requirements.txt
```

### Better Practice: Manual requirements.txt

Instead of `pip freeze`, manually specify only direct dependencies:

```
# requirements.txt
numpy>=1.20
pandas>=1.5
matplotlib>=3.5
```

This avoids locking unnecessary transitive dependencies.

---

## Virtual Environments

Always use virtual environments to isolate project dependencies.

### Create and Use venv

```bash
# Create
python -m venv myenv

# Activate (Linux/macOS)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Install packages (isolated)
pip install numpy pandas

# Deactivate
deactivate
```

### pip in Virtual Environments

```bash
# Check which pip
which pip                        # Should be in venv

# Upgrade pip itself
pip install --upgrade pip
```

---

## Advanced Usage

### Install from Git

```bash
pip install git+https://github.com/user/repo.git
pip install git+https://github.com/user/repo.git@v1.0.0  # Specific tag
pip install git+https://github.com/user/repo.git@main   # Branch
```

### Install in Editable Mode

For local development:

```bash
pip install -e .                 # Install current directory
pip install -e /path/to/project  # Install specific path
```

Changes to source code take effect immediately.

### Install from Local File

```bash
pip install ./mypackage-1.0.0.tar.gz
pip install ./mypackage-1.0.0-py3-none-any.whl
```

### Install to User Directory

```bash
pip install --user numpy         # Installs to ~/.local/
```

---

## Configuration

### pip.conf / pip.ini

```ini
# ~/.pip/pip.conf (Linux/macOS)
# %APPDATA%\pip\pip.ini (Windows)

[global]
timeout = 60
index-url = https://pypi.org/simple

[install]
trusted-host = pypi.org
```

### Environment Variables

```bash
export PIP_DEFAULT_TIMEOUT=60
export PIP_INDEX_URL=https://pypi.org/simple
```

---

## Common Issues

### Permission Denied

```bash
# Don't use sudo pip!
# Use virtual environment or --user
pip install --user package
```

### SSL Certificate Error

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package
```

### Dependency Conflicts

```bash
pip check                        # Check for conflicts
pip install package --force-reinstall
```

---

## pip vs pip3

| Command | Python Version |
|---------|----------------|
| `pip` | Default Python (could be 2 or 3) |
| `pip3` | Explicitly Python 3 |
| `python -m pip` | pip for specific Python |
| `python3 -m pip` | pip for Python 3 |

**Best practice**: Use `python -m pip` to ensure correct Python version.

```bash
python3 -m pip install numpy
```

---

## Summary

| Command | Description |
|---------|-------------|
| `pip install pkg` | Install package |
| `pip install pkg==1.0` | Install specific version |
| `pip install -U pkg` | Upgrade package |
| `pip uninstall pkg` | Remove package |
| `pip show pkg` | Show package info |
| `pip list` | List installed packages |
| `pip freeze` | Output installed packages |
| `pip install -r req.txt` | Install from file |
| `pip install -e .` | Editable install |

---

## Key Takeaways

- `pip` is Python's default package manager
- Always use virtual environments
- Use `requirements.txt` for reproducible environments
- Prefer `python -m pip` over bare `pip`
- Don't use `sudo pip` — use `--user` or virtual environments
