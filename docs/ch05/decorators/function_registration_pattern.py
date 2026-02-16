"""
TUTORIAL: Function Registration Pattern with Decorators

This tutorial covers the FUNCTION REGISTRATION PATTERN, a powerful way to use
decorators to dynamically build a registry of functions.

The Idea: You want to collect multiple functions into a central list or dict,
often for callbacks, plugins, or dispatch. Instead of manually maintaining the
registry, use a decorator to automatically register functions as they're defined.

The Pattern: When a function is decorated with @register, it's added to a
registry list/dict, then returned unchanged so it can still be called normally.

This is the foundation of plugin systems, event dispatchers, and dynamic dispatch
mechanisms. It's elegant because the registry is built naturally as the code runs.
"""

print("=" * 70)
print("TUTORIAL: Function Registration Pattern with Decorators")
print("=" * 70)

# ============ EXAMPLE 1: The Basic Registration Pattern
print("\n# ============ EXAMPLE 1: The Basic Registration Pattern")
print("The simplest registration decorator:\n")

# Create a registry list to hold functions
registry = []


def register(func):
    """Decorator that registers a function in the registry"""
    print(f"running register({func.__name__})")
    registry.append(func)  # Add the function to the registry
    return func  # Return the function unchanged


print("Define the registry and register decorator:")
print(f"registry = {registry}")
print()

# Now define some functions using the @register decorator
@register
def f1():
    """First registered function"""
    print("running f1()")


@register
def f2():
    """Second registered function"""
    print("running f2()")


def f3():
    """Not registered - no @register decorator"""
    print("running f3()")


print("\nFunctions have been defined. Check the registry:")
print(f"registry = {registry}")
print(f"registry[0].__name__ = {registry[0].__name__}")
print(f"registry[1].__name__ = {registry[1].__name__}")
print("\nNotice: f3 is NOT in the registry (no @register decorator)")

# ============ EXAMPLE 2: Using the Registered Functions
print("\n" + "=" * 70)
print("# ============ EXAMPLE 2: Using the Registered Functions")
print("Call registered and non-registered functions:\n")

print("Calling f1() directly:")
f1()

print("\nCalling f2() directly:")
f2()

print("\nCalling f3() directly (not registered):")
f3()

print("\nCalling all registered functions via the registry:")
for func in registry:
    func()

# ============ EXAMPLE 3: Understanding How Registration Works
print("\n" + "=" * 70)
print("# ============ EXAMPLE 3: Understanding How Registration Works")
print("Step-by-step breakdown of what happens:\n")

print("""
WHEN YOU WRITE:

    @register
    def f1():
        print('running f1()')

PYTHON DOES THIS:

    1. Define the function f1
    2. Call register(f1) <- decorator is applied
    3. Assign the return value back to f1

INSIDE register():
    1. func = f1 (the function object)
    2. print(f'running register({func})') <- debug message
    3. registry.append(func) <- ADD TO REGISTRY
    4. return func <- return unchanged

RESULT:
    - f1 is in the registry
    - f1 variable still points to the function
    - f1 can be called normally
    - It's also in the registry for batch operations
""")

# ============ EXAMPLE 4: Registry as a Dictionary
print("\n" + "=" * 70)
print("# ============ EXAMPLE 4: Registry as a Dictionary")
print("Use a dict registry instead of list for named lookups:\n")

# Create a dict registry
command_registry = {}


def register_command(func):
    """Register a function as a command by its name"""
    name = func.__name__
    print(f"Registering command: {name}")
    command_registry[name] = func
    return func


@register_command
def save():
    """Save current data"""
    print("Saving data...")


@register_command
def load():
    """Load data from disk"""
    print("Loading data...")


@register_command
def exit_program():
    """Exit the program"""
    print("Exiting...")


print("Registered commands:")
for name in command_registry:
    print(f"  {name}")

print("\nCall a command by name:")
command_registry['save']()

print("\nCall all commands:")
for name, cmd in command_registry.items():
    print(f"Calling {name}():")
    cmd()

# ============ EXAMPLE 5: Real-World Example - Event Dispatcher
print("\n" + "=" * 70)
print("# ============ EXAMPLE 5: Real-World Example - Event Dispatcher")
print("An event system where handlers register for specific events:\n")


class EventDispatcher:
    """Simple event dispatcher with registered handlers"""

    def __init__(self):
        self.handlers = {}  # event_name -> list of handler functions

    def register_handler(self, event_name):
        """Decorator to register a handler for an event"""
        def decorator(func):
            if event_name not in self.handlers:
                self.handlers[event_name] = []
            print(f"Registering {func.__name__} for event '{event_name}'")
            self.handlers[event_name].append(func)
            return func
        return decorator

    def emit(self, event_name, *args, **kwargs):
        """Trigger an event and call all registered handlers"""
        if event_name not in self.handlers:
            print(f"No handlers for event: {event_name}")
            return

        for handler in self.handlers[event_name]:
            handler(*args, **kwargs)


# Create a dispatcher
dispatcher = EventDispatcher()

# Register handlers for 'user_login' event
@dispatcher.register_handler('user_login')
def log_login(username):
    print(f"  LOG: User {username} logged in")


