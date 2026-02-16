"""
TUTORIAL: Class Factory Using type() - Creating Classes Dynamically
===================================================================

In this tutorial, you'll learn how to create classes dynamically using the
type() builtin. Normally, type(obj) returns the type of an object, but type()
has another mode: creating new classes!

Normal usage: type(obj) → returns the class

Dynamic creation: type(name, bases, dict) → creates a NEW class

The three arguments to type():
  1. name (str): The name of the new class
  2. bases (tuple): Parent classes (can be empty for object)
  3. dict (dict): Class attributes and methods

Why create classes dynamically?
  - Build flexible frameworks where classes are generated at runtime
  - Reduce boilerplate when creating many similar classes
  - Generate specialized classes based on data or configuration
  - Create classes from strings (parsing, serialization)

In this example:
  - record_factory() creates classes dynamically using type()
  - These classes are tuples with named fields and custom methods
  - They demonstrate the full power of runtime class creation

Key insight: Classes are objects too! You can create them, modify them,
and pass them around just like any other Python object.
"""

from typing import Union, Any
from collections.abc import Iterable, Iterator


# ============ Example 1: Understanding type() for Class Creation ============
print("=" * 70)
print("EXAMPLE 1: Creating classes with type()")
print("=" * 70)

# The type() builtin has two modes:
print(f"\nMode 1: type(obj) returns the class of obj")
print(f"  type(42) = {type(42)}")
print(f"  type('hello') = {type('hello')}")
print(f"  type([1, 2, 3]) = {type([1, 2, 3])}")

print(f"\nMode 2: type(name, bases, dict) creates a NEW class")
print(f"  MyClass = type('MyClass', (), {{}})")
print(f"  Creates: a class named MyClass with no parents and no attributes")

# Create a simple class dynamically
MyClass = type('MyClass', (), {})
print(f"\nMyClass = {MyClass}")
print(f"  Type: {type(MyClass)}")
print(f"  Instance: {MyClass()}")


# ============ Example 2: Adding Attributes and Methods ============
print("\n" + "=" * 70)
print("EXAMPLE 2: Adding methods to dynamically created classes")
print("=" * 70)

def say_hello(self):
    """A method to add to the class."""
    return f'Hello from {self.__class__.__name__}'

def __init__(self, name):
    """An initializer for the class."""
    self.name = name

def __repr__(self):
    """String representation."""
    return f'{self.__class__.__name__}(name={self.name!r})'

# Create a class with methods
Greeter = type('Greeter',
               (),
               {'__init__': __init__,
                'say_hello': say_hello,
                '__repr__': __repr__,
                'class_var': 'I am a class variable'})

print(f"\nGreeter = type('Greeter', (), {{'__init__': ..., 'say_hello': ..., ...}})")
print(f"\nCreated class: {Greeter}")
print(f"Class variable: {Greeter.class_var}")

greeter = Greeter('Alice')
print(f"\ngreeter = Greeter('Alice')")
print(f"  greeter.name = '{greeter.name}'")
print(f"  repr(greeter) = {repr(greeter)}")
print(f"  greeter.say_hello() = '{greeter.say_hello()}'")


# ============ Example 3: The record_factory() Function ============
print("\n" + "=" * 70)
print("EXAMPLE 3: Practical example - record_factory()")
print("=" * 70)

FieldNames = Union[str, Iterable[str]]

def record_factory(cls_name: str, field_names: FieldNames) -> type[tuple]:
    """Create a class for holding data, like a namedtuple.

    This factory function dynamically creates classes that:
    1. Store data efficiently using __slots__
    2. Support unpacking (for x, y in records)
    3. Have a nice __repr__ for debugging
    4. Accept both positional and keyword arguments

    Args:
        cls_name: The name for the new class.
        field_names: Field names as a string ('name age') or iterable.

    Returns:
        A new class that can be instantiated with the given fields.
    """

    slots = parse_identifiers(field_names)

    def __init__(self, *args, **kwargs) -> None:
        """Initialize instance, accepting positional and keyword args."""
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self) -> Iterator[Any]:
        """Allow unpacking of the instance (for x, y in instances)."""
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        """Return a nice representation like: Dog(name='Rex', weight=30)."""
        values = ', '.join(f'{name}={value!r}'
            for name, value in zip(self.__slots__, self))
        cls_name_local = self.__class__.__name__
        return f'{cls_name_local}({values})'

    # Prepare the class attributes dictionary
    cls_attrs = dict(
        __slots__=slots,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__,
    )

    # Create and return the class using type()
    return type(cls_name, (object,), cls_attrs)


