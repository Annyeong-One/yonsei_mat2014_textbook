# Development Tools


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

A good development environment improves productivity. This page covers IDEs, online notebooks, version control, and virtual environments.

---

## IDEs and Editors

### VS Code (Recommended)

Free, extensible, excellent Python support.

**Setup:**
1. Install VS Code from https://code.visualstudio.com
2. Install Python extension
3. Select Python interpreter: `Cmd/Ctrl + Shift + P` → "Python: Select Interpreter"

**Key features:**
- IntelliSense (autocomplete)
- Integrated terminal
- Debugger
- Git integration
- Jupyter notebook support

### PyCharm

Full-featured Python IDE by JetBrains.

| Edition | Cost | Features |
|---------|------|----------|
| Community | Free | Core Python development |
| Professional | Paid | Web, database, scientific tools |

### Jupyter Notebook / Lab

Interactive notebook for data science and exploration.

```bash
pip install notebook
jupyter notebook

# Or JupyterLab (newer interface)
pip install jupyterlab
jupyter lab
```

**Best for:**
- Data exploration
- Visualization
- Teaching and documentation
- Prototyping

### Other Editors

| Editor | Description |
|--------|-------------|
| Sublime Text | Fast, lightweight text editor |
| Vim/Neovim | Terminal-based, highly customizable |
| Atom | GitHub's editor (discontinued) |
| Spyder | Scientific Python IDE |

---

## Online Notebooks

No installation required — run Python in browser.

### Google Colab

Free Jupyter notebooks with GPU/TPU access.

**Setup:**
1. Go to https://colab.research.google.com
2. Sign in with Google account
3. Create new notebook or upload existing

**Features:**
- Free GPU/TPU runtime
- Pre-installed ML libraries (TensorFlow, PyTorch)
- Google Drive integration
- Easy sharing

### Kaggle Notebooks

Free notebooks with datasets and competitions.

**Setup:**
1. Go to https://www.kaggle.com
2. Create account
3. Go to "Code" → "New Notebook"

**Features:**
- Free GPU (30 hours/week)
- Access to Kaggle datasets
- Version control built-in

### Other Online Options

| Platform | Description |
|----------|-------------|
| Binder | Turn GitHub repos into notebooks |
| Replit | Online IDE for many languages |
| GitHub Codespaces | VS Code in browser |

---

## Version Control: Git and GitHub

### Git Basics

Git tracks changes to your code.

```bash
# Install Git
# macOS: brew install git
# Ubuntu: sudo apt install git
# Windows: Download from git-scm.com

# Configure
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Basic workflow
git init                    # Initialize repository
git add .                   # Stage changes
git commit -m "message"     # Commit changes
git status                  # Check status
git log                     # View history
```

### GitHub

Remote hosting for Git repositories.

```bash
# Clone repository
git clone https://github.com/user/repo.git

# Push changes
git push origin main

# Pull changes
git pull origin main
```

### Essential Commands

| Command | Description |
|---------|-------------|
| `git init` | Initialize new repository |
| `git clone <url>` | Copy remote repository |
| `git add <file>` | Stage file for commit |
| `git commit -m "msg"` | Commit staged changes |
| `git push` | Upload to remote |
| `git pull` | Download from remote |
| `git branch` | List/create branches |
| `git checkout <branch>` | Switch branches |
| `git merge <branch>` | Merge branches |

---

## Virtual Environments

Isolate project dependencies to avoid conflicts.

### Why Use Virtual Environments?

```
Project A needs: numpy 1.21, pandas 1.3
Project B needs: numpy 1.24, pandas 2.0

Without venv: Conflict!
With venv: Each project has its own packages
```

### Using `venv` (Built-in)

```bash
# Create virtual environment
python -m venv myenv

# Activate
# macOS/Linux:
source myenv/bin/activate

# Windows:
myenv\Scripts\activate

# Install packages (isolated)
pip install numpy pandas

# Deactivate
deactivate
```

### Using Conda

```bash
# Create environment
conda create -n myenv python=3.11

# Activate
conda activate myenv

# Install packages
conda install numpy pandas

# Deactivate
conda deactivate

# List environments
conda env list
```

### Project Structure

```
my_project/
├── venv/               # Virtual environment (don't commit)
├── src/
│   └── main.py
├── requirements.txt    # Dependencies
├── .gitignore          # Ignore venv/
└── README.md
```

### requirements.txt

```bash
# Generate
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt
```

Example `requirements.txt`:
```
numpy==1.24.0
pandas==2.0.0
matplotlib==3.7.0
```

---

## Code Quality Tools

### Linting: Pylint / Flake8

```bash
pip install pylint flake8

pylint my_script.py
flake8 my_script.py
```

### Formatting: Black

```bash
pip install black

black my_script.py      # Auto-format
```

### Type Checking: mypy

```bash
pip install mypy

mypy my_script.py       # Check type hints
```

---

## Recommended Setup

| Tool | Purpose |
|------|---------|
| VS Code | Editor/IDE |
| Git + GitHub | Version control |
| venv or Conda | Virtual environments |
| Black | Code formatting |
| Pylint | Linting |

```bash
# Quick project setup
mkdir my_project && cd my_project
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install black pylint
git init
echo "venv/" > .gitignore
```

---

## Key Takeaways

- **VS Code** or **PyCharm** for local development
- **Google Colab** or **Kaggle** for quick experiments with GPU
- **Git/GitHub** for version control — learn the basics early
- **Virtual environments** isolate dependencies — always use them
- **Black + Pylint** for clean, consistent code
