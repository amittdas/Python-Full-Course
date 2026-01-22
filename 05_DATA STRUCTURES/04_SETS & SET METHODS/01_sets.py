s = {2, 23, 45, 71, 8}

print(s)
print(type(s))

# We cannot access each index or elements of sets because sets sre not in ordered collection. It is like a basket. Each element can have onlt one occurance   s[0], s[1] is not allowed in sets

s.add(32)
print(s)

s.remove(2)
print(s)

s.discard(3456)   # Remove it only if it is present in the set
print(s)

s.pop()   # Removes a random element in the set
print(s)