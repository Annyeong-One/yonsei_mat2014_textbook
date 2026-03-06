"""
Example 01: Basic Encapsulation

Encapsulation is the concept of bundling data and methods that work on that data
within a class, while controlling access to prevent misuse.
"""

# BAD EXAMPLE - No Encapsulation

# =============================================================================
# Definitions
# =============================================================================

class BankAccountBad:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # Anyone can modify this!


# GOOD EXAMPLE - With Encapsulation
class BankAccountGood:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (name mangling)
    
    def deposit(self, amount):
        """Controlled way to add money"""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Controlled way to remove money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Controlled way to view balance"""
        return self.__balance


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    # BAD EXAMPLE - No encapsulation (problem with no encapsulation)
    bad_account = BankAccountBad("John", 1000)
    print(f"Initial balance: ${bad_account.balance}")

    # Direct access allows invalid operations
    bad_account.balance = -5000  # Negative balance? No validation!
    print(f"After direct modification: ${bad_account.balance}")  # This is bad!

    print("\n" + "=" * 60)
    print("ENCAPSULATION DEMONSTRATION")
    print("=" * 60)

    # GOOD EXAMPLE - Using encapsulated class
    good_account = BankAccountGood("Jane", 1000)
    print(f"\nInitial balance: ${good_account.get_balance()}")
    
    # Must use methods to modify balance
    good_account.deposit(500)
    print(f"After deposit: ${good_account.get_balance()}")
    
    good_account.withdraw(200)
    print(f"After withdrawal: ${good_account.get_balance()}")
    
    # Try invalid operations
    print("\n--- Testing validation ---")
    if not good_account.deposit(-100):
        print("❌ Cannot deposit negative amount")
    
    if not good_account.withdraw(5000):
        print("❌ Cannot withdraw more than balance")
    
    # Try to access private attribute directly
    print("\n--- Testing encapsulation ---")
    try:
        print(good_account.__balance)  # This will fail!
    except AttributeError as e:
        print(f"❌ Cannot access private attribute: {e}")
    
    # Python's name mangling allows this (but you shouldn't do it!)
    print(f"\nName mangled attribute: {good_account._BankAccountGood__balance}")
    print("⚠️  But you shouldn't access it this way!")

"""
KEY TAKEAWAYS:
1. Encapsulation protects data from invalid modifications
2. Use private attributes (double underscore) for internal data
3. Provide public methods for controlled access
4. Validation happens in methods, not everywhere in your code
5. Name mangling makes attributes harder (but not impossible) to access
6. Encapsulation makes code safer and more maintainable
"""
