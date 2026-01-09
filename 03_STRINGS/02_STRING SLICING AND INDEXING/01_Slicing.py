name = "Amit0123456789"

print(name[0:2])       #  Slicing goes from 0 to n-1
print(name[1:-1])      #  [1:-1] --> [1:3]
print(name[0:10:1])    #  [0:10:n]  --> Skip n-1 character
print(name[0:10:2])    #  [0:10:2]  --> Skip 2-1=1 character
print(name[0:10:3])    #  [0:10:3]  --> Skip 3-1=2 character
print(name[3:])        #  Replace the second empty number with (Length-1)
print(name[:3])        #  Replace the first empty number with 0