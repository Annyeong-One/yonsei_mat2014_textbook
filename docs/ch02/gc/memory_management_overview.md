# Memory Management Overview

Python의 메모리 관리는 두 가지 메커니즘이 함께 동작합니다.

## Two Mechanisms

### 1. Reference Counting

대부분의 객체는 참조 카운팅으로 즉시 해제됩니다.

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # Count references
```

### 2. Garbage Collection

순환 참조는 주기적인 가비지 컬렉션으로 처리됩니다.

```python
import gc

# Handle cycles
gc.collect()
```

## How They Work Together

```
Object Created
     │
     ▼
┌─────────────────┐
│ Reference Count │ ──→ refcount == 0 ──→ Freed Immediately
└─────────────────┘
     │
     ▼ (refcount > 0 but unreachable)
┌─────────────────┐
│  Cycle GC       │ ──→ Detects cycles ──→ Freed
└─────────────────┘
```

- **Refcount**: 즉각적인 메모리 해제 (대부분의 경우)
- **GC**: 순환 참조 처리 (주기적 실행)

## Summary

- Reference counting: immediate, deterministic
- Garbage collection: handles cycles
- Both work automatically
