"""
04_super_and_mro.py

INTERMEDIATE LEVEL: Understanding super() and its Relationship with MRO

This file provides a deep dive into how super() works with MRO in Python.
The super() function is essential for cooperative multiple inheritance and
understanding it is key to mastering MRO.

Learning Objectives:
- Understand what super() really does
- Learn the difference between super() and direct parent calls
- Master cooperative inheritance patterns
- Handle initialization chains correctly
- Debug super() issues
"""

# ============================================================================
# SECTION 1: What super() Actually Does
# ============================================================================

"""
COMMON MISCONCEPTION:
super() calls the parent class

REALITY:
super() calls the NEXT CLASS in the MRO, not necessarily the parent!

This is crucial for understanding cooperative multiple inheritance.

super() returns a proxy object that delegates method calls to the next
class in the MRO chain, starting after the current class.
"""


# ============================================================================
# SECTION 2: super() vs Direct Parent Call
# ============================================================================

class Parent:
    """Simple parent class."""
    
    def __init__(self):
        print("Parent.__init__ called")
        self.parent_value = "from parent"
    
    def method(self):
        return "Parent method"


class ChildWithSuper(Parent):
    """Child using super() - recommended way."""
    
    def __init__(self):
        print("ChildWithSuper.__init__ called")
        super().__init__()  # Calls next in MRO
        self.child_value = "from child"
    
    def method(self):
        # super() calls the next class's method in MRO
        parent_result = super().method()
        return f"Child method (parent says: {parent_result})"


class ChildDirect(Parent):
    """Child using direct parent call."""
    
    def __init__(self):
        print("ChildDirect.__init__ called")
        Parent.__init__(self)  # Directly calls Parent
        self.child_value = "from child"
    
    def method(self):
        # Direct call to parent method
        parent_result = Parent.method(self)
        return f"Child method (parent says: {parent_result})"


print("="*70)
print("SUPER() VS DIRECT PARENT CALL")
print("="*70)

print("\nUsing super():")
child1 = ChildWithSuper()
print(f"Result: {child1.method()}")

print("\nUsing direct parent call:")
child2 = ChildDirect()
print(f"Result: {child2.method()}")

print("\nBoth work the same for single inheritance!")
print("But super() is better for multiple inheritance...")


# ============================================================================
# SECTION 3: Why super() Matters - Diamond Problem Example
# ============================================================================

class Base:
    """Common base class."""
    
    def __init__(self):
        print("Base.__init__ called")
        self.base_value = "base"


class LeftWithSuper(Base):
    """Left branch using super()."""
    
    def __init__(self):
        print("LeftWithSuper.__init__ called")
        super().__init__()  # Calls NEXT in MRO, not Base!
        self.left_value = "left"


class RightWithSuper(Base):
    """Right branch using super()."""
    
    def __init__(self):
        print("RightWithSuper.__init__ called")
        super().__init__()  # Calls NEXT in MRO, not Base!
        self.right_value = "right"


class DiamondWithSuper(LeftWithSuper, RightWithSuper):
    """
    Diamond inheritance using super().
    
    MRO: DiamondWithSuper -> LeftWithSuper -> RightWithSuper -> Base -> object
    """
    
    def __init__(self):
        print("DiamondWithSuper.__init__ called")
        super().__init__()  # Starts the MRO chain


# Now compare with direct parent calls:

class LeftDirect(Base):
    """Left branch using direct call."""
    
    def __init__(self):
        print("LeftDirect.__init__ called")
        Base.__init__(self)  # Directly calls Base
        self.left_value = "left"


class RightDirect(Base):
    """Right branch using direct call."""
    
    def __init__(self):
        print("RightDirect.__init__ called")
        Base.__init__(self)  # Directly calls Base
        self.right_value = "right"


class DiamondDirect(LeftDirect, RightDirect):
    """
    Diamond inheritance using direct calls.
    This will call Base.__init__ TWICE!
    """
    
    def __init__(self):
        print("DiamondDirect.__init__ called")
        LeftDirect.__init__(self)   # Calls Base.__init__
        RightDirect.__init__(self)  # Calls Base.__init__ AGAIN!


print("\n" + "="*70)
print("SUPER() IN DIAMOND INHERITANCE")
print("="*70)

print("\nUsing super() - Base.__init__ called ONCE:")
d1 = DiamondWithSuper()

