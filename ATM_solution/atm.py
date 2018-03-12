def atm(mony,req):
    if mony >=req:
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
    else:
        print "not avalable "
    if req <0:
        print "try positive value"

atm(500,-154)


