# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))

def reverse(string):
    string = string[::-1]
    return string


for i in range(int(input())):
    n = int(input())
    s = input()
    number = int(s)
    lenS = len(s)
    initial = "1"+"0"*(lenS-1)
    last = "9"*(lenS)
    initValue = int(initial)
    latValue = int(last)
    # print(reverse(s))
    for i in range(initValue, latValue+1):
        checkNum = number+i
        checkAns = str(checkNum)
        if checkAns == reverse(checkAns):
            print(i)
            break

