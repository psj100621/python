a = input("side a: ")
b = input("side b: ")
c = input("side c: ")
A = float(a)
B = float(b)
C = float(c)

def is_triangle(X,Y,Z):
    if X >= Y+Z:
        return False
    elif Y >= X+Z:
        return False
    elif Z >= X+Y:
        return False
    else:
        return True

if is_triangle(A,B,C):
    print("YES")
else:
    print("NO")