# Classes and Instances

## Classes

### 1. Definition

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name):
        # Instance attribute
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"
```

## Instances

### 1. Creating

```python
dog1 = Dog("Rex")
dog2 = Dog("Max")

print(dog1.name)   # Rex
print(dog2.name)   # Max
```

### 2. Independent

```python
print(dog1.bark())  # Rex says woof!
print(dog2.bark())  # Max says woof!

# Different objects
print(dog1 is dog2)  # False
```

## Class vs Instance

### 1. Attributes

```python
class MyClass:
    class_var = "shared"
    
    def __init__(self):
        self.instance_var = "unique"

obj1 = MyClass()
obj2 = MyClass()

print(obj1.class_var)      # shared
print(obj1.instance_var)   # unique
```

## Summary

- Class: blueprint
- Instance: object from class
- self refers to instance
- Each instance independent

---

## Runnable Example: `classes_basic_examples.py`

```python
"""
Basic Classes and Objects Examples
Run this file to see classes in action!
"""

# ============================================================================
# Example 1: Simple Class

if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Simple Car Class")
    print("=" * 50)

    class Car:
        def __init__(self, brand, model, year):
            self.brand = brand
            self.model = model
            self.year = year
            self.odometer = 0

        def drive(self, miles):
            self.odometer += miles
            return f"Drove {miles} miles. Total: {self.odometer}"

        def get_info(self):
            return f"{self.year} {self.brand} {self.model}"

    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Civic", 2021)

    print(car1.get_info())
    print(car1.drive(100))
    print(car1.drive(50))
    print()

    # ============================================================================
    # Example 2: Bank Account with Encapsulation
    print("=" * 50)
    print("Example 2: Bank Account with Encapsulation")
    print("=" * 50)

    class BankAccount:
        def __init__(self, owner, initial_balance=0):
            self.owner = owner
            self.__balance = initial_balance  # Private attribute
            self.__transaction_history = []

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                self.__transaction_history.append(f"Deposit: +${amount}")
                return f"Deposited ${amount}. New balance: ${self.__balance}"
            return "Invalid deposit amount"

        def withdraw(self, amount):
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                self.__transaction_history.append(f"Withdrawal: -${amount}")
                return f"Withdrew ${amount}. New balance: ${self.__balance}"
            return "Invalid withdrawal amount or insufficient funds"

        def get_balance(self):
            return self.__balance

        def get_statement(self):
            statement = f"\n--- Account Statement for {self.owner} ---\n"
            for transaction in self.__transaction_history:
                statement += transaction + "\n"
            statement += f"Current Balance: ${self.__balance}\n"
            return statement

    account = BankAccount("Alice", 1000)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.withdraw(2000))  # Should fail
    print(account.get_statement())

    # ============================================================================
    # Example 3: Student Management
    print("=" * 50)
    print("Example 3: Student with Grades")
    print("=" * 50)

    class Student:
        school_name = "Tech High School"  # Class attribute

        def __init__(self, name, student_id):
            self.name = name
            self.student_id = student_id
            self.grades = []

        def add_grade(self, grade):
            if 0 <= grade <= 100:
                self.grades.append(grade)
                return f"Grade {grade} added for {self.name}"
            return "Invalid grade (must be 0-100)"

        def get_average(self):
            if not self.grades:
                return 0
            return sum(self.grades) / len(self.grades)

        def get_letter_grade(self):
            avg = self.get_average()
            if avg >= 90:
                return 'A'
            elif avg >= 80:
                return 'B'
            elif avg >= 70:
                return 'C'
            elif avg >= 60:
                return 'D'
            else:
                return 'F'

        def __str__(self):
            return f"Student: {self.name} (ID: {self.student_id})"

    student1 = Student("Bob", "S001")
    student2 = Student("Carol", "S002")

    print(student1)
    print(student1.add_grade(85))
    print(student1.add_grade(92))
    print(student1.add_grade(78))
    print(f"Average: {student1.get_average():.2f}")
    print(f"Letter Grade: {student1.get_letter_grade()}")
    print()

    # ============================================================================
    # Example 4: Rectangle with Properties
    print("=" * 50)
    print("Example 4: Rectangle with Properties")
    print("=" * 50)

    class Rectangle:
        def __init__(self, width, height):
            self._width = width
            self._height = height

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            if value > 0:
                self._width = value
            else:
                raise ValueError("Width must be positive")

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, value):
            if value > 0:
                self._height = value
            else:
                raise ValueError("Height must be positive")

        @property
        def area(self):
            return self._width * self._height

        @property
        def perimeter(self):
            return 2 * (self._width + self._height)

        def __str__(self):
            return f"Rectangle({self._width}x{self._height})"

    rect = Rectangle(5, 3)
    print(rect)
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")
    rect.width = 10
    print(f"After changing width: {rect}")
    print(f"New area: {rect.area}")
    print()

    # ============================================================================
    # Example 5: Shopping Cart
    print("=" * 50)
    print("Example 5: Shopping Cart System")
    print("=" * 50)

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __str__(self):
            return f"{self.name}: ${self.price:.2f}"

    class ShoppingCart:
        def __init__(self):
            self.items = []

        def add_item(self, product, quantity=1):
            self.items.append({"product": product, "quantity": quantity})
            return f"Added {quantity}x {product.name} to cart"

        def remove_item(self, product_name):
            for i, item in enumerate(self.items):
                if item["product"].name == product_name:
                    removed = self.items.pop(i)
                    return f"Removed {removed['product'].name} from cart"
            return "Product not found in cart"

        def get_total(self):
            total = 0
            for item in self.items:
                total += item["product"].price * item["quantity"]
            return total

        def display_cart(self):
            if not self.items:
                return "Cart is empty"

            cart_str = "\n--- Shopping Cart ---\n"
            for item in self.items:
                product = item["product"]
                quantity = item["quantity"]
                subtotal = product.price * quantity
                cart_str += f"{quantity}x {product.name} @ ${product.price:.2f} = ${subtotal:.2f}\n"
            cart_str += f"\nTotal: ${self.get_total():.2f}\n"
            return cart_str

    # Create products
    laptop = Product("Laptop", 999.99)
    mouse = Product("Mouse", 29.99)
    keyboard = Product("Keyboard", 79.99)

    # Create cart and add items
    cart = ShoppingCart()
    print(cart.add_item(laptop))
    print(cart.add_item(mouse, 2))
    print(cart.add_item(keyboard))
    print(cart.display_cart())
    print(cart.remove_item("Mouse"))
    print(cart.display_cart())
