for i in range(int(input())):
    zero, one = map(int, input().split())
    output = ""
    while(zero>0 and one>0):
        output+="01"
        zero-=1
        one-=1
    while(zero>0):
        output+="0"
        zero-=1
    while(one>0):
        output+="1"
        one-=1
    print(output)