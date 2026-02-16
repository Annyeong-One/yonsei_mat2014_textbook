"""
TUTORIAL: Methods as Descriptors - Understanding the Descriptor Protocol

This tutorial reveals the magic behind Python methods. Every time you access
a method on an object, Python's descriptor protocol is at work. Functions
are actually non-data descriptors that use __get__ to bind 'self'.

Understanding this explains fundamental Python behavior: why methods work,
why 'self' is implicit, and how you can manipulate methods if needed.

Key Learning Goals:
  - See methods as descriptors (functions with __get__)
  - Understand how 'self' gets bound automatically
  - Learn the difference between bound and unbound methods
  - Understand access via instance vs class
  - See practical uses of this knowledge
"""

import collections

print("=" * 70)
print("TUTORIAL: Methods as Descriptors - The Function Protocol")
print("=" * 70)

# ============ EXAMPLE 1: Functions Are Descriptors ============
print("\n# Example 1: Functions Implement the Descriptor Protocol")
print("=" * 70)

class MyClass:
    """Simple class with a method."""

    def method(self):
        """A simple method."""
        return "method result"


print("A function object is a descriptor:")
print(f"type(MyClass.method) = {type(MyClass.method)}")
print(f"hasattr(function, '__get__') = {hasattr(MyClass.method, '__get__')}")
print()

print("When you access via instance, __get__ is called:")
obj = MyClass()
print(f"obj.method = {obj.method}")
print(f"type(obj.method) = {type(obj.method)}")
print()

print("When you access via class:")
print(f"MyClass.method = {MyClass.method}")
print(f"type(MyClass.method) = {type(MyClass.method)}")
print()

print("""
WHY: Functions are non-data descriptors:
    - They have __get__ but not __set__
    - When accessed via instance, __get__ creates a bound method
    - When accessed via class, __get__ returns the function itself
    - Instance __dict__ can shadow methods (methods aren't data descriptors)

This is the descriptor protocol in action!
""")

# ============ EXAMPLE 2: The Bound Method ============
print("\n# Example 2: Accessing Methods Creates Bound Methods")
print("=" * 70)

class Text(collections.UserString):
    """Text class with a reverse method."""

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        """Return text reversed."""
        return self[::-1]


word = Text('forward')

print(f"Original: {word}")
print()

# Access method via instance
print("Access method via instance:")
method = word.reverse
print(f"  word.reverse = {method}")
print(f"  type = {type(method)}")
print()

# Call it
result = method()
print(f"  word.reverse() = {result}")
print()

# Access method via class
print("Access method via class:")
func = Text.reverse
print(f"  Text.reverse = {func}")
print(f"  type = {type(func)}")
print()

# Call it with instance as argument
result = func(word)
print(f"  Text.reverse(word) = {result}")

print("""
WHY: The bound method:
    - Returned by obj.method (instance access)
    - Carries a reference to both the function and the instance
    - When called, automatically passes the instance as 'self'

The unbound function:
    - Returned by Class.method (class access)
    - Just the function, no 'self' binding
    - You must pass an instance if you call it

This is how Python makes 'self' implicit and convenient.
""")

# ============ EXAMPLE 3: How __get__ Works ============
print("\n# Example 3: Calling __get__ Directly")
print("=" * 70)

class Demo:
    def method(self):
        return f"method called on {self}"


obj = Demo()

print("The __get__ method creates the bound method:")
print(f"Demo.method.__get__(obj, Demo) = {Demo.method.__get__(obj, Demo)}")
print()

print("Calling __get__ with None instance returns unbound:")
print(f"Demo.method.__get__(None, Demo) = {Demo.method.__get__(None, Demo)}")
print()

print("The bound method carries references to function and instance:")
bound = obj.method
print(f"bound.__func__ = {bound.__func__}")
print(f"bound.__self__ = {bound.__self__}")
print(f"bound.__func__ is Demo.method = {bound.__func__ is Demo.method}")
print(f"bound.__self__ is obj = {bound.__self__ is obj}")
print()

print("You can call the bound method:")
print(f"bound() = {bound()}")

print("""
WHY: Understanding __get__ explains:
    - __func__: The actual function object
    - __self__: The instance it's bound to
    - When you call the bound method, __self__ is passed as 'self'

This is all transparent normally, but now you see the mechanism!
""")

# ============ EXAMPLE 4: Shadowing Methods ============
print("\n# Example 4: Instance Attributes Shadow Methods")
print("=" * 70)

class Shadowing:
    def method(self):
        return "class method"


obj = Shadowing()

print("Initially, call the class method:")
print(f"  obj.method() = {obj.method()}")
print()

print("Shadow it with an instance attribute:")
obj.method = lambda: "instance lambda"
print(f"  obj.method = {obj.method}")
print()

print("Now it calls the instance attribute:")
print(f"  obj.method() = {obj.method()}")
print()

print("Class still has the original:")
print(f"  Shadowing.method = {Shadowing.method}")
print(f"  Shadowing.method(obj) = {Shadowing.method(obj)}")
print()

