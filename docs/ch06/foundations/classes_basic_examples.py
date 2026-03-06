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
