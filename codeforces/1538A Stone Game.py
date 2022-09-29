def minValue(a):
    value = a[0]
    for i in range(len(a)):
        if a[i] < value:
            value = a[i]
    return value


def maxValue(a):
    value = a[0]
    for i in range(len(a)):
        if a[i] > value:
            value = a[i]
    return value


def findIndex(value, inputList):
    for i in range(len(inputList)):
        if inputList[i] == value:
            return i


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    getMinValue = minValue(a)
    getMaxValue = maxValue(a)
    if n%2==0:
        midValue = n/2
    else:
        midValue = int(n/2)+1
    minValueIndex = findIndex(inputList=a, value=getMinValue)
    maxValueIndex = findIndex(inputList=a, value=getMaxValue)

    ans1 = maxValue([minValueIndex, maxValueIndex])+1
    ans2 = n-minValue([maxValueIndex, minValueIndex])
    ans3 = (minValue([maxValueIndex, minValueIndex])+1)+(n-maxValue([maxValueIndex, minValueIndex]))

    print(minValue([ans1, ans2, ans3]))