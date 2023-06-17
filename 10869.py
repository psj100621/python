x = input()
y = x.split()
[a , b] = y

A = int(a)
B = int(b)

def sum(x,y):
    return (x+y)

def minus(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(X,Y):
    return X//Y

def remainder(X,Y):
    return X%Y

C = sum(A,B)
D = minus(A,B)
E = multiply(A,B)
F = division(A,B)
G = remainder(A,B)
print(C)
print(D)
print(E)
print(F)
print(G)