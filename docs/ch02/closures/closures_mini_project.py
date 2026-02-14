"""
Closures Mini-Project: Event Management System
This project demonstrates how to use closures to create a simple event
management system with event handlers, state management, and callbacks.
"""

import time
from datetime import datetime

print("=" * 70)
print("CLOSURES MINI-PROJECT: EVENT MANAGEMENT SYSTEM")
print("=" * 70)

# ============================================================================
# EVENT EMITTER USING CLOSURES
# ============================================================================
print("\n1. EVENT EMITTER")
print("-" * 70)

def create_event_emitter():
    """
    Create an event emitter that allows subscribing to events and
    triggering callbacks. Uses closures to maintain the list of listeners.
    """
    listeners = {}  # Private to the closure
    
    def on(event_name, callback):
        """Subscribe to an event"""
        if event_name not in listeners:
            listeners[event_name] = []
        listeners[event_name].append(callback)
        print(f"✓ Subscribed to '{event_name}'")
    
    def off(event_name, callback):
        """Unsubscribe from an event"""
        if event_name in listeners and callback in listeners[event_name]:
            listeners[event_name].remove(callback)
            print(f"✓ Unsubscribed from '{event_name}'")
    
    def emit(event_name, *args, **kwargs):
        """Trigger an event and call all subscribers"""
        if event_name in listeners:
            print(f"📢 Emitting '{event_name}' event")
            for callback in listeners[event_name]:
                callback(*args, **kwargs)
        else:
            print(f"⚠️  No listeners for '{event_name}'")
    
    def get_listener_count(event_name=None):
        """Get number of listeners"""
        if event_name:
            return len(listeners.get(event_name, []))
        return sum(len(v) for v in listeners.values())
    
    return {
        'on': on,
        'off': off,
        'emit': emit,
        'listener_count': get_listener_count
    }

# Create an event emitter
emitter = create_event_emitter()

# Create event handlers using closures
def make_user_handler(user_id):
    """Factory function to create user-specific handlers"""
    login_count = 0
    
    def on_login():
        nonlocal login_count
        login_count += 1
        print(f"  User {user_id} logged in (total: {login_count} times)")
    
    def on_logout():
        print(f"  User {user_id} logged out")
    
    return on_login, on_logout

# Subscribe to events
user1_login, user1_logout = make_user_handler("user_001")
user2_login, user2_logout = make_user_handler("user_002")

emitter['on']('user_login', user1_login)
emitter['on']('user_logout', user1_logout)
emitter['on']('user_login', user2_login)

print(f"Total listeners: {emitter['listener_count']()}")

# Trigger events
print("\nSimulating user activity:")
emitter['emit']('user_login')
emitter['emit']('user_login')
emitter['emit']('user_logout')

# ============================================================================
# STATE MACHINE USING CLOSURES
# ============================================================================
print("\n\n2. STATE MACHINE")
print("-" * 70)

def create_state_machine(initial_state, transitions):
    """
    Create a state machine using closures.
    Maintains current state privately.
    """
    current_state = initial_state
    history = [initial_state]
    
    def get_state():
        """Get current state"""
        return current_state
    
    def transition(event):
        """Attempt to transition to a new state"""
        nonlocal current_state
        
        if current_state in transitions and event in transitions[current_state]:
            new_state = transitions[current_state][event]
            print(f"  {current_state} --[{event}]--> {new_state}")
            current_state = new_state
            history.append(current_state)
            return True
        else:
            print(f"  ⚠️ Invalid transition: {event} from {current_state}")
            return False
    
    def get_history():
        """Get state history"""
        return history.copy()
    
    def reset():
        """Reset to initial state"""
        nonlocal current_state
        current_state = initial_state
        history.clear()
        history.append(initial_state)
        print(f"  Reset to {initial_state}")
    
    return {
        'state': get_state,
        'transition': transition,
        'history': get_history,
        'reset': reset
    }

# Create a door state machine
door_transitions = {
    'closed': {'open': 'open'},
    'open': {'close': 'closed'},
}

door = create_state_machine('closed', door_transitions)

print(f"Initial state: {door['state']()}")
print("\nDoor operations:")
door['transition']('open')
door['transition']('close')
door['transition']('close')  # Invalid
door['transition']('open')
print(f"\nHistory: {' -> '.join(door['history']())}")

# ============================================================================
# RATE-LIMITED API CLIENT
# ============================================================================
print("\n\n3. RATE-LIMITED API CLIENT")
print("-" * 70)

