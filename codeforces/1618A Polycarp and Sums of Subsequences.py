for i in range(int(input())):
    a=list(map(int, input().split()))
    minValue = a[0]
    secondValue = a[len(a)-3]-minValue
    thirdValue = a[len(a)-1]-minValue-secondValue
    print(minValue, secondValue, thirdValue)
