# Backtracking


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Backtracking is a recursive algorithm pattern that explores possible solutions, abandoning paths when they become invalid. It's used for constraint satisfaction problems.

---

## The Backtracking Pattern

1. Choose a candidate solution path
2. Explore recursively
3. If path leads to solution, return it
4. If path is invalid, backtrack and try another path

## N-Queens Problem

```python
def solve_nqueens(n):
    '''Find all valid placements of n queens on n×n board'''
    results = []
    board = []
    
    def is_safe(row, col):
        '''Check if position is safe from other queens'''
        for i in range(row):
            if board[i] == col:  # Same column
                return False
            if abs(board[i] - col) == abs(i - row):  # Diagonal
                return False
        return True
    
    def backtrack(row):
        '''Recursively place queens'''
        if row == n:
            results.append(board[:])  # Found solution
            return
        
        for col in range(n):
            if is_safe(row, col):
                board.append(col)              # Choose
                backtrack(row + 1)             # Explore
                board.pop()                    # Backtrack
    
    backtrack(0)
    return results

solutions = solve_nqueens(4)
print(f"Found {len(solutions)} solutions for 4 queens")  # 2 solutions
```

## Word Search Problem

```python
def word_search(board, word):
    '''Find word in 2D board by tracing paths'''
    if not board or not word:
        return False
    
    visited = set()
    
    def backtrack(row, col, index):
        # Base case: matched entire word
        if index == len(word):
            return True
        
        # Check bounds and visited
        if (row < 0 or row >= len(board) or
            col < 0 or col >= len(board[0]) or
            (row, col) in visited or
            board[row][col] != word[index]):
            return False
        
        # Choose: mark as visited
        visited.add((row, col))
        
        # Explore: try all 4 directions
        result = (backtrack(row + 1, col, index + 1) or
                 backtrack(row - 1, col, index + 1) or
                 backtrack(row, col + 1, index + 1) or
                 backtrack(row, col - 1, index + 1))
        
        # Backtrack: unmark visited
        visited.remove((row, col))
        
        return result
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

print(word_search(board, "ABCB"))   # False
print(word_search(board, "SEE"))    # True
```

## Combination Problem

```python
def generate_combinations(n, k):
    '''Generate all combinations of k numbers from 1 to n'''
    results = []
    
    def backtrack(start, combination):
        # Base case: combination is complete
        if len(combination) == k:
            results.append(combination[:])
            return
        
        # Try adding each number
        for i in range(start, n + 1):
            combination.append(i)      # Choose
            backtrack(i + 1, combination)  # Explore
            combination.pop()           # Backtrack
    
    backtrack(1, [])
    return results

print(generate_combinations(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

## Performance Notes

- Backtracking explores exponential search space
- Pruning (early rejection) is critical for performance
- Best used for constraint satisfaction problems
- Always check validity before exploring deeper
