# Installing Python (brew, conda, pip)

Python is the primary language used throughout this book. This section explains common ways to install Python reliably on different systems.

---

## 1. System Python vs user-installed Python

Most operating systems ship with a system Python, but:
- it may be outdated,
- modifying it can break system tools.

It is strongly recommended to install a separate Python distribution.

---

## 2. Installing with Homebrew (macOS)

On macOS, Homebrew is a popular package manager.

Steps:
1. Install Homebrew from https://brew.sh
2. Run:
```bash
brew install python
```

This installs the latest stable Python and `pip`.

---

## 3. Installing with Conda (Anaconda / Miniconda)

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

## 4. Installing with pip and pyenv

Advanced users may prefer `pyenv` to manage Python versions.

Typical workflow:
```bash
pyenv install 3.11.6
pyenv global 3.11.6
pip install --upgrade pip
```

This gives fine-grained control over Python versions.

---

## 5. Verification

Check installation with:
```bash
python --version
pip --version
```

You should see Python 3.10+.

---

## Key takeaways

- Avoid modifying system Python.
- Use Homebrew or Conda for simplicity.
- Use virtual environments for projects.
