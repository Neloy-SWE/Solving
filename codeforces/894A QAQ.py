n = input()
count =0
for i in range(len(n)):
    for j in range(i+1, len(n)):
        for k in range(j+1, len(n)):
            if n[i]=="Q" and n[j] =="A" and n[k] =="Q":
                count+=1
print(count)