"""
Example 03: Using super() Function

The super() function is used to call methods from the parent class.
This is especially useful when you want to extend (not replace) parent functionality.
"""

# =============================================================================
# Definitions
# =============================================================================

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        print(f"Employee.__init__ called for {name}")
    
    def get_details(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}"
    
    def calculate_bonus(self):
        return self.salary * 0.05  # 5% base bonus


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        # Call parent constructor using super()
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team_size = 0
        print(f"Manager.__init__ called for {name}")
    
    def get_details(self):
        # Extend parent's method
        parent_details = super().get_details()
        return f"{parent_details}, Department: {self.department}, Team Size: {self.team_size}"
    
    def calculate_bonus(self):
        # Extend parent's calculation
        base_bonus = super().calculate_bonus()
        management_bonus = self.salary * 0.10  # Additional 10% for managers
        return base_bonus + management_bonus


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_languages):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages
        self.projects_completed = 0
        print(f"Developer.__init__ called for {name}")
    
    def get_details(self):
        parent_details = super().get_details()
        langs = ", ".join(self.programming_languages)
        return f"{parent_details}, Languages: {langs}, Projects: {self.projects_completed}"
    
    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        # Bonus per project completed
        project_bonus = self.projects_completed * 500
        return base_bonus + project_bonus


class TechLead(Manager, Developer):
    """
    A TechLead is both a Manager and a Developer
    This demonstrates multiple inheritance and super() with MRO
    """
    def __init__(self, name, employee_id, salary, department, programming_languages):
        # super() handles the complex inheritance chain
        Manager.__init__(self, name, employee_id, salary, department)
        self.programming_languages = programming_languages
        self.projects_completed = 0
        print(f"TechLead.__init__ called for {name}")
    
    def get_details(self):
        # Get base employee details
        base_details = Employee.get_details(self)
        langs = ", ".join(self.programming_languages)
        return f"{base_details}, Department: {self.department}, Languages: {langs}"
    
    def calculate_bonus(self):
        # Combines bonuses from both Manager and Developer roles
        base_bonus = Employee.calculate_bonus(self)
        management_bonus = self.salary * 0.10
        project_bonus = self.projects_completed * 500
        return base_bonus + management_bonus + project_bonus


# Testing super() usage

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("SUPER() FUNCTION DEMO")
    print("=" * 70)
    
    print("\n1. Creating a Manager:")
    print("-" * 70)
    manager = Manager("Alice Johnson", "M001", 80000, "Engineering")
    manager.team_size = 5
    print(manager.get_details())
    print(f"Bonus: ${manager.calculate_bonus():.2f}")
    
    print("\n2. Creating a Developer:")
    print("-" * 70)
    dev = Developer("Bob Smith", "D001", 75000, ["Python", "JavaScript", "Go"])
    dev.projects_completed = 8
    print(dev.get_details())
    print(f"Bonus: ${dev.calculate_bonus():.2f}")
    
    print("\n3. Creating a TechLead (Multiple Inheritance):")
    print("-" * 70)
    tech_lead = TechLead("Carol Williams", "TL001", 95000, "Backend", ["Python", "Java"])
    tech_lead.team_size = 3
    tech_lead.projects_completed = 5
    print(tech_lead.get_details())
    print(f"Bonus: ${tech_lead.calculate_bonus():.2f}")
    
    print("\n" + "=" * 70)
    print("METHOD RESOLUTION ORDER (MRO)")
    print("=" * 70)
    print(f"TechLead MRO: {[cls.__name__ for cls in TechLead.__mro__]}")

"""
KEY TAKEAWAYS:
1. super() calls the parent class methods
2. Use super() to extend (not replace) parent functionality
3. super() is essential in __init__ to properly initialize parent classes
4. With multiple inheritance, super() follows the Method Resolution Order (MRO)
5. super() makes your code more maintainable and flexible
6. You can call parent methods explicitly, but super() is usually better

COMMON PATTERNS:
- super().__init__(...) - Initialize parent in child __init__
- super().method() - Call parent's method before/after child's logic
- parent_result = super().method() - Get parent's result and extend it
"""
