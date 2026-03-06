# Python Comprehensions - Exercises

## Part 1: List Comprehensions

### Exercise 1: Basic Transformation
Create a list of the first 10 cube numbers (1³, 2³, 3³, ..., 10³)

### Exercise 2: String Manipulation
Given a list of names, create a new list with each name in lowercase.
```python
names = ['ALICE', 'Bob', 'CHARLIE', 'diana', 'EVE']
# Expected: ['alice', 'bob', 'charlie', 'diana', 'eve']
```

### Exercise 3: Filtering
From the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing only:
1. Odd numbers
2. Numbers divisible by 3
3. Numbers greater than 5

### Exercise 4: Conditional Transformation
Given a list of temperatures in Celsius, convert to Fahrenheit. If the temperature is below 0°C, set it to "Freezing".
```python
celsius = [25, -5, 15, -10, 30, 0]
# Formula: F = C * 9/5 + 32
# Expected: [77.0, 'Freezing', 59.0, 'Freezing', 86.0, 32.0]
```

### Exercise 5: Working with Strings
Extract all vowels from the sentence "Python Programming is Fun"
```python
# Expected: ['o', 'o', 'a', 'i', 'i', 'u']
```

### Exercise 6: List of Tuples
Given two lists, create a list of tuples combining them:
```python
subjects = ['Math', 'Science', 'English']
scores = [85, 92, 88]
# Expected: [('Math', 85), ('Science', 92), ('English', 88)]
```

### Exercise 7: Nested List Comprehension
Create a 5x5 matrix where each cell contains the sum of its row and column indices.
```python
# Expected:
# [[0, 1, 2, 3, 4],
#  [1, 2, 3, 4, 5],
#  [2, 3, 4, 5, 6],
#  [3, 4, 5, 6, 7],
#  [4, 5, 6, 7, 8]]
```

### Exercise 8: Flattening
Flatten this nested list: `[[1, 2, 3], [4, 5], [6, 7, 8, 9]]`

### Exercise 9: Multiple Conditions
From numbers 1 to 50, get all numbers that are:
- Divisible by 3 OR divisible by 5
- BUT NOT divisible by both 3 AND 5

### Exercise 10: String Processing
Given a list of words, create a list containing only words that:
- Start with a vowel
- Have more than 3 characters
- Convert them to uppercase
```python
words = ['apple', 'cat', 'elephant', 'dog', 'orange', 'ant', 'umbrella']
```

## Part 2: Dictionary Comprehensions

### Exercise 11: Create Character Count
Given a string, create a dictionary with each unique character as the key and its count as the value.
```python
text = "hello world"
# Expected: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

### Exercise 12: Square Dictionary
Create a dictionary where keys are numbers 1-10 and values are their squares.

### Exercise 13: Filter Dictionary
Given a dictionary of products and prices, create a new dictionary with only products under \$50.
```python
products = {'laptop': 1200, 'mouse': 25, 'keyboard': 75, 'monitor': 300, 'cable': 15}
# Expected: {'mouse': 25, 'cable': 15}
```

### Exercise 14: Transform Values
Given a dictionary of names and ages, create a new dictionary with ages increased by 1.
```python
ages = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
# Expected: {'Alice': 26, 'Bob': 31, 'Charlie': 36}
```

### Exercise 15: Swap Keys and Values
Reverse the mapping of this dictionary:
```python
grade_letters = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
# Expected: {90: 'A', 80: 'B', 70: 'C', 60: 'D'}
```

### Exercise 16: Combine Lists into Dictionary
Create a dictionary from these lists where fruits are keys and colors are values:
```python
fruits = ['apple', 'banana', 'cherry', 'date']
colors = ['red', 'yellow', 'red', 'brown']
# Expected: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown'}
```

### Exercise 17: Conditional Dictionary
From a list of words, create a dictionary where:
- Key is the word
- Value is "short" if length ≤ 5, "long" if length > 5
```python
words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
```

### Exercise 18: Nested Dictionary
Create a grade book for 3 students and 3 subjects, initialized to 0:
```python
students = ['Alice', 'Bob', 'Charlie']
subjects = ['Math', 'Science', 'English']
# Expected: {'Alice': {'Math': 0, 'Science': 0, 'English': 0}, ...}
```

## Part 3: Set Comprehensions

### Exercise 19: Unique Squares
From the list [1, 2, 3, 4, 5, 2, 3, 4, 5, 6], create a set of unique squares.

### Exercise 20: First Letters
Extract the first letter of each word (unique) from:
```python
sentence = "the quick brown fox jumps over the lazy dog"
# Expected: {'t', 'q', 'b', 'f', 'j', 'o', 'l', 'd'}
```

### Exercise 21: Unique Lengths
From a list of words, create a set of unique word lengths:
```python
words = ['cat', 'elephant', 'dog', 'bird', 'butterfly', 'ant']
```

### Exercise 22: Even Numbers Set
Create a set of even numbers from 1 to 20.

### Exercise 23: Common Factors
Find all unique factors of both 24 and 36 using a set comprehension.

## Part 4: Generator Expressions

### Exercise 24: Sum of Squares
Calculate the sum of squares of numbers 1 to 1000 using a generator expression.

### Exercise 25: Memory Efficiency
Create a generator that yields the first 1 million even numbers, then find their sum.

### Exercise 26: File Processing Simulation
Create a generator that yields lengths of words in this list:
```python
words = ['python', 'is', 'awesome', 'and', 'powerful']
# Don't convert to list - iterate directly to find the maximum length
```

### Exercise 27: Filtering with Generator
Use a generator expression to find if any number from 1-100 is divisible by 7 and 11.

### Exercise 28: Large Dataset
Create a generator for the first 10000 numbers, filter for numbers divisible by 17, and get the sum.

## Part 5: Mixed Comprehensions

### Exercise 29: Grade Analysis
Given student scores, create:
1. A list of students who passed (score ≥ 70)
2. A dictionary of student names and their letter grades (A: 90+, B: 80-89, C: 70-79, F: <70)
3. A set of unique letter grades in the class

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
scores = [92, 85, 67, 78, 95, 71]
```

