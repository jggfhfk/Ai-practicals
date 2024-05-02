def get_user_input():
    print("Enter the initial state of the puzzle (3x3 grid):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)
    return initial_state

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move_blank(state, direction):
    def find_blank(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    blank_i, blank_j = find_blank(state)
    new_state = [row[:] for row in state]
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    move_i, move_j = moves[direction]
    new_i, new_j = blank_i + move_i, blank_j + move_j

    if 0 <= new_i < 3 and 0 <= new_j < 3:
        new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]

    return new_state


def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def solve_puzzle(initial_state):
    moves = ["up", "down", "left", "right"]
    explored_states = set()
    queue = [(initial_state, [])]

    while queue:
        state, path = queue.pop(0)
        if is_goal(state):
            return path
        explored_states.add(str(state))
        for move in moves:
            new_state = move_blank(state, move)
            if str(new_state) not in explored_states:
                queue.append((new_state, path + [move]))

    return None

def main():
    initial_state = get_user_input()
    solution = solve_puzzle(initial_state)
    if solution:
        print("Solution found in", len(solution), "steps:")
        current_state = initial_state
        for move in solution:
            current_state = move_blank(current_state, move)
            print_puzzle(current_state)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
    
    
    
# Let's illustrate the N-Puzzle solver with a simple example:

# Suppose we have the following initial puzzle state:
# ```
# 1 2 3
# 4 5 0
# 7 8 6
# ```

# We want to move the '0' (blank space) to the right. So, we call the `move_blank` function with the direction "right". The function finds the blank space at position (1, 2) and checks if moving right is valid. Since the blank space can move right, it swaps the positions of '0' and '5'. The new state becomes:
# ```
# 1 2 3
# 4 0 5
# 7 8 6
# ```

# Now, let's explain the example functions briefly:

# 1. **User Input Function (`get_user_input`):**
#    - The user inputs the initial state of the puzzle:
#      ```
#      Enter the initial state of the puzzle (3x3 grid):
#      1 2 3
#      4 5 0
#      7 8 6
#      ```

# 2. **Find Blank Function (`find_blank`):**
#    - It locates the position of the blank space (0). In our example, it's at position (1, 2).

# 3. **Move Blank Function (`move_blank`):**
#    - It moves the blank space according to the specified direction.
#    - For example, moving the blank space right in our example swaps '0' with '5', resulting in a new puzzle state.

# 4. **Print Puzzle Function (`print_puzzle`):**
#    - It prints the puzzle state in a readable format.
#    - After moving the blank space right, it would print the updated puzzle state.

# 5. **Is Goal Function (`is_goal`):**
#    - It checks if the current puzzle state matches the goal state (all numbers in ascending order).
#    - If the current state matches the goal, it means the puzzle is solved.

# 6. **Solve Puzzle Function (`solve_puzzle`):**
#    - It attempts to solve the puzzle using a breadth-first search algorithm.
#    - It explores possible moves from the initial state until it reaches the goal state or exhausts all possibilities.

# 7. **Main Function (`main`):**
#    - It orchestrates the entire puzzle-solving process:
#      - It gets the initial state from the user.
#      - Calls the `solve_puzzle` function to find the solution steps.
#      - Prints the solution steps if a solution is found.

