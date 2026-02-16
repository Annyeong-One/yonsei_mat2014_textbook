"""
TUTORIAL: Single Dispatch - Type-Based Function Polymorphism

This tutorial covers functools.singledispatch, a powerful decorator that enables
FUNCTION OVERLOADING based on the type of the first argument.

The Problem: In Python, we often need to handle the same operation differently
depending on the type of data. You could write a giant if/elif/else chain, but
that's ugly and hard to extend.

The Solution: @singledispatch lets you define a generic function, then register
type-specific implementations. When called, Python automatically dispatches to
the right implementation based on the argument type.

This is elegant, extensible, and Pythonic. The htmlize function demonstrates
this perfectly - one function that handles strings, lists, numbers, fractions,
and more, each with custom formatting.
"""

from functools import singledispatch
from collections import abc
import fractions
import decimal
import html
import numbers

print("=" * 70)
print("TUTORIAL: Single Dispatch - Type-Based Function Polymorphism")
print("=" * 70)

# ============ EXAMPLE 1: The Problem Without Singledispatch
print("\n# ============ EXAMPLE 1: The Problem Without Singledispatch")
print("Why we need singledispatch - handling multiple types with if/elif:\n")


def htmlize_bad(obj):
    """Convert any object to HTML - WITHOUT singledispatch"""
    if isinstance(obj, str):
        # For strings, escape HTML and preserve newlines
        content = html.escape(obj).replace('\n', '<br/>\n')
        return f'<p>{content}</p>'
    elif isinstance(obj, abc.Sequence):
        # For sequences, create a list with each item htmlized
        inner = '</li>\n<li>'.join(htmlize_bad(item) for item in obj)
        return '<ul>\n<li>' + inner + '</li>\n</ul>'
    elif isinstance(obj, numbers.Integral):
        # For integers, show decimal and hex
        return f'<pre>{obj} (0x{obj:x})</pre>'
    else:
        # Default: escape the repr
        content = html.escape(repr(obj))
        return f'<pre>{content}</pre>'


print("The bad approach - giant if/elif chain:")
print("Problems:")
print("  1. Hard to read - all cases mixed together")
print("  2. Hard to extend - must modify the function itself")
print("  3. Couples types together - adding a new type means rewriting the function")
print("  4. No way for external code to add handlers")

print("\nTest the bad version:")
test_str = 'Hello\nWorld'
print(f"htmlize_bad('Hello\\nWorld') = {htmlize_bad(test_str)}")
test_list = [1, 2, 3]
print(f"htmlize_bad([1, 2, 3]) = {htmlize_bad(test_list)}")
print(f"htmlize_bad(42) = {htmlize_bad(42)}")

# ============ EXAMPLE 2: Introduction to Singledispatch
print("\n" + "=" * 70)
print("# ============ EXAMPLE 2: Introduction to Singledispatch")
print("The elegant solution - using @singledispatch:\n")

print("""
@singledispatch CREATES POLYMORPHIC FUNCTIONS

Steps:
1. Define a generic function with @singledispatch decorator
2. Register type-specific implementations with @func.register
3. When called, Python dispatches to the right implementation
4. Much cleaner than if/elif chains!

BENEFITS:
- Each type's logic is separate and focused
- Easy to add new types - just register them
- Extensible - external code can register new types
- Pythonic and elegant
- Type specialization is clear and explicit
""")


# ============ EXAMPLE 3: Basic Singledispatch Example
print("\n" + "=" * 70)
print("# ============ EXAMPLE 3: Basic Singledispatch Example")
print("Building htmlize step-by-step with singledispatch:\n")


@singledispatch
def htmlize(obj: object) -> str:
    """
    Generic function to convert any object to HTML.
    This is the BASE implementation - handles unknown types.
    """
    # For unknown types, just escape the repr
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


print("Step 1: Define the generic base function")
print(f"htmlize(42) = {htmlize(42)}")
print(f"htmlize({{1, 2, 3}}) = {htmlize({1, 2, 3})}")


@htmlize.register(str)
def _(text: str) -> str:
    """Specialized handler for strings"""
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'


print("\nStep 2: Register a handler for str")
print(f"htmlize('Hello') = {htmlize('Hello')}")
hello_world = 'Hello\nWorld'
print(f"htmlize('Hello\\nWorld') = {htmlize(hello_world)}")


@htmlize.register(abc.Sequence)
def _(seq: abc.Sequence) -> str:
    """Specialized handler for sequences (lists, tuples, etc.)"""
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print("\nStep 3: Register a handler for Sequence")
print(f"htmlize([1, 2, 3]) = {htmlize([1, 2, 3])}")
print(f"htmlize(('a', 'b')) = {htmlize(('a', 'b'))}")


@htmlize.register(numbers.Integral)
def _(n: numbers.Integral) -> str:
    """Specialized handler for integers"""
    return f'<pre>{n} (0x{n:x})</pre>'


