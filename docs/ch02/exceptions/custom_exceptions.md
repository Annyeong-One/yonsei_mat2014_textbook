# Custom Exceptions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python allows creating custom exception classes by subclassing the built-in `Exception` class. Custom exceptions improve code clarity and enable specific error handling.


## Basic Custom Exception

Create a custom exception by inheriting from `Exception`.

```python
class TooHotError(Exception):
    pass

def check_temperature(temp):
    if temp > 60:
        raise TooHotError
    print("Temperature is fine.")

try:
    check_temperature(65)
except TooHotError:
    print("Too hot!")
```

Output:
```
Too hot!
```


## Custom Exception with Message

Pass a message to provide context about the error.

```python
class TooHotError(Exception):
    pass

def check_temperature(temp):
    if temp > 60:
        raise TooHotError("Temperature exceeds safe limit.")
    print("Temperature is fine.")

try:
    check_temperature(65)
except TooHotError as e:
    print(e)
```

Output:
```
Temperature exceeds safe limit.
```


## Custom Exception with __init__

Override `__init__` for custom initialization.

```python
class TooHotError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

raise TooHotError("Too hot for a walk.")
```


## Using super().__init__

The preferred approach uses `super()` to initialize the parent class.

```python
class TooHotError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

try:
    raise TooHotError("Temperature is 65°F, too hot!")
except TooHotError as e:
    print(e)
```

Output:
```
Temperature is 65°F, too hot!
```


## Practical Example

A class that raises custom exceptions based on conditions.

```python
class TooHotError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Walk:
    def __init__(self, temperature):
        self.temperature = temperature
    
    def walk(self):
        if self.temperature > 60:
            raise TooHotError("Too hot for a walk.")
        print("Enjoy walking!")

aug_7_2023 = Walk(65)

try:
    aug_7_2023.walk()
except TooHotError as e:
    print(e)
```

Output:
```
Too hot for a walk.
```


## When to Create Custom Exceptions

Create custom exceptions when:

- Built-in exceptions don't describe the error adequately
- You need to catch specific errors in your application
- You want to provide domain-specific error messages
- You need to add custom attributes to the exception

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount}. Balance is ${balance}."
        )
```


## Exception Hierarchy for Custom Classes

Create a hierarchy of related exceptions.

```python
class WeatherError(Exception):
    """Base class for weather-related errors."""
    pass

class TooHotError(WeatherError):
    pass

class TooColdError(WeatherError):
    pass

# Catch all weather errors
try:
    raise TooHotError("Heat wave!")
except WeatherError as e:
    print(f"Weather issue: {e}")
```
