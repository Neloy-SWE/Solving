alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
count = 0
s = input()
start = 0
for i in range(len(s)):
    if (abs(alphabet.index(s[i])-start) < 14):
        count += abs(alphabet.index(s[i])-start)
    else:
        minValue = min(start, alphabet.index(s[i]))
        maxValue = max(start, alphabet.index(s[i]))
        count += minValue+(26-maxValue)
    start = alphabet.index(s[i])
print(count)