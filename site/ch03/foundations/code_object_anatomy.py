"""
Code Object Anatomy: Bytecode, co_* Attributes, and Disassembly

Every function in Python is compiled into a code object that the
CPython virtual machine executes. This tutorial explores code object
attributes, manual bytecode decoding, and the line number table.

Topics covered:
1. Code object attributes (co_argcount, co_varnames, co_cellvars, etc.)
2. Manual bytecode decoding from co_code
3. Line number table (co_lnotab) mapping
4. Nested code objects (closures)
5. Code object flags (co_flags)
6. Comparing code objects across functions

Based on CPython-Internals Interpreter/code/code.md examples.
"""

import dis
import opcode
import types


# =============================================================================
# 1. Code Object Attributes Overview
# =============================================================================

def demo_code_attributes():
    """Explore all major attributes of a code object.

    Access a function's code object via func.__code__.
    """
    print("=== Code Object Attributes ===\n")

    def example(x, y, *args, z=3, **kwargs):
        """Function with diverse parameter types."""
        def inner():
            inner_local = 4
            print(x, k, inner_local)
        k = 4
        print(x, y, args, kwargs)

    code = example.__code__

    attrs = [
        ('co_name',           'Function name'),
        ('co_argcount',       'Positional arg count (excludes *args, **kwargs)'),
        ('co_kwonlyargcount', 'Keyword-only arg count'),
        ('co_nlocals',        'Total local variables'),
        ('co_stacksize',      'Max stack depth needed'),
        ('co_flags',          'Flags bitmap (see section 5)'),
        ('co_firstlineno',    'First line number in source'),
        ('co_varnames',       'Local variable names (params first)'),
        ('co_cellvars',       'Variables also used in nested functions'),
        ('co_freevars',       'Variables from enclosing scope'),
        ('co_consts',         'Constants used (including nested code objects)'),
        ('co_names',          'Names used (globals, attributes)'),
        ('co_filename',       'Source filename'),
    ]

    for attr, description in attrs:
        val = getattr(code, attr)
        print(f"  {attr:25s} = {val!r}")
        print(f"  {'':25s}   # {description}")
        print()


# =============================================================================
# 2. Manual Bytecode Decoding
# =============================================================================

def demo_bytecode_decoding():
    """Decode raw bytecode (co_code) into human-readable instructions.

    CPython bytecode uses 2-byte instructions: opcode + argument.
    Opcodes >= HAVE_ARGUMENT (90) use the argument byte.
    Opcodes < 90 ignore the argument byte.
    """
    print("=== Manual Bytecode Decoding ===\n")

    def add(a, b):
        return a + b

    code = add.__code__
    raw = code.co_code
    print(f"Raw co_code bytes: {raw!r}")
    print(f"As integers: {list(raw)}")
    print()

    # Decode manually
    print("Manual decode:")
    print(f"  {'Offset':>6}  {'Opcode':>6}  {'Arg':>4}  {'Name':<20}  Detail")
    print(f"  {'------':>6}  {'------':>6}  {'----':>4}  {'----':<20}  ------")

    i = 0
    while i < len(raw):
        op = raw[i]
        arg = raw[i + 1] if i + 1 < len(raw) else 0
        name = opcode.opname[op]

        detail = ""
        if op >= opcode.HAVE_ARGUMENT:
            if op in opcode.hasconst:
                detail = f"({code.co_consts[arg]!r})"
            elif op in opcode.haslocal:
                detail = f"({code.co_varnames[arg]})"
            elif op in opcode.hasname:
                detail = f"({code.co_names[arg]})"
        else:
            arg = None  # type: ignore[assignment]

        print(f"  {i:>6}  {op:>6}  {str(arg):>4}  {name:<20}  {detail}")
        i += 2

    # Compare with dis output
    print(f"\ndis.dis() output for verification:")
    dis.dis(add)
    print()


# =============================================================================
# 3. Line Number Table (co_lnotab)
# =============================================================================

def demo_lnotab():
    """Decode co_lnotab: maps bytecode offsets to source line numbers.

    co_lnotab is a sequence of (bytecode_increment, line_increment) pairs.
    Starting from co_firstlineno, accumulate increments to find which
    source line each bytecode offset corresponds to.
    """
    print("=== Line Number Table (co_lnotab) ===\n")

    def multi_line(x):
        x = 3
        y = 4
        z = x + y
        return z

    code = multi_line.__code__
    lnotab = list(code.co_lnotab)

    print(f"co_firstlineno: {code.co_firstlineno}")
    print(f"co_lnotab bytes: {lnotab}")
    print()

    # Decode the table
    print("Decoded line number table:")
    print(f"  {'Byte offset':>12}  {'Source line':>12}")
    print(f"  {'----------':>12}  {'----------':>12}")

    byte_offset = 0
    line_number = code.co_firstlineno
    print(f"  {byte_offset:>12}  {line_number:>12}  (start)")

    for i in range(0, len(lnotab), 2):
        byte_incr = lnotab[i]
        line_incr = lnotab[i + 1]
        byte_offset += byte_incr
        line_number += line_incr
        print(f"  {byte_offset:>12}  {line_number:>12}  "
              f"(+{byte_incr} bytes, +{line_incr} lines)")

    # Compare with dis output
    print(f"\ndis.dis() for verification:")
    dis.dis(multi_line)
    print()


