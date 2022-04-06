a, b = map(int, input().split())
serial = input()
list1 = list(serial)
while(b>0):
    n=0
    while n<len(serial)-1:
        if list1[n]=="B" and list1[n+1]=="G":
            list1[n]="G"
            list1[n+1]="B"
            n+=1
        n+=1
    b-=1
serial = "".join(list1)
print(serial)
