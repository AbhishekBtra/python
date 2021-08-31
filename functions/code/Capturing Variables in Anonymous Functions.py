x = 10
a = lambda y: x+y
x = 20
b = lambda y: x+y
print(a(10)) # 30
print(b(10)) # 30

x=10
a= lambda y,x=x: x+y

x=20
b= lambda y,x=x: x+y

print(a(10)) # 20
print(b(10)) # 30