# =============================================================================
# 4. Nested Code Objects (Closures)
# =============================================================================

def demo_nested_code_objects():
    """Nested functions create child code objects stored in co_consts.

    co_cellvars: variables captured BY nested functions (in the outer).
    co_freevars: variables FROM enclosing scope (in the inner).
    """
    print("=== Nested Code Objects (Closures) ===\n")

    def outer(x):
        k = 10
        def inner():
            return x + k
        return inner

    outer_code = outer.__code__

    print(f"outer() code object:")
    print(f"  co_varnames:  {outer_code.co_varnames}")
    print(f"  co_cellvars:  {outer_code.co_cellvars}")
    print(f"  co_freevars:  {outer_code.co_freevars}")
    print()

    # Find inner's code object in co_consts
    inner_code = None
    for const in outer_code.co_consts:
        if isinstance(const, types.CodeType):
            inner_code = const
            break

    if inner_code:
        print(f"inner() code object (found in outer.co_consts):")
        print(f"  co_name:      {inner_code.co_name}")
        print(f"  co_varnames:  {inner_code.co_varnames}")
        print(f"  co_cellvars:  {inner_code.co_cellvars}")
        print(f"  co_freevars:  {inner_code.co_freevars}")
        print()
        print("  Note: inner.co_freevars matches outer.co_cellvars")
        print("  This is how closures capture variables from enclosing scope.")
    print()


# =============================================================================
# 5. Code Object Flags (co_flags)
# =============================================================================

def demo_code_flags():
    """co_flags is a bitmap encoding function properties.

    Common flags (from Include/cpython/code.h):
      0x01  CO_OPTIMIZED     — uses fast locals
      0x02  CO_NEWLOCALS     — creates new locals dict
      0x04  CO_VARARGS       — has *args
      0x08  CO_VARKEYWORDS   — has **kwargs
      0x20  CO_GENERATOR     — is a generator function
      0x40  CO_NOFREE        — no free/cell variables
      0x100 CO_COROUTINE     — is an async function
      0x200 CO_ITERABLE_COROUTINE
    """
    print("=== Code Object Flags ===\n")

    flag_names = {
        0x01:  'CO_OPTIMIZED',
        0x02:  'CO_NEWLOCALS',
        0x04:  'CO_VARARGS',
        0x08:  'CO_VARKEYWORDS',
        0x20:  'CO_GENERATOR',
        0x40:  'CO_NOFREE',
        0x100: 'CO_COROUTINE',
    }

    def regular(x): return x
    def with_args(*args): return args
    def with_kwargs(**kw): return kw
    def gen_func(): yield 1
    async def async_func(): pass

    functions = [
        ('regular(x)',      regular),
        ('with_args(*args)', with_args),
        ('with_kwargs(**kw)', with_kwargs),
        ('gen_func()',      gen_func),
        ('async_func()',    async_func),
    ]

    for label, func in functions:
        flags = func.__code__.co_flags
        active = [name for bit, name in sorted(flag_names.items())
                  if flags & bit]
        print(f"  {label:25s}  flags=0x{flags:04x}  {active}")
    print()


# =============================================================================
# 6. Comparing Code Objects
# =============================================================================

def demo_code_comparison():
    """Compare code objects from similar functions to see
    what changes and what stays the same.
    """
    print("=== Comparing Code Objects ===\n")

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def add_three(a, b, c):
        return a + b + c

    pairs = [
        ('add vs multiply', add.__code__, multiply.__code__),
        ('add vs add_three', add.__code__, add_three.__code__),
    ]

    compare_attrs = [
        'co_argcount', 'co_nlocals', 'co_stacksize',
        'co_varnames', 'co_code',
    ]

    for label, c1, c2 in pairs:
        print(f"  --- {label} ---")
        for attr in compare_attrs:
            v1 = getattr(c1, attr)
            v2 = getattr(c2, attr)
            match = "==" if v1 == v2 else "!="
            print(f"    {attr:20s}  {match}  "
                  f"{v1!r} vs {v2!r}")
        print()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_code_attributes()
    demo_bytecode_decoding()
    demo_lnotab()
    demo_nested_code_objects()
    demo_code_flags()
    demo_code_comparison()
