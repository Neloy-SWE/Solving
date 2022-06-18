for i in range(int(input())):
    h, m = map(int, input().split())
    lastH = ((23-h)*60)+(60-m)
    print(lastH)