"""
Python Loops - Examples
Run this to see for and while loops in action!
"""

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("="*60)
    print("EXAMPLE 1: Basic for Loop")
    print("="*60)
    for i in range(5):
        print(f"Count: {i}")
    print()

    print("="*60)
    print("EXAMPLE 2: Iterating Over List")
    print("="*60)
    fruits = ["apple", "banana", "orange"]
    for fruit in fruits:
        print(f"I like {fruit}")
    print()

    print("="*60)
    print("EXAMPLE 3: while Loop")
    print("="*60)
    count = 1
    while count <= 5:
        print(f"Count: {count}")
        count += 1
    print()

    print("="*60)
    print("EXAMPLE 4: break Statement")
    print("="*60)
    for i in range(10):
        if i == 5:
            print("Breaking at 5")
            break
        print(i)
    print()

    print("="*60)
    print("EXAMPLE 5: continue Statement")
    print("="*60)
    for i in range(10):
        if i % 2 == 0:
            continue  # Skip even numbers
        print(i)
    print()

    print("="*60)
    print("EXAMPLE 6: range() Function")
    print("="*60)
    print("range(5):", end=" ")
    for i in range(5):
        print(i, end=" ")
    print("\nrange(2, 8):", end=" ")
    for i in range(2, 8):
        print(i, end=" ")
    print("\nrange(0, 10, 2):", end=" ")
    for i in range(0, 10, 2):
        print(i, end=" ")
    print("\n")

    print("="*60)
    print("EXAMPLE 7: enumerate()")
    print("="*60)
    fruits = ["apple", "banana", "orange"]
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    print()

    print("="*60)
    print("EXAMPLE 8: Dictionary Iteration")
    print("="*60)
    person = {"name": "Alice", "age": 30, "city": "NYC"}
    for key, value in person.items():
        print(f"{key}: {value}")
    print()

    print("="*60)
    print("EXAMPLE 9: Nested Loops")
    print("="*60)
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i}x{j}={i*j}", end="  ")
        print()
    print()

    print("="*60)
    print("EXAMPLE 10: Loop with else")
    print("="*60)
    for i in range(5):
        if i == 10:
            break
    else:
        print("Loop completed without break")
    print()

    print("="*60)
    print("EXAMPLE 11: Sum of Numbers")
    print("="*60)
    total = 0
    for num in [1, 2, 3, 4, 5]:
        total += num
    print(f"Sum: {total}")
    print()

    print("="*60)
    print("EXAMPLE 12: Factorial")
    print("="*60)
    n = 5
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(f"{n}! = {factorial}")
    print()

    print("="*60)
    print("EXAMPLE 13: zip() Function")
    print("="*60)
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")
    print()

    print("="*60)
    print("EXAMPLE 14: List Comprehension (Bonus)")
    print("="*60)
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")
    print()

    print("="*60)
    print("EXAMPLE 15: Pattern Printing")
    print("="*60)
    for i in range(1, 6):
        print("*" * i)
    print()

    print("All examples completed!")
