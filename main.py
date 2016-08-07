import time

def init ():
    print "\t WEIGHT TRACKER"
    print "Options: "
    print "1. Enter weight"
    print "2. Exit"
    # open data file or create one
    global fo
    fo = open("data", "ab")
    return

def enterWeight ():
    # get weight from user
    weight = raw_input("Enter your current weight (lb): ")
    # save to file
    fo.write (str(time.time()) + "\t" + str(weight) + "\n")
    return

# ---main---
init ()

while True:
    choice = raw_input("Select Option: ")
    if (choice == '1'):
        enterWeight()
    elif (choice == '2'):
        fo.close()
        break
    else:
        print "Invalid choice!"
