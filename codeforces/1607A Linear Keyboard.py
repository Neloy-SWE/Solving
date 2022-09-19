def getIndex(myList, value):
    for i in range(len(myList)):
        if value == myList[i]:
          return i

def absoluteValue(a):
    if a>= 0:
        return a
    else:
        return a*(-1)

def makeList(s):
    myList = []
    for i in s:
        myList.append(i)
    return myList


for i in range(int(input())):
    alphabet = makeList(input())
    s = input()
    if(len(set(s))==1):
        print(0)
    else:
        count=0
        for i in range(1, len(s)):
            pre = getIndex(myList=alphabet, value=s[i-1])
            post = getIndex(myList=alphabet, value=s[i])
            count+= absoluteValue(post-pre)
        
        print(count)