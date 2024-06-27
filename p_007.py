a = True
print(type(a))
if "왕감자":
    print("왕감자란말이야")
else: 
    print("왕감자가 아니란 말이야")

print(bool(0))
print(bool('0'))

a = [1,2,3]
b= a
print(id(a))
print(id(b))
b = a[:]
print(id(a))
print(id(b))

a = 5
b = 3
print(a, b)
a,b = b,a
print(a,b)