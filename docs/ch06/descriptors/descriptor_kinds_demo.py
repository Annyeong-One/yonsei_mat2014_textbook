"""
TUTORIAL: Data vs Non-Data Descriptors - The Descriptor Protocol

This advanced tutorial teaches you about Python's descriptor protocol using
__get__ and __set__ dunder methods. Descriptors are the mechanism behind
properties, methods, and other magical attribute access in Python.

You'll learn the difference between data descriptors (with __set__) and
non-data descriptors (only __get__), and how Python's attribute lookup
order works.

This is advanced but essential for understanding Python's internals.

Key Learning Goals:
  - Understand the descriptor protocol (__get__ and __set__)
  - Learn the difference between data and non-data descriptors
  - Understand attribute lookup order in Python
  - See how methods work as non-data descriptors
  - Know when to use descriptors
"""

print("=" * 70)
print("TUTORIAL: Descriptors - Data vs Non-Data Descriptors")
print("=" * 70)

# ============ EXAMPLE 1: What Are Descriptors? ============
print("\n# Example 1: Introduction to Descriptors")
print("=" * 70)

print("""
DEFINITION: A descriptor is an object that implements __get__ and/or __set__
and/or __delete__ dunder methods. When you access an attribute, Python
checks if it's a descriptor and calls the appropriate method.

SIMPLE EXAMPLE:
    class Descriptor:
        def __get__(self, obj, objtype=None):
            print("__get__ called!")
            return "descriptor value"

    class MyClass:
        x = Descriptor()

    obj = MyClass()
    obj.x  # Calls Descriptor.__get__()

IMPORTANT DISTINCTION:

    DATA DESCRIPTOR: Has __set__ (and/or __delete__)
        - Takes priority over instance __dict__
        - Even if instance has an attribute with the same name

    NON-DATA DESCRIPTOR: Only has __get__
        - Instance __dict__ can "shadow" it
        - Instance attribute takes priority
        - Methods are non-data descriptors

This is why you can't accidentally override instance attributes when
properties (data descriptors) are used - the property always intercepts.
""")

# ============ EXAMPLE 2: Attribute Lookup Order ============
print("\n# Example 2: Python's Attribute Lookup Order")
print("=" * 70)

print("""
When you access obj.name, Python looks in this order:

    1. DATA DESCRIPTOR on the class and its bases
       (descriptor with __set__)
    2. Instance __dict__
       (attributes specific to this object)
    3. NON-DATA DESCRIPTOR on the class and its bases
       (descriptor with only __get__)
    4. Class attributes that aren't descriptors
    5. __getattr__() if defined

This order is why data descriptors (like @property) override instance
attributes. They're checked first!

Example:
    class Managed:
        x = DataDescriptor()
        y = NonDataDescriptor()
        z = "plain_attribute"

    obj = Managed()
    obj.__dict__['x'] = "instance"
    obj.__dict__['y'] = "instance"
    obj.__dict__['z'] = "instance"

    obj.x  # DataDescriptor (lookup #1)
    obj.y  # "instance" (lookup #2 - instance dict wins!)
    obj.z  # "instance" (lookup #2)
""")

# ============ EXAMPLE 3: Data Descriptor (with __set__) ============
print("\n# Example 3: Data Descriptor - Taking Priority")
print("=" * 70)

# Helper functions for display
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


class Overriding:
    """
    A data descriptor (has __set__).

    This is a "data descriptor" because it defines __set__.
    It overrides instance attributes - always takes priority.
    """

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class Managed:
    over = Overriding()


obj = Managed()

print("Accessing via instance (calls __get__):")
obj.over
print()

print("Accessing via class (calls __get__ with instance=None):")
Managed.over
print()

print("Setting via instance (calls __set__):")
obj.over = 7
print()

print("Accessing again (still calls __get__, not the stored value!):")
obj.over
print()

print("Even if we force a value into __dict__:")
obj.__dict__['over'] = 8
print(f"Instance __dict__: {obj.__dict__}")
print()

print("The descriptor still wins:")
obj.over  # Still calls __get__!

print("""
WHY: Data descriptors (with __set__) are checked FIRST in attribute
lookup. They take priority even over instance __dict__. This is how
@property works - it's a data descriptor.

Use case: When you want to ensure code always runs (properties,
validators, computed attributes).
""")

# ============ EXAMPLE 4: Non-Data Descriptor (only __get__) ============
print("\n# Example 4: Non-Data Descriptor - Instance Dict Wins")
print("=" * 70)


class NonOverriding:
    """
    A non-data descriptor (only __get__, no __set__).

    Instance __dict__ can "shadow" this descriptor.
    Instance attributes take priority.
    """

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    non_over = NonOverriding()


obj = Managed()

print("Accessing via instance (calls __get__):")
obj.non_over
print()

print("Setting an instance attribute (stores in __dict__):")
obj.non_over = 7
print()

