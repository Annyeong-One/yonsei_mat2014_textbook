"""
Topic 45.2 - Threading Basics with threading.Thread

Complete guide to Python's threading module, covering thread creation,
management, and basic patterns.

Learning Objectives:
- Create and start threads
- Pass arguments to threads
- Wait for thread completion (join)
- Daemon threads
- Thread naming and identification
- Thread-local storage

Author: Python Educator
Date: 2024
"""

import threading
import time
import random
from queue import Queue


# ============================================================================
# PART 1: BEGINNER - Creating and Starting Threads
# ============================================================================

def basic_thread_creation():
    """
    The most fundamental way to create a thread: using threading.Thread
    with a target function.
    """
    print("=" * 70)
    print("BEGINNER: Creating Your First Thread")
    print("=" * 70)
    
    def worker():
        """Simple function that will run in a separate thread"""
        print(f"  Worker thread started: {threading.current_thread().name}")
        time.sleep(1)  # Simulate some work
        print(f"  Worker thread finished: {threading.current_thread().name}")
    
    print("\n📝 Creating a thread:")
    print("   thread = threading.Thread(target=worker)")
    print("   thread.start()")
    
    # Create the thread
    thread = threading.Thread(target=worker)
    
    print(f"\nMain thread: {threading.current_thread().name}")
    print("Starting worker thread...")
    
    # Start the thread (begins execution)
    thread.start()
    
    print("Main thread continues while worker runs...")
    
    # Wait for the thread to complete
    thread.join()
    
    print("Worker thread has finished. Main thread exiting.\n")
    print("=" * 70 + "\n")


def threads_with_arguments():
    """
    Pass arguments to thread functions using args and kwargs.
    """
    print("=" * 70)
    print("BEGINNER: Passing Arguments to Threads")
    print("=" * 70)
    
    def greet(name, greeting="Hello"):
        """
        Function that takes arguments - will be run in a thread.
        
        Args:
            name: Person's name
            greeting: Greeting message (default: "Hello")
        """
        thread_name = threading.current_thread().name
        print(f"[{thread_name}] {greeting}, {name}!")
        time.sleep(0.5)
    
    print("\n📝 Method 1: Using args tuple")
    # Pass arguments as tuple
    thread1 = threading.Thread(target=greet, args=("Alice",))
    thread1.start()
    thread1.join()
    
    print("\n📝 Method 2: Using kwargs dictionary")
    # Pass arguments as keyword arguments
    thread2 = threading.Thread(
        target=greet,
        kwargs={"name": "Bob", "greeting": "Hi"}
    )
    thread2.start()
    thread2.join()
    
    print("\n📝 Method 3: Both args and kwargs")
    # Mix positional and keyword arguments
    thread3 = threading.Thread(
        target=greet,
        args=("Charlie",),
        kwargs={"greeting": "Hey"}
    )
    thread3.start()
    thread3.join()
    
    print("\n" + "=" * 70 + "\n")


def multiple_threads_example():
    """
    Create and manage multiple threads simultaneously.
    """
    print("=" * 70)
    print("BEGINNER: Running Multiple Threads")
    print("=" * 70)
    
    def download_file(file_id, duration):
        """
        Simulate downloading a file.
        
        Args:
            file_id: File identifier
            duration: Download duration in seconds
        """
        thread = threading.current_thread().name
        print(f"[{thread}] Starting download of file {file_id}")
        time.sleep(duration)  # Simulate download time
        print(f"[{thread}] Completed download of file {file_id}")
    
    print("\n⏱️  Downloading 5 files concurrently...\n")
    start_time = time.time()
    
    # Create multiple threads
    threads = []
    for i in range(5):
        # Each download takes 1-2 seconds
        duration = random.uniform(1.0, 2.0)
        
        thread = threading.Thread(
            target=download_file,
            args=(i, duration),
            name=f"Downloader-{i}"  # Give thread a meaningful name
        )
        threads.append(thread)
        thread.start()  # Start immediately
    
    # Wait for all threads to complete
    print("Main thread waiting for all downloads to complete...")
    for thread in threads:
        thread.join()  # Block until this thread finishes
    
    elapsed = time.time() - start_time
    print(f"\n✓ All downloads completed in {elapsed:.2f} seconds")
    print("  (Sequential would have taken ~7.5 seconds)")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# PART 2: INTERMEDIATE - Thread Management and Control
