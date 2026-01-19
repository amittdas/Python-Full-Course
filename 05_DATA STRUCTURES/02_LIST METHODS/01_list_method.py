marks = [5, 2, 21, 5, 7]
extra_marks = [23, 45, 35, 78]
print(marks)

marks.append(63)             # Add element at the last index
print(marks)

marks.pop()                  # removes element from the last index
print(marks)

marks.extend(extra_marks)    # Add another list to a list
print(marks)

marks.remove(21)             # Removes element "21" from the list
print(marks)

marks.insert(2, 1000)        # Inserts 1000 at index 2
print(marks)

marks.sort()                 # Sorts the entire list
print(marks)

marks.reverse()              # Reverse the entire list
print(marks)