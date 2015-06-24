a=1
b=1
print(a)
print(b)
for i in range(100):
    (a,b)=(b,a+b)
    print(b)
