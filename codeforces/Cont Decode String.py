alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(int(input())):
    n = int(input())
    code = input()
    ans = ""
    while(len(code)):
        if code[len(code)-1]=="0":
            temp = code[len(code)-3]+code[len(code)-2]
            ans =  alphabet[int(temp)-1] +ans
            code = code[:-3]
        else:
            ans =  alphabet[int(code[len(code)-1])-1] + ans
            code = code[:-1]
    print(ans)