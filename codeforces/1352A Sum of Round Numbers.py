from unittest import result


num1 = int(input())
for i in range(num1):
    num2 = input()
    if (int(num2)<10):
        print(1)
        print(num2)
    else:
        if(int(num2)%(10**(len(num2)-1))==0):
           print(1)
           print(num2)
        else:
            result = []
            while(int(num2)):
                result.append(str(int(num2[0])*(10**(len(num2)-1))))
                num2=str(int(num2)%(10**(len(num2)-1)))
            print(len(result))
            print(" ".join(result))