@dispatcher.register_handler('user_login')
def send_welcome_email(username):
    print(f"  EMAIL: Sending welcome email to {username}")


@dispatcher.register_handler('user_login')
def update_last_seen(username):
    print(f"  DB: Updating last_seen for {username}")


# Register handlers for 'user_logout' event
@dispatcher.register_handler('user_logout')
def log_logout(username):
    print(f"  LOG: User {username} logged out")


print("\nDispatcher handlers registered:")
for event, handlers in dispatcher.handlers.items():
    print(f"  {event}: {len(handlers)} handlers")

print("\nEmitting 'user_login' event:")
dispatcher.emit('user_login', 'alice')

print("\nEmitting 'user_logout' event:")
dispatcher.emit('user_logout', 'alice')

# ============ EXAMPLE 6: Plugin System Pattern
print("\n" + "=" * 70)
print("# ============ EXAMPLE 6: Plugin System Pattern")
print("Using registration for a simple plugin system:\n")


class PluginRegistry:
    """Registry for plugins that process different file types"""

    def __init__(self):
        self.plugins = {}  # file_extension -> processor function

    def register(self, *extensions):
        """Decorator to register a plugin for file extensions"""
        def decorator(func):
            for ext in extensions:
                print(f"Registering {func.__name__} for .{ext} files")
                self.plugins[ext] = func
            return func
        return decorator

    def process(self, filename):
        """Process a file using the appropriate plugin"""
        # Extract file extension
        if '.' not in filename:
            print(f"No extension for file: {filename}")
            return

        ext = filename.split('.')[-1]

        if ext not in self.plugins:
            print(f"No processor for .{ext} files")
            return

        processor = self.plugins[ext]
        processor(filename)


# Create a plugin registry
plugins = PluginRegistry()


@plugins.register('txt')
def process_text(filename):
    print(f"Processing text file: {filename}")


@plugins.register('jpg', 'jpeg', 'png')
def process_image(filename):
    print(f"Processing image file: {filename}")


@plugins.register('py')
def process_python(filename):
    print(f"Processing Python file: {filename}")


print("\nRegistered file processors:")
for ext, processor in plugins.plugins.items():
    print(f"  .{ext} -> {processor.__name__}")

print("\nProcessing various files:")
plugins.process('document.txt')
plugins.process('photo.jpg')
plugins.process('script.py')
plugins.process('backup.zip')  # No processor

# ============ EXAMPLE 7: Comparison - Manual vs Registration Pattern
print("\n" + "=" * 70)
print("# ============ EXAMPLE 7: Comparison - Manual vs Registration Pattern")
print("Why the registration pattern is better:\n")

print("""
MANUAL APPROACH (without registration):

def process_files(files):
    processors = [
        process_txt,
        process_json,
        process_csv,
        # Must remember to add every processor here
        # Hard to extend from other modules
    ]
    for file in files:
        # Check type and call processor
        ...

PROBLEMS:
- Central list must be manually maintained
- Hard to extend without modifying this function
- Couples all processors together
- External modules can't register processors


REGISTRATION PATTERN:

@register
def process_txt():
    ...

@register
def process_json():
    ...

# External module can do:
@register
def process_csv():
    ...

BENEFITS:
- Processors register themselves as they're defined
- Easy to extend - just add @register
- No central coupling
- Each processor is independent
- Works great with plugins from external modules
""")

# ============ EXAMPLE 8: Registration with Validation
print("\n" + "=" * 70)
print("# ============ EXAMPLE 8: Registration with Validation")
print("Add validation/requirements to registration:\n")


class ValidatedRegistry:
    """Registry that validates handlers before registration"""

    def __init__(self):
        self.handlers = {}

    def register(self, **requirements):
        """
        Decorator that registers with validation.
        Usage: @register(priority=1, required=True)
        """
        def decorator(func):
            # Validate the function
            if not callable(func):
                raise ValueError(f"{func} is not callable")

            name = func.__name__
            meta = {'function': func, **requirements}

            print(f"Registering {name} with {requirements}")
            self.handlers[name] = meta
            return func

        return decorator

    def call_handler(self, name, *args, **kwargs):
        """Call a registered handler by name"""
        if name not in self.handlers:
            raise KeyError(f"Handler {name} not registered")

        handler = self.handlers[name]['function']
        return handler(*args, **kwargs)


validated_registry = ValidatedRegistry()


@validated_registry.register(priority=1, required=True)
def database_check():
    print("  Checking database...")


@validated_registry.register(priority=2)
def cache_check():
    print("  Checking cache...")


print("\nRegistered handlers with metadata:")
for name, meta in validated_registry.handlers.items():
    print(f"  {name}: priority={meta.get('priority')}, "
          f"required={meta.get('required')}")

print("\nCalling handlers:")
validated_registry.call_handler('database_check')
validated_registry.call_handler('cache_check')

# ============ EXAMPLE 9: Decorator Chaining
print("\n" + "=" * 70)
print("# ============ EXAMPLE 9: Decorator Chaining")
print("Combine registration with other decorators:\n")

import time


call_log = []


