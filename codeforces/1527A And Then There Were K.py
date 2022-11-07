for i in range(int(input())):
    n = int(input())
    count = 1
    while(True):
        if(count*2>n):
            break
        count*=2
    print(count-1)