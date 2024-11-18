f=open("Input.txt")
x=int(f.read())
allx=[]
for i in range(0,len(str(x))):
    allx.append(i)
    for j in range(i,len(str(x))):
        allx.append(int(str(x)[i]+str(x)[j]))
tmp=0
while tmp in allx:
    tmp+=1
print(tmp)
f.close()