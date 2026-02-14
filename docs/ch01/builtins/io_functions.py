"""
01_input_output_functions.py

TOPIC: Input and Output Built-in Functions
LEVEL: Basic
DURATION: 30-45 minutes

LEARNING OBJECTIVES:
1. Master the print() function and its parameters
2. Use input() to read user data
3. Format output using f-strings and format()
4. Handle basic input validation

KEY FUNCTIONS:
- print() - Output data to console
- input() - Read user input as string
- format() - Format strings (older method)
"""

# ============================================================================
# SECTION 1: The print() Function
# ============================================================================

print("=" * 70)
print("SECTION 1: The print() Function")
print("=" * 70)

# Basic usage - print() outputs to console
print("Hello, World!")
print("Python is awesome!")

# print() can take multiple arguments
print("Name:", "Alice", "Age:", 25)

# By default, print() adds a space between arguments
print("One", "Two", "Three")  # Output: One Two Three

# The sep parameter changes the separator
print("One", "Two", "Three", sep=", ")  # Output: One, Two, Three
print("2025", "11", "12", sep="-")      # Output: 2025-11-12
print("A", "B", "C", sep="")            # Output: ABC

# The end parameter changes what's printed at the end (default is newline)
print("Hello", end=" ")
print("World")  # Output: Hello World (on same line)

print("Loading", end="...")
print("Done!")  # Output: Loading...Done!

# Reset to normal
print()  # Empty print() just prints a newline

# ============================================================================
# SECTION 2: Formatting Output
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 2: Formatting Output")
print("=" * 70)

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# f-strings can include expressions
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}")

# Formatting numbers in f-strings
pi = 3.14159265359
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi to 4 decimal places: {pi:.4f}")

price = 1234.5
print(f"Price: ${price:,.2f}")  # Adds thousand separators

# Method 2: format() method
print("My name is {} and I am {} years old".format(name, age))
print("Sum: {} + {} = {}".format(x, y, x + y))

# Method 3: % formatting (old style, not recommended)
print("My name is %s and I am %d years old" % (name, age))

print("""
BEST PRACTICE: Use f-strings for readability and performance
""")

# ============================================================================
# SECTION 3: The input() Function
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 3: The input() Function")
print("=" * 70)

# input() reads user input as a STRING
# Note: Uncomment the lines below to test interactively

# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# IMPORTANT: input() ALWAYS returns a string
# age_str = input("Enter your age: ")
# print(f"Type of input: {type(age_str)}")  # <class 'str'>

# To use as number, you must convert it
# age = int(input("Enter your age: "))
# print(f"Next year you'll be {age + 1}")

# For demonstration without user interaction:
print("\nDemonstration (simulated input):")
print('>>> name = input("Enter your name: ")')
print('User enters: Alice')
name = "Alice"  # Simulating input
print(f"Hello, {name}!")

# ============================================================================
# SECTION 4: Common Patterns
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 4: Common Input/Output Patterns")
print("=" * 70)

# Pattern 1: Prompt and store
print("\nPattern 1: Simple input and response")
print('name = input("What is your name? ")')
print('print(f"Nice to meet you, {name}!")')

# Pattern 2: Input validation (basic)
print("\nPattern 2: Input validation")
print("""
while True:
    age_str = input("Enter your age: ")
    if age_str.isdigit():  # Check if all characters are digits
        age = int(age_str)
        break
    else:
        print("Please enter a valid number")
""")

# Pattern 3: Multiple inputs
print("\nPattern 3: Multiple inputs")
print('first_name = input("First name: ")')
print('last_name = input("Last name: ")')
print('full_name = f"{first_name} {last_name}"')

# Pattern 4: Yes/No questions
print("\nPattern 4: Yes/No questions")
print("""
response = input("Do you want to continue? (y/n): ")
if response.lower() == 'y':
    print("Continuing...")
else:
    print("Exiting...")
""")

# ============================================================================
# SECTION 5: Print() Advanced Features
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 5: Advanced print() Features")
print("=" * 70)