# ============================================================================

def daemon_threads_explained():
    """
    Daemon threads are background threads that don't prevent program exit.
    They're useful for background tasks that should stop when main exits.
    """
    print("=" * 70)
    print("INTERMEDIATE: Daemon Threads")
    print("=" * 70)
    
    def background_task(task_id):
        """
        Background task that runs indefinitely.
        
        Args:
            task_id: Task identifier
        """
        try:
            while True:
                print(f"  Background task {task_id} is running...")
                time.sleep(1)
        except Exception as e:
            print(f"  Task {task_id} interrupted: {e}")
    
    print("\n📝 Normal (Non-Daemon) Thread:")
    print("   Keeps program alive until it completes\n")
    
    # Create a normal thread (daemon=False is default)
    normal_thread = threading.Thread(
        target=lambda: print("  Normal thread: I'll complete my work"),
        daemon=False
    )
    normal_thread.start()
    normal_thread.join()  # Wait for it
    print("  ✓ Normal thread completed\n")
    
    print("📝 Daemon Thread:")
    print("   Automatically stops when main program exits\n")
    
    # Create a daemon thread
    daemon_thread = threading.Thread(
        target=background_task,
        args=(1,),
        daemon=True  # This makes it a daemon thread
    )
    
    print("  Starting daemon thread...")
    daemon_thread.start()
    
    # Let it run for a bit
    time.sleep(2.5)
    
    print("\n  Main thread exiting (daemon will stop automatically)")
    print("  Notice: daemon thread doesn't prevent program exit")
    
    print("\n💡 Use Cases for Daemon Threads:")
    print("  ✓ Background monitoring")
    print("  ✓ Periodic cleanup tasks")
    print("  ✓ Logging/metrics collection")
    print("  ✓ Keep-alive connections")
    
    print("\n" + "=" * 70 + "\n")


def thread_properties_and_methods():
    """
    Explore thread properties: name, ident, daemon status, alive status.
    """
    print("=" * 70)
    print("INTERMEDIATE: Thread Properties and Methods")
    print("=" * 70)
    
    def worker(duration):
        """Worker that sleeps for specified duration"""
        time.sleep(duration)
    
    # Create a thread
    thread = threading.Thread(
        target=worker,
        args=(2,),
        name="MyWorkerThread"
    )
    
    print("\n📊 Before Starting:")
    print(f"  Name: {thread.name}")
    print(f"  Daemon: {thread.daemon}")
    print(f"  Is alive: {thread.is_alive()}")
    print(f"  Ident: {thread.ident}")  # None until started
    
    # Start the thread
    thread.start()
    
    print("\n📊 After Starting:")
    print(f"  Name: {thread.name}")
    print(f"  Daemon: {thread.daemon}")
    print(f"  Is alive: {thread.is_alive()}")
    print(f"  Ident: {thread.ident}")  # Now has an ID
    
    # Wait for completion
    thread.join()
    
    print("\n📊 After Completion:")
    print(f"  Is alive: {thread.is_alive()}")
    print(f"  Ident: {thread.ident}")  # Still has ID
    
    # Current thread info
    print("\n📊 Current (Main) Thread:")
    current = threading.current_thread()
    print(f"  Name: {current.name}")
    print(f"  Ident: {current.ident}")
    
    # All active threads
    print("\n📊 All Active Threads:")
    for t in threading.enumerate():
        print(f"  - {t.name} (daemon={t.daemon}, alive={t.is_alive()})")
    
    print("\n" + "=" * 70 + "\n")


