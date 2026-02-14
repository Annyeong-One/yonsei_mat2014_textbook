"""
03_diamond_problem.py

INTERMEDIATE LEVEL: The Diamond Problem and Python's Solution

This file explains the classic "diamond problem" in multiple inheritance
and demonstrates how Python's MRO (using C3 linearization) solves it elegantly.

The diamond problem occurs when a class inherits from two classes that both
inherit from a common base class, creating a diamond-shaped inheritance graph.

Learning Objectives:
- Understand what the diamond problem is
- See how Python prevents the diamond problem
- Learn about duplicate base class prevention
- Understand why C3 linearization is important
"""

# ============================================================================
# SECTION 1: What is the Diamond Problem?
# ============================================================================

"""
The Diamond Problem:

        A
       / \
      B   C
       \ /
        D

Class D inherits from B and C
Classes B and C both inherit from A

Questions that arise:
1. Which version of A's methods does D get?
2. Is A's __init__ called once or twice?
3. In what order are methods searched?
4. How do we prevent conflicts and ambiguity?

Python solves this using C3 Linearization algorithm, which ensures:
- Each class appears only ONCE in the MRO
- The MRO is consistent and predictable
- Child classes come before parent classes
- Parent order is preserved from the class definition
"""


# ============================================================================
# SECTION 2: Classic Diamond Problem Example
# ============================================================================

class A:
    """
    Base class at the top of the diamond.
    This is the common ancestor.
    """
    
    def __init__(self):
        print("A.__init__ called")
        self.value_a = "From A"
    
    def method(self):
        return "Method from A"
    
    def show_mro(self):
        """Helper method to show where method is called from."""
        return "show_mro from A"


class B(A):
    """
    Left branch of the diamond.
    Inherits from A.
    """
    
    def __init__(self):
        print("B.__init__ called")
        super().__init__()  # Call A.__init__
        self.value_b = "From B"
    
    def method(self):
        return "Method from B"
    
    def method_b(self):
        return "Specific to B"


class C(A):
    """
    Right branch of the diamond.
    Also inherits from A.
    """
    
    def __init__(self):
        print("C.__init__ called")
        super().__init__()  # Call A.__init__
        self.value_c = "From C"
    
    def method(self):
        return "Method from C"
    
    def method_c(self):
        return "Specific to C"


class D(B, C):
    """
    Bottom of the diamond.
    Inherits from both B and C, which both inherit from A.
    
    This creates the diamond:
           A
          / \
         B   C
          \ /
           D
    
    Python's MRO: D -> B -> C -> A -> object
    
    Notice: A appears only ONCE at the end, not twice!
    This is Python's solution to the diamond problem.
    """
    
    def __init__(self):
        print("D.__init__ called")
        super().__init__()  # This will call the next class in MRO
        self.value_d = "From D"


print("="*70)
print("CLASSIC DIAMOND PROBLEM")
print("="*70)

# Create an instance of D
print("\nCreating instance of D:")
d = D()
# Notice: A.__init__ is called only ONCE, not twice!

# View the MRO
print("\nMRO for class D:")
for i, cls in enumerate(D.__mro__, 1):
    print(f"{i}. {cls.__name__}")
# Output:
# 1. D
# 2. B
# 3. C
# 4. A      <- A appears only once!
# 5. object

# Method resolution follows this MRO
print(f"\nCalling d.method(): {d.method()}")  # Finds in B (first in MRO after D)
print(f"Calling d.method_b(): {d.method_b()}")  # Finds in B
print(f"Calling d.method_c(): {d.method_c()}")  # Finds in C
print(f"Calling d.show_mro(): {d.show_mro()}")  # Finds in A


# ============================================================================
# SECTION 3: Understanding super() in Diamond Inheritance
# ============================================================================

"""
The key to Python's diamond problem solution is super().

super() doesn't just call the parent class - it calls the NEXT class in MRO!

This ensures:
1. Each class's __init__ is called exactly once
2. The MRO is followed correctly
3. No duplicate initialization
"""


class Animal:
    """Base animal class."""
    
    def __init__(self, name):
        print(f"Animal.__init__ called for {name}")
        self.name = name


class Mammal(Animal):
    """Mammal branch."""
    
    def __init__(self, name, warm_blooded=True):
        print(f"Mammal.__init__ called for {name}")
        super().__init__(name)  # Calls next in MRO, not necessarily Animal!
        self.warm_blooded = warm_blooded


class Winged(Animal):
    """Winged branch."""
    
    def __init__(self, name, can_fly=True):
        print(f"Winged.__init__ called for {name}")
        super().__init__(name)  # Calls next in MRO
        self.can_fly = can_fly