def parse_identifiers(names: FieldNames) -> tuple[str, ...]:
    """Parse field names from string or iterable.

    Args:
        names: Either a string like 'name age weight' or a list/tuple.

    Returns:
        Tuple of validated identifier strings.

    Raises:
        ValueError: If any name is not a valid Python identifier.
    """
    if isinstance(names, str):
        names = names.replace(',', ' ').split()
    if not all(s.isidentifier() for s in names):
        raise ValueError('names must all be valid identifiers')
    return tuple(names)


print(f"\nrecord_factory() creates data classes using type()")
print(f"\nSignature: record_factory(cls_name, field_names) -> class")
print(f"\nExample: Dog = record_factory('Dog', 'name weight owner')")


# ============ Example 4: Using the Created Classes ============
print("\n" + "=" * 70)
print("EXAMPLE 4: Creating and using classes from record_factory()")
print("=" * 70)

# Create a Dog class
Dog = record_factory('Dog', 'name weight owner')

print(f"\nDog = record_factory('Dog', 'name weight owner')")
print(f"  Created: {Dog}")
print(f"  Fields (__slots__): {Dog.__slots__}")

# Create instances
rex = Dog('Rex', 30, 'Bob')
buddy = Dog('Buddy', 25, 'Alice')

print(f"\nrex = Dog('Rex', 30, 'Bob')")
print(f"  repr(rex) = {repr(rex)}")

print(f"\nbuddy = Dog('Buddy', 25, 'Alice')")
print(f"  repr(buddy) = {repr(buddy)}")

print(f"\nAccessing attributes:")
print(f"  rex.name = '{rex.name}'")
print(f"  rex.weight = {rex.weight}")
print(f"  rex.owner = '{rex.owner}'")


# ============ Example 5: Unpacking and Iteration ============
print("\n" + "=" * 70)
print("EXAMPLE 5: Unpacking and iteration support")
print("=" * 70)

print(f"\nUnpacking (like tuple unpacking):")
name, weight, owner = rex
print(f"  name, weight, owner = rex")
print(f"  name = '{name}', weight = {weight}, owner = '{owner}'")

print(f"\nIndexing (like tuple indexing):")
print(f"  rex[0] = '{rex[0]}'  (name)")
print(f"  rex[1] = {rex[1]}  (weight)")
print(f"  rex[2] = '{rex[2]}'  (owner)")

print(f"\nFormatting with unpacking:")
message = "{2}'s dog {0} weighs {1}kg"
print(f"  message = \"{message}\"")
print(f"  message.format(*rex) = '{message.format(*rex)}'")

print(f"\nIteration:")
print(f"  for value in rex:")
for i, value in enumerate(rex):
    print(f"    [{i}] = {value!r}")


# ============ Example 6: Modifying Instance Attributes ============
print("\n" + "=" * 70)
print("EXAMPLE 6: Instances are mutable (can be modified)")
print("=" * 70)

print(f"\nOriginal: rex = {repr(rex)}")

rex.weight = 32
print(f"  rex.weight = 32")
print(f"  Modified: rex = {repr(rex)}")

print(f"\nThis is different from namedtuples (immutable)")
print(f"  - record_factory classes are mutable")
print(f"  - namedtuples are immutable")
print(f"  - Both are efficient with __slots__")


# ============ Example 7: Creating with String or List ============
print("\n" + "=" * 70)
print("EXAMPLE 7: Flexible field name input")
print("=" * 70)

# Create with string
Person = record_factory('Person', 'name age city')
print(f"\nPerson = record_factory('Person', 'name age city')")
print(f"  Fields: {Person.__slots__}")

alice = Person('Alice', 30, 'NYC')
print(f"  alice = Person('Alice', 30, 'NYC')")
print(f"  repr(alice) = {repr(alice)}")

# Create with list
Product = record_factory('Product', ['id', 'name', 'price'])
print(f"\nProduct = record_factory('Product', ['id', 'name', 'price'])")
print(f"  Fields: {Product.__slots__}")

item = Product(1, 'Laptop', 999.99)
print(f"  item = Product(1, 'Laptop', 999.99)")
print(f"  repr(item) = {repr(item)}")

