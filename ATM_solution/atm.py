
def withdraw(balance,req):
    if req>balance:
        print "Can't give you all this money !!"
    elif req<=0:
        print("More than zero plz!")
    
    if balance >=req:
        balance =balance - req
        while req > 0:
            if req >= 100:
                print "give 100"
                req = req - 100
            elif req >= 50:
                print "give 50"
                req = req - 50
            elif req >= 10:
                print "give 10"
                req = req - 10
            elif req >= 5:
                print "give 5"
                req = req - 5
            elif req >= 2:
                print "give 2"
                req = req - 2
            elif req >=1:
                print "give 1"
                req=req-1
    
    return balance - req
    
balance=500
print "current balance : "+str(balance)
balance=withdraw(balance, 277)
print "current balance: "+str(balance)
balance=withdraw(balance, 165)
print "current balance: "+str(balance)
balance=withdraw(balance, 30)
print "current balance: "+str(balance)
balance=withdraw(balance, 133)
print "current balance: "+str(balance)

