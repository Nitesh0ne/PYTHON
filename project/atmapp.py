p = "1234"
balance = 10000 
i = 0 
while (i !=3 ):
    pin = input("Enter a pin : ")
    if pin != p :
        print("Pin doesn't match ")
    else : 
        withDrawAmt = int(input("Enter a amount: "))
        if withDrawAmt <= balance :
            print("Amount withdraw successfull")
            balance = balance - withDrawAmt 
            print("Balance :",balance)
        else: 
            print("Not Enough Balance ")
        break 
    i = i +1 
else :
    print("Card Blocked")