print("Now accessing returns the instance value (no __get__):")
print(f"obj.non_over = {obj.non_over}")
print()

print("Accessing via class still calls __get__:")
Managed.non_over
print()

print("Delete the instance attribute:")
del obj.non_over
print()

print("Now __get__ is called again:")
obj.non_over

print("""
WHY: Non-data descriptors (only __get__) are checked AFTER instance
__dict__. If instance has an attribute, it wins.

Use case: Methods are non-data descriptors. That's why you can store
a different object in instance.__dict__ with the same name.
""")

# ============ EXAMPLE 5: Methods Are Non-Data Descriptors ============
print("\n# Example 5: Methods - The Most Important Non-Data Descriptor")
print("=" * 70)


class Demo:
    def method(self):
        print(f"  method() called on {self}")


obj = Demo()

print("Accessing a method via instance:")
print(f"obj.method = {obj.method}")
print()

print("Accessing via class:")
print(f"Demo.method = {Demo.method}")
print()

print("Notice the difference:")
print(f"  obj.method is a BOUND method")
print(f"  Demo.method is a FUNCTION")
print()

print("The function's __get__ descriptor creates the bound method:")
bound_method = Demo.method.__get__(obj, Demo)
print(f"Demo.method.__get__(obj, Demo) = {bound_method}")
print()

print("Call the bound method:")
bound_method()
print()

print("Call the unbound method via class:")
print("Demo.method(obj):")
Demo.method(obj)
print()

print("You can override the method in instance __dict__:")
obj.method = lambda: print("  Overridden method!")
print(f"obj.method = {obj.method}")
obj.method()
print()

print("""
WHY: Methods are non-data descriptors. The function object's __get__
method binds 'self' to create a callable method.

When you do obj.method, Python:
    1. Looks in instance __dict__ (finds the lambda)
    2. Returns it directly (no descriptor protocol)

If you hadn't overridden in instance __dict__:
    1. Looks in class (finds the function)
    2. Calls function.__get__(obj, Demo)
    3. Returns a bound method

This is why you can shadow methods with instance attributes!
""")

# ============ EXAMPLE 6: Practical Data Descriptor - Validator ============
print("\n# Example 6: Practical Use - Validator Descriptor")
print("=" * 70)


class ValidatedAttribute:
    """
    A data descriptor that validates values.

    Practical example of when you'd use __get__ and __set__.
    """

    def __init__(self, name, validator=None):
        self.name = name
        self.validator = validator or (lambda x: True)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self  # Accessed from class, return descriptor itself
        return obj.__dict__.get(self.name, None)

    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"{self.name} validation failed for {value}")
        obj.__dict__[self.name] = value


class User:
    # Use descriptors for validated attributes
    name = ValidatedAttribute('name', lambda x: isinstance(x, str) and len(x) > 0)
    age = ValidatedAttribute('age', lambda x: isinstance(x, int) and 0 <= x <= 150)


user = User()

print("Setting valid values:")
user.name = "Alice"
user.age = 30
print(f"user.name = {user.name}")
print(f"user.age = {user.age}")
print()

print("Trying invalid value:")
try:
    user.age = 200
except ValueError as e:
    print(f"Error: {e}")

print()
print("""
WHY: Data descriptors like ValidatedAttribute let you:
    - Run code on every attribute access
    - Validate values transparently
    - Store computed properties
    - Enforce constraints

This is the foundation for ORM frameworks (SQLAlchemy, Django ORM).
They use descriptors to track column values and changes.
""")

# ============ EXAMPLE 7: Summary - The Complete Picture ============
print("\n# Example 7: Complete Descriptor Hierarchy")
print("=" * 70)

print("""
DESCRIPTOR TYPES:

1. DATA DESCRIPTOR (has __set__ and/or __delete__)
   - Intercepts attribute setting
   - Takes priority over instance __dict__
   - Used for: @property, validators, computed attributes
   - Lookup priority: #1

2. NON-DATA DESCRIPTOR (only __get__)
   - Only intercepts attribute getting
   - Instance __dict__ can shadow it
   - Used for: methods, lazy-loading
   - Lookup priority: #3

3. ATTRIBUTE LOOKUP ORDER (obj.attr):
   #1. Data descriptor from class
   #2. Instance __dict__
   #3. Non-data descriptor from class
   #4. Class __dict__ (non-descriptor)
   #5. Bases and __getattr__()

4. DESCRIPTOR PROTOCOL METHODS:
   - __get__(self, instance, owner) -> value
   - __set__(self, instance, value) -> None
   - __delete__(self, instance) -> None

PRACTICAL IMPLICATIONS:

@property is a data descriptor:
    class X:
        @property
        def x(self):
            return self._x

    obj.__dict__['x'] = 5  # This gets ignored!
    obj.x  # Still returns property result

Methods are non-data descriptors:
    class X:
        def method(self): pass

    obj.__dict__['method'] = lambda: print("hi")
    obj.method()  # Calls the lambda (instance dict wins)

Regular attributes:
    class X:
        attr = "default"

    obj.__dict__['attr'] = "instance"
    obj.attr  # Returns instance value

WHY THIS MATTERS:

Understanding descriptors explains:
    - How properties work
    - How methods get bound to objects
    - How ORM frameworks track changes
    - How decorators can intercept access
    - The difference between class and instance attributes
    - Why some things can be overridden and others can't
""")

