num1 = int(input())
count = 0
for i in range(num1):
    str1=input()
    if str1=="Tetrahedron":
        count+=4
    elif str1=="Cube":
        count+=6
    elif str1=="Octahedron":
        count+=8
    elif str1=="Dodecahedron":
        count+=12
    elif str1=="Icosahedron":
        count+=20
print(count)
    
        
    
