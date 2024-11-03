n=int(input("Введите количество магазинов: "))
p_15=[]
p_20=[]
p_25=[]
print("Введите цену для 15%: ")
for i in range(n):
    p_15.append(int(input()))
print("Введите цену для 20%: ")
for i in range(n):
    p_20.append(int(input()))
print("Введите цену для 25%: ")
for i in range(n):
    p_25.append(int(input()))
p_15f=[x for x in p_15 if x!=0]
if not p_15f:
    count15=0
else:
    count15 = p_15f.count(min(p_15f))
p_20f=[x for x in p_20 if x!=0]
if not p_20f:
    count20=0
else:
    count20 = p_20f.count(min(p_20f))
p_25f=[x for x in p_25 if x!=0]
if not p_25f:
    count25=0
else:
    count25 = p_25f.count(min(p_25f))
print("Количество магазинов с минимальная стоимостью для 15%: ",count15,"\nКоличество магазинов с минимальная стоимостью для 20%: ",count20,"\nКоличество магазинов с минимальная стоимостью для 25%: ",count25)