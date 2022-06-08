# Author : Calvin Lai

import copy
#  To have access to a code that allows me to get a completely independent copy
import time

#  The Inventory of the VM
machineInventory = {

    'IM': {'Description': 'Iced Milo', 'Price': 1.5, 'Quantity': 30},
    'HM': {'Description': 'Hot Milo', 'Price': 1.2, 'Quantity': 30},
    'IC': {'Description': 'Iced Coffee', 'Price': 1.5, 'Quantity': 0},
    'HC': {'Description': 'Hot Coffee', 'Price': 1.2, 'Quantity': 0},
    '1P': {'Description': '100 Plus', 'Price': 1.1, 'Quantity': 0},
    'CC': {'Description': 'Coca Cola', 'Price': 1.3, 'Quantity': 0},

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


# function to add drinks
def add_drink_type(drink_id, description, price, quantity):
    itemdict = {"Description": description, "Price": price, "Quantity": quantity}  # Creates a dict to put into the VM
    machineInventory[drink_id] = itemdict  # Puts it into the VM


# function to refill drinks
def replenish_drink(drink_id, quantity):
    qty2 = machineInventory[drink_id].get("Quantity")  # Gets the Quantity amount of the drink_ID
    qty2 = qty2 + quantity  # Adds in the quantity requested
    machineInventory[drink_id]["Quantity"] = qty2  # Changing the value in the dictionary to updated amount
    print(machineInventory[drink_id].get('Description') + " has been topped up!")


# function to check if cost inputted is valid
def checkcost(prompt, error):
    valid = 1
    while valid == 1:
        try:
            cost2 = float(input(prompt))  # Cost needs to be a float and more than 0
            if cost2 > 0:
                valid = 0
                return cost2
            else:
                print(error)
        except:
            print(error)


# function to check if number (quantity inputted) is valid, for those that can't be 0
def checknum(prompt, error):
    valid = 1
    while valid == 1:
        try:
            quant1 = int(input(prompt))
            if quant1 > 0:
                return quant1
            else:
                print(error)
        except:
            print(error)


# function to check if number (quantity inputted) is valid, those that can be 0
def checknum2(prompt, error):
    valid = 1
    while valid == 1:
        try:
            quant2 = int(input(prompt))
            if quant2 < 0:
                print(error)

            else:
                return quant2

        except:
            print(error)


# function to check if space
def space_check(prompt, error):
    id_valid = ""
    while id_valid != "0":
        drinkz = input(prompt)
        space = drinkz.isspace()  # Checks if the content of the input is spaces only
        if len(drinkz) > 0 and space is not True:
            return drinkz
        else:
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
                            select = checknum2("How many of the drink do you want? ", "Invalid Number")  # Asking for the amount of drinks
                            qty = machineInventory[choice].get("Quantity")
                            if select > qty:  # Amount selected more than quantity will print this message and loop again to ask for amount
                                print("Sorry we don't have enough drinks to fulfil your request.")
                            else:  # Sufficient amount, this block of code adds the amount u inputted and adds that to your amount of drinks selected while also minusing it from the Quantity
                                amount = amount + select
                                print("No of drinks selected: %d" % amount)
                                cost = cost + (machineInventory[choice].get("Price") * select)  # They take the price of your choice times the amount of drinks selected, and add it to the total cost.
                                qty = qty - select
                                machineInventory[choice]["Quantity"] = qty  # Minuses off the Quantity every time u select a drink
                                sufficient = 0
                elif choice == "0":  # When user chooses to stop selecting drinks
                    if amount == 0:
                        print("Thank you for using ABC Vending Machine")
                    else:
                        cancel = ""
                        while cancel != "Y":
                            print("Total Amount is: $%.2f " % cost)
                            time.sleep(0.5)  # For better look / feel
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
        verified = ''
        while verified != '0':
            password = input("Enter Vending Password(PW: 1234): ")  # Non-vendors cannot access
            if password == '1234':
                welcome_msg()
                verified = '0'
                choice = ""
                while choice != "0":
                    print("1. Add Drink Type")
                    print("2. Replenish Drink")
                    print("3. Shut Down Vending Machine")
                    print("0. Exit")
                    choice = input("Enter Choice: ")
                    choice = choice.strip()
                    cont = ''
                    if choice == '1':
                        while cont != '0':
                            display_drinks()
                            newdrink = space_check("Enter Drink ID(0 to cancel): ", "Invalid Drink ID")
                            newdrink = newdrink.upper().replace(" ", "")
                            if newdrink == "0":
                                cont = '0'
                            elif newdrink in machineInventory:
                                print("Drink ID already exists")
                                cont = '1'
                            else:
                                desc = space_check("Enter Drink Description: ", "Invalid Description")
                                cost = checkcost("Enter Price Of Drink: $", "Invalid Price")
                                quant = checknum("Enter Quantity: ", "Invalid Quantity")
                                add_drink_type(newdrink, desc, cost, quant)
                                cont = '0'
                            # print(machineInventory)
                    elif choice == '2':
                        display_drinks()
                        while cont != '0':
                            existdrink = input("Enter Drink ID(0 to cancel): ").upper().replace(" ", "")  # Gets rid of spaces
                            if existdrink == "0":
                                cont = '0'
                            elif existdrink not in machineInventory:
                                print("No Drink with this drink ID. Try Again:")
                            else:
                                if machineInventory[existdrink].get('Quantity') > 5:
                                    print("No Need to Replenish. Quantity More Than 5")
                                    cont = '0'
                                else:
                                    increase = checknum("Enter Quantity: ", "Invalid Quantity")
                                    replenish_drink(existdrink, increase)
                                    cont = '0'
                    elif choice == '3':
                        off = ''
                        while off != 0:
                            # If vendor wants to shut down machine, additional features
                            function = input("Do you wish to shut down the Vending Machine? (Y/N) ").upper()
                            if function == "Y":
                                print("Vending Machine Has Been Shut Down")
                                off = 0
                                choice = "0"
                            elif function == "N":
                                print("Returning to Vendor Menu")
                                time.sleep(0.5)
                                off = 0
                            else:
                                print("Invalid Input")
                    elif choice != '0':
                        print("Invalid Selection")
                    else:
                        print("Thank you for using ABC Vending Machine")

            else:
                print("Incorrect Password. Please re-input")

    else:
        print("Invalid Choice")
