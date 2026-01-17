def sum(a,b):
    print("hello world")
    c = a + b
    global z
    z = 0     # Now Z will be refered as global variable
    return c

z = 3
print(sum(2,3))
print(z)   # 0