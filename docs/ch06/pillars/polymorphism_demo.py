"""
Example 05: Polymorphism

Polymorphism means "many forms". It allows objects of different classes
to be treated as objects of a common parent class, and the correct method
is called based on the object's actual type.
"""

# Example 1: Basic Polymorphism
class PaymentMethod:
    def __init__(self, name):
        self.name = name
    
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement this method")
    
    def get_receipt(self, amount):
        return f"Payment of ${amount:.2f} via {self.name}"


class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv):
        super().__init__("Credit Card")
        self.card_number = card_number[-4:]  # Store only last 4 digits
        self.cvv = cvv
    
    def process_payment(self, amount):
        return f"Processing ${amount:.2f} on card ending in {self.card_number}"


class PayPal(PaymentMethod):
    def __init__(self, email):
        super().__init__("PayPal")
        self.email = email
    
    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via PayPal account {self.email}"


class Bitcoin(PaymentMethod):
    def __init__(self, wallet_address):
        super().__init__("Bitcoin")
        self.wallet_address = wallet_address
    
    def process_payment(self, amount):
        btc_amount = amount / 30000  # Simplified conversion
        return f"Processing {btc_amount:.6f} BTC to wallet {self.wallet_address[:8]}..."


# Example 2: Polymorphism with Different Return Types
class DataProcessor:
    def process(self, data):
        raise NotImplementedError


class TextProcessor(DataProcessor):
    def process(self, data):
        # Returns uppercase text
        return data.upper()


class NumberProcessor(DataProcessor):
    def process(self, data):
        # Returns sum of numbers
        return sum(data)


class ListProcessor(DataProcessor):
    def process(self, data):
        # Returns sorted list
        return sorted(data)


# Example 3: Duck Typing (Python's Polymorphism)
class Duck:
    def speak(self):
        return "Quack!"
    
    def swim(self):
        return "Duck is swimming"


class Person:
    def speak(self):
        return "Hello!"
    
    def swim(self):
        return "Person is swimming"


class Robot:
    def speak(self):
        return "Beep boop!"
    
    def swim(self):
        return "Robot cannot swim (error: water damage)"


def make_it_speak_and_swim(entity):
    """
    Duck typing: If it walks like a duck and quacks like a duck, it's a duck.
    We don't check the type, we just try to call the methods.
    """
    print(entity.speak())
    print(entity.swim())


# Example 4: Polymorphism in Action - File System
class FileSystemItem:
    def __init__(self, name):
        self.name = name
    
    def get_size(self):
        raise NotImplementedError
    
    def display(self, indent=0):
        raise NotImplementedError


class File(FileSystemItem):
    def __init__(self, name, size_kb):
        super().__init__(name)
        self.size_kb = size_kb
    
    def get_size(self):
        return self.size_kb
    
    def display(self, indent=0):
        return "  " * indent + f"📄 {self.name} ({self.size_kb} KB)"


class Folder(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_size(self):
        # Polymorphism: call get_size() on different types
        return sum(item.get_size() for item in self.items)
    
    def display(self, indent=0):
        result = "  " * indent + f"📁 {self.name}/\n"
        for item in self.items:
            result += item.display(indent + 1) + "\n"
        return result.rstrip()


# Testing Polymorphism
if __name__ == "__main__":
    print("=" * 70)
    print("EXAMPLE 1: PAYMENT PROCESSING POLYMORPHISM")
    print("=" * 70)
    
    # Different payment methods, same interface
    payment_methods = [
        CreditCard("1234-5678-9012-3456", "123"),
        PayPal("user@email.com"),
        Bitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    ]
    
    total = 99.99
    for payment in payment_methods:
        print(f"\n{payment.name}:")
        print(payment.process_payment(total))
        print(payment.get_receipt(total))
    
    print("\n" + "=" * 70)
    print("EXAMPLE 2: DATA PROCESSING POLYMORPHISM")
    print("=" * 70)
    
    processors = [
        (TextProcessor(), "hello world"),
        (NumberProcessor(), [1, 2, 3, 4, 5]),
        (ListProcessor(), [5, 2, 8, 1, 9])
    ]
    
    for processor, data in processors:
        print(f"\n{processor.__class__.__name__}:")
        print(f"  Input: {data}")
        print(f"  Output: {processor.process(data)}")
    
    print("\n" + "=" * 70)
    print("EXAMPLE 3: DUCK TYPING")
    print("=" * 70)
    
    entities = [Duck(), Person(), Robot()]
    for entity in entities:
        print(f"\n{entity.__class__.__name__}:")
        make_it_speak_and_swim(entity)
    
    print("\n" + "=" * 70)
    print("EXAMPLE 4: FILE SYSTEM POLYMORPHISM")
    print("=" * 70)
    
    # Create file system structure
    root = Folder("root")
    
    docs = Folder("documents")
    docs.add_item(File("report.pdf", 250))
    docs.add_item(File("notes.txt", 15))
    
    images = Folder("images")
    images.add_item(File("photo1.jpg", 1200))
    images.add_item(File("photo2.jpg", 1500))
    
    root.add_item(docs)
    root.add_item(images)
    root.add_item(File("readme.md", 8))
    
    # Polymorphism in action: both File and Folder have get_size() and display()
    print(root.display())
    print(f"\nTotal size: {root.get_size()} KB")

"""
KEY TAKEAWAYS:
1. Polymorphism allows treating different objects through a common interface
2. Different classes can implement the same method differently
3. The correct method is called based on the object's actual type (runtime)
4. Python uses "duck typing" - if it has the method, you can call it
5. Polymorphism makes code more flexible and maintainable
6. Common parent classes define the interface

BENEFITS OF POLYMORPHISM:
1. Flexibility: Easy to add new types without changing existing code
2. Maintainability: Changes to one class don't affect others
3. Extensibility: New classes can be added that work with existing code
4. Code Reusability: Same function/loop works with multiple types
5. Abstraction: Hide implementation details behind common interface

REAL-WORLD USES:
- Payment processing (multiple payment methods)
- File handling (different file types)
- Database connections (MySQL, PostgreSQL, MongoDB)
- UI components (buttons, inputs, dropdowns)
- Game entities (players, enemies, NPCs)
- Notification systems (email, SMS, push notifications)
"""
