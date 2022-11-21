alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(int(input())):
    n = input()
    s = sorted(input())
    print(alphabet.index(s[len(s)-1])+1)