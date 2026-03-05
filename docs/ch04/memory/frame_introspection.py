"""
Frame Object Introspection: Generators, f_lasti, and Zombie Frames

Deep exploration of CPython frame objects using generators as
an introspection tool. Generators freeze execution mid-function,
letting us inspect the frame's internal state at each step.

Topics covered:
1. Generator-based frame stepping (gi_frame, f_lasti)
2. Frame back chain (f_back linked list)
3. Frame locals and code object relationship
4. Zombie frame reuse (memory optimization)
5. Block stack observation via try/except in generators

Based on CPython-Internals Interpreter/frame/frame.md examples.
"""

import dis
import inspect
import sys


# =============================================================================
# 1. Generator Frame Stepping with f_lasti
# =============================================================================

def demo_generator_frame_stepping():
    """Use a generator to observe frame state at each yield point.

    Every generator object has a gi_frame attribute pointing to
    its execution frame. f_lasti tracks the bytecode offset of
    the last executed instruction.
    """
    print("=== Generator Frame Stepping ===\n")

    def gen(a, b=1, c=2):
        yield a
        c = str(b + c)
        yield c
        new_g = range(3)
        yield from new_g

    # Show bytecode so we can correlate f_lasti values
    print("--- Bytecode for gen() ---")
    dis.dis(gen)
    print()

    gg = gen("param_a")

    # Before first next(): frame exists but hasn't executed
    print(f"Before first next():")
    print(f"  gi_frame: {gg.gi_frame}")
    print(f"  f_lasti:  {gg.gi_frame.f_lasti}")
    print(f"  f_locals: {gg.gi_frame.f_locals}")
    print()

    # Step through and observe f_lasti advancing
    step = 0
    for val in gg:
        step += 1
        frame = gg.gi_frame
        if frame is not None:
            print(f"Step {step}: yielded {val!r}")
            print(f"  f_lasti:    {frame.f_lasti}")
            print(f"  f_locals:   {frame.f_locals}")
            print(f"  f_lineno:   {frame.f_lineno}")
        else:
            print(f"Step {step}: yielded {val!r}")
            print(f"  gi_frame is None (generator exhausted)")
        print()

    # After exhaustion
    print(f"After StopIteration:")
    print(f"  gi_frame: {gg.gi_frame}")
    print()


# =============================================================================
# 2. Frame Back Chain (f_back Linked List)
# =============================================================================

def demo_frame_back_chain():
    """Each frame's f_back points to the caller's frame,
    forming a singly linked list (the call stack).
    """
    print("=== Frame Back Chain ===\n")

    def show_stack(depth):
        """Recursively descend, then print the frame chain."""
        if depth > 0:
            show_stack(depth - 1)
        else:
            # Walk the f_back chain from current frame
            frame = inspect.currentframe()
            chain = []
            while frame is not None:
                chain.append(
                    f"{frame.f_code.co_name}() "
                    f"[line {frame.f_lineno}]"
                )
                frame = frame.f_back

            print("Call stack (current -> outermost):")
            for i, entry in enumerate(chain):
                indent = "  " * i
                print(f"  {indent}{entry}")
            print()

    show_stack(3)


# =============================================================================
# 3. Frame Locals vs Code Object
# =============================================================================

def demo_frame_code_relationship():
    """The frame's f_code points to the code object being executed.
    We can inspect code object metadata through the frame.
    """
    print("=== Frame and Code Object Relationship ===\n")

    def example_func(x, y, *args, key=None, **kwargs):
        """A function with various parameter types."""
        local_var = x + y
        frame = inspect.currentframe()

        code = frame.f_code
        print(f"Function: {code.co_name}")
        print(f"  co_argcount:      {code.co_argcount}")
        print(f"  co_varnames:      {code.co_varnames}")
        print(f"  co_nlocals:       {code.co_nlocals}")
        print(f"  co_stacksize:     {code.co_stacksize}")
        print(f"  co_firstlineno:   {code.co_firstlineno}")
        print()
        print(f"  f_locals keys:    {list(frame.f_locals.keys())}")
        print(f"  f_lineno:         {frame.f_lineno}")
        print()

    example_func(10, 20, 30, 40, key="test", extra=99)


# =============================================================================
# 4. Zombie Frame Reuse
# =============================================================================

def demo_zombie_frame_reuse():
    """CPython reuses frame objects for the same code object.

    The first frame created for a code object becomes a 'zombie'
    frame after execution. Next call to the same function reuses
    that frame, saving malloc overhead.

    We can observe this with generators: after a generator is
    exhausted, the next generator from the same function often
    gets a frame at the same memory address.
    """
    print("=== Zombie Frame Reuse ===\n")

    def simple_gen():
        yield 1

    # First generator
    g1 = simple_gen()
    frame1_id = id(g1.gi_frame)
    print(f"g1 frame id: {frame1_id}")

    # Exhaust it
    list(g1)
    print(f"g1 exhausted, gi_frame: {g1.gi_frame}")

    # Second generator from same function
    g2 = simple_gen()
    frame2_id = id(g2.gi_frame)
    print(f"g2 frame id: {frame2_id}")

    if frame1_id == frame2_id:
        print("  -> Same frame object reused (zombie frame)!")
    else:
        print("  -> Different frame object (may vary by Python version)")

    # Exhaust g2 and try a third
    list(g2)
    g3 = simple_gen()
    frame3_id = id(g3.gi_frame)
    print(f"g3 frame id: {frame3_id}")

    if frame3_id == frame1_id:
        print("  -> Same zombie frame reused again!")
    print()


# =============================================================================
# 5. Block Stack via Generator Try/Except
# =============================================================================

def demo_block_stack():
    """Generators with try/except blocks demonstrate how the
    frame manages exception handling context.

    Each try/except/finally creates entries on the frame's
    internal block stack (f_iblock in CPython).
    """
    print("=== Block Stack via Try/Except in Generator ===\n")

    def error_gen():
        """Generator that steps through nested exception handlers."""
        try:
            yield "in try block"
            1 / 0
        except ZeroDivisionError:
            yield "in except ZeroDivisionError"
            try:
                yield "in nested try"
                import nonexistent_module_xyz  # noqa: F401
            except ModuleNotFoundError:
                yield "in except ModuleNotFoundError"
            finally:
                yield "in finally"

    gg = error_gen()
    step = 0
    for val in gg:
        step += 1
        frame = gg.gi_frame
        info = ""
        if frame is not None:
            info = f"  f_lasti={frame.f_lasti}, f_lineno={frame.f_lineno}"
        print(f"  Step {step}: {val!r}{info}")

    print(f"\n  After exhaustion: gi_frame = {gg.gi_frame}")
    print()


# =============================================================================
# 6. sys._current_frames() — All Thread Frames
# =============================================================================

def demo_current_frames():
    """sys._current_frames() returns a dict mapping thread IDs
    to their current frame objects. Useful for debugging hangs.
    """
    print("=== sys._current_frames() ===\n")

    frames = sys._current_frames()
    print(f"Active threads: {len(frames)}")
    for tid, frame in frames.items():
        chain = []
        f = frame
        while f is not None:
            chain.append(f.f_code.co_name)
            f = f.f_back
        print(f"  Thread {tid}: {' -> '.join(chain)}")
    print()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_generator_frame_stepping()
    demo_frame_back_chain()
    demo_frame_code_relationship()
    demo_zombie_frame_reuse()
    demo_block_stack()
    demo_current_frames()
