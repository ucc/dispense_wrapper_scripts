#!/usr/bin/env python 
import subprocess as sp



while True:
    username=None
    while(not(username)):
        username = raw_input("Username: ")
        try:
            sp.check_call(["dispense","acct", username])
            #sp.check_call(["id", username])
            sp.check_call(["finger", username])

        except sp.CalledProcessError:
            username = None 
            continue #Restart the loop

    amount=None
    int_amount = None
    while(not amount):
        try:
            int_amount = int(raw_input("Amount (in cents): "))
            amount = "+"+str(int_amount)
        except ValueError:
            print "Please enter a number."
            amount = None
            continue
    print "Adding: $%2.2f" % (int_amount/100.0)

    reason = raw_input('Reason/Bag Number (Enter just a digit, to say "money in safe. Bag number <input>"): ')
    if reason.isdigit():
        reason = "Money in safe. Bag number " + reason
    elif len(reason)==0:
        reason = "Money in safe."
    


    cmd =" ".join(['dispense acct ',username, amount,' "' + reason+'"'])
    print "Will call: " + cmd 

    confirm = raw_input("Correct (Y/N): ").lower()
    if confirm and confirm[0]=='n':
        #Restart
        continue
    else:
        break
   
  
#subprocess call hastes me for not useing speratre args
sp.call(["dispense", "acct", username, amount, reason])

print "Thankyou please remember to do what ever crazy plan the treasurer wants done with the safe today."
    



