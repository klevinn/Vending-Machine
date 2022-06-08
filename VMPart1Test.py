# Author : Calvin Lai

import copy
#  To have access to a code that allows me to get a completely independent copy
import time

#  The Inventory of the VM
machineInventory = {

    'IM': {'Description': 'Iced Milo', 'Price': 1.5, 'Quantity': 30},
    'HM': {'Description': 'Hot Milo', 'Price': 1.2, 'Quantity': 30},
    'IC': {'Description': 'Iced Coffee', 'Price': 1.5, 'Quantity': 50},
    'HC': {'Description': 'Hot Coffee', 'Price': 1.2, 'Quantity': 20},
    '1P': {'Description': '100 Plus', 'Price': 1.1, 'Quantity': 40},
    'CC': {'Description': 'Coca Cola', 'Price': 1.3, 'Quantity': 60},

}


# function to display a welcome message
def welcome_msg():
    print("Welcome to ABC Vending Machine")
    print("Select from following choices to continue.")


# function to display drinks
def display_drinks():
    longestname = 0
    for key2, value2 in machineInventory.items():
        desc2 = (str(key2) + " : " + str(value2.get('Description')))  # Puts description besides corresponding keys
        lol = "($" + str(value2.get('Price')) + ")"  # Puts price in brackets beside desc
        test = str(desc2) + "" + str(lol)
        length = len(test)
        if length > longestname:
            longestname = length

    for key2, value2 in machineInventory.items():
        desc2 = (str(key2) + " : " + str(value2.get('Description')))  # Puts description besides corresponding keys
        lol = "($" + str(value2.get('Price')) + ")"  # Puts price in brackets beside desc
        test = str(desc2) + "" + str(lol)
        align_left = test.ljust(longestname + 3)  # Forces it so that no matter what its 25 spaces from the left, so as to align the Quantities
        if value2.get('Quantity') == 0:
            print(align_left, "Qty: *** Out Of Stock ***")  # If no quantity, display as out of stock
        else:
            print(align_left, "Qty:" + str(value2.get('Quantity')))


# function to check if number (quantity inputted) is valid, for those that can't be 0
def checknum(prompt, error):
    valid = 1
    while valid == 1:
        try:
            quant1 = int(input(prompt))
            if quant1 > 0:
                valid = 0
                return quant1
            else:
                print(error)
        except:
            print(error)


# function to check if number (quantity inputted) is valid, can be 0
def checknum2(prompt, error):
    valid = 1
    while valid == 1:
        try:
            quant2 = int(input(prompt))
            if quant2 < 0:
                print(error)
            else:
                valid = 0
                return quant2

        except:
            print(error)


#  machine[key].get(value) gets the value of the specific value in the nested dictionary
#  machine[key][value] does the same thing as the previously mentioned comment
#  I have set so that any input requiring alphabets to .upper() so that it is easier to code
#  I have used the formatting method that utilises % for majority of my print statements
function = ''  # an empty variable to use to loop the VM
while function != "Y":
    original = copy.deepcopy(machineInventory)  # to note down the initial quantity of VM
    vendor = input("Are you a vendor (Y/N)? ")
    vendor = vendor.upper().replace(" ", "")

    if vendor == "N":
        eachquantity1 = 0
        for key, value in machineInventory.items():
            eachquantity = value.get("Quantity")
            eachquantity1 = eachquantity1 + eachquantity  # To get total quantity of vending machine
        if eachquantity1 == 0:  # If VM is empty, the non-vendor menu wont open
            print("Sorry Vending Machine Out Of Stock. Please wait for Vendor Refill")
        else:
            welcome_msg()
            display_drinks()
            print("0 : Exit / Payment")
            choice = 1
            amount = 0  # Initial amount of drinks selected
            cost = 0  # Initial total cost
            cool = ''   # For later code
            while choice != "0":
                choice = input("Enter Choice: ")
                choice = choice.upper().replace(" ", "")
                if choice in machineInventory:
                    if machineInventory[choice].get("Quantity") == 0:  # If the code detects that the quantity is 0, it tells you there is none and continues the loop
                        print(machineInventory[choice].get("Description") + " is out of stock.")
                        print("No of drinks selected: %d" % amount)
                    else:
                        sufficient = ''  # Empty variable for loop
                        while sufficient != 0:
                            select = checknum("How many of the drink do you want? ", "Invalid Number")  # Asking for the amount of drinks
                            qty = machineInventory[choice].get("Quantity")
                            if select > qty:  # Amount selected more than quantity will print this message and loop again to ask for amount
                                print("Sorry we don't have enough drinks to fulfil your request.")
                            else:  # Sufficient amount, this block of code adds the amount u inputted and adds that to your amount of drinks selected while also minusing it from the Quantity
                                amount = amount + select
                                print("No of drinks selected: %d" % amount)
                                cost = cost + (machineInventory[choice].get("Price") * select)
                                qty = qty - select
                                machineInventory[choice]["Quantity"] = qty
                                sufficient = 0
                elif choice == "0":  # When user chooses to stop selecting drinks
                    if amount == 0:
                        print("Thank you for using ABC Vending Machine")
                    else:
                        cancel = ""
                        while cancel != "Y":
                            print("Total Amount is: $%.2f " % cost)
                            time.sleep(0.5)
                            print("Indicate your payment: ")
                            ten = checknum2("Input the number of $10 notes: ", "Invalid Number")
                            payment = ten * 10
                            if payment < cost:
                                five = checknum2("Input the number of $5 notes: ", "Invalid Number")
                                payment = payment + five * 5
                                if payment < cost:
                                    two = checknum2("Input the number of $2 notes: ", "Invalid Number")
                                    payment = payment + two * 2
                                    if payment == cost:
                                        print("Drink fully paid! Thank you for using ABC Vending Machine")
                                        cancel = "Y"
                                    elif payment > cost:
                                        change = payment - cost
                                        print("Please collect your change $%.2f" % change)
                                        print("Drink fully paid! Thank you for using ABC Vending Machine")
                                        cancel = "Y"
                                    else:
                                        print("Insufficient to pay for drinks!")
                                        print("Take back your cash")
                                        cool = ''
                                        while cool != '0':
                                            cancel = input("Do you want to cancel your purchase (Y/N)? ")
                                            cancel = cancel.upper()
                                            if cancel == "Y":
                                                print("Purchase is cancelled. Thank you for using ABC Vending Machine!")
                                                machineInventory.clear()  # Clears the dictionary with the decreased Quantities
                                                machineInventory.update(original)  # Replaces the dictionary with the initial Quantities that were copied
                                                cool = '0'
                                            elif cancel == "N":
                                                print("Please Re-Enter Cash")
                                                cool = '0'
                                            else:
                                                print("Invalid input")

                                elif payment == cost:
                                    print("Drink fully paid! Thank you for using ABC Vending Machine")
                                    cancel = "Y"
                                else:
                                    change = payment - cost
                                    print("Please collect your change $%.2f" % change)
                                    print("Drink fully paid! Thank you for using ABC Vending Machine")
                                    cancel = "Y"
                            elif payment == cost:
                                print("Drink fully paid! Thank you for using ABC Vending Machine")
                                cancel = "Y"
                            else:
                                change = payment - cost
                                print("Please collect your change $%.2f" % change)
                                print("Drink fully paid! Thank you for using ABC Vending Machine")
                                cancel = "Y"
                else:
                    print("Invalid")

    elif vendor == "Y":
        welcome_msg()
        print("1. Add Drink Type")
        print("2. Replenish Drink")
        print("0. Exit")
        print("Enter choice: ")
        function = "Y"

    else:
        print("Invalid Answer")