### Exercise 30: Data Transformation
From this data, create:
1. A list of tuples (name, salary_after_raise) where raise is 10%
2. A dictionary of employees earning over \$50,000 after raise
3. A set of unique salary brackets (e.g., "40k-50k", "50k-60k")

```python
employees = ['Alice', 'Bob', 'Charlie', 'Diana']
salaries = [45000, 52000, 38000, 61000]
```

### Exercise 31: Text Analysis
From a paragraph:
1. List of words longer than 4 letters (lowercase)
2. Dictionary of word: length for words starting with 't'
3. Set of unique word lengths
4. Generator that yields words containing 'e'

```python
text = "The quick brown fox jumps over the lazy dog in the garden"
```

### Exercise 32: Number Analysis
For numbers 1-100:
1. List of perfect squares
2. Dictionary of number: [divisors] for numbers divisible by 6
3. Set of prime numbers (numbers with exactly 2 divisors)
4. Generator expression to find sum of all primes

## Challenge Exercises

### Challenge 33: Cartesian Product
Create all possible coordinates (x, y) where x ranges from 0-2 and y ranges from 0-2, but exclude (1, 1).

### Challenge 34: Matrix Transpose
Given a matrix, transpose it using comprehensions:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Challenge 35: Fibonacci Generator
Create a generator that yields Fibonacci numbers up to n:
```python
def fibonacci_gen(n):
    # Your code here
    pass

# list(fibonacci_gen(10)) should give first 10 Fibonacci numbers
```

### Challenge 36: Dictionary Merge
Given two dictionaries, merge them. If a key exists in both, sum the values:
```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
# Expected: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
```

### Challenge 37: Nested Filter
From this nested structure, extract all even numbers:
```python
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
# Expected: [2, 4, 6, 8, 10]
```

### Challenge 38: Word Frequency (Top 5)
Given a sentence, create a dictionary of the 5 most common words and their counts:
```python
sentence = "the quick brown fox jumps over the lazy dog the fox was quick"
```

### Challenge 39: Spiral Matrix
Create a 3x3 matrix using comprehensions that follows this pattern:
```
1 2 3
8 9 4
7 6 5
```

### Challenge 40: Complex Filter
From a list of dictionaries representing people, use comprehensions to:
1. Get names of people over 25
2. Create {name: age} for people with names starting with 'A'
3. Get unique ages as a set
4. Calculate average age using generator

```python
people = [
    {'name': 'Alice', 'age': 28, 'city': 'NYC'},
    {'name': 'Bob', 'age': 32, 'city': 'LA'},
    {'name': 'Charlie', 'age': 25, 'city': 'Chicago'},
    {'name': 'Amanda', 'age': 30, 'city': 'Boston'},
    {'name': 'David', 'age': 28, 'city': 'Seattle'}
]
```

## Bonus: Performance Challenge

### Challenge 41: Benchmark
Compare the performance of:
1. Regular loop
2. List comprehension
3. Generator expression

For calculating the sum of squares of numbers 1-10000.

### Challenge 42: Memory Challenge
Create a function that processes 1 million numbers:
- Using list comprehension
- Using generator expression
Compare memory usage and determine when each is appropriate.
