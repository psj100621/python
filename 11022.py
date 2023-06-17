x = input()
T = int(x)

for i in range(T):
    y = input()
    z = y.split()
    [a, b] = z
    A = int(a)
    B = int(b)
    print("Case #"+str(i+1)+":",A,"+",B,"=",A+B)