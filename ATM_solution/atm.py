class ATM:
    def withdraw(self,req):
        print "Welcome to "+self.bank_name
        print "current balance : "+str(self.balance)
        
        if req>self.balance:
            print "Can't give you all this money !!"
        
        if self.balance >=req:
            self.balance=self.balance-req
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
        
        return self.balance
    def __init__(self,bank_name,balance):
        self.bank_name=bank_name
        self.balance=balance

balance1 = 500
balance2 = 1000


atm1=ATM("Baraka bank",balance1)
atm2=ATM("Islamic bank",balance2)        


atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