def log_calls(func):
    """Decorator that logs when a function is called"""
    def wrapper(*args, **kwargs):
        print(f"  LOG: Calling {func.__name__}")
        result = func(*args, **kwargs)
        call_log.append(func.__name__)
        return result
    return wrapper


def time_calls(func):
    """Decorator that times function execution"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  TIME: {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


timed_registry = []


def register_timed(func):
    """Register and apply timing decorator"""
    print(f"Registering {func.__name__}")
    timed_registry.append(func)
    return func


@register_timed
@time_calls
@log_calls
def operation_a():
    time.sleep(0.01)
    print("    Operation A complete")


@register_timed
@time_calls
@log_calls
def operation_b():
    time.sleep(0.02)
    print("    Operation B complete")


print("\nRunning registered operations:")
for op in timed_registry:
    op()

print(f"\nAll operations called: {call_log}")

# ============ EXAMPLE 10: Common Use Cases
print("\n" + "=" * 70)
print("# ============ EXAMPLE 10: Common Use Cases")
print("Where the registration pattern shines:\n")

print("""
COMMON USE CASES:

1. PLUGIN SYSTEMS
   - Plugins register themselves at import time
   - Main app calls all registered plugins
   - Easy to add/remove plugins

2. EVENT SYSTEMS
   - Register handlers for events
   - When event occurs, call all handlers
   - Multiple handlers per event

3. COMMAND DISPATCHERS
   - Commands register by name
   - Main loop dispatches to command by name
   - Easy to add new commands

4. TESTING FRAMEWORKS
   - Test functions register themselves
   - Test runner discovers and runs all tests
   - No need to manually list tests

5. API ENDPOINTS
   - Routes register themselves as they're defined
   - Server builds routing table automatically
   - Similar to Flask @app.route()

6. PROTOCOL HANDLERS
   - Different handlers for different data types
   - Each handler registers for its type(s)
   - Extensible dispatch system

7. MIDDLEWARE CHAINS
   - Middleware registers itself in order
   - Request passes through all middleware
   - Easy to add/remove middleware


KEY PATTERN:

1. Create a registry (list or dict)
2. Define a register decorator that:
   - Adds function to registry
   - Optionally validates
   - Returns function unchanged
3. Use @register on functions you want to collect
4. Execute or dispatch to registered functions as needed
""")

# ============ EXAMPLE 11: Best Practices
print("\n" + "=" * 70)
print("# ============ EXAMPLE 11: Best Practices")
print("Guidelines for using the registration pattern:\n")

print("""
BEST PRACTICES:

1. ALWAYS RETURN THE FUNCTION
   @decorator should return the original function unchanged
   This way it can still be called and used normally

2. DOCUMENT REGISTRATION REQUIREMENTS
   Make clear what a function must do to be registered
   Validate inputs and raise clear errors

3. CONSIDER NAMING CONVENTIONS
   Functions registered the same way often have similar names
   Use decorators to discover and group related functions

4. PROVIDE INTROSPECTION
   Make it easy to see what's registered
   offer ways to query the registry

5. HANDLE REGISTRATION CONFLICTS
   What happens if two functions have the same name/key?
   Should you error, warn, or replace?
   Make policy clear

6. USE DECORATOR FACTORIES FOR PARAMETERS
   If decorator needs parameters, use a factory:
   @register(name='custom_name')  <- factory
   def func(): ...

7. KEEP DECORATORS FOCUSED
   Register decorator should only register
   Don't mix in validation, timing, etc.
   (Or do, but document it clearly)

8. MAKE REGISTRATION EXPLICIT
   Use a clear name like @register, not @dec
   Makes it obvious what the decorator does

ANTI-PATTERNS:

X Don't lose the original function
  Don't do: register(func) then ignore return value

X Don't silently fail
  Raise clear errors if registration fails

X Don't make registry hard to inspect
  Expose it for debugging and introspection

X Don't mix registration with side effects
  If decorator does registration, make that clear
""")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
KEY TAKEAWAYS:

1. REGISTRATION PATTERN BASICS
   - Create a registry (list or dict)
   - Create a @register decorator
   - Decorator adds function to registry and returns it
   - Use @register on functions you want to collect

2. BASIC PATTERN:

   registry = []

   def register(func):
       registry.append(func)
       return func

   @register
   def my_function():
       ...

3. COMMON VARIATIONS
   - Dict registry for named lookup: registry[name] = func
   - Decorator factory for parameters: @register(priority=1)
   - Validation: check requirements before registering
   - Metadata: attach extra info to registered functions

4. BENEFITS
   - Automatic collection of functions
   - Easy to extend without modifying core code
   - Elegant way to build dispatch systems
   - Works great with plugins

5. COMMON USES
   - Event systems and callbacks
   - Plugin architectures
   - Command dispatchers
   - API routing
   - Test discovery
   - Middleware chains

6. KEY PRINCIPLE
   "Register functions as they're defined, not in a central list"
   This makes code more decoupled and extensible.

7. REMEMBER
   - Always return the function unchanged
   - Keep decorator focused
   - Document registration requirements
   - Make registry inspectable
   - Handle conflicts clearly
""")
