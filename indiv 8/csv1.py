import csv
with open("8 - 1.csv", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter = ",")
    count = 0
    k1=0
    k2=0
    pedogog=0
    pshyco=0
    inptdate=input("Введите дату: ")
    parse_info = []
    for row in file_reader:
        if count == 0:
            print()
        else:
            date=row[7][:2].strip()
            if(date=="-" or date==""):
                date=99
            if(int(inptdate)>int(date)):
                pedogog +=float(row[13].replace(",","."))
                pedogog +=float(row[14].replace(",","."))
                k1 +=1

                pshyco += float(row[15].replace(",", "."))
                pshyco += float(row[16].replace(",", "."))
                k2 += 1
        count += 1
    if(k1==0):
        otvet1=0
    else:
        otvet1=pedogog/k1

    if (k2 == 0):
        otvet2 = 0
    else:
        otvet2 = pedogog / k1
    print("Ср. ареф Педагогика = ", otvet1,"\nСр. ареф Психология = ", otvet2)
