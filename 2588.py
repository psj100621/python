x = input()
y = input()

A = int(x)
B = int(y)

def division(X,Y):
    return X//Y

def remainder(X,Y):
    return X%Y

C = remainder(B,10)
D = division(B-C,10)
E = remainder(D,10)
F = division(B,100)
print(C*A)
print(E*A)
print(F*A)
print(A*B)