# Create with comma-separated string
Coordinate = record_factory('Coordinate', 'x,y,z')
print(f"\nCoordinate = record_factory('Coordinate', 'x,y,z')")
print(f"  Fields: {Coordinate.__slots__}")

point = Coordinate(10, 20, 30)
print(f"  point = Coordinate(10, 20, 30)")
print(f"  repr(point) = {repr(point)}")


# ============ Example 8: Keyword Arguments ============
print("\n" + "=" * 70)
print("EXAMPLE 8: Creating instances with keyword arguments")
print("=" * 70)

# Using positional arguments
dog1 = Dog('Max', 28, 'Charlie')
print(f"\ndog1 = Dog('Max', 28, 'Charlie')")
print(f"  {repr(dog1)}")

# Using keyword arguments
dog2 = Dog(name='Lucy', weight=24, owner='Diana')
print(f"\ndog2 = Dog(name='Lucy', weight=24, owner='Diana')")
print(f"  {repr(dog2)}")

# Using mixed positional and keyword
dog3 = Dog('Buddy', owner='Eve', weight=26)
print(f"\ndog3 = Dog('Buddy', owner='Eve', weight=26)")
print(f"  {repr(dog3)}")


# ============ Example 9: Why Use type() for Class Creation ============
print("\n" + "=" * 70)
print("EXAMPLE 9: Why dynamically create classes with type()")
print("=" * 70)

print(f"\nBenefits of type()-based class creation:")
print(f"  1. Reduce boilerplate - don't repeat similar classes")
print(f"  2. Generate from data - create classes from strings, configs")
print(f"  3. Framework design - base frameworks on runtime class generation")
print(f"  4. Meta-programming - inspect and modify classes at runtime")

print(f"\nUse cases:")
print(f"  - ORM systems (database mapping): create model classes dynamically")
print(f"  - Data validation: generate validators from schemas")
print(f"  - API clients: generate resource classes from API specs")
print(f"  - Configuration: create classes based on config files")

print(f"\nAlternatives to type():")
print(f"  - dataclass: for data-holding classes with less boilerplate")
print(f"  - namedtuple: for immutable tuple-like classes")
print(f"  - type(): for maximum flexibility and runtime creation")


# ============ Example 10: Class Hierarchy ============
print("\n" + "=" * 70)
print("EXAMPLE 10: Classes created with type() in the hierarchy")
print("=" * 70)

print(f"\nDog.__mro__ (method resolution order):")
print(f"  {Dog.__mro__}")

print(f"\nDog class details:")
print(f"  Dog.__name__ = '{Dog.__name__}'")
print(f"  Dog.__bases__ = {Dog.__bases__}")
print(f"  Dog.__dict__ keys = {list(Dog.__dict__.keys())}")

print(f"\nInstance details:")
print(f"  rex.__class__.__name__ = '{rex.__class__.__name__}'")
print(f"  isinstance(rex, Dog) = {isinstance(rex, Dog)}")
print(f"  type(rex) = {type(rex)}")
print(f"  type(type(rex)) = {type(type(rex))}")

print(f"\nThe full chain:")
print(f"  rex is an instance of Dog")
print(f"  Dog is an instance of type (it's a class)")
print(f"  type is an instance of type (it's a metaclass)")


# ============ Example 11: Summary - Dynamic Class Creation ============
print("\n" + "=" * 70)
print("EXAMPLE 11: Summary - When and How to Use type()")
print("=" * 70)

print(f"\nThe type() function has three jobs:")
print(f"  1. type(obj) - returns the type of an object")
print(f"  2. type(name, bases, dict) - creates a new class")
print(f"  3. type as a metaclass - controls class creation")

print(f"\nCreating classes with type():")
print(f"  Syntax: NewClass = type(name, bases, attributes_dict)")
print(f"  name: String name for the class")
print(f"  bases: Tuple of parent classes (or () for object)")
print(f"  attributes_dict: Dict of methods and class variables")

print(f"\nKey benefits:")
print(f"  - Powerful for framework and library design")
print(f"  - Can generate many similar classes from data")
print(f"  - Allows runtime inspection and modification")

print(f"\nImportant notes:")
print(f"  - Classes created with type() are normal classes")
print(f"  - They work with inheritance, isinstance(), etc.")
print(f"  - __slots__ makes them memory-efficient")
print(f"  - Custom methods work just like normal classes")

print(f"\n" + "=" * 70)
