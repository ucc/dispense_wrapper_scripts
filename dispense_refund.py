#!/usr/bin/env python 
import subprocess as sp

sp.call(['tail', '-n3', "/home/other/coke/cokelog"])

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

item_id=None
while(not(item_id)):
    item_id = raw_input("item_id (Usually of the form <item>:<slot> eg coke:6 or snack:33): ")

amount=None
while(True):
    raw_amount = raw_input("Amount (in cents): (Leave blank for default): ")
    if len(raw_amount)==0:
        amount=""
        print "Refunding at default value"
        break
    else:
        try:
            int_amount = int(raw_amount)  #Throw the exception
            amount = str(int_amount)
        except ValueError:
            print "Please enter a number."
            continue
        print "Refunding: $%2.2f" % (int_amount/100.0)
        break

cmd =" ".join(['dispense refund ',username, item_id, amount ])
print "Will call: " + cmd

command_args = ["dispense","refund", username, item_id]
if amount:
    command_args.add(amount)

sp.check_call(command_args)
print("Done. Please Don't Make Mistakes Again.")