# ============ EXAMPLE 8: Advanced Pattern - Lazy Loading ============
print("\n# Example 8: Advanced Pattern - Lazy Loading with Descriptors")
print("=" * 70)


class LazyAttribute:
    """
    Descriptor that loads a value only on first access.

    Useful for expensive computations or resources.
    """

    def __init__(self, loader_func):
        self.loader_func = loader_func

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # First access: compute and store
        # Subsequent: return stored value
        name = self.loader_func.__name__
        value = obj.__dict__.get(name)
        if value is None:
            print(f"  [Loading {name}...]")
            value = self.loader_func(obj)
            obj.__dict__[name] = value
        return value


class WebPage:
    def __init__(self, url):
        self.url = url

    @LazyAttribute
    def content(self):
        """Simulate downloading page content."""
        print(f"    Downloading from {self.url}")
        return f"Content from {self.url}"


page = WebPage("https://example.com")

print("First access (loads):")
print(page.content)
print()

print("Second access (cached):")
print(page.content)

print("""
WHY: Lazy-loading with descriptors:
    - Defers expensive work until needed
    - Transparent to caller (looks like normal attribute)
    - Works seamlessly with ORM frameworks
    - More efficient than computing everything upfront
""")

# ============ EXAMPLE 9: Descriptor Statistics ============
print("\n# Example 9: Key Statistics to Remember")
print("=" * 70)

print("""
DESCRIPTOR CHECKLIST:

__get__(self, instance, owner)
    - Called when attribute is accessed (obj.attr)
    - instance: the object being accessed (None if via class)
    - owner: the class of the object
    - Return: the computed value
    - Every descriptor must have this

__set__(self, instance, value)
    - Called when attribute is assigned (obj.attr = value)
    - Makes this a DATA descriptor
    - Takes priority over instance __dict__
    - Optional (only for data descriptors)

__delete__(self, instance)
    - Called on del obj.attr
    - Makes this a DATA descriptor
    - Optional (rarely used)

ATTRIBUTE ACCESS RULES:

instance.attr  ->  obj.__dict__.get('attr', MISSING)
                OR descriptor.__get__(obj, type(obj))
                OR class.__dict__.get('attr', MISSING)
                OR obj.__getattribute__('attr')

obj.attr = value  ->  descriptor.__set__(obj, value)
                   OR obj.__dict__['attr'] = value

PERFORMANCE NOTES:

- Descriptors have slight overhead vs direct attribute access
- Data descriptors require __set__ lookup even for reads
- Methods (non-data descriptors) are cached by Python internally
- Properties are optimized for common access patterns
- Use descriptors for enforcing constraints, not fast loops

WHEN TO USE DESCRIPTORS:

DO:
    ✓ Validating values (@property with validator)
    ✓ Computing values (cached properties)
    ✓ Tracking access (monitoring, debugging)
    ✓ ORM mappings (SQLAlchemy-style)
    ✓ Lazy-loading (deferred computation)

DON'T:
    ✗ Simple getter/setter (use @property instead)
    ✗ Performance-critical code (too much overhead)
    ✗ Simple caching (use functools.lru_cache)
    ✗ When you don't understand them yet (learn first!)
""")

print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. DESCRIPTORS ARE THE FOUNDATION: Properties, methods, and many other
   Python features are built on descriptors.

2. __GET__ AND __SET__ ARE THE PROTOCOL: Implement these and you control
   attribute access for your objects.

3. DATA VS NON-DATA MATTERS: Data descriptors (__set__) take priority
   over instance dict. This is crucial to understand.

4. ATTRIBUTE LOOKUP HAS AN ORDER: Know the order so you understand why
   something is or isn't overrideable.

5. METHODS ARE DESCRIPTORS: Understanding methods as non-data descriptors
   explains why 'self' is bound automatically.

6. DESCRIPTORS ARE ADVANCED: You rarely write descriptors directly.
   Use @property or other tools instead.

7. FRAMEWORKS USE THEM EXTENSIVELY: ORMs, web frameworks, and validators
   all rely on descriptors internally.

8. UNDERSTAND BEFORE USING: Descriptors can be confusing. Make sure you
   understand the lookup order before implementing custom descriptors.

NEXT: Learn about metaprogramming and introspection to see how descriptors
can be used in advanced patterns like ORMs and data validation frameworks.
""")
