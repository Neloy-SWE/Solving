num1 = int(input())
list1 = []
count = 0
for i in range(num1):
    list1.append(input())
    if list1[i]=="Tetrahedron":
        count+=4
    elif list1[i]=="Cube":
        count+=6
    elif list1[i]=="Octahedron":
        count+=8
    elif list1[i]=="Dodecahedron":
        count+=12
    elif list1[i]=="Icosahedron":
        count+=20
print(count)
    
        
    
