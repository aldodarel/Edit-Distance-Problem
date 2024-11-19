import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Codes', 'visual')))

# Import the backtracking edit distance function
from Algoritma import editDistanceBacktracking

def test_edit_distance_backtracking():
    # Accept user input for two strings
    str_A = input("Enter the first string: ")
    str_B = input("Enter the second string: ")

    # Testing edit_distance_backtracking
    print("\nTesting Greedy - Backtracking approach:")
    start_time = time.time()
    edit_distance = editDistanceBacktracking(str_A, str_B)
    end_time = time.time()
    
    # Display results
    print("Edit Distance:", edit_distance)
    print("Execution Time:", end_time - start_time, "seconds")

    # Display steps
    print("\nStep-by-step counting:")
    
    alignment_steps = []
    
    # Modify step_by_step_trace to capture all steps
    def step_by_step_trace(a, b, i=0, j=0, steps=[]):
        if i == len(a): 
            while j < len(b):
                steps.append(f"Insert '{b[j]}' at position {i} in A")
                j += 1
            return len(b) - j
        if j == len(b): 
            while i < len(a):
                steps.append(f"Delete '{a[i]}' from position {i} in A")
                i += 1
            return len(a) - i
        if a[i] == b[j]: 
            steps.append(f"Characters match at A[{i}] and B[{j}]: '{a[i]}' - No edit needed")
            return step_by_step_trace(a, b, i + 1, j + 1, steps)

        # Recursive operations with choices for insert, delete, and replace
        insert_steps = steps.copy()
        delete_steps = steps.copy()
        replace_steps = steps.copy()

        insert_steps.append(f"Insert '{b[j]}' at position {i} in A")
        delete_steps.append(f"Delete '{a[i]}' from position {i} in A")
        replace_steps.append(f"Replace '{a[i]}' with '{b[j]}' at position {i} in A")

        # Compute each operation recursively
        insert_op = 1 + step_by_step_trace(a, b, i, j + 1, insert_steps)
        delete_op = 1 + step_by_step_trace(a, b, i + 1, j, delete_steps)
        replace_op = 1 + step_by_step_trace(a, b, i + 1, j + 1, replace_steps)

        # Choose the operation with the minimum edit distance
        min_op = min(insert_op, delete_op, replace_op)

        # Update steps based on the chosen operation
        if min_op == insert_op:
            steps.extend(insert_steps[len(steps):])
        elif min_op == delete_op:
            steps.extend(delete_steps[len(steps):])
        else:
            steps.extend(replace_steps[len(steps):])

        return min_op

    # Start the recursive tracing
    step_by_step_trace(str_A, str_B, steps=alignment_steps)
    
    # Display each step
    for step in alignment_steps:
        print(step)

# Run the test function
test_edit_distance_backtracking()
