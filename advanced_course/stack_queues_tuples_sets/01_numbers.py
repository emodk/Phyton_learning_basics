from collections import deque
first_sequence = set(input().split())
second_sequence = set(input().split())
number_of_lines = int(input())
for n in range(number_of_lines):
    sequence = deque(input().split())
    command = sequence.popleft()
    sequence_number = sequence.popleft()
    sequence_as_set = set(sequence)
    if command == "Add":
        if sequence_number == "First":
            first_sequence = first_sequence.union(sequence_as_set)
        elif sequence_number == "Second":
            second_sequence = second_sequence.union(sequence_as_set)
    elif command == "Remove":
        if sequence_number == "First":
            first_sequence = first_sequence.difference(sequence_as_set)
        elif sequence_number == "Second":
            second_sequence = second_sequence.difference(sequence_as_set)
    else:
        if first_sequence > second_sequence:
            print("True")
        elif first_sequence < second_sequence:
            print("True")
        else:
            print("False")
print(", ".join(sorted(first_sequence)))
print(", ".join(sorted(second_sequence)))
