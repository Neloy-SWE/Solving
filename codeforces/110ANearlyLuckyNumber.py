lucky = input()

count =0

for i in range(0,len(lucky)):
    if lucky[i] == "4" or lucky[i]=="7":
        count+=1
if count==4 or count==7:
    print("YES")
else:
    print("NO")