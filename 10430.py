x = input()
y = x.split()
[a, b, c] = y

A = int(a)
B = int(b)
C = int(c)

def plus_divide(X,Y,Z):
    return (X+Y) % Z

def divide_plus_divide(X,Y,Z):
    return ((X % Z) + (Y % Z)) % Z

def multiply_divide(X,Y,Z):
    return (X*Y) % Z

def divide_multiply_divide(X,Y,Z):
    return ((X % Z)*(Y % Z)) % Z

D = plus_divide(A, B, C)
E = divide_plus_divide(A, B, C)
F = multiply_divide(A, B, C)
G = divide_multiply_divide(A, B, C)
print(D)
print(E)
print(F)
print(G)