class Bat(Mammal, Winged):
    """
    Bat is both a mammal and winged.
    
    Diamond structure:
           Animal
           /    \
      Mammal  Winged
           \    /
            Bat
    
    MRO: Bat -> Mammal -> Winged -> Animal -> object
    """
    
    def __init__(self, name):
        print(f"Bat.__init__ called for {name}")
        # super().__init__ will call Mammal.__init__ (next in MRO)
        # Mammal's super().__init__ will call Winged.__init__ (next in MRO)
        # Winged's super().__init__ will call Animal.__init__ (next in MRO)
        super().__init__(name, warm_blooded=True)
        self.nocturnal = True


print("\n" + "="*70)
print("SUPER() IN DIAMOND INHERITANCE")
print("="*70)

print("\nCreating a Bat instance:")
print("Watch the order of __init__ calls:\n")
bruce = Bat("Bruce")

print("\nMRO for Bat:")
for i, cls in enumerate(Bat.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print(f"\nBat attributes:")
print(f"  Name: {bruce.name}")
print(f"  Warm-blooded: {bruce.warm_blooded}")
print(f"  Nocturnal: {bruce.nocturnal}")
# Note: can_fly is not set because we didn't pass it to Mammal.__init__


# ============================================================================
# SECTION 4: Proper Diamond Pattern with Keyword Arguments
# ============================================================================

"""
To properly handle diamond inheritance with different parameters,
use **kwargs to pass arguments through the MRO chain.
"""


class Shape:
    """Base shape class."""
    
    def __init__(self, color="black", **kwargs):
        print(f"Shape.__init__ called with color={color}")
        super().__init__(**kwargs)  # Pass remaining kwargs up the chain
        self.color = color


class Rectangle(Shape):
    """Rectangle shape."""
    
    def __init__(self, width=0, height=0, **kwargs):
        print(f"Rectangle.__init__ called with width={width}, height={height}")
        super().__init__(**kwargs)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Border(Shape):
    """Border mixin."""
    
    def __init__(self, border_width=1, **kwargs):
        print(f"Border.__init__ called with border_width={border_width}")
        super().__init__(**kwargs)
        self.border_width = border_width


class BorderedRectangle(Rectangle, Border):
    """
    Rectangle with a border.
    
    Diamond structure:
           Shape
           /    \
    Rectangle  Border
           \    /
     BorderedRectangle
    
    MRO: BorderedRectangle -> Rectangle -> Border -> Shape -> object
    """
    
    def __init__(self, width=0, height=0, border_width=1, color="black"):
        print(f"BorderedRectangle.__init__ called")
        super().__init__(
            width=width,
            height=height,
            border_width=border_width,
            color=color
        )
    
    def total_area(self):
        """Calculate total area including border."""
        inner_area = self.width * self.height
        border_area = (self.width + 2*self.border_width) * (self.height + 2*self.border_width)
        return border_area


print("\n" + "="*70)
print("PROPER DIAMOND PATTERN WITH KWARGS")
print("="*70)

print("\nCreating a BorderedRectangle:")
print("Watch how arguments flow through the MRO:\n")
rect = BorderedRectangle(width=10, height=5, border_width=2, color="red")

print("\nMRO for BorderedRectangle:")
for i, cls in enumerate(BorderedRectangle.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print(f"\nBorderedRectangle attributes:")
print(f"  Width: {rect.width}")
print(f"  Height: {rect.height}")
print(f"  Border width: {rect.border_width}")
print(f"  Color: {rect.color}")
print(f"  Inner area: {rect.area()}")
print(f"  Total area: {rect.total_area()}")


# ============================================================================
# SECTION 5: Invalid MRO - When Diamond Goes Wrong
# ============================================================================

"""
Not all inheritance patterns are valid. Python will raise TypeError
if the MRO cannot be computed consistently using C3 linearization.
"""


class X:
    pass


class Y:
    pass


class A(X, Y):
    """A inherits from X, then Y."""
    pass


class B(Y, X):
    """B inherits from Y, then X - opposite order!"""
    pass


# This would create an inconsistent MRO and raise TypeError:
# class C(A, B):
#     """
#     C inherits from A and B.
#     A says: X before Y
#     B says: Y before X
#     This is inconsistent - Python cannot resolve this!
#     """
#     pass

print("\n" + "="*70)
print("INVALID MRO EXAMPLE")
print("="*70)

print("\nTrying to create an inconsistent MRO:")
print("class A(X, Y): pass  # A says X before Y")
print("class B(Y, X): pass  # B says Y before X")
print("class C(A, B): pass  # C cannot resolve: X before Y or Y before X?")
print("\nThis would raise: TypeError: Cannot create a consistent MRO")


# Uncomment to see the actual error:
# try:
#     class C(A, B):
#         pass
# except TypeError as e:
#     print(f"\nActual error: {e}")


# ============================================================================
# SECTION 6: Real-World Diamond Example - GUI Components
# ============================================================================

"""
A practical example: GUI components that share common functionality.
"""


class Widget:
    """Base widget class."""
    
    def __init__(self, id="widget", **kwargs):
        super().__init__(**kwargs)
        print(f"Widget.__init__: creating {id}")
        self.id = id
        self.visible = True
    
    def show(self):
        self.visible = True
        return f"{self.id} is now visible"
    
    def hide(self):
        self.visible = False
        return f"{self.id} is now hidden"


class Clickable(Widget):
    """Mixin for clickable widgets."""
    
    def __init__(self, on_click=None, **kwargs):
        super().__init__(**kwargs)
        print(f"Clickable.__init__: setting up click handler")
        self.on_click = on_click
        self.click_count = 0
    
    def click(self):
        self.click_count += 1
        result = f"Clicked {self.id} (count: {self.click_count})"
        if self.on_click:
            self.on_click()
        return result


class Hoverable(Widget):
    """Mixin for hoverable widgets."""
    
    def __init__(self, on_hover=None, **kwargs):
        super().__init__(**kwargs)
        print(f"Hoverable.__init__: setting up hover handler")
        self.on_hover = on_hover
        self.is_hovered = False
    
    def hover(self):
        self.is_hovered = True
        result = f"Hovering over {self.id}"
        if self.on_hover:
            self.on_hover()
        return result


class Button(Clickable, Hoverable):
    """
    Button widget that is both clickable and hoverable.
    
    Diamond structure:
           Widget
           /    \
    Clickable  Hoverable
           \    /
           Button
    
    MRO: Button -> Clickable -> Hoverable -> Widget -> object
    """
    
    def __init__(self, id="button", label="Click me", **kwargs):
        super().__init__(id=id, **kwargs)
        print(f"Button.__init__: creating button with label '{label}'")
        self.label = label
    
    def render(self):
        """Render the button."""
        state = "visible" if self.visible else "hidden"
        hover = " (hovered)" if self.is_hovered else ""
        return f"[Button '{self.label}' - {state}{hover} - clicks: {self.click_count}]"


print("\n" + "="*70)
print("REAL-WORLD EXAMPLE: GUI BUTTON")
print("="*70)

print("\nCreating a Button:")
print("Initialization order follows MRO:\n")

def click_handler():
    print("  -> Click handler executed!")

def hover_handler():
    print("  -> Hover handler executed!")

submit_btn = Button(
    id="submit_button",
    label="Submit Form",
    on_click=click_handler,
    on_hover=hover_handler
)

print("\nMRO for Button:")
for i, cls in enumerate(Button.__mro__, 1):
    print(f"{i}. {cls.__name__}")

print(f"\nButton operations:")
print(submit_btn.render())
print(submit_btn.click())
print(submit_btn.hover())
print(submit_btn.render())
print(submit_btn.click())
print(submit_btn.render())


# ============================================================================
# SECTION 7: Key Takeaways
# ============================================================================

"""
KEY POINTS ABOUT THE DIAMOND PROBLEM:

1. Diamond Problem Structure:
           A
          / \
         B   C
          \ /
           D
   D inherits from B and C, both inherit from A

2. Python's Solution:
   - C3 Linearization algorithm
   - Each class appears ONLY ONCE in MRO
   - Preserves order of parent classes
   - Ensures consistent, predictable method resolution

3. super() is the Key:
   - super() calls the NEXT class in MRO, not the parent
   - This prevents duplicate initialization
   - Always use super() in cooperative inheritance

4. Use **kwargs:
   - Pass parameters through the MRO chain
   - Each class takes what it needs
   - Passes the rest to super().__init__()

5. Invalid MROs:
   - Some inheritance patterns are inconsistent
   - Python raises TypeError for invalid MRO
   - Different parent orders can create conflicts

6. Practical Uses:
   - Mixin classes (Clickable, Hoverable, etc.)
   - Shared functionality across hierarchies
   - Plugin architectures
   - Framework base classes

7. Best Practices:
   - Document your MRO intentions
   - Use super() consistently
   - Design parent classes to be "cooperative"
   - Test complex hierarchies thoroughly
   - Consider composition for very complex scenarios
"""

print("\n" + "="*70)
print("END OF DIAMOND PROBLEM TUTORIAL")
print("="*70)
print("\nNext: Learn about super() and its relationship with MRO!")
