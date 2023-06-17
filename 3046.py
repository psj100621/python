x = input()
y = x.split()
[a, b] = y
A = int(a)
B = int(b)

def find_R2(X,Y):
    return (Y*2)-X

C = find_R2(A,B)
print(C)



