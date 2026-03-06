"""
Loop Practice Problems: Classic Algorithmic Exercises

A collection of practical loop exercises that strengthen understanding
of control flow, nested loops, and algorithmic thinking.

Problems covered:
1. Prime numbers under 100
2. Fibonacci sequence
3. Armstrong (narcissistic) numbers
4. Integer reversal using // and %
5. Hundred Chickens problem (exhaustive search)
6. CRAPS dice game (game loop with state)

Based on Python-100-Days Day07 practice problems.
"""

import random


# =============================================================================
# Problem 1: Prime Numbers Under 100
# =============================================================================

def primes_under_100() -> list[int]:
    """Find all prime numbers less than 100.

    A prime number is only divisible by 1 and itself.
    Optimization: only check divisors up to sqrt(n).

    >>> primes = primes_under_100()
    >>> primes[:5]
    [2, 3, 5, 7, 11]
    >>> len(primes)
    25
    """
    primes = []
    for num in range(2, 100):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# =============================================================================
# Problem 2: Fibonacci Sequence
# =============================================================================

def fibonacci(n: int) -> list[int]:
    """Generate the first n Fibonacci numbers.

    Each number is the sum of the two preceding ones: 1, 1, 2, 3, 5, 8, ...
    Uses tuple unpacking for clean simultaneous assignment: a, b = b, a + b

    >>> fibonacci(10)
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    result = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # Simultaneous assignment
        result.append(a)
    return result


# =============================================================================
# Problem 3: Armstrong (Narcissistic) Numbers
# =============================================================================

def armstrong_numbers() -> list[int]:
    """Find all 3-digit Armstrong numbers (100-999).

    An Armstrong number (narcissistic number) is an N-digit number equal
    to the sum of its digits each raised to the Nth power.
    For 3 digits: 153 = 1^3 + 5^3 + 3^3

    Key technique: digit extraction using // and %
    - ones digit:    num % 10
    - tens digit:    num // 10 % 10
    - hundreds digit: num // 100

    >>> armstrong_numbers()
    [153, 370, 371, 407]
    """
    result = []
    for num in range(100, 1000):
        ones = num % 10
        tens = num // 10 % 10
        hundreds = num // 100
        if num == ones ** 3 + tens ** 3 + hundreds ** 3:
            result.append(num)
    return result


# =============================================================================
# Problem 4: Integer Reversal
# =============================================================================

def reverse_integer(num: int) -> int:
    """Reverse the digits of a positive integer.

    Uses the // and % trick repeatedly:
    - num % 10 extracts the last digit
    - num // 10 removes the last digit
    - reversed = reversed * 10 + digit builds the reversed number

    >>> reverse_integer(12389)
    98321
    >>> reverse_integer(100)
    1
    """
    reversed_num = 0
    n = abs(num)
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num if num >= 0 else -reversed_num


# =============================================================================
# Problem 5: Hundred Chickens (Exhaustive Search)
# =============================================================================

def hundred_chickens() -> list[tuple[int, int, int]]:
    """Solve the Hundred Chickens problem using exhaustive search.

    Classic Chinese math problem (Zhang Qiujian, ~5th century):
    A rooster costs 5 coins, a hen costs 3 coins, and 3 chicks cost 1 coin.
    Buy exactly 100 birds with exactly 100 coins.
    How many roosters, hens, and chicks?

    Optimization: instead of 3 nested loops, derive the third variable
    from the constraint (rooster + hen + chick = 100).

    >>> solutions = hundred_chickens()
    >>> len(solutions)
    4
    """
    solutions = []
    for roosters in range(0, 21):       # 5 coins each, max 20
        for hens in range(0, 34):       # 3 coins each, max 33
            chicks = 100 - roosters - hens
            if (chicks >= 0 and chicks % 3 == 0 and
                    5 * roosters + 3 * hens + chicks // 3 == 100):
                solutions.append((roosters, hens, chicks))
    return solutions


# =============================================================================
# Problem 6: CRAPS Dice Game (Non-Interactive Demo)
# =============================================================================

def play_craps_round() -> tuple[str, int]:
    """Play one round of simplified CRAPS dice game.

    Rules:
    - First roll: 7 or 11 -> Player wins
    - First roll: 2, 3, or 12 -> House wins
    - Any other first roll becomes the "point"
    - Keep rolling: 7 -> House wins, point -> Player wins

    Returns:
        Tuple of (winner, number_of_rolls).

    >>> winner, rolls = play_craps_round()
    >>> winner in ('player', 'house')
    True
    """
    def roll_dice():
        return random.randint(1, 6) + random.randint(1, 6)

    first_roll = roll_dice()
    rolls = 1

    if first_roll in (7, 11):
        return 'player', rolls
    elif first_roll in (2, 3, 12):
        return 'house', rolls
    else:
        point = first_roll
        while True:
            current = roll_dice()
            rolls += 1
            if current == 7:
                return 'house', rolls
            elif current == point:
                return 'player', rolls


def simulate_craps(num_games: int = 10000) -> None:
    """Simulate many CRAPS games and show statistics."""
    player_wins = 0
    total_rolls = 0

    for _ in range(num_games):
        winner, rolls = play_craps_round()
        total_rolls += rolls
        if winner == 'player':
            player_wins += 1

    print(f"=== CRAPS Simulation ({num_games:,} games) ===")
    print(f"Player win rate: {player_wins/num_games:.2%}")
    print(f"House win rate:  {(num_games - player_wins)/num_games:.2%}")
    print(f"Avg rolls/game:  {total_rolls/num_games:.2f}")
    print()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    print("=== Primes Under 100 ===")
    print(primes_under_100())
    print()

    print("=== First 20 Fibonacci Numbers ===")
    print(fibonacci(20))
    print()

    print("=== Armstrong Numbers (3-digit) ===")
    print(armstrong_numbers())
    print()

    print("=== Integer Reversal ===")
    for n in [12389, 100, 54321]:
        print(f"  {n} -> {reverse_integer(n)}")
    print()

    print("=== Hundred Chickens Problem ===")
    for r, h, c in hundred_chickens():
        print(f"  Roosters: {r}, Hens: {h}, Chicks: {c}")
    print()

    simulate_craps()
