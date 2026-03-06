"""Abstract Base Classes (ABC) - Defining contracts"""
from abc import ABC, abstractmethod

# =============================================================================
# Definitions
# =============================================================================

class PaymentProcessor(ABC):
    """Abstract interface for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount):
        """All processors must implement this"""
        pass
    
    @abstractmethod
    def refund(self, transaction_id):
        """All processors must implement this"""
        pass
    
    def log_transaction(self, details):
        """Common implementation for all"""
        print(f"Logged: {details}")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Stripe")
        self.log_transaction(f"Stripe: ${amount}")
    
    def refund(self, transaction_id):
        print(f"Refunding Stripe transaction {transaction_id}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")
        self.log_transaction(f"PayPal: ${amount}")
    
    def refund(self, transaction_id):
        print(f"Refunding PayPal transaction {transaction_id}")

# Polymorphism with abstraction
def process_order(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    stripe = StripeProcessor()
    paypal = PayPalProcessor()
    
    process_order(stripe, 100)
    process_order(paypal, 50)
