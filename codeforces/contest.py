# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))


# for i in range(int(input())):
#     n = int(input())
#     s1 = list(map(str, input().split()))
#     s2 = list(map(str, input().split()))
#     s3 = list(map(str, input().split()))
#     p1 = 0
#     p2 = 0
#     p3 = 0
#     for j in range(n):
#         if s1[j] in s2 and s1[j] in s3:
#             p1+=0
#         elif s1[j] in s2 or s1[j] in s3:
#             p1+=1
#         elif s1[j] not in s2 or s1[j] not in s3:
#             p1+=3
#         if s2[j] in s1 and s2[j] in s3:
#             p2+=0
#         elif s2[j] in s1 or s2[j] in s3:
#             p2+=1
#         elif s2[j] not in s1 or s2[j] not in s3:
#             p2+=3
#         if s3[j] in s1 and s3[j] in s2:
#             p3+=0
#         elif s3[j] in s1 or s3[j] in s2:
#             p3+=1
#         elif s3[j] not in s1 or s3[j] not in s2:
#             p3+=3
#     print(p1, p2, p3)


# for i in range(int(input())):
#     n = int(input())
#     count = (n&(n-1))
#     if (count==0):
#         print(n-1)
#     else:
#         for j in range(2,n):
#             count = count&(n-j)
#             if (count==0):
#                 print(n-j)
#                 break


for i in range(int(input())):
    n = int(input())
    for j in range(1,n+1):
        print(j,end=" ")
    print()