print("\nStep 4: Register a handler for Integral")
print(f"htmlize(42) = {htmlize(42)}")
print(f"htmlize(255) = {htmlize(255)}")

# ============ EXAMPLE 4: Handling Boolean Special Case
print("\n" + "=" * 70)
print("# ============ EXAMPLE 4: Handling Boolean Special Case")
print("Important: bool is a subtype of int, handle it separately:\n")

print("""
GOTCHA: In Python, bool is a subclass of int!
  isinstance(True, int) -> True
  isinstance(True, bool) -> True

If you don't register bool, it will use the int handler:
  htmlize(True) -> '<pre>1 (0x1)</pre>'  <- WRONG!

Solution: Register bool specifically, it takes precedence.
""")


@htmlize.register(bool)
def _(b: bool) -> str:
    """Specialized handler for booleans (registered AFTER int handler)"""
    return f'<pre>{b}</pre>'


print("Testing boolean handler:")
print(f"htmlize(True) = {htmlize(True)}")
print(f"htmlize(False) = {htmlize(False)}")
print(f"htmlize(42) = {htmlize(42)}")
print("Note: bool handler takes precedence over int handler!")

# ============ EXAMPLE 5: Registering With Explicit Types
print("\n" + "=" * 70)
print("# ============ EXAMPLE 5: Registering With Explicit Types")
print("Alternative syntax using explicit type arguments:\n")

print("""
TWO WAYS TO REGISTER:

Method 1 (type annotation in function signature):
  @htmlize.register(str)
  def _(text: str) -> str:
      ...

Method 2 (explicit type as argument):
  @htmlize.register(fractions.Fraction)
  def _(x) -> str:
      ...

Both work! Use whichever is clearer.
""")


@htmlize.register(fractions.Fraction)
def _(x) -> str:
    """Specialized handler for fractions"""
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'


print("Testing fraction handler:")
result = htmlize(fractions.Fraction(2, 3))
print(f"htmlize(Fraction(2, 3)) = {result}")

# ============ EXAMPLE 6: Registering Multiple Types to Same Handler
print("\n" + "=" * 70)
print("# ============ EXAMPLE 6: Registering Multiple Types to Same Handler")
print("Decorating one handler for multiple types:\n")

print("""
Sometimes you want the SAME handler for multiple types.
You can stack @register decorators on a single function.

Example: float and decimal.Decimal should both show with fractions
""")


@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    """Specialized handler for floats and decimals"""
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'


print("Testing float and decimal handlers:")
print(f"htmlize(2/3) = {htmlize(2/3)}")
print(f"htmlize(0.6666666666666666) = {htmlize(0.6666666666666666)}")
print(f"htmlize(Decimal('0.02380952')) = {htmlize(decimal.Decimal('0.02380952'))}")

# ============ EXAMPLE 7: Complete htmlize Example
print("\n" + "=" * 70)
print("# ============ EXAMPLE 7: Complete htmlize Example")
print("Using the complete htmlize function:\n")

examples = [
    42,
    'Hello & goodbye',
    ['apple', 10, {3, 2, 1}],
    True,
    fractions.Fraction(2, 3),
    2/3,
    decimal.Decimal('0.02380952'),
    {1, 2, 3},
]

print("Testing htmlize with various types:\n")
for obj in examples:
    result = htmlize(obj)
    print(f"htmlize({obj!r})")
    print(f"  -> {result}\n")

# ============ EXAMPLE 8: Understanding Dispatch Rules
print("\n" + "=" * 70)
print("# ============ EXAMPLE 8: Understanding Dispatch Rules")
print("How Python decides which handler to call:\n")

print("""
DISPATCH ALGORITHM:
1. Check the type of the first argument
2. If exact match in registered types, use that handler
3. Otherwise, check the MRO (Method Resolution Order)
4. Use the most specific handler in the MRO
5. If no match, use the @singledispatch base function

EXAMPLE MRO FOR bool:
  bool -> int -> numbers.Integral -> numbers.Number -> object

If you register handlers for:
  - bool: calls bool handler
  - int: calls int handler (if bool not registered)
  - numbers.Integral: calls Integral handler (if bool/int not registered)
  - object: calls base handler (default)

WHY THIS MATTERS:
Register specific types AFTER general types. The most specific handler wins.
But the order of decorator application doesn't matter - dispatch is by type.
""")

# ============ EXAMPLE 9: Introspection - Exploring Registered Types
print("\n" + "=" * 70)
print("# ============ EXAMPLE 9: Introspection - Exploring Registered Types")
print("Discovering what types are registered:\n")

print("The dispatch registry is accessible as htmlize.registry:")
print(f"Type(s): {type(htmlize.registry)}")
print(f"Registered types: {list(htmlize.registry.keys())}")

print("\nFor each type, you can get the handler:")
print(f"Handler for str: {htmlize.register(str)}")
print(f"Handler for list: {htmlize.register(abc.Sequence)}")

