x = input()
d = input()
y = x.split()
[a, b, c] = y
A = int(a)
B = int(b)
C = int(c)
D = int(d)

def remainder(x,y):
    return x%y

def quotient(x,y):
    return x//y
Sec = C + D
A3 = remainder(Sec,60)
E = quotient(Sec,60)

Min = B + E
A2 = remainder(Min,60)
F = quotient(Min,60)

Hrs = A + F
A1 = remainder(Hrs,24)

print(A1, A2, A3)