for i in range(int(input())):
    ticketNo = input()
    if(int(ticketNo[0])+int(ticketNo[1])+int(ticketNo[2])==int(ticketNo[3])+int(ticketNo[4])+int(ticketNo[5])):
        print("YES")
    else:
        print("NO")