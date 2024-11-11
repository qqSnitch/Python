n= int(input("Введите N: "))
tree_name=[]
tree_child=[]
for i in range(n):
    tree_name.append(input())
print (tree_name)
tree_child=tree_name.copy()
tree_child.remove(tree_child[0])
tree_child.append("No")
print(tree_child)
tree_info=dict(zip(tree_name,tree_child))
i=0
for str in tree_info.keys():
    i+=1
    print(str,": ", len(tree_info)-i)

