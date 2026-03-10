# Divide and Conquer


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Divide and Conquer is a recursive algorithm pattern that solves problems by breaking them into smaller subproblems, solving each independently, then combining results.

---

## The Divide and Conquer Pattern

1. **Divide**: Break problem into smaller subproblems
2. **Conquer**: Solve subproblems recursively (or directly if small)
3. **Combine**: Merge solutions to subproblems

## Merge Sort Example

```python
def merge_sort(arr):
    '''Sort array using divide and conquer'''
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Combine
    return merge(left_sorted, right_sorted)

def merge(left, right):
    '''Merge two sorted arrays'''
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # [3, 9, 10, 27, 38, 43, 82]
```

## Binary Search (Divide and Conquer)

```python
def binary_search(arr, target, low=0, high=None):
    '''Search for target in sorted array'''
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1  # Not found
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid  # Found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # Search right half
    else:
        return binary_search(arr, target, low, mid - 1)   # Search left half

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 7))   # 3
print(binary_search(arr, 6))   # -1
```

## Quick Sort Example

```python
def quick_sort(arr):
    '''Sort array using divide and conquer with pivot'''
    if len(arr) <= 1:
        return arr
    
    # Divide using pivot
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    # Conquer (recursive)
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    
    # Combine
    return left_sorted + [pivot] + right_sorted

arr = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(arr))  # [3, 9, 10, 27, 38, 43, 82]
```

## Time Complexity Analysis

- **Merge Sort**: O(n log n) - always
- **Quick Sort**: O(n log n) average, O(n²) worst case
- **Binary Search**: O(log n)

Divide and Conquer is powerful for problems naturally decomposable into similar subproblems.
