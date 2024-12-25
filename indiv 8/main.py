from lxml import etree

tree1 = etree.parse('8.osm')
root1 = tree1.getroot()
tree2 = etree.parse('8.2.osm')
root2 = tree2.getroot()
#motel hotel hostel
namelist=[]
typelist=[]
i=0
for element in root1.findall('node'):
    if element.xpath('tag[@k="tourism"]'):
        if element.xpath('tag[@v="hotel"] or tag[@v="guest_house"] or tag[@v="apartment"]'):
            name=str(element.xpath('tag[@k="name"]/attribute::v'))[2:-2]
            if(name == ""):
                name=f"No Data({i})"
                i+=1
            hotelType=str(element.xpath('tag[@k="tourism"]/attribute::v'))[2:-2]
            namelist.append(name)
            typelist.append(hotelType)

for element in root2.findall('node'):
    if element.xpath('tag[@k="tourism"]'):
        if element.xpath('tag[@v="hotel"] or tag[@v="motel"] or tag[@v="hostel"]'):
            name=str(element.xpath('tag[@k="name"]/attribute::v'))[2:-2]
            if(name == ""):
                name=f"No Data({i})"
                i+=1
            hotelType=str(element.xpath('tag[@k="tourism"]/attribute::v'))[2:-2]
            namelist.append(name)
            typelist.append(hotelType)
hotels_set=dict(zip(namelist,typelist))
sorted_hotels=dict(sorted(hotels_set.items()))
for key,val in sorted_hotels.items():
    print(key,': ',val)
print("\nКоличество отелей: ",len(sorted_hotels))