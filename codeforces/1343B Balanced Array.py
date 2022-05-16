num1 = int(input())
for i in range(num1):
    num2 = int(input())
    if num2<4 or (num2//2)%2!=0:
        print("NO")
    else:
        a = 0
        b = 0
        c = 0
        for j in range(2, num2+1, 2):
            a+=j
            b+=(j-1)
        if(b>a):
                print("NO")
        else:
            print("YES")
            for j in range(2, num2+1, 2):
                print(j, end=" ")
            for j in range(2, num2+1, 2):
                if(j<num2):
                    c+=j-1
                    print(j-1, end=" ")
                else:
                    print(a-c, end=" ")
