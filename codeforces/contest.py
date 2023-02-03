# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))


for i in range(int(input())):
    a = int(input())
    s = list(input())
    ans=0
    for j in range(a):
        count=0
        flag = False
        for k in range(1+j,a):
            if s[k]==s[j] and s[k]!="0":
                s[k]="0"
                flag = False
                count+=1
            else:
                flag = True
        print("Hello",count)
        if flag:
            ans+=1
        elif count==1:
            print("ifok")
            ans+=1
        elif count>1:
            print("else ok")
            ans+=2
    print("Ans",ans)
