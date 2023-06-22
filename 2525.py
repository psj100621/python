x = input()
c = input()
y = x.split()
[a, b] = y
A = int(a)
B = int(b)
C = int(c)


def find_quotient_hrs(x):
    return x//60

def find_remainder_hrs(x):
    return x % 60

def find_remainder_day(x):
    return x % 24


D = B+C
E = find_quotient_hrs(D)
F = find_remainder_hrs(D)
G = A+E
H = find_remainder_day(G)

print(H, F)
