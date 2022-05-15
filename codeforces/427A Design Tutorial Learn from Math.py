def prime(a):
    result = 0

    for i in range(2, (a//2)+1):
        if(a%i==0):
            result = 1
            break
        else:
            continue
    return result


num1 = int(input())
if num1%2==0:
    n = num1//2
    if(n%2==0):
        print(n,n)
    else:
        print(n-1,n+1)
    
else:
   a = num1-4
   b = num1-6
   c = num1-8
   d = num1-9

   if (prime(a)):
       print(4,a)
   elif(prime(b)):
        print(6,b)
   elif(prime(c)):
        print(8,c)
   elif(prime(c)):
        print(9,d)