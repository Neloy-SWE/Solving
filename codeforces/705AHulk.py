num1 = int(input())

if(num1==1):
    print("I hate it")
elif(num1>1): 
    for i in range(1, num1+1):
        if i<num1 and i%2==0:
            print("I love", end=" that ")
        elif i<num1 and i%2!=0:
            print("I hate", end=" that ")
        elif i==num1 and i%2==0:
            print("I love it")
        elif i==num1 and i%2!=0:
            print("I hate it")