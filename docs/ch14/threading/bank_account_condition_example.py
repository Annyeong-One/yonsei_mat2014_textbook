"""
Thread Synchronization: Bank Account with Condition Variables

A practical example of thread coordination using threading.Condition.
Multiple depositor and withdrawer threads operate on a shared bank
account, with withdrawals waiting until sufficient funds are available.

Topics covered:
- threading.Condition for wait/notify coordination
- Producer-consumer pattern (depositors produce, withdrawers consume)
- threading.Lock for mutual exclusion
- ThreadPoolExecutor for managing thread pools
- Thread-safe balance updates

Based on concepts from Python-100-Days example21 and ch14/threading materials.
"""

import threading
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep


# =============================================================================
# Example 1: Thread-Safe Bank Account
# =============================================================================

class BankAccount:
    """A bank account with thread-safe deposit and withdrawal.

    Uses threading.Condition (which wraps a Lock) to coordinate:
    - Deposits: add money and notify waiting withdrawals
    - Withdrawals: wait until sufficient balance is available
    """

    def __init__(self, initial_balance: float = 0.0):
        self._balance = initial_balance
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        """Deposit money and notify any waiting withdrawals.

        After depositing, notify_all() wakes up threads that
        are waiting in withdraw() so they can re-check balance.
        """
        with self._condition:
            self._balance += amount
            self._condition.notify_all()  # Wake up waiting withdrawers

    def withdraw(self, amount: float) -> None:
        """Withdraw money, waiting if balance is insufficient.

        The while loop re-checks the condition after being notified,
        because another thread might have consumed the funds first
        (spurious wakeup protection).
        """
        with self._condition:
            while amount > self._balance:
                self._condition.wait()  # Release lock and wait
            self._balance -= amount


# =============================================================================
# Example 2: Depositor and Withdrawer Workers
# =============================================================================

def depositor(account: BankAccount, name: str, rounds: int = 5) -> None:
    """Worker that makes random deposits."""
    for i in range(rounds):
        amount = randint(50, 200)
        account.deposit(amount)
        print(f"  {name} deposited ${amount:>3} -> balance: ${account.balance:.0f}")
        sleep(0.1)


def withdrawer(account: BankAccount, name: str, rounds: int = 3) -> None:
    """Worker that makes random withdrawals (waits if insufficient funds)."""
    for i in range(rounds):
        amount = randint(100, 300)
        print(f"  {name} wants to withdraw ${amount}...")
        account.withdraw(amount)
        print(f"  {name} withdrew  ${amount:>3} -> balance: ${account.balance:.0f}")
        sleep(0.2)


# =============================================================================
# Example 3: Running the Simulation
# =============================================================================

def run_simulation():
    """Run the bank account simulation with multiple threads."""
    print("=== Bank Account Thread Simulation ===")
    print("3 depositors (5 rounds each) + 3 withdrawers (3 rounds each)")
    print()

    account = BankAccount(initial_balance=100)
    print(f"Initial balance: ${account.balance:.0f}")
    print()

    with ThreadPoolExecutor(max_workers=6) as pool:
        # Submit depositor tasks
        for i in range(3):
            pool.submit(depositor, account, f"Depositor-{i+1}")
        # Submit withdrawer tasks
        for i in range(3):
            pool.submit(withdrawer, account, f"Withdrawer-{i+1}")

    print(f"\nFinal balance: ${account.balance:.0f}")
    print()


# =============================================================================
# Example 4: Understanding Condition vs Lock
# =============================================================================

def demo_condition_vs_lock():
    """Explain when to use Condition vs plain Lock."""
    print("=== Condition vs Lock ===")
    print("""
    threading.Lock:
      - Mutual exclusion only
      - One thread at a time in critical section
      - Use when: protecting shared data from concurrent access

    threading.Condition:
      - Mutual exclusion + wait/notify
      - Threads can WAIT for a condition to become true
      - Other threads NOTIFY when condition might have changed
      - Use when: threads need to coordinate (producer-consumer)

    Pattern:
      # Waiting thread:
      with condition:
          while not ready:      # Always use while (not if)
              condition.wait()  # Releases lock, blocks, reacquires lock
          # ... proceed ...

      # Notifying thread:
      with condition:
          # ... make changes ...
          condition.notify_all()  # Wake up waiting threads
    """)


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    run_simulation()
    demo_condition_vs_lock()
