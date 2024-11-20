import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Codes', 'visual')))

from Algoritma import rec_ed_with_path_and_alignment

def test_recursive_edit_distance():
    # Accept user input for two strings
    str_a = input("Enter the first string: ")
    str_b = input("Enter the second string: ")

    # Measure execution time
    start_time = time.time()
    result, (aligned_a, aligned_b) = rec_ed_with_path_and_alignment(str_a, str_b)
    end_time = time.time()

    # Extract the edit distance and path
    edit_distance = result[0]
    path = result[1]

    # Display results
    print("\nTesting Recursive Edit Distance:")
    print(f"Edit Distance: {edit_distance}")
    print(f"Execution Time: {end_time - start_time} seconds")
    print("\nStep-by-step counting:")

    # Display alignment results step by step
    for i, (char_a, char_b, action) in enumerate(zip(aligned_a, aligned_b, path)):
        if action == 'g':
            print(f"Delete '{char_a}' from position {i} in A")
        elif action == 'm':
            print(f"Insert '{char_b}' at position {i} in A")
        elif action == 'd':
            if char_a != char_b:
                print(f"Replace '{char_a}' with '{char_b}' at position {i} in A")
            else:
                print(f"Characters match at A[{i}] and B[{i}]: '{char_a}' - No edit needed")

    # Display aligned strings
    print("\nAlignment Results:")
    print("A:", ''.join(aligned_a))
    print("B:", ''.join(aligned_b))

# Run the test
test_recursive_edit_distance()	