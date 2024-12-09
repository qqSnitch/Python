f=open("Input.txt")
x=f.read().split()
y=[]
z=[]
sum=[]
n=len(x)
flag = True
c = 1
while flag:
    if c == 1:
        for i in range(0, n - 1, 2):
            y.append((int(x[i]) + int(x[i + 1])))
            sum.append((int(x[i]) + int(x[i + 1])) * 0.05)
            if len(y) == 1:
                flag = False
        c=0
    elif flag == True:
        for i in range(0, n - 1, 2):
            z.append((int(y[i]) + int(y[i + 1])))
            sum.append((int(y[i]) + int(y[i + 1])) * 0.05)
            if len(z) == 1:
                flag = False
        c=1


print(y)
print(sum)
f.close()
