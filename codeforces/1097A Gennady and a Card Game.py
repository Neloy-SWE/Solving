card = input()
cards = list(map(str, input().split()))
ok = False
for i in cards:
    if card[0] == i[0] or card[1]== i[1]:
        print("YES")
        ok = False
        break
    else:
        ok = True
if ok:
    print("NO")