# Printing to files (instead of console)
print("\nPrinting to a file:")
print("""
with open('output.txt', 'w') as f:
    print("This goes to a file", file=f)
    print("So does this", file=f)
""")

# Printing special characters
print("\nSpecial characters in strings:")
print("Tab:\tIndented text")
print("Newline:\nNew line")
print("Quote: \"Hello\"")
print("Backslash: C:\\Users\\Documents")

# Raw strings (don't interpret escape sequences)
print("\nRaw strings (r prefix):")
print(r"This is a raw string: \n is not a newline")

# ============================================================================
# SECTION 6: Practical Examples
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 6: Practical Examples")
print("=" * 70)

# Example 1: Simple calculator prompt
print("\nExample 1: Calculator")
print("Simulating: num1 = 10, num2 = 5")
num1, num2 = 10, 5
result = num1 + num2
print(f"{num1} + {num2} = {result}")

# Example 2: Receipt formatting
print("\nExample 2: Receipt")
item1, price1 = "Apple", 1.50
item2, price2 = "Banana", 0.75
item3, price3 = "Orange", 2.00

print("-" * 30)
print("RECEIPT")
print("-" * 30)
print(f"{item1:<20} ${price1:>6.2f}")
print(f"{item2:<20} ${price2:>6.2f}")
print(f"{item3:<20} ${price3:>6.2f}")
print("-" * 30)
total = price1 + price2 + price3
print(f"{'TOTAL':<20} ${total:>6.2f}")
print("-" * 30)

# Example 3: Progress indicator
print("\nExample 3: Progress indicator")
for i in range(5):
    print(f"Processing... {i+1}/5", end="\r")
    import time
    time.sleep(0.3)
print("\nComplete!              ")  # Extra spaces to clear the line

# ============================================================================
# SECTION 7: Common Mistakes and Solutions
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 7: Common Mistakes")
print("=" * 70)

print("""
MISTAKE 1: Forgetting that input() returns a string
  Wrong:  age = input("Age: ")
          age = age + 1  # TypeError!
  Right:  age = int(input("Age: "))
          age = age + 1

MISTAKE 2: Not handling invalid input
  Wrong:  age = int(input("Age: "))  # Crashes if user enters "abc"
  Right:  Use try/except or validation

MISTAKE 3: Confusion with print() return value
  Wrong:  x = print("Hello")  # x is None!
  Right:  print() displays output but returns None

MISTAKE 4: Concatenating wrong types
  Wrong:  print("Age: " + 25)  # TypeError!
  Right:  print("Age: " + str(25))
  Better: print(f"Age: {25}")
""")

# ============================================================================
# SECTION 8: Key Takeaways
# ============================================================================

print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)

print("""
1. print() displays output to console (or file)
2. print() can take multiple arguments, separated by sep
3. Use end parameter to control what's printed at the end
4. input() ALWAYS returns a string - convert if needed
5. f-strings are the modern, preferred way to format output
6. Format numbers with {value:.2f} for decimals
7. Always validate user input before using it
8. print() returns None (doesn't return the string)
9. Use help(print) and help(input) to learn more
10. Practice is key - try different formatting options!

BEST PRACTICES:
- Use f-strings for formatting (readable and fast)
- Always convert input() to appropriate type
- Validate user input before processing
- Use descriptive prompts in input()
- Format numbers consistently (decimal places)
""")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
1. Write a program that asks for name and age, then prints:
   "Hello [name], you will be [age+1] next year"

2. Create a program that asks for 3 numbers and prints their sum and average

3. Format a table showing 5 products with names and prices, aligned nicely

4. Ask user for temperature in Celsius, convert to Fahrenheit, display result

5. Create a mad libs program (ask for nouns, verbs, adjectives)

6. Print a pattern using loops and print(end='')

7. Validate age input: must be a number between 0 and 120

8. Create a receipt printer that formats prices with $ and 2 decimals

9. Print progress bar: [####------] 40%

10. Ask multiple questions and display summary at the end

See exercises.py for complete practice problems!
""")