print("\nCheck if a type has a handler:")
print(f"str in registry: {str in htmlize.registry}")
print(f"int in registry: {int in htmlize.registry}")

# ============ EXAMPLE 10: Real-World Use Case - Data Serialization
print("\n" + "=" * 70)
print("# ============ EXAMPLE 10: Real-World Use Case - Data Serialization")
print("Using singledispatch for type-based serialization:\n")


@singledispatch
def serialize(obj):
    """Serialize any Python object to a JSON-compatible format"""
    raise TypeError(f"Cannot serialize {type(obj).__name__}")


@serialize.register(str)
def _(s: str):
    return s


@serialize.register(int)
def _(i: int):
    return i


@serialize.register(float)
def _(f: float):
    return f


@serialize.register(list)
def _(lst: list):
    return [serialize(item) for item in lst]


@serialize.register(dict)
def _(d: dict):
    return {k: serialize(v) for k, v in d.items()}


@serialize.register(tuple)
def _(t: tuple):
    return [serialize(item) for item in t]


print("Serialization examples:")
data = {
    'name': 'Alice',
    'age': 30,
    'scores': [85.5, 92.0, 78.5],
    'tags': ('python', 'programming'),
}

print(f"Original: {data}")
result = serialize(data)
print(f"Serialized: {result}")

# ============ EXAMPLE 11: When to Use Singledispatch
print("\n" + "=" * 70)
print("# ============ EXAMPLE 11: When to Use Singledispatch")
print("Best practices and patterns:\n")

print("""
WHEN TO USE @singledispatch:

✓ When you need type-based behavior variation
  - Different processing for different types
  - Format, convert, validate based on type

✓ When you want clean, extensible code
  - Add new types without modifying existing code
  - Each type handler is self-contained
  - External code can register new types

✓ When you need to avoid if/elif chains
  - More Pythonic and readable
  - Type specialization is explicit

EXAMPLES:
- Format/serialize different types differently
- Visitor pattern without visitor classes
- Type-specific validation
- Rendering/display by type
- Database operations by type


WHEN NOT TO USE:

✗ When you need multiple dispatch (multiple argument types matter)
  - Use multipledispatch library instead
  - Or use method dispatch on an object

✗ When a simple isinstance check is sufficient
  - If you only handle 2-3 types, if/else might be clearer

✗ When you need class method dispatch
  - Use @functools.singledispatchmethod instead (Python 3.8+)

CAUTION: singledispatch dispatches on FIRST ARGUMENT ONLY
If you need to dispatch on other arguments, use multipledispatch or another pattern.
""")

# ============ EXAMPLE 12: Common Gotchas
print("\n" + "=" * 70)
print("# ============ EXAMPLE 12: Common Gotchas")
print("Things to watch out for:\n")

print("""
GOTCHA 1: Order of registration matters for subtypes
  bool is a subclass of int. Register bool AFTER int for correct dispatch.

GOTCHA 2: Only the first argument is checked
  @singledispatch only looks at type of first argument.
  For other arguments, use isinstance checks inside the handler.

GOTCHA 3: Non-registered types don't error by default
  They use the base @singledispatch function.
  If you want strict typing, raise TypeError in the base function.

GOTCHA 4: Registering abstract types catches subtypes
  @htmlize.register(abc.Sequence) catches list, tuple, str, etc.
  This is powerful but can be surprising!

GOTCHA 5: Can't override a registered type at runtime
  Once registered, the handler is locked in.
  You can't change it or unregister it.
  (Well, you can access registry.register() but it's not recommended)
""")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
KEY TAKEAWAYS:

1. @singledispatch ENABLES TYPE-BASED FUNCTION POLYMORPHISM
   One generic function, multiple type-specific implementations.

2. BASIC PATTERN:
   @singledispatch
   def func(obj): ...          # Generic implementation

   @func.register(TypeA)
   def _(obj: TypeA): ...      # Type-specific handler A

   @func.register(TypeB)
   def _(obj: TypeB): ...      # Type-specific handler B

3. DISPATCH RULES:
   - Check exact type match first
   - If not found, check MRO (Method Resolution Order)
   - Use most specific match
   - Fall back to base @singledispatch if no match

4. BENEFITS:
   - Cleaner than if/elif chains
   - Extensible - add types without modifying function
   - Type specialization is explicit and clear
   - Pythonic and elegant

5. IMPORTANT POINTS:
   - Only first argument is checked
   - All type handlers are separate functions
   - Subtypes are handled via MRO
   - Order matters for subtypes (e.g., bool vs int)
   - Use @func.register(Type) or type annotations

6. PRACTICAL USES:
   - Format/serialize by type
   - Render/display by type
   - Validate by type
   - Process data differently per type
   - Extensible visitor patterns

7. WHEN TO USE:
   - Type-based behavior variation
   - Want clean, extensible code
   - Avoiding complex if/elif chains
""")
