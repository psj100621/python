A = input()
B = input()
a = int(A)
b = int(B)

def is_prime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

L = []
for i in range(a,b+1):
    c = is_prime(i)
    if c == True:
        L.append(i)

if len(L) == 0:
    print("-1")
else:
    print(sum(L))
    print(L[0])
