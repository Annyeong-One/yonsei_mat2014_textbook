"""
Python Recursion - Examples
See recursion in action with these demonstrations!
"""

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("="*60)
    print("EXAMPLE 1: Simple Countdown")
    print("="*60)

    def countdown(n):
        if n <= 0:
            print("Blastoff!")
        else:
            print(n)
            countdown(n - 1)

    countdown(5)
    print()

    print("="*60)
    print("EXAMPLE 2: Factorial")
    print("="*60)

    def factorial(n):
        """Calculate n! recursively"""
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print(f"5! = {factorial(5)}")
    print(f"7! = {factorial(7)}")
    print()

    print("="*60)
    print("EXAMPLE 3: Fibonacci Sequence")
    print("="*60)

    def fibonacci(n):
        """Return nth Fibonacci number"""
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
    print()

    print("="*60)
    print("EXAMPLE 4: Sum of Numbers")
    print("="*60)

    def sum_numbers(n):
        """Sum numbers from 1 to n"""
        if n == 0:
            return 0
        return n + sum_numbers(n - 1)

    print(f"Sum 1 to 10: {sum_numbers(10)}")
    print(f"Sum 1 to 100: {sum_numbers(100)}")
    print()

    print("="*60)
    print("EXAMPLE 5: Power Function")
    print("="*60)

    def power(base, exp):
        """Calculate base^exp recursively"""
        if exp == 0:
            return 1
        return base * power(base, exp - 1)

    print(f"2^5 = {power(2, 5)}")
    print(f"3^4 = {power(3, 4)}")
    print()

    print("="*60)
    print("EXAMPLE 6: Reverse a String")
    print("="*60)

    def reverse_string(s):
        """Reverse string recursively"""
        if len(s) <= 1:
            return s
        return s[-1] + reverse_string(s[:-1])

    print(f"'hello' reversed: {reverse_string('hello')}")
    print(f"'Python' reversed: {reverse_string('Python')}")
    print()

    print("="*60)
    print("EXAMPLE 7: Sum of List")
    print("="*60)

    def sum_list(numbers):
        """Sum all numbers in list"""
        if len(numbers) == 0:
            return 0
        return numbers[0] + sum_list(numbers[1:])

    print(f"Sum of [1,2,3,4,5]: {sum_list([1,2,3,4,5])}")
    print(f"Sum of [10,20,30]: {sum_list([10,20,30])}")
    print()

    print("="*60)
    print("EXAMPLE 8: Count Occurrences")
    print("="*60)

    def count_occurrences(lst, target):
        """Count how many times target appears in list"""
        if len(lst) == 0:
            return 0
        count = 1 if lst[0] == target else 0
        return count + count_occurrences(lst[1:], target)

    numbers = [1, 2, 3, 2, 4, 2, 5]
    print(f"List: {numbers}")
    print(f"Count of 2: {count_occurrences(numbers, 2)}")
    print()

    print("="*60)
    print("EXAMPLE 9: Greatest Common Divisor (GCD)")
    print("="*60)

    def gcd(a, b):
        """Calculate GCD using Euclidean algorithm"""
        if b == 0:
            return a
        return gcd(b, a % b)

    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"GCD(100, 35) = {gcd(100, 35)}")
    print()

    print("="*60)
    print("EXAMPLE 10: Binary Search")
    print("="*60)

    def binary_search(arr, target, left, right):
        """Search for target in sorted array"""
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, left, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, right)

    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"Array: {sorted_array}")
    print(f"Search for 7: index {binary_search(sorted_array, 7, 0, len(sorted_array)-1)}")
    print(f"Search for 13: index {binary_search(sorted_array, 13, 0, len(sorted_array)-1)}")
    print(f"Search for 6: index {binary_search(sorted_array, 6, 0, len(sorted_array)-1)}")
    print()

    print("="*60)
    print("EXAMPLE 11: Palindrome Checker")
    print("="*60)

    def is_palindrome(s):
        """Check if string is palindrome"""
        # Remove spaces and convert to lowercase
        s = s.lower().replace(" ", "")

        # Base cases
        if len(s) <= 1:
            return True

        # Check first and last character
        if s[0] != s[-1]:
            return False

        # Recurse on middle part
        return is_palindrome(s[1:-1])

    print(f"'racecar' is palindrome: {is_palindrome('racecar')}")
    print(f"'hello' is palindrome: {is_palindrome('hello')}")
    print(f"'A man a plan a canal Panama' is palindrome: {is_palindrome('A man a plan a canal Panama')}")
    print()

    print("="*60)
    print("EXAMPLE 12: Flatten Nested List")
    print("="*60)

    def flatten(nested_list):
        """Flatten a nested list"""
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"Nested: {nested}")
    print(f"Flattened: {flatten(nested)}")
    print()

    print("="*60)
    print("EXAMPLE 13: Print All Permutations")
    print("="*60)

    def permutations(s):
        """Generate all permutations of string"""
        if len(s) <= 1:
            return [s]

        result = []
        for i, char in enumerate(s):
            rest = s[:i] + s[i+1:]
            for perm in permutations(rest):
                result.append(char + perm)
        return result

    print(f"Permutations of 'ABC': {permutations('ABC')}")
    print()

    print("="*60)
    print("EXAMPLE 14: Tower of Hanoi")
    print("="*60)

    def tower_of_hanoi(n, source, destination, auxiliary):
        """Solve Tower of Hanoi puzzle"""
        if n == 1:
            print(f"Move disk 1 from {source} to {destination}")
            return

        tower_of_hanoi(n-1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n-1, auxiliary, destination, source)

    print("Tower of Hanoi with 3 disks:")
    tower_of_hanoi(3, 'A', 'C', 'B')
    print()

    print("="*60)
    print("EXAMPLE 15: Fibonacci with Memoization")
    print("="*60)

    def fibonacci_memo(n, memo=None):
        """Optimized Fibonacci with memoization"""
        if memo is None:
            memo = {}

        if n in memo:
            return memo[n]

        if n <= 1:
            return n

        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        return memo[n]

    print("Computing Fibonacci(30) with memoization:")
    print(f"F(30) = {fibonacci_memo(30)}")
    print(f"F(40) = {fibonacci_memo(40)}")
    print("(Much faster than regular recursion!)")
    print()

    print("="*60)
    print("EXAMPLE 16: Count Digits")
    print("="*60)

    def count_digits(n):
        """Count number of digits"""
        if n < 10:
            return 1
        return 1 + count_digits(n // 10)

    print(f"Digits in 12345: {count_digits(12345)}")
    print(f"Digits in 987654321: {count_digits(987654321)}")
    print()

    print("="*60)
    print("EXAMPLE 17: Digital Root")
    print("="*60)

    def digital_root(n):
        """Find digital root (sum digits until single digit)"""
        if n < 10:
            return n

        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10

        return digital_root(digit_sum)

    print(f"Digital root of 38: {digital_root(38)}")  # 3+8=11, 1+1=2
    print(f"Digital root of 1234: {digital_root(1234)}")  # 1+2+3+4=10, 1+0=1
    print()

    print("="*60)
    print("EXAMPLE 18: List Maximum")
    print("="*60)

    def find_max(lst):
        """Find maximum in list recursively"""
        if len(lst) == 1:
            return lst[0]

        max_of_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

    numbers = [3, 7, 2, 9, 1, 5, 8]
    print(f"List: {numbers}")
    print(f"Maximum: {find_max(numbers)}")
    print()

    print("="*60)
    print("EXAMPLE 19: String to Integer")
    print("="*60)

    def string_to_int(s):
        """Convert string to integer recursively"""
        if len(s) == 1:
            return int(s)
        return int(s[0]) * (10 ** (len(s)-1)) + string_to_int(s[1:])

    print(f"'1234' to int: {string_to_int('1234')}")
    print(f"'987' to int: {string_to_int('987')}")
    print()

    print("="*60)
    print("EXAMPLE 20: Recursive vs Iterative Comparison")
    print("="*60)

    def sum_recursive(n):
        """Sum 1 to n recursively"""
        if n == 0:
            return 0
        return n + sum_recursive(n - 1)

    def sum_iterative(n):
        """Sum 1 to n iteratively"""
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    n = 10
    print(f"Sum 1 to {n}:")
    print(f"  Recursive: {sum_recursive(n)}")
    print(f"  Iterative: {sum_iterative(n)}")
    print(f"  Both give same result!")
    print()

    print("="*60)
    print("All examples completed!")
    print("="*60)
    print("\nKey Insights:")
    print("• Recursion breaks problems into smaller pieces")
    print("• Always need a base case to stop")
    print("• Recursive case moves toward base case")
    print("• Many problems have both recursive and iterative solutions")
    print("• Memoization can dramatically improve performance")
    print("• Choose recursion when it makes code clearer")
