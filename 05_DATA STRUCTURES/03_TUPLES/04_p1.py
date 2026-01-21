# Create a tuple coordinates = (10, 20) and print both elements.

tu = (10, 20)

print(tu[0])
print(tu[1])

# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

li = list(tu)
print(li)
li[0] = 50
print(li)

tup = tuple(li)
print(tup)