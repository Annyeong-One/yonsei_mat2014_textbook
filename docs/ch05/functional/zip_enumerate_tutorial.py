"""
02_zip_enumerate_functions.py - zip() and enumerate()
"""

print("=" * 70)
print("ZIP() AND ENUMERATE() FUNCTIONS")
print("=" * 70)

# zip() - Combine multiple iterables
print("\n1. zip() - Combine Iterables")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Cities: {cities}")

# Zip them together
combined = list(zip(names, ages, cities))
print(f"\nzipped: {combined}")

# Iterate over zipped data
print("\nIterating:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} is {age} years old and lives in {city}")

# Unzipping
print("\nUnzipping:")
pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names, ages = zip(*pairs)  # * unpacks the list
print(f"Names: {names}")
print(f"Ages: {ages}")

# enumerate() - Add index to iterable
print("\n2. enumerate() - Add Index")
fruits = ["apple", "banana", "cherry"]

print("Without enumerate:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

print("\nWith enumerate:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

print("\nWith enumerate (start=1):")
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}: {fruit}")

# Practical Examples
print("\n" + "=" * 70)
print("PRACTICAL EXAMPLES")
print("=" * 70)

# Example 1: Create dictionary from two lists
print("\nExample 1: Lists to Dictionary")
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = dict(zip(keys, values))
print(f"Dictionary: {person}")

# Example 2: Parallel iteration with enumerate
print("\nExample 2: Numbered list with enumerate")
tasks = ["Buy groceries", "Call mom", "Finish homework"]
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# Example 3: Find index of matching items
print("\nExample 3: Find indices")
numbers = [10, 25, 30, 15, 40]
for i, num in enumerate(numbers):
    if num > 20:
        print(f"  Index {i}: {num} > 20")

print("\nSee exercises.py for practice!")
