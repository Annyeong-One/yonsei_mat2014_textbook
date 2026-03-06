"""
Example 5: Callable Objects and Context Managers
Demonstrates: __call__, __enter__, __exit__
"""

import time


class Multiplier:
    """A callable class that multiplies by a factor."""
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Make the object callable."""
        return x * self.factor
    
    def __repr__(self):
        return f"Multiplier({self.factor})"


class Counter:
    """A callable counter that increments each time it's called."""
    
    def __init__(self, start=0):
        self.count = start
    
    def __call__(self):
        """Increment and return the count."""
        self.count += 1
        return self.count
    
    def reset(self):
        """Reset the counter."""
        self.count = 0
    
    def __repr__(self):
        return f"Counter(current={self.count})"


class Timer:
    """A context manager that times code execution."""
    
    def __init__(self, name="Code block"):
        self.name = name
        self.start_time = None
        self.elapsed_time = None
    
    def __enter__(self):
        """Start the timer when entering the context."""
        print(f"Starting timer for: {self.name}")
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop the timer when exiting the context."""
        self.elapsed_time = time.time() - self.start_time
        print(f"Finished: {self.name}")
        print(f"Time elapsed: {self.elapsed_time:.4f} seconds")
        
        # Return False to propagate any exceptions
        # Return True to suppress exceptions
        return False


class FileWriter:
    """A context manager for safe file writing."""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        """Open the file when entering the context."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the file when exiting the context."""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")
        
        return False  # Don't suppress exceptions


class DatabaseConnection:
    """A context manager simulating a database connection."""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        """Establish connection when entering context."""
        print(f"Connecting to database: {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection when exiting context."""
        print(f"Disconnecting from database: {self.db_name}")
        self.connected = False
        return False
    
    def execute(self, query):
        """Simulate executing a query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        print(f"Executing query: {query}")
        return f"Result of: {query}"


# Examples
if __name__ == "__main__":

    # ============================================================================
    print("=== Callable Objects: Multiplier ===")
    double = Multiplier(2)
    triple = Multiplier(3)
    
    print(f"double: {double}")
    print(f"double(5) = {double(5)}")
    print(f"double(10) = {double(10)}")
    
    print(f"\ntriple: {triple}")
    print(f"triple(5) = {triple(5)}")
    print(f"triple(10) = {triple(10)}")
    
    # Use in map
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(double, numbers))
    print(f"\nOriginal: {numbers}")
    print(f"Doubled: {doubled}")
    
    print("\n\n=== Callable Objects: Counter ===")
    counter = Counter()
    print(f"Counter: {counter}")
    
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print(f"Current state: {counter}")
    
    counter.reset()
    print(f"After reset: {counter}")
    print(f"Next call: {counter()}")
    
    print("\n\n=== Context Manager: Timer ===")
    with Timer("Example computation"):
        # Simulate some work
        total = 0
        for i in range(1000000):
            total += i
        print(f"Sum calculated: {total}")
    
    print("\n=== Context Manager: Timer with Variable ===")
    with Timer("Another task") as timer:
        time.sleep(0.1)  # Sleep for 100ms
    print(f"Recorded time: {timer.elapsed_time:.4f} seconds")
    
    print("\n\n=== Context Manager: FileWriter ===")
    # Note: In this example, we won't actually create a file
    # but show how it would work
    print("Example of file writing (demonstration):")
    print("with FileWriter('output.txt') as f:")
    print("    f.write('Hello, World!')")
    print("    f.write('This is a test.')")
    
    print("\n\n=== Context Manager: DatabaseConnection ===")
    with DatabaseConnection("mydb") as db:
        result1 = db.execute("SELECT * FROM users")
        print(f"Result: {result1}")
        
        result2 = db.execute("INSERT INTO users VALUES (1, 'Alice')")
        print(f"Result: {result2}")
    
    print("\n=== Multiple Context Managers ===")
    with Timer("Database operations"), DatabaseConnection("testdb") as db:
        db.execute("SELECT * FROM products")
        db.execute("UPDATE products SET price = 99.99")
    
    print("\n=== Combining Callable and Context Manager ===")
    
    class CallableTimer:
        """A class that's both callable and a context manager."""
        
        def __init__(self):
            self.times = []
        
        def __call__(self, duration):
            """Record a time when called."""
            self.times.append(duration)
            print(f"Recorded time: {duration:.4f}s")
        
        def __enter__(self):
            """Start timing."""
            self.start = time.time()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            """Calculate and record elapsed time."""
            elapsed = time.time() - self.start
            self(elapsed)  # Use __call__ to record
            return False
        
        def average(self):
            """Calculate average time."""
            return sum(self.times) / len(self.times) if self.times else 0
    
    timer_recorder = CallableTimer()
    
    # Use as context manager
    with timer_recorder:
        time.sleep(0.05)
    
    with timer_recorder:
        time.sleep(0.08)
    
    print(f"\nAverage time: {timer_recorder.average():.4f}s")
