"""
Backtracking: The Knight's Tour Problem

Backtracking is a systematic trial-and-error approach:
1. Try a candidate solution
2. If it leads to a dead end, undo (backtrack) and try the next option
3. Continue until a solution is found or all options are exhausted

The Knight's Tour: place a knight on a chessboard and visit every
square exactly once using valid knight moves.

Based on concepts from Python-100-Days example05 and ch05/recursion materials.
"""


# =============================================================================
# Example 1: Knight's Tour with Backtracking
# =============================================================================

# Knight's 8 possible L-shaped moves: (row_delta, col_delta)
KNIGHT_MOVES = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1),   (1, 2),   (-1, 2), (-2, 1),
]


def print_board(board: list[list[int]]) -> None:
    """Display the board with visit order numbers."""
    size = len(board)
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()
    print()


def knights_tour(size: int = 5, start_row: int = 0, start_col: int = 0,
                 find_all: bool = False) -> int:
    """Find knight's tour solutions using backtracking.

    Args:
        size: Board dimension (size x size).
        start_row: Starting row position.
        start_col: Starting column position.
        find_all: If True, find all solutions. If False, stop at first.

    Returns:
        Number of solutions found.
    """
    board = [[0] * size for _ in range(size)]
    solutions = [0]

    def solve(row: int, col: int, step: int) -> bool:
        """Recursively try to complete the tour.

        Backtracking logic:
        1. Place knight at (row, col) with step number
        2. If all squares visited -> solution found
        3. Try all 8 possible next moves
        4. If no move works -> undo placement (backtrack)
        """
        # Check bounds and whether square is already visited
        if not (0 <= row < size and 0 <= col < size and board[row][col] == 0):
            return False

        board[row][col] = step  # Place knight

        if step == size * size:  # All squares visited
            solutions[0] += 1
            print(f"Solution #{solutions[0]}:")
            print_board(board)
            if not find_all:
                return True  # Stop at first solution
            board[row][col] = 0  # Backtrack to find more
            return False

        # Try all 8 knight moves
        for dr, dc in KNIGHT_MOVES:
            if solve(row + dr, col + dc, step + 1):
                return True  # Solution found downstream

        board[row][col] = 0  # Backtrack: undo this placement
        return False

    solve(start_row, start_col, 1)
    return solutions[0]


# =============================================================================
# Example 2: Warnsdorff's Heuristic (optimization)
# =============================================================================

def count_valid_moves(board: list[list[int]], row: int, col: int) -> int:
    """Count how many valid moves exist from position (row, col)."""
    size = len(board)
    count = 0
    for dr, dc in KNIGHT_MOVES:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 0:
            count += 1
    return count


def knights_tour_warnsdorff(size: int = 8, start_row: int = 0,
                             start_col: int = 0) -> bool:
    """Knight's tour using Warnsdorff's rule: always move to the square
    with the fewest onward moves.

    This heuristic dramatically reduces backtracking and typically finds
    a solution in O(n^2) time for standard board sizes.
    """
    board = [[0] * size for _ in range(size)]
    board[start_row][start_col] = 1
    row, col = start_row, start_col

    for step in range(2, size * size + 1):
        # Get all valid next positions
        candidates = []
        for dr, dc in KNIGHT_MOVES:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 0:
                moves_from_next = count_valid_moves(board, nr, nc)
                candidates.append((moves_from_next, nr, nc))

        if not candidates:
            return False  # No valid moves - stuck

        # Choose square with fewest onward moves (Warnsdorff's rule)
        candidates.sort()
        _, row, col = candidates[0]
        board[row][col] = step

    print("Solution (Warnsdorff's heuristic):")
    print_board(board)
    return True


# =============================================================================
# Example 3: N-Queens as Another Backtracking Problem
# =============================================================================

def n_queens(n: int = 8) -> int:
    """Count solutions to the N-Queens problem using backtracking.

    Place n queens on an n x n board so no two queens threaten each other.

    >>> n_queens(4)
    2
    >>> n_queens(8)
    92
    """
    solutions = [0]
    cols = set()        # Columns with queens
    diag1 = set()       # row - col diagonals
    diag2 = set()       # row + col diagonals

    def place_queen(row: int):
        if row == n:
            solutions[0] += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # Conflict - skip
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            place_queen(row + 1)
            cols.remove(col)        # Backtrack
            diag1.remove(row - col)
            diag2.remove(row + col)

    place_queen(0)
    return solutions[0]


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    # Knight's tour on a small board (5x5)
    print("=== Knight's Tour (5x5, backtracking) ===")
    count = knights_tour(size=5, start_row=0, start_col=0)
    print(f"Found {count} solution(s)\n")

    # Warnsdorff's heuristic on a larger board (8x8)
    print("=== Knight's Tour (8x8, Warnsdorff's heuristic) ===")
    knights_tour_warnsdorff(size=8)

    # N-Queens
    print("=== N-Queens Solutions ===")
    for n in range(4, 11):
        print(f"  {n}-Queens: {n_queens(n)} solutions")
