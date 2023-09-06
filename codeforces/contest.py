# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))


def isOdd(num):
    if (num%2==0):
        return True
    else:
        return False

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if (n==1):
        print("YES")
    else:
        minValue = min(a)
        isMinOdd = isOdd(minValue)
        isFstValue = isOdd(a[0])
        if (isMinOdd==isFstValue):
            print("YES")
        else:
            print("NO")

