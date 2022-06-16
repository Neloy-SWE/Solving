for i in range(int(input())):
        w,h,n = map(int, input().split())
        c = 1
        for i in range(n):
            if w%2!=0 and h%2!=0:
                c=c
                break
            elif w%2==0 and w>1:
                c*=2
                w=w//2
            elif h%2==0 and h>1:
                c*=2
                h=h//2
        if c>=n:
            print("YES")
        else:
            print("NO")