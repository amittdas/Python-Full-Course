# Create a dictionary of three friends and their phone numbers. Use:

# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

frnds = {
        "Amit" : 9876543210,
        "Raj" : "9876543211",
        "Alex" : 9876543212
    }

print(frnds)

print(frnds.keys())
print(frnds.values())

for key, value in frnds.items():
    print(key, value)