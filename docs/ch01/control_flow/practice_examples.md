
# Practice Examples

These exercises demonstrate common loop patterns.

---

## Fibonacci Sequence

```python
def fibonacci(n):

    a,b = 0,1

    for _ in range(n):

        a,b = b,a+b

        print(a)
````

---

## Prime Numbers

```python
for num in range(2,100):

    for i in range(2,int(num**0.5)+1):

        if num%i==0:
            break

    else:
        print(num)
```

---

## Armstrong Numbers

```python
for num in range(100,1000):

    a = num//100
    b = num//10%10
    c = num%10

    if num == a**3 + b**3 + c**3:

        print(num)
```

## Exercises

**Exercise 1.**
Write a program that prints all even numbers from 1 to 20 using a `for` loop and the `range` function.

??? success "Solution to Exercise 1"
    ```python
    for i in range(2, 21, 2):
        print(i)
    ```

    Output:

    ```
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    ```

    `range(2, 21, 2)` starts at 2, ends before 21, and steps by 2. An alternative approach uses `range(1, 21)` with an `if i % 2 == 0` check inside the loop.

---

**Exercise 2.**
Trace the Fibonacci example above by hand for `n = 6`. Write out the values of `a` and `b` after each iteration and the value printed on each step.

??? success "Solution to Exercise 2"
    Initial values: `a = 0`, `b = 1`.

    | Iteration | Before: `a, b` | After `a, b = b, a+b` | Printed (`a`) |
    |-----------|----------------|------------------------|---------------|
    | 1         | 0, 1           | 1, 1                   | 1             |
    | 2         | 1, 1           | 1, 2                   | 1             |
    | 3         | 1, 2           | 2, 3                   | 2             |
    | 4         | 2, 3           | 3, 5                   | 3             |
    | 5         | 3, 5           | 5, 8                   | 5             |
    | 6         | 5, 8           | 8, 13                  | 8             |

    The printed sequence is: `1, 1, 2, 3, 5, 8`.

---

**Exercise 3.**
The prime number example uses a `for...else` construct. Rewrite the prime checker for a single number `n` **without** using `else` on the loop. Use a boolean flag variable instead.

??? success "Solution to Exercise 3"
    ```python
    n = 29
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime and n >= 2:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
    ```

    Output:

    ```
    29 is prime
    ```

    The flag `is_prime` starts as `True` and is set to `False` if any divisor is found. The `break` exits the loop early when a factor is discovered. This is functionally equivalent to the `for...else` pattern but uses an explicit boolean variable.

---

**Exercise 4.**
Write a program that finds all **perfect numbers** between 1 and 1000. A perfect number equals the sum of its proper divisors (divisors excluding itself). For example, $6 = 1 + 2 + 3$.

??? success "Solution to Exercise 4"
    ```python
    for num in range(1, 1001):
        divisor_sum = 0

        for i in range(1, num):
            if num % i == 0:
                divisor_sum += i

        if divisor_sum == num:
            print(num)
    ```

    Output:

    ```
    6
    28
    496
    ```

    For each candidate number, the inner loop sums all proper divisors. If the sum equals the number, it is perfect. The three perfect numbers below 1000 are 6, 28, and 496.

---

**Exercise 5.**
Explain why the Armstrong number example uses `a**3 + b**3 + c**3` specifically with the exponent 3. What would happen if you searched for four-digit Armstrong numbers? What exponent would you use?

??? success "Solution to Exercise 5"
    An Armstrong number (also called a narcissistic number) is a number where each digit is raised to the power equal to the **number of digits**, and the sum of those powers equals the original number.

    For three-digit numbers, there are 3 digits, so the exponent is 3. For example, $153 = 1^3 + 5^3 + 3^3$.

    For four-digit numbers, the exponent would be 4. The search would look like:

    ```python
    for num in range(1000, 10000):
        digits = str(num)
        if num == sum(int(d) ** 4 for d in digits):
            print(num)
    ```

    This prints `1634`, `8208`, and `9474` -- the three four-digit Armstrong numbers. The general pattern uses an exponent equal to `len(str(num))`.