```

---

## Exercises

**Exercise 1.**
Create a `Dog` class with instance attributes `name`, `breed`, and `age`. Add methods `bark()` (returns a string), `birthday()` (increments age), and `__str__`. Create two dogs and show they are independent instances with separate state.

??? success "Solution to Exercise 1"

        class Dog:
            def __init__(self, name, breed, age):
                self.name = name
                self.breed = breed
                self.age = age

            def bark(self):
                return f"{self.name} says: Woof!"

            def birthday(self):
                self.age += 1

            def __str__(self):
                return f"{self.name} ({self.breed}, {self.age} years)"

        d1 = Dog("Buddy", "Lab", 3)
        d2 = Dog("Max", "Poodle", 5)

        print(d1)          # Buddy (Lab, 3 years)
        print(d2.bark())   # Max says: Woof!
        d1.birthday()
        print(d1.age)      # 4
        print(d2.age)      # 5 — independent

---

**Exercise 2.**
Write a `BankAccount` class with `owner` and `balance` attributes. Add `deposit(amount)`, `withdraw(amount)` (raises `ValueError` if insufficient funds), and `__repr__` methods. Create two accounts, perform transactions, and show balances are independent.

??? success "Solution to Exercise 2"

        class BankAccount:
            def __init__(self, owner, balance=0):
                self.owner = owner
                self.balance = balance

            def deposit(self, amount):
                self.balance += amount

            def withdraw(self, amount):
                if amount > self.balance:
                    raise ValueError("Insufficient funds")
                self.balance -= amount

            def __repr__(self):
                return f"BankAccount('{self.owner}', {self.balance})"

        a1 = BankAccount("Alice", 1000)
        a2 = BankAccount("Bob", 500)
        a1.deposit(200)
        a2.withdraw(100)
        print(a1)  # BankAccount('Alice', 1200)
        print(a2)  # BankAccount('Bob', 400)

---

**Exercise 3.**
Build a `Classroom` class that stores a `name` and a list of `students`. Add `enroll(student_name)`, `drop(student_name)`, and `roster()` (returns sorted list) methods. Show that `isinstance()` confirms the type, and two classrooms maintain separate student lists.

??? success "Solution to Exercise 3"

        class Classroom:
            def __init__(self, name):
                self.name = name
                self.students = []

            def enroll(self, student_name):
                if student_name not in self.students:
                    self.students.append(student_name)

            def drop(self, student_name):
                self.students.remove(student_name)

            def roster(self):
                return sorted(self.students)

        c1 = Classroom("Math 101")
        c2 = Classroom("Physics 201")
        c1.enroll("Alice")
        c1.enroll("Bob")
        c2.enroll("Charlie")

        print(c1.roster())   # ['Alice', 'Bob']
        print(c2.roster())   # ['Charlie'] — independent
        print(isinstance(c1, Classroom))  # True