print("Delete the instance attribute to restore:")
del obj.method
print(f"  obj.method() = {obj.method()}")

print("""
WHY: Methods are non-data descriptors:
    - Non-data means instance __dict__ can shadow them
    - Set obj.method = something, and that takes priority
    - This is unlike @property (data descriptor), which always intercepts
    - This flexibility is useful but requires care

This shows why non-data descriptors matter - methods are practical!
""")

# ============ EXAMPLE 5: Bound Method Equality ============
print("\n# Example 5: Bound Methods and Equality")
print("=" * 70)

class Data:
    def check(self):
        return True


obj1 = Data()
obj2 = Data()

print("Getting the same bound method twice:")
m1 = obj1.check
m2 = obj1.check
print(f"  m1 = obj1.check")
print(f"  m2 = obj1.check")
print(f"  m1 == m2 = {m1 == m2}")
print(f"  m1 is m2 = {m1 is m2}")  # Different objects!
print()

print("Bound methods from different instances:")
m3 = obj1.check
m4 = obj2.check
print(f"  m3 = obj1.check")
print(f"  m4 = obj2.check")
print(f"  m3 == m4 = {m3 == m4}")
print(f"  m3.__self__ is m4.__self__ = {m3.__self__ is m4.__self__}")

print("""
WHY: Bound methods are created fresh on each access:
    - obj.method doesn't cache the bound method
    - Each access calls __get__ and creates a new bound method object
    - They compare equal if they wrap the same function and instance
    - But they're not identical (different objects)

This is usually transparent, but matters if you use bound methods as dict keys.
""")

# ============ EXAMPLE 6: Using map With Methods ============
print("\n# Example 6: Practical Use - Applying Methods Across Objects")
print("=" * 70)

class Number:
    def __init__(self, value):
        self.value = value

    def squared(self):
        return self.value ** 2

    def __repr__(self):
        return f"Number({self.value})"


numbers = [Number(1), Number(2), Number(3)]

print("Using map with a method:")
print(f"numbers = {numbers}")
print()

print("Apply squared() to all:")
# This works because the unbound method can take any instance
results = list(map(Number.squared, numbers))
print(f"map(Number.squared, numbers) = {results}")
print()

print("""
WHY: This works because:
    - Number.squared is the unbound function
    - map passes each number as the first argument
    - The function is called as Number.squared(number)

You could also do:
    results = [num.squared() for num in numbers]

But using the unbound method is more elegant in some cases.
""")

# ============ EXAMPLE 7: Staticmethod and Classmethod ============
print("\n# Example 7: Other Descriptor Types - staticmethod and classmethod")
print("=" * 70)

class Demo:
    @staticmethod
    def static():
        """Static methods don't get 'self' or 'cls' binding."""
        return "static result"

    @classmethod
    def cls_method(cls):
        """Class methods get 'cls' as first argument."""
        return f"class method from {cls.__name__}"

    def instance_method(self):
        """Normal methods get 'self'."""
        return "instance method"


print("Instance method (normal):")
print(f"  Demo.instance_method = {Demo.instance_method}")
print()

print("Class method (bound to class):")
print(f"  Demo.cls_method = {Demo.cls_method}")
print(f"  Demo.cls_method() = {Demo.cls_method()}")
print()

print("Static method (no binding):")
print(f"  Demo.static = {Demo.static}")
print(f"  Demo.static() = {Demo.static()}")
print()

print("All are descriptors but work differently:")
obj = Demo()
print(f"obj.instance_method() = {obj.instance_method()}")
print(f"obj.cls_method() = {obj.cls_method()}")
print(f"obj.static() = {obj.static()}")

print("""
WHY: Python provides three method types:

1. INSTANCE METHOD (normal function)
   - Descriptor: __get__ binds self
   - Access: obj.method() or Class.method(obj)
   - Use: Most methods

2. CLASS METHOD (@classmethod)
   - Descriptor: __get__ binds cls
   - Access: obj.method() or Class.method()
   - Use: Factory methods, class-specific operations

3. STATIC METHOD (@staticmethod)
   - Not a descriptor, just a plain function wrapper
   - Access: obj.method() or Class.method()
   - Use: Utility functions in a class namespace

All are descriptors (or descriptor-like) but serve different purposes!
""")

# ============ EXAMPLE 8: Custom Descriptor Mimicking Methods ============
print("\n# Example 8: Building a Method-Like Descriptor")
print("=" * 70)

class MethodLike:
    """Descriptor that mimics method behavior."""

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func  # Accessed from class
        # Create a bound method-like object
        return lambda *args, **kwargs: self.func(obj, *args, **kwargs)


class MyClass:
    @MethodLike
    def my_method(self):
        return f"Called on {self}"


obj = MyClass()

print("Using the descriptor:")
print(f"MyClass.my_method = {MyClass.my_method}")
print(f"obj.my_method = {obj.my_method}")
print()

