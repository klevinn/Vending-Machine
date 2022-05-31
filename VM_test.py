inventory = {'IM':{"Description": "Iced Milo", "Price": 1.5, "Quantity": 0},
             'HM':{"Description": "Hot Milo", "Price": 1.2, "Quantity": 0},
             'IC':{"Description": "Iced Coffee", "Price": 1.5, "Quantity": 0},
             'HC':{"Description": "Hot Coffee", "Price": 1.2, "Quantity": 0},
             '1P':{"Description": "100 Plus", "Price": 1.1, "Quantity": 0},
             'CC':{"Description": "Coca cola", "Price": 1.3, "Quantity": 0}}
amount = 0
choice = 1
sumOfPrice = 0
paid = 1
payment= 0
def checkpayment(payment, sumOfPrice):
    if payment >= sumOfPrice:
        change = payment - sumOfPrice
        print("Please collect your change: ${:.2f} ".format(change))
        print("Drinks paid. Thank you.")
        return True
    else:
        return False

#check if its vendor
vendor = input("Are you a vendor (Y/N)? ").upper()
#it is vendor
if vendor == "Y":
    print("Welcome to ABC Vending Machine\nSelect from the following choices to continue:\n1. Add Drink Type\n2. Replenish Drink\n3. Exit")
    vchoice = input("Enter Choice: "
)
#its not vendor
elif vendor == "N":
    print("Welcome to ABC Vending Machine\nSelect from the following choices to continue:")
    #print choices
    for short_form in inventory:
        print("{}. {} (S${})".format(short_form, inventory[short_form]["Description"], inventory[short_form]["Price"]))
    print("0. Exit/Payment")


    while choice != 0:
        choice = input("Enter Choice: ").upper()
        if choice in inventory:
            amount +=1
            sumOfPrice = sumOfPrice + inventory[choice]["Price"]
            print("No. of drink(s) selected = ",amount)
        elif choice == "0" and sumOfPrice != 0:
            print("Please pay: {:.2f}".format(sumOfPrice))
            break
        elif choice == "0" and sumOfPrice == 0:
            print("No drinks selected\nThank you for using")
            break
        else:
            print("Invalid option")
            break

    while paid != 0:
        print("Indicate your payment:")
        tendollars = int(input("Enter no. of $10 notes: "))
        payment += tendollars * 10
        if checkpayment(payment, sumOfPrice):
            break

        fivedollars = int(input("Enter no. of $5 notes: "))
        payment += fivedollars * 5
        if checkpayment(payment, sumOfPrice):
            break

        twodollars = int(input("Enter no. of $2 notes: "))
        payment += twodollars * 2
        if checkpayment(payment, sumOfPrice):
            break

        print("Not enough to pay for drinks\nTake back your cash!")
        cancel = input("Do you want to cancel the purchase? Y/N: ").upper()
        if cancel == "Y":
            print("Purchase is cancelled. Thank you")
        elif cancel == "N":
            paid = 1
