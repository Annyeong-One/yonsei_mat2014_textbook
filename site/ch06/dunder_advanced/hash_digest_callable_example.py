"""
Callable Objects: Stream Hasher with __call__

Demonstrates the __call__ magic method by creating a callable class
that computes file hash digests. The object acts like a function but
maintains internal state (algorithm, buffer size).

Topics covered:
- __call__ to make instances callable
- hashlib for cryptographic hash functions
- Dynamic module/attribute loading with __import__ and getattr
- Iterator pattern with iter(callable, sentinel)

Based on concepts from Python-100-Days example07 and ch06/dunder_advanced materials.
"""

import hashlib
import io


# =============================================================================
# Example 1: Stream Hasher (Callable Class)
# =============================================================================

class StreamHasher:
    """A callable object that computes hash digests of data streams.

    By implementing __call__, instances can be used like functions:
        hasher = StreamHasher('sha256')
        digest = hasher(file_stream)  # Calls hasher.__call__(file_stream)

    This is more flexible than a plain function because the object
    retains configuration (algorithm, buffer size) as state.
    """

    SUPPORTED = ('md5', 'sha1', 'sha256', 'sha512')

    def __init__(self, algorithm: str = 'md5', buffer_size: int = 4096):
        """Initialize with hash algorithm and buffer size.

        Args:
            algorithm: Hash algorithm name (md5, sha1, sha256, sha512).
            buffer_size: Bytes to read per chunk.
        """
        if algorithm.lower() not in self.SUPPORTED:
            raise ValueError(
                f"Unsupported algorithm '{algorithm}'. "
                f"Choose from: {self.SUPPORTED}"
            )
        self.algorithm = algorithm.lower()
        self.buffer_size = buffer_size

    def digest(self, data_stream) -> str:
        """Compute hexadecimal hash digest from a data stream.

        Uses iter(callable, sentinel) pattern to read chunks:
        - callable: lambda that reads buffer_size bytes
        - sentinel: b'' (empty bytes = end of stream)
        """
        hasher = hashlib.new(self.algorithm)
        for chunk in iter(lambda: data_stream.read(self.buffer_size), b''):
            hasher.update(chunk)
        return hasher.hexdigest()

    def __call__(self, data_stream) -> str:
        """Make instances callable: hasher(stream) == hasher.digest(stream)."""
        return self.digest(data_stream)

    def __repr__(self):
        return f"StreamHasher('{self.algorithm}', buffer_size={self.buffer_size})"


# =============================================================================
# Example 2: Using Callable Objects
# =============================================================================

def demo_callable():
    """Demonstrate callable objects with hash computation."""
    print("=== Callable Object Demo ===")

    # Create hashers for different algorithms
    md5_hasher = StreamHasher('md5')
    sha256_hasher = StreamHasher('sha256')

    # Hash some data using BytesIO as a stream
    data = b"Hello, World! This is a test of the callable hasher."

    stream1 = io.BytesIO(data)
    stream2 = io.BytesIO(data)

    # Both calling styles work:
    md5_digest = md5_hasher(stream1)           # Using __call__
    sha256_digest = sha256_hasher.digest(stream2)  # Using method directly

    print(f"Data: {data.decode()!r}")
    print(f"MD5:    {md5_digest}")
    print(f"SHA256: {sha256_digest}")
    print()

    # Verify callable() built-in
    print(f"callable(md5_hasher): {callable(md5_hasher)}")
    print(f"callable('string'):   {callable('string')}")
    print()


# =============================================================================
# Example 3: Callable vs Function
# =============================================================================

def simple_md5(data: bytes) -> str:
    """Plain function alternative to callable class."""
    return hashlib.md5(data).hexdigest()


def demo_callable_vs_function():
    """Compare callable class vs plain function."""
    print("=== Callable Class vs Function ===")

    data = b"test data"

    # Function: simple but no configuration
    result1 = simple_md5(data)
    print(f"Function:        {result1}")

    # Callable object: configurable and stateful
    hasher = StreamHasher('md5', buffer_size=2)
    result2 = hasher(io.BytesIO(data))
    print(f"Callable object: {result2}")
    print(f"Same result:     {result1 == result2}")

    print()
    print("When to use callable classes:")
    print("  - Need configurable behavior (algorithm, buffer size)")
    print("  - Want to maintain state between calls")
    print("  - Implementing strategy/command patterns")
    print("  - Need both function-call and method-call interfaces")
    print()


# =============================================================================
# Example 4: iter(callable, sentinel) Pattern
# =============================================================================

def demo_iter_sentinel():
    """Demonstrate the iter(callable, sentinel) pattern used in StreamHasher."""
    print("=== iter(callable, sentinel) Pattern ===")

    # iter() with two args: calls the callable until it returns sentinel
    data = io.BytesIO(b"Hello World")

    print("Reading 3 bytes at a time until empty:")
    chunks = list(iter(lambda: data.read(3), b''))
    print(f"  Chunks: {chunks}")
    print()

    print("This is equivalent to:")
    print("  while True:")
    print("      chunk = stream.read(3)")
    print("      if chunk == b'':  # sentinel")
    print("          break")
    print("      process(chunk)")
    print()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_callable()
    demo_callable_vs_function()
    demo_iter_sentinel()
