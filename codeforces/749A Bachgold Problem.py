num1 = int(input())
print(num1//2)
if num1%2==0:
    for i in range(num1//2):
        print(2, end=" ")
else:
    for i in range((num1//2)-1):
        print(2, end=" ")
    print(3)