def thread_joining_patterns():
    """
    Different patterns for waiting on threads with join().
    """
    print("=" * 70)
    print("INTERMEDIATE: Thread Joining Patterns")
    print("=" * 70)
    
    def task(task_id, duration):
        """Task that takes specified time to complete"""
        print(f"  Task {task_id} started")
        time.sleep(duration)
        print(f"  Task {task_id} completed")
    
    # Pattern 1: Join with timeout
    print("\n📝 Pattern 1: Join with Timeout")
    thread = threading.Thread(target=task, args=(1, 2))
    thread.start()
    
    print("  Waiting up to 1 second...")
    thread.join(timeout=1.0)  # Wait max 1 second
    
    if thread.is_alive():
        print("  ⏱️  Timeout! Thread still running")
        print("  Continuing without waiting...")
        thread.join()  # Wait for actual completion
    
    # Pattern 2: Join all threads
    print("\n📝 Pattern 2: Join All Threads")
    threads = []
    for i in range(3):
        t = threading.Thread(target=task, args=(i+2, 1))
        threads.append(t)
        t.start()
    
    print("  Waiting for all threads...")
    for t in threads:
        t.join()
    print("  ✓ All threads completed")
    
    # Pattern 3: Non-blocking check
    print("\n📝 Pattern 3: Non-blocking Status Check")
    thread = threading.Thread(target=task, args=(5, 1.5))
    thread.start()
    
    while thread.is_alive():
        print("  Thread still running, doing other work...")
        time.sleep(0.5)
    
    print("  ✓ Thread finished")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# PART 3: ADVANCED - Thread Classes and Local Storage
# ============================================================================

class WorkerThread(threading.Thread):
    """
    Advanced: Custom thread class by inheriting from threading.Thread.
    Override run() method to define thread behavior.
    """
    
    def __init__(self, task_name, iterations):
        """
        Initialize the custom thread.
        
        Args:
            task_name: Name of the task
            iterations: Number of iterations to perform
        """
        # IMPORTANT: Call parent __init__
        super().__init__()
        
        # Store instance variables
        self.task_name = task_name
        self.iterations = iterations
        self.result = None
    
    def run(self):
        """
        This method is called when start() is invoked.
        Override this to define what the thread does.
        """
        print(f"[{self.name}] Starting task: {self.task_name}")
        
        # Perform work
        total = 0
        for i in range(self.iterations):
            total += i
            if i % 100000 == 0:
                time.sleep(0.01)  # Simulate some I/O
        
        # Store result
        self.result = total
        
        print(f"[{self.name}] Completed task: {self.task_name}")
        print(f"[{self.name}] Result: {self.result}")


def custom_thread_class_example():
    """
    Demonstrate using a custom thread class.
    """
    print("=" * 70)
    print("ADVANCED: Custom Thread Class")
    print("=" * 70)
    
    print("\n📝 Creating custom thread instances:\n")
    
    # Create thread instances
    thread1 = WorkerThread("Calculate-A", 500000)
    thread2 = WorkerThread("Calculate-B", 300000)
    
    # Give them custom names
    thread1.name = "Calculator-1"
    thread2.name = "Calculator-2"
    
    # Start them
    thread1.start()
    thread2.start()
    
    # Wait for completion
    thread1.join()
    thread2.join()
    
    # Access results
    print(f"\n📊 Results:")
    print(f"  Thread 1 result: {thread1.result}")
    print(f"  Thread 2 result: {thread2.result}")
    
    print("\n💡 Benefits of Custom Thread Class:")
    print("  ✓ Encapsulate thread logic")
    print("  ✓ Store thread-specific data")
    print("  ✓ Easier to access results")
    print("  ✓ More object-oriented design")
    
    print("\n" + "=" * 70 + "\n")


