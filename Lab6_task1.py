L = [0,1]

while L[-1] < 1000:
    A = L[-1]
    B = L[-2]
    L.append(A+B)

L.pop()
print(L)