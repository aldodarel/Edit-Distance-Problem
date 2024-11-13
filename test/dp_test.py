import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Codes', 'visual')))

from Algoritma import edit_distance, edit_distance_wotr


import numpy as np
import time

def test_edit_distance():
    # Accept user input for two strings
    str_A = input("Enter the first string: ")
    str_B = input("Enter the second string: ")
    
    # Convert strings to numpy arrays
    A = np.array(list(str_A), dtype='|S1')
    B = np.array(list(str_B), dtype='|S1')
    
    # Testing edit_distance (with traceback matrix)
    print("\nTesting edit_distance (with traceback matrix):")
    start_time = time.time()
    ED_matrix, ptr_matrix, ed, A_aligned, B_aligned = edit_distance(A, B)
    end_time = time.time()
    
    # Display results
    print("Edit Distance:", ed)
    print("Execution Time:", end_time - start_time, "seconds")
    print("Edit Distance Matrix:\n", ED_matrix)
    print("Aligned Sequences:")
    print("A:", "".join([char.decode("utf-8") if isinstance(char, np.bytes_) else char for char in A_aligned]))
    print("B:", "".join([char.decode("utf-8") if isinstance(char, np.bytes_) else char for char in B_aligned]))
    
    # Testing edit_distance_wotr (without traceback matrix)
    print("\nTesting edit_distance_wotr (without traceback matrix):")
    start_time = time.time()
    ED_matrix_wotr, ed_wotr, trace_steps, A_aligned_wotr, B_aligned_wotr = edit_distance_wotr(str_A, str_B)
    end_time = time.time()
    
    # Display results
    print("Edit Distance:", ed_wotr)
    print("Execution Time:", end_time - start_time, "seconds")
    print("Edit Distance Matrix:\n", ED_matrix_wotr)
    print("Alignment Steps:")
    for step in trace_steps:
        print(step)
    print("Aligned Sequences:")
    print("A:", "".join([char.decode("utf-8") if isinstance(char, np.bytes_) else char for char in A_aligned]))
    print("B:", "".join([char.decode("utf-8") if isinstance(char, np.bytes_) else char for char in B_aligned]))

# Run the test function
test_edit_distance()

