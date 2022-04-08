num1=int(input())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

set1 = set(list1[1:]+list2[1:])

# if len(set1)==1 and 0 in set1:
#     print("Oh, my keyboard!")

if len(set1)<num1:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")
