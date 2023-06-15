x = input()
y = x.split()
[a, b, c] = y
A = int(a)
B = int(b)
C = int(c)

def euclid():
    if A < B+C:
        return True
    elif B < A+C:
        return True
    elif C < A+B:
        return True
    else:
        return False

D = euclid(A, B, C)
