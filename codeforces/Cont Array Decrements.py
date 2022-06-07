num1 = int(input())
for i in range(num1):
    k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dif = max(a)-max(b)
    if dif<0:
        print("NO")
    else:
        count=0
        for i in range(k):
            if b[i]==0 and a[i]<dif:
                count+=1
            elif a[i]-b[i]==dif:
                count+=1
            else:
                break
        if(count==k):
            print("YES")
        else:
            print("NO")
