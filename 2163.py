x = input()
y = x.split()
[a , b] = y

A = int(a)
B = int(b)

def cut(X,Y):
    return (X*Y)-1

C = cut(A,B)
print(C)