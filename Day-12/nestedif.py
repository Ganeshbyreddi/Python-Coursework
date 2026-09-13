sales = int(input())
if sales > 1000 :
    print("best seller")
    
    eli_acc = eval(input("Eligible Account:"))
    ver_sub = eval(input("Meta Verified Subscription:"))
    if eli_acc and ver_sub:
        print("Verified Badge Granted")

    status = eval(input())
    if status:
        print("Extra Rain Charges Applied")
    reg = eval(input("registered.; "))

    if reg:
       fee = eval(input("entry fee : "))
       if fee:
          print("Tournament Entry Confirmed")   
       else:
          print("Entry Fee Pending")
    else:
        print("Invalid File Link")
        