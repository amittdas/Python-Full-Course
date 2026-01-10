s = "hello world"   # Strings are immutable

# s[0] = "R"   # We cannot do this

a = len(s)
print(a)

print(s.upper())         # HELLO WORLD
print(s.capitalize())    # Hello world
print(s.title())         # Hello World
print(s)                 # hello world

print("---------------")

s2 = " hello world "

print(s2.strip())        # "hello world"
print(s2.lstrip())       # "hello world "
print(s2.rstrip())       # " hello world"

print("---------------")

s3 = "python is fun and fun"

print(s3.find("is"))                    # 7
print(s3.replace("fun", "awesome"))     # python is awesome and awesome


text = "Apples,Bananas,Pineapples"
print(text.split(","))
print(".".join(['Apples', 'Bananas', 'Pineapples']))

text2 = "Python1234"
print(text2.isalpha())   # FALSE
print(text2.isdigit())   # FALSE
print(text2.isalnum())   # TRUE
print(text2.isspace())   # FALSE


print(ord('A'))
print(chr(67))