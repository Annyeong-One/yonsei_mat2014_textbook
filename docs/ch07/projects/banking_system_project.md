# Banking System Project

## Overview
Build a complete banking system with different account types using inheritance and polymorphism.

## Objectives
- Design a class hierarchy for different account types
- Implement transaction handling
- Apply polymorphism for interest calculation
- Manage customer accounts

## Requirements

### 1. Base Account Class
Create an abstract `BankAccount` class with:
- Attributes: account_number, account_holder, balance, transactions (list)
- Methods:
  - `deposit(amount)` - add money to account
  - `withdraw(amount)` - remove money (check sufficient balance)
  - `get_balance()` - return current balance
  - `get_transaction_history()` - return list of all transactions
  - `apply_fees()` - apply monthly fees (if any)
  - Abstract method: `calculate_interest()` - varies by account type
  - Abstract method: `get_account_type()` - return account type name

### 2. Account Types
Implement these account types:

**SavingsAccount**
- Minimum balance: \$100
- Monthly fee: \$0 (no fee)
- Interest rate: 2% annual (compounded monthly)
- Withdrawal limit: 6 per month
- Penalty: \$5 fee if minimum balance not maintained

**CheckingAccount**
- Minimum balance: \$25
- Monthly fee: \$5 (waived if balance > \$500)
- Interest rate: 0.1% annual
- No withdrawal limit
- Overdraft protection: Can go negative up to -\$100 (with \$35 fee)

**BusinessAccount**
- Minimum balance: \$1000
- Monthly fee: \$15
- Interest rate: 1.5% annual
- No withdrawal limit
- Transaction fee: \$0.50 per transaction after 50 transactions/month

**StudentAccount** (inherits from SavingsAccount)
- Minimum balance: \$0
- Monthly fee: \$0
- Interest rate: 1.5% annual
- Withdrawal limit: 10 per month
- Age restriction: Account holder must be student

### 3. Customer Class
Create a `Customer` class with:
- Attributes: customer_id, name, email, accounts (list)
- Methods:
  - `add_account(account)` - open new account
  - `close_account(account_number)` - close account
  - `get_total_balance()` - sum of all account balances
  - `get_all_accounts()` - return list of all accounts
  - `transfer(from_account, to_account, amount)` - move money between accounts

### 4. Bank Class
Create a `Bank` class that:
- Manages all customers and accounts
- Assigns account numbers
- Processes monthly maintenance (fees and interest)
- Generates reports
- Methods:
  - `create_customer(name, email)` - create new customer
  - `find_customer(customer_id)` - find customer by ID
  - `open_account(customer_id, account_type)` - open account for customer
  - `process_monthly_maintenance()` - apply fees and interest to all accounts
  - `get_total_assets()` - sum of all balances
  - `generate_report()` - display bank statistics

### 5. Transaction Class
Create a `Transaction` class to track:
- Transaction ID
- Date/time
- Transaction type (deposit, withdrawal, transfer, fee, interest)
- Amount
- Balance after transaction

## Sample Usage
```python
# Create bank
bank = Bank("First National Bank")

# Create customer
customer = bank.create_customer("John Doe", "john@email.com")

# Open accounts
savings = bank.open_account(customer.customer_id, "savings")
checking = bank.open_account(customer.customer_id, "checking")

# Perform transactions
savings.deposit(1000)
checking.deposit(500)
checking.withdraw(50)

# Transfer money
customer.transfer(savings, checking, 200)

# Check balances
print(f"Savings: ${savings.get_balance()}")
print(f"Checking: ${checking.get_balance()}")

# Monthly maintenance
bank.process_monthly_maintenance()
```

## Bonus Features
- Add credit card accounts
- Implement loan accounts
- Add transaction categories
- Create account statements
- Add fraud detection
- Implement direct deposit
- Add bill payment system

## Testing Requirements
Your implementation should:
1. Create multiple customers
2. Open different account types
3. Perform various transactions
4. Test withdrawal limits
5. Test minimum balance violations
6. Test overdraft protection
7. Calculate and apply interest
8. Generate transaction history
9. Test monthly maintenance
10. Generate bank reports

## Files to Create
- `accounts.py` - All account classes
- `customer.py` - Customer class
- `bank.py` - Bank management
- `transaction.py` - Transaction tracking
- `main.py` - Demo program
- `README.md` - This file

Good luck building your bank! 💰
