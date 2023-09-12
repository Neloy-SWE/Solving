# s = input()
# if (s[0]==")" or s[0]=="}" or s[0]=="]"):
#     print("false if")
# else:
#     ans = ""
#     for i in s:
#         if (i=="(" or i=="{" or i=="["):
#             ans+=i
#         elif (ans[len(ans)-1]=="(" and i==")" or ans[len(ans)-1]=="{" and i=="}" or ans[len(ans)-1]=="[" and i=="]"):
#             ans=ans[:-1]
#         else:
#             print("fasle else")
#     if not ans:
#         print("True last")
#     else:
#         print("False last")


def isValid( s: str) -> bool:
    ans = ""
    for i in s:
        if not ans:
            if (i==")" or i=="}" or i=="]"):
                return False
        if (i=="(" or i=="{" or i=="["):
            ans+=i
        elif (ans[len(ans)-1]=="(" and i==")" or ans[len(ans)-1]=="{" and i=="}" or ans[len(ans)-1]=="[" and i=="]"):
            ans=ans[:-1]
        else:
            return False
    if not ans:
        return True
    else:
        return False

print(isValid(s=input()))