def create_rate_limited_client(max_requests, time_window):
    """
    Create an API client with rate limiting using closures.
    Tracks request times privately.
    """
    request_times = []
    request_count = 0
    
    def make_request(endpoint):
        """Make an API request with rate limiting"""
        nonlocal request_count
        now = time.time()
        
        # Remove old requests outside the time window
        request_times[:] = [t for t in request_times if now - t < time_window]
        
        if len(request_times) >= max_requests:
            wait_time = time_window - (now - request_times[0])
            print(f"  ⏸️  Rate limit reached. Wait {wait_time:.1f}s")
            return None
        
        request_times.append(now)
        request_count += 1
        print(f"  ✓ Request #{request_count} to {endpoint}")
        return {"status": "success", "endpoint": endpoint}
    
    def get_stats():
        """Get request statistics"""
        return {
            'total_requests': request_count,
            'recent_requests': len(request_times),
            'limit': max_requests,
            'window': time_window
        }
    
    def reset_stats():
        """Reset request statistics"""
        nonlocal request_count
        request_times.clear()
        request_count = 0
        print("  Stats reset")
    
    return {
        'request': make_request,
        'stats': get_stats,
        'reset': reset_stats
    }

# Create a rate-limited client (3 requests per 1 second)
api_client = create_rate_limited_client(max_requests=3, time_window=1.0)

print("Making API requests (max 3 per second):")
for i in range(5):
    result = api_client['request'](f'/api/users/{i}')
    time.sleep(0.2)

stats = api_client['stats']()
print(f"\nStats: {stats}")

# ============================================================================
# CONFIGURABLE VALIDATORS
# ============================================================================
print("\n\n4. CONFIGURABLE VALIDATORS")
print("-" * 70)

def create_validator(rules):
    """
    Create a validator with configurable rules using closures.
    """
    validation_count = 0
    failed_count = 0
    
    def validate(data):
        """Validate data against rules"""
        nonlocal validation_count, failed_count
        validation_count += 1
        errors = []
        
        for field, rule in rules.items():
            if field not in data:
                errors.append(f"Missing field: {field}")
            elif not rule['check'](data[field]):
                errors.append(f"{field}: {rule['message']}")
        
        if errors:
            failed_count += 1
            return {'valid': False, 'errors': errors}
        
        return {'valid': True, 'errors': []}
    
    def get_stats():
        """Get validation statistics"""
        return {
            'total': validation_count,
            'failed': failed_count,
            'success_rate': f"{((validation_count - failed_count) / validation_count * 100):.1f}%"
                if validation_count > 0 else "N/A"
        }
    
    return {
        'validate': validate,
        'stats': get_stats
    }

# Create validators with different rules
user_rules = {
    'username': {
        'check': lambda x: len(x) >= 3,
        'message': 'Must be at least 3 characters'
    },
    'email': {
        'check': lambda x: '@' in x and '.' in x,
        'message': 'Must be a valid email'
    },
    'age': {
        'check': lambda x: isinstance(x, int) and 18 <= x <= 120,
        'message': 'Must be between 18 and 120'
    }
}

user_validator = create_validator(user_rules)

# Test validation
test_users = [
    {'username': 'alice', 'email': 'alice@example.com', 'age': 25},
    {'username': 'bo', 'email': 'invalid', 'age': 15},
    {'username': 'charlie', 'email': 'charlie@test.com', 'age': 30},
]

print("Validating users:")
for user in test_users:
    result = user_validator['validate'](user)
    if result['valid']:
        print(f"  ✓ {user['username']}: Valid")
    else:
        print(f"  ✗ {user['username']}: {', '.join(result['errors'])}")

print(f"\nValidation stats: {user_validator['stats']()}")

# ============================================================================
# CACHE WITH EXPIRATION
# ============================================================================
print("\n\n5. CACHE WITH EXPIRATION")
print("-" * 70)

