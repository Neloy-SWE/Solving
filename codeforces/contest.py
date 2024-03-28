# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))


# A
# for i in range(int(input())):
#     a, b, c = map(int, input().split())

#     if a<b and b<c:
#         print("STAIR")
#     elif a<b and b>c:
#         print("PEAK")
#     else:
#         print("NONE")

#
        
# for i in range(int(input())):
#     n = int(input())
#     for j in range(n):
#         for k in range(n):
#             if (j+1)%2==1:
#                 if (k+1)%2==0:
#                     print("..", end="")
#                 else:
#                     print("##", end="")
#             else:
#                 if (k+1)%2==0:
#                     print("##", end="")
#                 else:
#                     print("..", end="")
#         print()

# B
# def output(n):
#     for i in range(2 * n):
#         row = ''
#         for j in range(2 * n):
#             if (i // 2 + j // 2) % 2 == 0:
#                 row += '#'
#             else:
#                 row += '.'
#         print(row)

# for i in range(int(input())):
#     n = int(input())
#     output(n)

# C
# for i in range(int(input())):
#     s = input()
#     n = int(s[:2])
#     if (n==0):
#         print("12"+s[2:]+" AM")
#     elif n==12:
#         print(s+" PM")
#     elif n>12:
#         a=n-12
#         if len(str(a))==1:
#             b="0"+str(a)
#         else:
#             b=str(a)
#         print(b+s[2:]+" PM")
#     else:
#         print(s+" AM")

# D
# for j in range(int(input())):
#     s = input()
#     a= True
#     for i in range(len(s)):
#         if int(s[i])>2:
#             if int(s[i])/2==int(s[i-1]):
#                 a = False
#                 break
#             else:
#                 continue
#     if(a):
#         print("YES")
#     else:
#         print("NO")

# def is_binary_decimal(num):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             factor = i
#             quotient = num // i
#             if all(digit in {'0', '1'} for digit in str(factor)) and all(digit in {'0', '1'} for digit in str(quotient)):
#                 return True
#     return False

# # Input number of test cases
# for _ in range(int(input())):
#     s = int(input())
#     if is_binary_decimal(s):
#         print("YES")
#     else:
#         print("NO")
def is_binary_decimal(num):
    if num == 1:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factor = i
            quotient = num // i
            if all(digit in {'0', '1'} for digit in str(factor)) and all(digit in {'0', '1'} for digit in str(quotient)):
                return True
    return False

# Input number of test cases
for _ in range(int(input())):
    s = int(input())
    if is_binary_decimal(s):
        print("YES")
    else:
        print("NO")




