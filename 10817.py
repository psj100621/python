x = input()
y = x.split()
[a,b,c] = y
A = int(a)
B = int(b)
C = int(c)

if A >= B:
    if  A >= C:
        if B >= C:
            print(B)
        else:
            print(C)
    else:
        print(A)
else:
    if B >= C:
        if A >= C:
            print(A)
        else:
            print(C)
    else:
        print(B)

