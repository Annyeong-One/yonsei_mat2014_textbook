# Final Project: Object-Oriented Task Management System

## Project Overview
Build a complete task management application using object-oriented programming principles. This project will test your understanding of classes, objects, inheritance, encapsulation, and composition.

## Requirements

### 1. User Class
Create a `User` class with the following:

**Attributes:**
- username (string, unique)
- email (string)
- created_at (datetime)
- tasks (list of Task objects)

**Methods:**
- `add_task(task)`: Add a task to user's task list
- `remove_task(task_id)`: Remove task by ID
- `get_tasks()`: Return all tasks
- `get_tasks_by_status(status)`: Filter tasks by status
- `get_tasks_by_priority(priority)`: Filter tasks by priority
- `get_completed_percentage()`: Return percentage of completed tasks
- `__str__()`: Return formatted user info

### 2. Task Class
Create a `Task` class with the following:

**Attributes:**
- task_id (unique integer, auto-generated)
- title (string)
- description (string)
- status (string: 'pending', 'in_progress', 'completed')
- priority (string: 'low', 'medium', 'high')
- created_at (datetime)
- due_date (datetime, optional)
- tags (list of strings)

**Methods:**
- `mark_completed()`: Set status to completed
- `mark_in_progress()`: Set status to in_progress
- `add_tag(tag)`: Add a tag
- `remove_tag(tag)`: Remove a tag
- `is_overdue()`: Check if task is past due date
- `days_until_due()`: Calculate days remaining
- `__str__()`: Return formatted task info
- `__eq__()`: Compare tasks by task_id

**Class Methods:**
- `from_dict(data)`: Create task from dictionary

### 3. Project Class
Create a `Project` class that groups related tasks:

**Attributes:**
- project_id (unique integer)
- name (string)
- description (string)
- tasks (list of Task objects)
- created_at (datetime)
- status (string: 'active', 'completed', 'archived')

**Methods:**
- `add_task(task)`: Add task to project
- `remove_task(task_id)`: Remove task from project
- `get_progress()`: Return percentage of completed tasks
- `get_task_count()`: Return number of tasks
- `get_overdue_tasks()`: Return list of overdue tasks
- `mark_completed()`: Mark project as completed
- `__str__()`: Return project summary

### 4. TaskManager Class
Create a main `TaskManager` class that coordinates everything:

**Attributes:**
- users (dictionary: username -> User object)
- projects (dictionary: project_id -> Project object)

**Methods:**
- `create_user(username, email)`: Create and register new user
- `get_user(username)`: Retrieve user by username
- `create_project(name, description)`: Create new project
- `get_project(project_id)`: Retrieve project by ID
- `assign_task_to_user(task, username)`: Assign task to user
- `assign_task_to_project(task, project_id)`: Add task to project
- `get_all_tasks()`: Return all tasks across all users
- `search_tasks(keyword)`: Search tasks by keyword in title/description
- `get_tasks_by_tag(tag)`: Find all tasks with specific tag
- `generate_report()`: Create summary report

### 5. Additional Features (Bonus)
Implement these for extra challenge:

**Priority Queue for Tasks:**
- Sort tasks by priority and due date

**Recurring Tasks:**
- Create `RecurringTask` subclass that inherits from `Task`
- Add frequency attribute (daily, weekly, monthly)
- Implement `create_next_instance()` method

**Task Dependencies:**
- Add `dependencies` attribute to Task
- Implement `can_start()` method (checks if dependencies completed)

**Notifications:**
- Create `Notification` class
- Generate notifications for due tasks
- Send reminders for overdue tasks

**Statistics:**
- Track average completion time
- Most productive days
- Task completion trends

## Implementation Guidelines

### Code Organization
```
task_management/
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── task.py
│   ├── project.py
│   └── task_manager.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── main.py
└── tests.py
```

### Best Practices
1. Use properties with getters and setters for validation
2. Implement proper encapsulation (private attributes where appropriate)
3. Add docstrings to all classes and methods
4. Use class variables for shared constants
5. Implement special methods (`__str__`, `__repr__`, `__eq__`, etc.)
6. Handle exceptions gracefully
7. Follow PEP 8 style guidelines

## Sample Usage

```python
# Initialize system
manager = TaskManager()

# Create users
manager.create_user("alice", "alice@example.com")
manager.create_user("bob", "bob@example.com")

# Get user
alice = manager.get_user("alice")

# Create tasks
task1 = Task(
    title="Complete project proposal",
    description="Write the Q4 project proposal",
    priority="high",
    due_date=datetime(2024, 3, 15)
)
task1.add_tag("work")
task1.add_tag("urgent")

task2 = Task(
    title="Review code",
    description="Review pull requests",
    priority="medium"
)

# Assign tasks
manager.assign_task_to_user(task1, "alice")
alice.add_task(task2)

# Create project
project = manager.create_project("Q4 Initiative", "Major Q4 deliverables")
manager.assign_task_to_project(task1, project.project_id)

# Update task status
task1.mark_in_progress()
task2.mark_completed()

# Query tasks
pending = alice.get_tasks_by_status("pending")
high_priority = alice.get_tasks_by_priority("high")
work_tasks = manager.get_tasks_by_tag("work")

# Generate report
report = manager.generate_report()
print(report)
```

## Testing Requirements

Create a `tests.py` file with test cases for:
1. User creation and task management
2. Task status transitions
3. Project progress calculation
4. Task filtering and searching
5. Overdue task detection
6. Task dependencies (if implemented)

## Deliverables

1. Complete source code with all classes
2. Test file demonstrating functionality
3. README documenting:
   - How to run the program
   - Class structure
   - Example usage
   - Any assumptions made

## Evaluation Criteria

- **Functionality (40%)**: All required features work correctly
- **OOP Principles (30%)**: Proper use of classes, inheritance, encapsulation
- **Code Quality (20%)**: Clean, readable, well-documented code
- **Design (10%)**: Good class design and organization

## Tips for Success

1. Start with the basic classes (User, Task) and test them thoroughly
2. Add complexity gradually (Project, TaskManager)
3. Use inheritance wisely (don't force it where composition is better)
4. Think about the relationships between classes
5. Test each feature as you build it
6. Keep methods focused (single responsibility)
7. Use descriptive variable and method names

## Extensions (Optional)

Once you complete the basic requirements, consider adding:
- Persistent storage (save/load from JSON or database)
- Web interface using Flask
- Command-line interface (CLI)
- Task comments and collaboration features
- File attachments
- Task templates
- Time tracking
- Calendar integration
- Export to various formats (CSV, PDF)

Good luck! This project will demonstrate your mastery of OOP concepts.
