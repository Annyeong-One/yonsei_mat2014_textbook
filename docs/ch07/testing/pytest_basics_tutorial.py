"""
08_pytest_basics.py - Introduction to pytest
===========================================
Modern, powerful testing with pytest framework.
"""
# pytest uses simple functions, not classes (though classes work too)
# No need to import unittest or inherit from TestCase

# =============================================================================
# Definitions
# =============================================================================

def add(a, b):
    """Add two numbers."""
    return a + b

def test_add_positive_numbers():
    """Test adding positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-1, -1) == -2

def test_add_zero():
    """Test adding zero."""
    assert add(5, 0) == 5

# pytest provides better assertion introspection than unittest
def test_list_operations():
    """pytest shows detailed failure information."""
    my_list = [1, 2, 3]
    assert 3 in my_list
    assert len(my_list) == 3

def test_dict_operations():
    """Test dictionary operations."""
    my_dict = {'name': 'Alice', 'age': 30}
    assert my_dict['name'] == 'Alice'
    assert 'age' in my_dict

# pytest fixtures (simple version)
import pytest


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    @pytest.fixture
    def sample_list():
        """Fixture that provides a sample list."""
        return [1, 2, 3, 4, 5]

    def test_with_fixture(sample_list):
        """Test using a fixture."""
        assert len(sample_list) == 5
        assert sum(sample_list) == 15

    # Testing exceptions with pytest
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def test_divide_by_zero():
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError):
            divide(10, 0)

    def test_divide_by_zero_message():
        """Test exception message."""
        with pytest.raises(ValueError, match="Cannot divide"):
            divide(10, 0)

    # Run with: pytest 08_pytest_basics.py -v