print("Calling the bound version:")
result = obj.my_method()
print(f"obj.my_method() = {result}")
print()

print("""
WHY: This demonstrates:
    - How to build a descriptor from scratch
    - How __get__ can return different things based on context
    - How to create a "bound method" using a lambda
    - That descriptors give you complete control over access

In practice, use @property or regular methods. This is educational!
""")

# ============ EXAMPLE 9: Summary - The Method Mechanism ============
print("\n# Example 9: Complete Picture - How Methods Work")
print("=" * 70)

print("""
THE METHOD MECHANISM - STEP BY STEP:

WHEN YOU WRITE:
    class MyClass:
        def method(self):
            pass

PYTHON CREATES:
    - A function object (the code)
    - Stores it as MyClass.method

WHEN YOU ACCESS obj.method:
    1. Python looks up 'method' in obj.__dict__ (not found)
    2. Python looks in MyClass.__dict__ (finds the function)
    3. Function is a descriptor, so calls function.__get__(obj, MyClass)
    4. __get__ returns a bound method (the function + obj + call wrapper)
    5. You get a callable bound method

WHEN YOU CALL obj.method():
    1. The bound method is callable
    2. It calls the original function with obj as the first argument
    3. That first argument is named 'self' in the function definition
    4. Everything works transparently

WHY THIS IS BRILLIANT:
    - Functions implement __get__ to enable method binding
    - No special syntax needed (no need to write obj.method(obj))
    - Class and instance access both work (different behaviors)
    - Non-data descriptor means instance __dict__ can shadow (flexibility)
    - The same mechanism is used for @property, @staticmethod, etc.

THE DESCRIPTOR PROTOCOL MAKES THIS POSSIBLE:
    - __get__(self, instance, owner)
    - instance: the object being accessed (None if via class)
    - owner: the class
    - Returns: the computed value (in this case, a bound method)

PERFORMANCE NOTE:
    - Each obj.method access calls __get__ (creates new bound method)
    - But Python optimizes this so it's very fast
    - You shouldn't cache bound methods unless you have a specific reason

WHEN YOU'D USE THIS KNOWLEDGE:
    - Understanding how Python works internally
    - Implementing custom descriptors
    - Debugging method binding issues
    - Advanced metaprogramming
    - Building frameworks and tools
""")

# ============ EXAMPLE 10: Practical Takeaway ============
print("\n# Example 10: Practical Application - Knowing This Helps")
print("=" * 70)

print("""
NOW THAT YOU KNOW METHODS ARE DESCRIPTORS:

YOU UNDERSTAND WHY:
    ✓ obj.method needs no argument but method() gets 'self'
    ✓ You can access unbound methods via Class.method
    ✓ Instance methods can be shadowed by instance attributes
    ✓ @property and @staticmethod are also descriptors
    ✓ Python's attribute access is so flexible and powerful

YOU CAN:
    ✓ Debug issues with method binding
    ✓ Write custom descriptors when needed
    ✓ Understand frameworks that use descriptors
    ✓ Know why certain patterns work
    ✓ Appreciate Python's elegance

YOU KNOW TO:
    ✓ Use methods normally (no need for manual binding)
    ✓ Not worry about __get__ in daily code
    ✓ Reach for descriptors when you need custom access control
    ✓ Read framework code with understanding

REMEMBER:
    - This is advanced knowledge
    - You probably won't write custom descriptors often
    - But understanding them makes you a better Python programmer
    - Every Python feature you use depends on this protocol
""")

print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. FUNCTIONS ARE DESCRIPTORS: Every function has __get__, making them
   descriptors that create bound methods.

2. METHODS ARE CREATED ON ACCESS: Accessing obj.method calls function.__get__
   which creates a bound method carrying both function and instance.

3. BOUND VS UNBOUND: obj.method is bound (self is fixed), Class.method is
   unbound (you must pass instance).

4. __GET__ DOES THE MAGIC: The function's __get__ method is what creates
   the callable bound method with 'self' implicitly available.

5. THIS IS THE DESCRIPTOR PROTOCOL: Understanding __get__ and __set__ explains
   how Python implements methods, properties, and more.

6. NON-DATA DESCRIPTORS: Since functions don't have __set__, instance __dict__
   can shadow them (unlike @property).

7. METHODS ARE FLEXIBLE: You can replace them with instance attributes, call
   unbound versions, use them with map(), etc.

8. THIS EXTENDS BEYOND METHODS: The same mechanism powers @property,
   @staticmethod, @classmethod, and custom descriptors.

9. PYTHON'S ELEGANCE: All of Python's method magic boils down to a simple
   protocol (__get__, __set__, __delete__).

10. DEEP UNDERSTANDING: Knowing this puts you in the top tier of Python
    programmers who truly understand how the language works.

FINAL THOUGHT:
The beauty of Python's descriptor protocol is that it unifies behavior
that would require special-casing in other languages. One simple protocol
handles methods, properties, static methods, and more.
""")
