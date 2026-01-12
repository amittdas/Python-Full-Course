# Write a program that counts how many vowels are in a given string.

str = "I love python and it is awesome"

sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for ch in str.lower():
    print(ch)
    if(ch in vowels):
        sum+=1
        
print(f"There are {sum} vowels in this sentence.")