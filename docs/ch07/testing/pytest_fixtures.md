# pytest Fixtures

Use pytest fixtures for setup/teardown and parameterized test data.

## Creating and Using Fixtures

Define reusable test setup with fixtures.

```python
import pytest

@pytest.fixture
def sample_data():
    return {"users": ["Alice", "Bob"], "count": 2}

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("test content")
    return file

def test_data_access(sample_data):
    assert len(sample_data["users"]) == 2
    assert sample_data["count"] == 2

def test_file_exists(temp_file):
    assert temp_file.exists()
    assert "test" in temp_file.read_text()

print("Fixtures can provide test data and resources")
```

```
Fixtures can provide test data and resources
```

## Fixture Scopes

Control when fixtures are created and destroyed.

```python
import pytest

@pytest.fixture(scope="function")  # Default, run for each test
def function_scope():
    return "function"

@pytest.fixture(scope="class")  # Shared per test class
def class_scope():
    return "class"

@pytest.fixture(scope="module")  # Shared per module
def module_scope():
    return "module"

@pytest.fixture(scope="session")  # Shared for entire session
def session_scope():
    return "session"

def test_scopes(function_scope):
    assert function_scope == "function"

print("Fixture scopes control resource lifecycle")
```

```
Fixture scopes control resource lifecycle
```