print("\nMRO for DiamondWithSuper:")
for i, cls in enumerate(DiamondWithSuper.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print("\n" + "-"*70)

print("\nUsing direct calls - Base.__init__ called TWICE:")
d2 = DiamondDirect()

print("\nThis can cause bugs! Base is initialized twice.")


# ============================================================================
# SECTION 4: How super() Follows MRO
# ============================================================================

"""
super() uses the MRO to determine which class to call next.
Let's trace through the MRO step by step.
"""


class A:
    def __init__(self):
        print(f"  A.__init__ called (MRO position: {A.__mro__.index(A) + 1})")
        print(f"  A: next in MRO would be object")
        super().__init__()  # Calls object.__init__


class B(A):
    def __init__(self):
        print(f"  B.__init__ called (MRO position: {B.__mro__.index(B) + 1})")
        print(f"  B: next in MRO is {B.__mro__[B.__mro__.index(B) + 1].__name__}")
        super().__init__()  # Calls A.__init__


class C(A):
    def __init__(self):
        print(f"  C.__init__ called (MRO position: variable - depends on final class)")
        print(f"  C: calls super().__init__()")
        super().__init__()  # Calls next in MRO (might not be A!)


class D(B, C):
    """
    Diamond with detailed tracing.
    
    MRO: D -> B -> C -> A -> object
    """
    
    def __init__(self):
        print(f"  D.__init__ called (MRO position: 1)")
        print(f"  D: next in MRO is {D.__mro__[1].__name__}")
        super().__init__()  # Calls B.__init__


print("\n" + "="*70)
print("TRACING SUPER() THROUGH MRO")
print("="*70)

print("\nMRO for D:")
for i, cls in enumerate(D.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print("\nCreating D instance and tracing super() calls:")
d = D()

print("\nNotice:")
print("- Each class calls super().__init__()")
print("- super() in B calls C, not A (following MRO)")
print("- super() in C calls A (following MRO)")
print("- A's __init__ is called only once at the end")


# ============================================================================
# SECTION 5: Cooperative Inheritance Pattern
# ============================================================================

"""
Cooperative inheritance: all classes in the hierarchy cooperate by:
1. Taking their own parameters
2. Passing remaining parameters to super()
3. Ensuring all classes get properly initialized
"""


class Logger:
    """Base class for logging functionality."""
    
    def __init__(self, log_level="INFO", **kwargs):
        # Take our parameter
        print(f"Logger.__init__: log_level={log_level}")
        self.log_level = log_level
        
        # Pass remaining kwargs to next in MRO
        super().__init__(**kwargs)
    
    def log(self, message):
        return f"[{self.log_level}] {message}"


class Timestamped:
    """Mixin to add timestamps."""
    
    def __init__(self, include_timestamp=True, **kwargs):
        print(f"Timestamped.__init__: include_timestamp={include_timestamp}")
        self.include_timestamp = include_timestamp
        
        super().__init__(**kwargs)
    
    def get_timestamp(self):
        from datetime import datetime
        if self.include_timestamp:
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return ""


class FileHandler(Logger, Timestamped):
    """
    Handles file operations with logging and timestamps.
    
    MRO: FileHandler -> Logger -> Timestamped -> object
    
    Both Logger and Timestamped use cooperative inheritance,
    so all __init__ methods are called correctly.
    """
    
    def __init__(self, filename, log_level="INFO", include_timestamp=True):
        print(f"FileHandler.__init__: filename={filename}")
        self.filename = filename
        
        # Pass parameters to cooperative parent classes
        super().__init__(
            log_level=log_level,
            include_timestamp=include_timestamp
        )
    
    def write(self, data):
        """Write data to file with logging and timestamp."""
        timestamp = self.get_timestamp()
        prefix = f"{timestamp} " if timestamp else ""
        message = f"{prefix}Writing to {self.filename}: {data}"
        return self.log(message)


print("\n" + "="*70)
print("COOPERATIVE INHERITANCE PATTERN")
print("="*70)

print("\nCreating FileHandler:")
handler = FileHandler(
    filename="data.txt",
    log_level="DEBUG",
    include_timestamp=True
)

print("\nMRO for FileHandler:")
for i, cls in enumerate(FileHandler.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print(f"\nUsing FileHandler:")
print(handler.write("Hello, World!"))


# ============================================================================
# SECTION 6: Common super() Pitfalls
# ============================================================================

"""
Common mistakes when using super():
1. Mixing super() and direct calls
2. Not passing **kwargs
3. Incorrect parameter handling
4. Forgetting to call super()
"""


# PITFALL 1: Mixing super() and direct calls
class Bad1A:
    def __init__(self):
        print("Bad1A.__init__")


class Bad1B(Bad1A):
    def __init__(self):
        print("Bad1B.__init__")
        super().__init__()  # Uses super()


class Bad1C(Bad1A):
    def __init__(self):
        print("Bad1C.__init__")
        Bad1A.__init__(self)  # Direct call!


class Bad1D(Bad1B, Bad1C):
    """
    This might work but is fragile and unpredictable.
    Bad1A.__init__ gets called twice!
    """
    
    def __init__(self):
        print("Bad1D.__init__")
        super().__init__()


# PITFALL 2: Not passing **kwargs
class Good2A:
    def __init__(self, a=None, **kwargs):
        print(f"Good2A: a={a}")
        super().__init__(**kwargs)  # Passes remaining kwargs


class Bad2B(Good2A):
    def __init__(self, b=None, **kwargs):
        print(f"Bad2B: b={b}")
        super().__init__()  # Doesn't pass kwargs!
        # This breaks the chain!


class Good2C(Good2A):
    def __init__(self, c=None, **kwargs):
        print(f"Good2C: c={c}")
        super().__init__(**kwargs)  # Correctly passes kwargs


print("\n" + "="*70)
print("COMMON SUPER() PITFALLS")
print("="*70)

print("\nPitfall 1 - Mixing super() and direct calls:")
print("Bad1D might work but is unpredictable:")
# bad1d = Bad1D()  # Bad1A.__init__ called twice

print("\nPitfall 2 - Not passing **kwargs:")
print("This breaks the cooperative chain")
# If we had: class Bad2D(Bad2B, Good2C): pass
# Good2C's parameters wouldn't be passed through Bad2B


# ============================================================================
# SECTION 7: super() with Arguments
# ============================================================================

"""
super() can take arguments: super(Class, instance)
This is rarely needed but useful for understanding how super() works.
"""


class Base7:
    def method(self):
        return "Base7"


class Child7(Base7):
    def method(self):
        # These are equivalent:
        result1 = super().method()  # Modern way
        result2 = super(Child7, self).method()  # Explicit way
        
        return f"Child7 (base: {result1})"


class GrandChild7(Child7):
    def method(self):
        # Can skip a class in MRO if needed (rare!)
        result = super(Child7, self).method()  # Skip Child7, go to Base7
        return f"GrandChild7 (skipped to: {result})"


print("\n" + "="*70)
print("SUPER() WITH ARGUMENTS")
print("="*70)

child = Child7()
print(f"child.method(): {child.method()}")

grandchild = GrandChild7()
print(f"grandchild.method() - normal: {super(GrandChild7, grandchild).method()}")
print(f"grandchild.method() - skip: {super(Child7, grandchild).method()}")


# ============================================================================
# SECTION 8: Debugging super() and MRO
# ============================================================================

"""
Tips for debugging super() issues:
1. Print the MRO
2. Trace __init__ calls
3. Check for consistent use of super()
4. Verify **kwargs are passed correctly
"""


class DebugMixin:
    """Mixin to help debug MRO and super() issues."""
    
    def print_mro(self):
        """Print the MRO in a readable format."""
        print(f"\nMRO for {self.__class__.__name__}:")
        for i, cls in enumerate(self.__class__.__mro__, 1):
            print(f"  {i}. {cls.__name__}")
    
    def trace_method(self, method_name):
        """Trace which class provides a method."""
        print(f"\nTracing method '{method_name}':")
        for cls in self.__class__.__mro__:
            if method_name in cls.__dict__:
                print(f"  Found in: {cls.__name__}")
                break
        else:
            print(f"  Not found in MRO")


class DebugA(DebugMixin):
    def method_a(self):
        return "from A"


class DebugB(DebugMixin):
    def method_b(self):
        return "from B"


class DebugC(DebugA, DebugB):
    def method_c(self):
        return "from C"


print("\n" + "="*70)
print("DEBUGGING TOOLS")
print("="*70)

debug = DebugC()
debug.print_mro()
debug.trace_method("method_a")
debug.trace_method("method_b")
debug.trace_method("method_c")
debug.trace_method("nonexistent")


# ============================================================================
# SECTION 9: Key Takeaways
# ============================================================================

"""
KEY POINTS ABOUT SUPER():

1. What super() Does:
   - Returns a proxy that calls the NEXT class in MRO
   - NOT the same as calling the parent class directly
   - Essential for cooperative multiple inheritance

2. Why Use super():
   - Prevents duplicate initialization in diamond inheritance
   - Enables cooperative inheritance patterns
   - More maintainable and flexible code
   - Respects the MRO

3. Cooperative Inheritance Pattern:
   - Each class takes its own parameters
   - Pass remaining parameters using **kwargs
   - Always call super().__init__(**kwargs)
   - Document your MRO intentions

4. Common Pitfalls:
   - Mixing super() and direct parent calls
   - Not passing **kwargs through the chain
   - Inconsistent use of super() across hierarchy
   - Forgetting to call super() at all

5. Best Practices:
   - Use super() consistently in all classes
   - Pass **kwargs to handle unknown parameters
   - Document complex MRO chains
   - Test diamond inheritance scenarios
   - Use debugging tools to trace MRO

6. When NOT to Use super():
   - When you specifically need to call one parent
   - When you're not doing cooperative inheritance
   - Simple single inheritance (but super() still works!)

7. Python 2 vs Python 3:
   - Python 2: super(ClassName, self).method()
   - Python 3: super().method() (simpler!)
   - This course uses Python 3 syntax
"""

print("\n" + "="*70)
print("END OF SUPER() AND MRO TUTORIAL")
print("="*70)
print("\nNext: Learn MRO inspection tools and techniques!")