def create_cache(ttl=5):
    """
    Create a cache with time-to-live using closures.
    """
    cache = {}
    hits = 0
    misses = 0
    
    def get(key):
        """Get value from cache"""
        nonlocal hits, misses
        
        if key in cache:
            value, timestamp = cache[key]
            if time.time() - timestamp < ttl:
                hits += 1
                print(f"  💾 Cache HIT for '{key}'")
                return value
            else:
                del cache[key]
                print(f"  ⌛ Cache EXPIRED for '{key}'")
        
        misses += 1
        print(f"  ❌ Cache MISS for '{key}'")
        return None
    
    def set(key, value):
        """Set value in cache"""
        cache[key] = (value, time.time())
        print(f"  ✓ Cached '{key}'")
    
    def clear():
        """Clear all cache"""
        cache.clear()
        print(f"  🗑️  Cache cleared")
    
    def get_stats():
        """Get cache statistics"""
        total = hits + misses
        return {
            'hits': hits,
            'misses': misses,
            'hit_rate': f"{(hits / total * 100):.1f}%" if total > 0 else "N/A",
            'size': len(cache)
        }
    
    return {
        'get': get,
        'set': set,
        'clear': clear,
        'stats': get_stats
    }

# Create cache with 2-second TTL
cache = create_cache(ttl=2)

print("Testing cache:")
cache['set']('user_123', {'name': 'Alice', 'age': 30})
cache['get']('user_123')  # Hit
time.sleep(1)
cache['get']('user_123')  # Hit
time.sleep(1.5)
cache['get']('user_123')  # Expired
cache['set']('user_123', {'name': 'Alice', 'age': 30})
cache['get']('user_123')  # Hit

print(f"\nCache stats: {cache['stats']()}")

# ============================================================================
# COMMAND PATTERN WITH UNDO
# ============================================================================
print("\n\n6. COMMAND PATTERN WITH UNDO")
print("-" * 70)

def create_command_manager():
    """
    Create a command manager with undo/redo using closures.
    """
    history = []
    current_index = -1
    
    def execute(command, undo_command):
        """Execute a command and save for undo"""
        nonlocal current_index
        
        command()
        current_index += 1
        
        # Remove any commands after current index (for redo)
        history[:] = history[:current_index]
        history.append((command, undo_command))
        
        print(f"  ✓ Command executed (history size: {len(history)})")
    
    def undo():
        """Undo last command"""
        nonlocal current_index
        
        if current_index >= 0:
            _, undo_command = history[current_index]
            undo_command()
            current_index -= 1
            print(f"  ↶ Undo executed")
            return True
        
        print(f"  ⚠️ Nothing to undo")
        return False
    
    def redo():
        """Redo last undone command"""
        nonlocal current_index
        
        if current_index < len(history) - 1:
            current_index += 1
            command, _ = history[current_index]
            command()
            print(f"  ↷ Redo executed")
            return True
        
        print(f"  ⚠️ Nothing to redo")
        return False
    
    def get_history_size():
        """Get size of command history"""
        return len(history)
    
    return {
        'execute': execute,
        'undo': undo,
        'redo': redo,
        'history_size': get_history_size
    }

# Create command manager
cmd_manager = create_command_manager()

# Simulate a simple text editor
text = []

def add_text(word):
    """Command to add text"""
    def do():
        text.append(word)
        print(f"    Added: '{word}' -> {text}")
    
    def undo():
        text.pop()
        print(f"    Removed: '{word}' -> {text}")
    
    cmd_manager['execute'](do, undo)

print("Text editor simulation:")
add_text("Hello")
add_text("World")
add_text("!")

print("\nUndo operations:")
cmd_manager['undo']()
cmd_manager['undo']()

print("\nRedo operations:")
cmd_manager['redo']()

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)
print("""
This mini-project demonstrated practical closure usage:

✅ Patterns Demonstrated:
   1. Event Emitter - Subscribe/publish with private listener list
   2. State Machine - Maintain state with transition rules
   3. Rate Limiter - Track requests with time windows
   4. Validators - Configurable validation with statistics
   5. Cache - Time-based expiration with hit/miss tracking
   6. Command Pattern - Undo/redo functionality

✅ Key Closure Concepts:
   - Private variables (listeners, state, cache, history)
   - Multiple functions sharing state (nonlocal)
   - Factory functions (make_user_handler)
   - Encapsulation without classes
   - Stateful behavior

✅ Real-World Applications:
   - Event-driven systems (UI frameworks, game engines)
   - State management (workflows, processes)
   - API clients with rate limiting
   - Form validation systems
   - Caching layers
   - Undo/redo functionality (text editors, drawing apps)

✅ Benefits of Using Closures:
   - Clean, encapsulated code
   - No class boilerplate needed
   - Natural state management
   - Easy to test individual components
   - Functional programming style

Try extending this project by adding:
   - Priority-based event emitters
   - State machine with entry/exit actions
   - LRU cache eviction policy
   - Async validators
   - Transaction support for commands
""")

print("=" * 70)
print("END OF MINI-PROJECT")
print("=" * 70)
