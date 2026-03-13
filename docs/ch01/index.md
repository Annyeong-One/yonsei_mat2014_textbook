

# Chapter 1 — Python Basics

This chapter introduces the foundations of Python programming.
It begins with installing Python and understanding the development environment, then moves through the core elements of the language:

* syntax
* control flow
* built-in functions
* data types
* functions
* collections
* exceptions
* file input/output
* modules and packages

By the end of the chapter, you will understand how Python programs are structured and how the language organizes data and behavior.

```mermaid2
flowchart TD
    A[Python Basics]

    A --> B[Getting Started]
    A --> C[Basic Syntax]
    A --> D[Control Flow]
    A --> E[Built-in Functions]
    A --> F[Data Types]
    A --> G[Functions]
    A --> H[Composite Data Types]
    A --> I[Exceptions]
    A --> J[File I/O]
    A --> K[Modules and Imports]
```

Each section builds on the previous one, gradually introducing the tools needed to write complete Python programs.

---

# 1.1 Getting Started

The chapter begins by introducing Python itself and preparing the development environment.

Topics include:

* the motivations for using Python
* installing Python on different operating systems
* development tools such as editors and IDEs
* the Python interpreter and interactive REPL

The REPL allows experimentation with Python expressions before writing full programs.

```mermaid2
flowchart LR
    A[Python Installation]
    A --> B[Development Tools]
    B --> C[Python Interpreter]
    C --> D[Interactive REPL]
```

These tools form the foundation of the programming workflow used throughout the rest of the book.

---

# 1.2 Basic Syntax

This section introduces the fundamental structure of Python programs.

Key concepts include:

* running Python scripts
* variables and objects
* basic built-in data types
* operators and expressions
* code structure and indentation

These elements form the **core syntax of the language**.

```mermaid2
flowchart TD
    A[Basic Syntax]
    A --> B[Variables]
    A --> C[Expressions]
    A --> D[Data Types]
    A --> E[Operators]
    A --> F[Readable Code Structure]
```

Understanding these concepts allows you to write simple but meaningful Python programs.

---

# 1.3 Control Flow

Programs often need to make decisions and repeat operations.

Control flow constructs determine **how execution moves through a program**.

This section covers:

* conditional statements (`if`)
* loop control (`break`, `continue`)
* loop completion (`else`)
* conditional expressions
* structural pattern matching (`match`)

```mermaid2
flowchart TD
    A[Control Flow]
    A --> B[Conditions]
    A --> C[Loops]
    A --> D[Branching Logic]
```

Control flow is essential for writing programs that respond dynamically to input and changing conditions.

---

# 1.4 Essential Built-ins

Python includes many built-in functions that simplify common programming tasks.

Examples include:

* input/output (`print`, `input`)
* sequence utilities (`len`, `range`, `enumerate`)
* aggregation (`min`, `max`, `sum`)
* logical operations (`any`, `all`)
* sorting and ordering (`sorted`, `reversed`)
* inspection tools (`help`, `dir`)

```mermaid2
flowchart TD
    A[Built-in Functions]
    A --> B[Input / Output]
    A --> C[Sequence Utilities]
    A --> D[Aggregation]
    A --> E[Inspection]
```

Built-ins provide powerful functionality without requiring external libraries.

---

# 1.5 Numeric Types

Python supports several numeric types for representing numbers.

These include:

* integers (`int`)
* floating-point numbers (`float`)
* complex numbers (`complex`)

The section also explores type conversions between numeric types.

```mermaid2
flowchart TD
    A[Numeric Types]
    A --> B[int]
    A --> C[float]
    A --> D[complex]
```

Numeric types form the basis of calculations in Python programs.

---

# 1.6 Boolean and None

This section introduces the logical foundation of Python programs.

Topics include:

* Boolean values (`True`, `False`)
* truthiness rules
* logical operators
* comparison expressions
* the special value `None`

```mermaid2
flowchart TD
    A[Logical Values]
    A --> B[Booleans]
    A --> C[Truthiness]
    A --> D[Comparisons]
    A --> E[None]
```

These concepts are central to conditions and control flow.

---

# 1.7 Strings

Strings represent textual data and are one of the most commonly used data types.

Topics include:

* string creation
* escaping and literal syntax
* indexing and slicing
* string operators
* string methods
* formatting and docstrings

```mermaid2
flowchart TD
    A[Strings]
    A --> B[Text Representation]
    A --> C[Sequence Operations]
    A --> D[String Methods]
```

Mastering strings is essential for handling text and user input.

---

# 1.8 Function Basics

Functions organize programs into reusable units of logic.

This section covers:

* defining functions
* the call stack
* parameters and return values
* type hints
* practical examples

```mermaid2
flowchart TD
    A[Functions]
    A --> B[Definition]
    A --> C[Call Stack]
    A --> D[Parameters]
    A --> E[Return Values]
```

Functions are the building blocks of structured Python programs.

---

# 1.9 Composite Data Types

Python provides several container types that store collections of values.

These include:

* tuples
* lists
* dictionaries
* sets
* comprehensions

```mermaid2
flowchart TD
    A[Composite Data Types]
    A --> B[List]
    A --> C[Tuple]
    A --> D[Dictionary]
    A --> E[Set]
```

These structures allow programs to represent complex data relationships.

---

# 1.10 Exceptions

Errors are inevitable in programming. Python uses exceptions to detect and manage errors during execution.

Topics include:

* the exception hierarchy
* common runtime errors
* exception handling (`try`, `except`, `finally`)
* raising exceptions explicitly

```mermaid2
flowchart TD
    A[Program Execution]
    A --> B{Error Occurs?}
    B -->|Yes| C[Exception Raised]
    C --> D[Handled by try/except]
```

Exception handling helps programs remain robust and predictable.

---

# 1.11 File I/O

Programs frequently interact with external data stored in files.

This section introduces:

* reading files
* writing files
* context managers (`with`)
* CSV and JSON data formats
* filesystem paths using `pathlib`

```mermaid2
flowchart TD
    A[Program]
    A --> B[Read File]
    A --> C[Write File]
    A --> D[Structured Data Formats]
```

File I/O connects Python programs to persistent data.

---

# 1.12 Modules and Imports

As programs grow larger, code is organized into modules and packages.

Topics include:

* how imports work
* the `__name__ == "__main__"` pattern
* scripts versus modules
* installing external libraries with `pip` and PyPI

```mermaid2
flowchart TD
    A[Python Program]
    A --> B[Modules]
    B --> C[Imports]
    C --> D[Packages]
```

Modules make it possible to build large programs from smaller, reusable components.

---

# Chapter Summary

This chapter established the core foundations of Python programming.

You learned:

* how to install and run Python
* the syntax and structure of Python programs
* how control flow directs execution
* how built-in functions simplify common tasks
* how Python represents data using different types
* how functions structure programs
* how composite data structures organize collections
* how exceptions manage errors
* how programs read and write files
* how modules enable code reuse

These concepts form the **essential toolkit for writing Python programs**, and they provide the foundation for more advanced topics explored in later chapters.
