"""
Decorators Mini-Project: API Request Handler
This project demonstrates how to use multiple decorators to create
a robust API request handler with logging, timing, retry logic, and validation.
"""

import time
import functools
import random
from datetime import datetime

if __name__ == "__main__":

    print("=" * 70)
    print("DECORATORS MINI-PROJECT: API REQUEST HANDLER")
    print("=" * 70)

    # ============================================================================
    # DECORATOR DEFINITIONS
    # ============================================================================

    def log_request(func):
        """Log function calls with timestamp"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[{timestamp}] Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{timestamp}] {func.__name__} completed")
            return result
        return wrapper


    def timer(func):
        """Measure execution time"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"⏱️  Execution time: {end - start:.3f} seconds")
            return result
        return wrapper


    def retry(max_attempts=3, delay=1):
        """Retry function on failure"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(1, max_attempts + 1):
                    try:
                        print(f"🔄 Attempt {attempt}/{max_attempts}")
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts:
                            print(f"❌ All attempts failed")
                            raise
                        print(f"⚠️  Attempt {attempt} failed: {e}")
                        print(f"   Waiting {delay}s before retry...")
                        time.sleep(delay)
            return wrapper
        return decorator


    def validate_response(func):
        """Validate API response"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result is None:
                raise ValueError("Response is None")
            if not isinstance(result, dict):
                raise TypeError("Response must be a dictionary")
            if "status" not in result:
                raise KeyError("Response missing 'status' field")
            print(f"✅ Validation passed")
            return result
        return wrapper


    def rate_limit(calls_per_minute=10):
        """Limit API calls per minute"""
        def decorator(func):
            calls = []

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                now = time.time()
                # Remove calls older than 1 minute
                calls[:] = [call_time for call_time in calls if now - call_time < 60]

                if len(calls) >= calls_per_minute:
                    wait_time = 60 - (now - calls[0])
                    print(f"⏸️  Rate limit reached. Waiting {wait_time:.1f}s...")
                    time.sleep(wait_time)
                    calls[:] = []

                calls.append(time.time())
                return func(*args, **kwargs)
            return wrapper
        return decorator


    def cache_result(ttl=5):
        """Cache results for specified time-to-live (seconds)"""
        def decorator(func):
            cache = {}

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                key = str(args) + str(kwargs)
                now = time.time()

                if key in cache:
                    result, timestamp = cache[key]
                    if now - timestamp < ttl:
                        print(f"💾 Returning cached result")
                        return result

                result = func(*args, **kwargs)
                cache[key] = (result, now)
                return result
            return wrapper
        return decorator


    def handle_errors(func):
        """Gracefully handle errors"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"🚫 Error handled: {type(e).__name__}: {e}")
                return {"status": "error", "message": str(e)}
        return wrapper


    # ============================================================================
    # SIMULATED API FUNCTIONS
    # ============================================================================

    # Simulate unreliable network
    call_count = 0

    @handle_errors
    @log_request
    @timer
    @retry(max_attempts=3, delay=0.5)
    @validate_response
    def fetch_user_data(user_id):
        """Simulate fetching user data from API"""
        global call_count
        call_count += 1

        # Simulate network delay
        time.sleep(random.uniform(0.1, 0.3))

        # Simulate occasional failures
        if call_count < 2:
            raise ConnectionError("Network timeout")

        # Return mock user data
        return {
            "status": "success",
            "user_id": user_id,
            "name": f"User {user_id}",
            "email": f"user{user_id}@example.com"
        }


    @log_request
    @timer
    @cache_result(ttl=3)
    @validate_response
    def get_cached_data(data_id):
        """Simulate fetching cached data"""
        time.sleep(0.2)  # Simulate processing
        return {
            "status": "success",
            "data_id": data_id,
            "value": random.randint(1, 100)
        }


    @log_request
    @rate_limit(calls_per_minute=3)
    def rate_limited_request(endpoint):
        """Simulate rate-limited API endpoint"""
        time.sleep(0.1)
        print(f"📡 Request sent to {endpoint}")
        return {"status": "success", "endpoint": endpoint}


    # ============================================================================
    # DEMONSTRATION
    # ============================================================================

    print("\n" + "=" * 70)
    print("DEMONSTRATION 1: Retry with Validation")
    print("=" * 70)
    print("This function will fail initially but succeed after retry")

    result = fetch_user_data(123)
    print(f"\n📊 Final Result: {result}")


    print("\n" + "=" * 70)
    print("DEMONSTRATION 2: Caching")
    print("=" * 70)
    print("First call will fetch data, second call will use cache")

    print("\n--- First call ---")
    result1 = get_cached_data(456)
    print(f"Result: {result1}")

    print("\n--- Second call (should be cached) ---")
    result2 = get_cached_data(456)
    print(f"Result: {result2}")

    print("\n--- Wait for cache to expire (3 seconds) ---")
    time.sleep(3.5)

    print("\n--- Third call (cache expired) ---")
    result3 = get_cached_data(456)
    print(f"Result: {result3}")


    print("\n" + "=" * 70)
    print("DEMONSTRATION 3: Rate Limiting")
    print("=" * 70)
    print("Making 5 requests (limit is 3 per minute)")

    for i in range(5):
        print(f"\n--- Request {i+1} ---")
        rate_limited_request(f"/api/endpoint{i}")


    print("\n" + "=" * 70)
    print("DEMONSTRATION 4: Error Handling")
    print("=" * 70)

    @handle_errors
    @validate_response
    def buggy_function():
        """This function has a bug"""
        return None  # Invalid response

    result = buggy_function()
    print(f"\n📊 Result: {result}")


    # ============================================================================
    # REAL-WORLD EXAMPLE: Complete API Client
    # ============================================================================

    print("\n" + "=" * 70)
    print("REAL-WORLD EXAMPLE: Complete API Client")
    print("=" * 70)

    class APIClient:
        """Example API client using decorators"""

        @staticmethod
        @handle_errors
        @log_request
        @timer
        @cache_result(ttl=10)
        @validate_response
        def get_weather(city):
            """Fetch weather data"""
            time.sleep(0.2)  # Simulate API call
            return {
                "status": "success",
                "city": city,
                "temperature": random.randint(60, 80),
                "condition": random.choice(["Sunny", "Cloudy", "Rainy"])
            }

        @staticmethod
        @handle_errors
        @log_request
        @timer
        @retry(max_attempts=2, delay=0.5)
        @rate_limit(calls_per_minute=5)
        @validate_response
        def post_data(endpoint, data):
            """Post data to API"""
            time.sleep(0.1)
            return {
                "status": "success",
                "endpoint": endpoint,
                "data_received": data
            }


    print("\nFetching weather data...")
    weather = APIClient.get_weather("New York")
    print(f"🌤️  {weather}")

    print("\nFetching weather data again (should use cache)...")
    weather = APIClient.get_weather("New York")
    print(f"🌤️  {weather}")

    print("\nPosting data...")
    post_result = APIClient.post_data("/api/data", {"value": 42})
    print(f"📤 {post_result}")


    # ============================================================================
    # SUMMARY
    # ============================================================================

    print("\n" + "=" * 70)
    print("PROJECT SUMMARY")
    print("=" * 70)
    print("""
    This mini-project demonstrated practical decorator usage:

    ✅ Decorators Used:
       - @log_request: Activity logging with timestamps
       - @timer: Performance measurement
       - @retry: Automatic retry on failure
       - @validate_response: Response validation
       - @rate_limit: API call throttling
       - @cache_result: Result caching with TTL
       - @handle_errors: Graceful error handling

    ✅ Key Patterns:
       - Multiple decorators stacked on single function
       - Decorators with parameters (retry attempts, cache TTL)
       - Class-based decorators for stateful behavior
       - Error handling and validation layers

    ✅ Real-World Applications:
       - API clients (REST, GraphQL)
       - Microservices communication
       - Database query optimization
       - Web scraping with rate limiting
       - Caching expensive computations

    ✅ Benefits:
       - Separation of concerns (logging, validation separate from logic)
       - Reusable cross-cutting functionality
       - Clean, readable code
       - Easy to add/remove features

    Try extending this project by adding:
       - Authentication decorator
       - Request timeout decorator
       - Response transformation decorator
       - Metrics collection decorator
       - Circuit breaker pattern
    """)

    print("=" * 70)
    print("END OF MINI-PROJECT")
    print("=" * 70)
