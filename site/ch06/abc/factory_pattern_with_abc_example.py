"""
Factory Pattern with Abstract Base Classes

Combines ABCs for defining contracts with the Factory Pattern
for creating objects. This is a payroll system where different
employee types have different salary calculation methods.

Topics covered:
- Abstract base classes (ABCMeta, abstractmethod)
- Factory pattern (centralized object creation)
- Polymorphism (same interface, different behavior)
- Static methods in factory classes

Based on concepts from Python-100-Days examples 12-13 and ch06/abc materials.
"""

from abc import ABCMeta, abstractmethod


# =============================================================================
# Example 1: Abstract Employee Class
# =============================================================================

class Employee(metaclass=ABCMeta):
    """Abstract base class defining the employee contract.

    All employee types must implement get_salary().
    This ensures polymorphic salary calculation.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_salary(self) -> float:
        """Calculate monthly salary. Must be implemented by subclasses."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}')"

    def __repr__(self):
        return self.__str__()


# =============================================================================
# Example 2: Concrete Employee Subclasses
# =============================================================================

class Manager(Employee):
    """Department manager with fixed salary."""

    def __init__(self, name: str, monthly_salary: float = 15000.0):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_salary(self) -> float:
        return self.monthly_salary


class Programmer(Employee):
    """Programmer paid by hours worked."""

    def __init__(self, name: str, hourly_rate: float = 200.0,
                 hours_worked: int = 0):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self) -> float:
        return self.hourly_rate * self.hours_worked


class Salesperson(Employee):
    """Salesperson with base salary plus commission."""

    def __init__(self, name: str, base_salary: float = 1800.0,
                 sales: float = 0.0, commission_rate: float = 0.05):
        super().__init__(name)
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def get_salary(self) -> float:
        return self.base_salary + self.sales * self.commission_rate


# =============================================================================
# Example 3: Factory for Employee Creation
# =============================================================================

class EmployeeFactory:
    """Factory class for creating employees.

    The Factory Pattern decouples object creation from usage.
    Client code doesn't need to know the specific class - just
    the type code. This makes it easy to add new employee types.
    """

    _registry = {
        'M': Manager,
        'P': Programmer,
        'S': Salesperson,
    }

    @staticmethod
    def create(emp_type: str, *args, **kwargs) -> Employee:
        """Create an employee by type code.

        Args:
            emp_type: 'M' for Manager, 'P' for Programmer, 'S' for Salesperson.
            *args, **kwargs: Passed to the employee constructor.

        Raises:
            ValueError: If emp_type is not recognized.

        >>> emp = EmployeeFactory.create('P', 'Alice', hours_worked=160)
        >>> emp.get_salary()
        32000.0
        """
        cls = EmployeeFactory._registry.get(emp_type.upper())
        if cls is None:
            valid = ', '.join(EmployeeFactory._registry.keys())
            raise ValueError(f"Unknown type '{emp_type}'. Valid: {valid}")
        return cls(*args, **kwargs)

    @classmethod
    def register(cls, type_code: str, employee_class: type):
        """Register a new employee type dynamically.

        This makes the factory extensible without modifying its source.
        """
        if not issubclass(employee_class, Employee):
            raise TypeError(f"{employee_class} must be a subclass of Employee")
        cls._registry[type_code.upper()] = employee_class


# =============================================================================
# Example 4: Polymorphic Payroll Processing
# =============================================================================

def process_payroll(employees: list[Employee]) -> None:
    """Calculate and display payroll for all employees.

    Thanks to polymorphism, we don't need to check employee types.
    Each employee knows how to calculate its own salary.
    """
    print("=== Monthly Payroll ===")
    print(f"{'Name':<15} {'Type':<15} {'Salary':>10}")
    print("-" * 42)

    total = 0.0
    for emp in employees:
        salary = emp.get_salary()
        total += salary
        emp_type = emp.__class__.__name__
        print(f"{emp.name:<15} {emp_type:<15} ${salary:>9,.2f}")

    print("-" * 42)
    print(f"{'Total':<30} ${total:>9,.2f}")
    print()


# =============================================================================
# Example 5: Extending the Factory
# =============================================================================

class Intern(Employee):
    """Intern with stipend (extending the system)."""

    def __init__(self, name: str, stipend: float = 500.0):
        super().__init__(name)
        self.stipend = stipend

    def get_salary(self) -> float:
        return self.stipend


def demo_extensibility():
    """Show how to add new employee types without modifying existing code."""
    print("=== Extending with New Types ===")

    # Register new type at runtime
    EmployeeFactory.register('I', Intern)

    intern = EmployeeFactory.create('I', 'New Intern', stipend=800)
    print(f"{intern.name}: ${intern.get_salary():.2f}")

    # Demonstrate that abstract class can't be instantiated
    print("\nTrying to instantiate abstract Employee...")
    try:
        emp = Employee("Nobody")
    except TypeError as e:
        print(f"  TypeError: {e}")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    # Create employees using factory
    employees = [
        EmployeeFactory.create('M', 'Alice'),
        EmployeeFactory.create('P', 'Bob', hours_worked=120),
        EmployeeFactory.create('P', 'Charlie', hours_worked=85),
        EmployeeFactory.create('S', 'Diana', sales=123000),
    ]

    process_payroll(employees)
    demo_extensibility()
