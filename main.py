import time
import os
import csv

def init ():
    global settings, dfo
    settings = {}
    print "\t WEIGHT TRACKER"
    # open data file or create one
    dfo = open("data", "ab")
    if (os.path.isfile('./settings.csv')):
        settings = loadSettings ()
    else:
        createSettings ()
    outputOptions ()
    return

def createSettings ():
    while True: 
        standard_choice_w = raw_input("Enter which standard you would like to use for weight: \n 1. Pounds (lb) \n 2. Kilograms (kg) \n Choice: ")
        if (standard_choice_w == '1'):
            standard_w = 'lb'
            break
        elif (standard_choice_w == '2'):
            standard_w = 'kg'
            break
        else:
            print 'Invalid Choice'
    while True: 
        standard_choice_h = raw_input("Enter which standard you would like to use for height: \n 1. Inches (in) \n 2. Centimeters (cm) \n Choice: ")
        if (standard_choice_h == '1'):
            standard_h = 'in'
            break
        elif (standard_choice_h == '2'):
            standard_h = 'cm'
            break
        else:
            print 'Invalid Choice'
    height = raw_input("Enter your current height in CM: ")
    goal = raw_input("Enter your desired weight (" + standard_w + "): ")
    settings = {
        'height': height,
        'standard_h': standard_h, #in or cm
        'standard_w': standard_w, #lb or kg
        'goal': goal,
    }
    sfo = csv.writer(open("settings.csv", "w"))
    for key, val in settings.items():
        sfo.writerow([key, val])
    return

def changeSettings ():
    print "\nCurrent Settings"
    print "Weight: " + "Pounds (lb)" if settings['standard_w'] == 'lb' else "Kilograms (kg)"
    print "Height: " + "Inches (in)" if settings['standard_h'] == 'in' else "Centimeters (cm)"
    return

def loadSettings ():
    for key, val in csv.reader(open("settings.csv")):
        settings[key] = val
    return settings

def enterWeight ():
    # get weight from user
    weight = raw_input("Enter your current weight ("+ settings.standard_w + "): ")
    # save to file
    dfo.write (str(time.time()) + "\t" + str(weight) + "\n")
    return

def convertWeight (weight):
    if (settings.standard_w == 'lb'):
        weight = weight / 2.2046226218
    else:
        weight = weight * 2.2046226218
    return weight

def convertHeight (height):
    if (settings.standard_h == 'in'):
        height = height / 0.3937
    else:
        height = height * 0.3937
    return height

def calculateBMI (height, weight):
    if (settings.standard_h == 'in'):
        height = convertHeight (height)
    if (settings.standard_w == 'lb'):
        weight = convertWeight (weight)
    bmi = weight / (height * height)
    return bmi

def outputOptions ():
    print "Options: "
    print "1. Enter weight"
    print "2. Settings"
    print "3. Exit"

# ---main---
init ()

while True:
    choice = raw_input("Select Option: ")
    if (choice == '1'):
        enterWeight()
    elif (choice == '2'):
        changeSettings()
    elif (choice == '3'):
        dfo.close()
        break
    else:
        print "Invalid choice!"
