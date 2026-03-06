"""
TUTORIAL: Using threading.Event for Thread Coordination
========================================================

In this tutorial, you'll learn how to use threading.Event as a simple but
powerful synchronization mechanism for coordinating threads.

KEY CONCEPTS:
- threading.Event: A simple flag-like object for thread communication
- event.set() and event.wait(): Basic signaling mechanism
- Practical pattern: Using events to signal threads to stop gracefully
- Real-world example: Animated spinner that responds to task completion

CREDITS: Adapted from Michele Simionato's example in python-list:
https://mail.python.org/pipermail/python-list/2009-February/675659.html
"""

import itertools
import time
from threading import Thread, Event


print("=" * 70)
print("THREADING.EVENT FOR THREAD COORDINATION")
print("=" * 70)
print()


# ============ EXAMPLE 1: Understanding threading.Event
# =====================================================

print("EXAMPLE 1: What is threading.Event?")
print("-" * 70)
print()
print("threading.Event is like a simple 'flag' that threads can use to")
print("communicate with each other. It has two states: set or unset.")
print()

event = Event()
print(f"• Created an event: {event}")
print(f"• Is it set? {event.is_set()}")
print()

# When we call event.set(), the flag becomes True
event.set()
print(f"After event.set():")
print(f"• Is it set now? {event.is_set()}")
print()

# When we call event.clear(), the flag becomes False again
event.clear()
print(f"After event.clear():")
print(f"• Is it set now? {event.is_set()}")
print()


# ============ EXAMPLE 2: The Spinner Function - Showing Activity
# ================================================================

print("EXAMPLE 2: Creating a Spinner Thread")
print("-" * 70)
print()
print("A spinner shows the user that work is happening. We use an Event")
print("to let the spinner know when the work is complete so it can stop.")
print()


def spin(msg: str, done: Event) -> None:
    """
    Display an animated spinner while work is being done.

    WHY THIS DESIGN:
    - itertools.cycle creates a never-ending loop of characters
    - done.wait(timeout) checks if work is finished every 0.1 seconds
    - Using \r (carriage return) overwrites the same line for animation
    - flush=True ensures output appears immediately

    Args:
        msg: The message to display next to the spinner
        done: An Event that signals when to stop spinning
    """
    print(f"\nStarting spinner with message: '{msg}'")
    print("(Watch the animation below - it's cycling through characters)")
    print()

    spinner_chars = r'\|/-'
    char_count = 0

    for char in itertools.cycle(spinner_chars):
        # WHY cycle()? It lets us loop through 4 characters infinitely.
        # When we reach the end, it automatically starts over.

        status = f'\r{char} {msg}'
        print(status, end='', flush=True)

        # done.wait(0.1) does two things:
        # 1. Waits up to 0.1 seconds for the event to be set
        # 2. Returns True if event was set, False if timeout occurred
        if done.wait(0.1):
            # The event was set! This means we should stop spinning.
            break

        char_count += 1

    # Clear the spinner line so it doesn't stay visible
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

    print(f"Spinner stopped after {char_count} iterations")
    print()


def slow_task() -> int:
    """
    Simulate a long-running task that takes 3 seconds.

    WHY: This represents real work - downloading, processing, etc.
    We'll run the spinner while this happens.
    """
    print("Long task: Starting 3-second sleep...")
    time.sleep(3)
    print("Long task: Finished!")
    return 42


# ============ EXAMPLE 3: The Supervisor - Coordinating Threads
# ==============================================================

print("EXAMPLE 3: Coordinating Threads with an Event")
print("-" * 70)
print()
print("The supervisor orchestrates two things:")
print("1. A worker thread (spinner) showing progress")
print("2. The main thread doing the actual work")
print("Both use an Event to coordinate.")
print()


def supervisor() -> int:
    """
    Manage the spinner thread and the work.

    WHY THIS PATTERN:
    - done Event starts as unset (clear). This tells spinner: keep spinning!
    - We start() the spinner thread to run in parallel
    - Main thread calls slow_task() to do the actual work
    - When work is done, we call done.set() to stop the spinner
    - We join() to wait for the spinner thread to fully exit

    This is a clean, safe way to coordinate threads.
    """

    # Create an Event object. It starts in the "unset" state.
    done = Event()

    # Create a Thread object that will run the spin() function
    # We pass the message and the Event object
    spinner = Thread(target=spin, args=('thinking!', done))

    print(f"Created spinner thread: {spinner}")
    print()

    # Start the spinner thread. It now runs in parallel with this code.
    spinner.start()
    print("Spinner thread started (running in parallel now)")
    print()

    # Do the work. Meanwhile, the spinner thread is still animating.
    result = slow_task()

    # Now tell the spinner to stop by setting the event
    done.set()
    print("Main thread: Set the done event (telling spinner to stop)")
    print()

    # Wait for the spinner thread to fully finish
    spinner.join()
    print("Main thread: Joined with spinner thread (both are done now)")
    print()

    return result


# ============ EXAMPLE 4: Running the Full Demo
# ==============================================

def main() -> None:
    """Run the complete demonstration."""
    print("EXAMPLE 4: Running the Full Demonstration")
    print("-" * 70)
    print()

    result = supervisor()

    print()
    print("=" * 70)
    print(f"RESULT: The answer is {result}")
    print("=" * 70)


# ============ EXAMPLE 5: Key Takeaways
# ======================================

print()
print("=" * 70)
print("KEY CONCEPTS TO REMEMBER:")
print("=" * 70)
print()
print("1. threading.Event is like a flag threads can check/set")
print()
print("2. event.set() signals 'True' - work is done, stop waiting")
print("3. event.wait(timeout) pauses until set or timeout, returns bool")
print()
print("4. This pattern is much safer than forcefully killing threads")
print()
print("5. Perfect for: progress indicators, graceful shutdown, signals")
print()
print("=" * 70)
print()


if __name__ == '__main__':
    main()
