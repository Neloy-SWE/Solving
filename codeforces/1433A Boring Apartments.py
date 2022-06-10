num1 = int(input())
for i in range(num1):
    k = input()
    print(((int(k[0])-1)*10)+((len(k)*(len(k)+1))//2))