def thread_local_storage_example():
    """
    Thread-local storage: Each thread gets its own copy of data.
    Useful for storing per-thread state without passing it around.
    """
    print("=" * 70)
    print("ADVANCED: Thread-Local Storage")
    print("=" * 70)
    
    # Create thread-local storage
    thread_local = threading.local()
    
    def worker(worker_id):
        """
        Each thread stores its own data in thread_local.
        
        Args:
            worker_id: Worker identifier
        """
        # Store thread-specific data
        thread_local.worker_id = worker_id
        thread_local.counter = 0
        thread_local.name = f"Worker-{worker_id}"
        
        print(f"[{thread_local.name}] Starting work")
        
        # Do some work
        for i in range(5):
            thread_local.counter += 1
            time.sleep(0.1)
            print(f"[{thread_local.name}] Counter: {thread_local.counter}")
        
        # Access thread-specific data
        print(f"[{thread_local.name}] Final state:")
        print(f"  Worker ID: {thread_local.worker_id}")
        print(f"  Counter: {thread_local.counter}")
    
    print("\n📝 Starting threads with thread-local storage:\n")
    
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all
    for thread in threads:
        thread.join()
    
    print("\n💡 Key Points:")
    print("  • Each thread has its own copy of thread_local data")
    print("  • No need for locks when accessing thread_local")
    print("  • Data automatically cleaned up when thread exits")
    print("  • Useful for database connections, request contexts, etc.")
    
    print("\n" + "=" * 70 + "\n")


def producer_consumer_basic():
    """
    Advanced pattern: Basic producer-consumer using threads.
    One thread produces items, another consumes them.
    """
    print("=" * 70)
    print("ADVANCED: Producer-Consumer Pattern")
    print("=" * 70)
    
    # Shared queue (thread-safe)
    queue = Queue(maxsize=5)
    
    def producer(num_items):
        """
        Produce items and put them in the queue.
        
        Args:
            num_items: Number of items to produce
        """
        for i in range(num_items):
            item = f"Item-{i}"
            print(f"Producer: Creating {item}")
            queue.put(item)  # Thread-safe put
            time.sleep(0.5)  # Simulate production time
        
        # Signal completion
        queue.put(None)  # Sentinel value
        print("Producer: Finished producing")
    
    def consumer():
        """
        Consume items from the queue until None is received.
        """
        while True:
            item = queue.get()  # Thread-safe get (blocks if empty)
            
            if item is None:
                print("Consumer: Received stop signal")
                break
            
            print(f"Consumer: Processing {item}")
            time.sleep(0.8)  # Simulate processing time
            queue.task_done()  # Mark as processed
        
        print("Consumer: Finished consuming")
    
    print("\n⚙️  Starting producer-consumer system:\n")
    
    # Create threads
    producer_thread = threading.Thread(target=producer, args=(8,))
    consumer_thread = threading.Thread(target=consumer)
    
    # Start both
    producer_thread.start()
    consumer_thread.start()
    
    # Wait for completion
    producer_thread.join()
    consumer_thread.join()
    
    print("\n✓ Producer-consumer completed")
    
    print("\n💡 This pattern is useful for:")
    print("  • Decoupling production and consumption rates")
    print("  • Buffering between fast and slow operations")
    print("  • Load balancing across multiple workers")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run all threading demonstrations."""
    print("\n" + "=" * 70)
    print(" " * 20 + "THREADING BASICS")
    print(" " * 15 + "threading.Thread Tutorial")
    print("=" * 70 + "\n")
    
    # Beginner level
    basic_thread_creation()
    threads_with_arguments()
    multiple_threads_example()
    
    # Intermediate level
    daemon_threads_explained()
    thread_properties_and_methods()
    thread_joining_patterns()
    
    # Advanced level
    custom_thread_class_example()
    thread_local_storage_example()
    producer_consumer_basic()
    
    print("\n" + "=" * 70)
    print("Threading Basics Tutorial Complete!")
    print("=" * 70)
    print("\n💡 Key Takeaways:")
    print("1. Use threading.Thread(target=func) to create threads")
    print("2. Call start() to begin execution, join() to wait")
    print("3. Daemon threads stop automatically when main exits")
    print("4. Use thread.name and thread.is_alive() for monitoring")
    print("5. Custom thread classes offer better encapsulation")
    print("6. Thread-local storage provides per-thread data")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
