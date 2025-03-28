import datetime
import os

# Lists to store food,drinks and other services including names+prices
list_foods = []
list_drinks = []
list_services = []

# Variable List of item prices. Index: 0-39 for foods, index: 40-79 for drinks,Index: 80-99 for other services.
list_item_price = [0] * 100

# Initializing discount start prices.
var_discount_1 = 200
var_discount_2 = 1000
var_discount_3 = 5000

# Initializing different discount rates.
var_discount_1_rate = 0.05
var_discount_2_rate = 0.10
var_discount_3_rate = 0.15

# This will make the program runnable on any unix based enviroument because it has differnet file system
navigator_symbol = "/"
if os.name == "nt":
    # This will make the program runnable on Windows
    navigator_symbol = "\\"


# Function to declare global variable for different lists
def def_default():
    global list_drinks, list_foods, list_services, list_item_order, list_item_price
    list_item_order = [0] * 100


def_default()


# Main menu function
def def_main():
    while True:
        # Design for Main Menu.
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"
                                                  "\t(O) ORDER\n"
                                                  "\t(R) REPORT\n"
                                                  "\t(P) PAYMENT\n"
                                                  "\t(E) EXIT\n" +
              "_" * 72)

        # Choose desire operation from the main menu,choosing operations as per input
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (len(input_1) == 1):
            if (input_1 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_1 == 'R'):
                print("\n" * 10)
                def_report()
                break
            elif (input_1 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

        # Order menu function


def def_order_menu():
    # Design for Order menu
    while True:
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"
                                                   "\t(F) FOODS AND DRINKS\n"
                                                   "\t(O) OTHER SERVICES\n"
                                                   "\t(M) MAIN MENU\n"
                                                   "\t(E) EXIT\n" +
              "_" * 72)

        # Choose desire selection from the order menu,choosing operations as per input
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if len(input_1) == 1:
            if (input_1 == 'F'):
                print("\n" * 10)
                def_food_drink_order()
                break
            elif (input_1 == 'O'):
                print("\n" * 10)
                def_other_services()
                break
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main()
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

        # File reader function to read all items be it drinks, food or other services from files


def def_full_file_reader():
    # Reading Foods List
    file_foods = open('files' + navigator_symbol + 'list_foods.fsd', 'r')
    for i in file_foods:
        list_foods.append(str(i.strip()))
    file_foods.close()

    # Reading Drinks List
    file_drinks = open('files' + navigator_symbol + 'list_drinks.fsd', 'r')
    for i in file_drinks:
        list_drinks.append(str(i.strip()))
    file_drinks.close()

    # Reading Services
    file_services = open('files' + navigator_symbol + 'list_services.fsd', 'r')
    for i in file_services:
        list_services.append(str(i.strip()))
    file_services.close()

    # Enumarte through food list to filter out prices and setup print Formatting by
    # replacing spaces with count difference of string length and align Prices to the most left of the terminal

    i = 0
    while i <= (len(list_foods) - 1):
        if 'RM' in list_foods[i]:
            list_foods[i] = str(list_foods[i][:list_foods[i].index('RM') - 1]) + ' ' * (
                        20 - (list_foods[i].index('RM') - 1)) + str(list_foods[i][list_foods[i].index('RM'):])
        i += 1

    i = 0
    while i <= (len(list_drinks) - 1):
        if 'RM' in list_drinks[i]:
            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('RM') - 1]) + ' ' * (
                        20 - (list_drinks[i].index('RM') - 1)) + str(list_drinks[i][list_drinks[i].index('RM'):])
        i += 1

    i = 0
    while i <= (len(list_services) - 1):
        if 'RM' in list_services[i]:
            list_services[i] = str(list_services[i][:list_services[i].index('RM') - 1]) + ' ' * (
                        20 - (list_services[i].index('RM') - 1)) + str(list_services[i][list_services[i].index('RM'):])
        i += 1


def_full_file_reader()


# Applying Sorting to the array to be sorted from A-Z ASC ((AND))
# Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
def def_file_sorter():
    global list_foods, list_drinks, list_services
    list_foods = sorted(list_foods)
    list_drinks = sorted(list_drinks)
    list_services = sorted(list_services)

    # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
    i = 0
    while i < len(list_foods):
        list_item_price[i] = float(list_foods[i][int(list_foods[i].index("RM") + 3):])
        i += 1

    # Applying extraction on 40 and above items which are the drinks
    i = 0
    while i < len(list_drinks):
        list_item_price[40 + i] = float(list_drinks[i][int(list_drinks[i].index("RM") + 3):])
        i += 1

    # Applying extraction on 80 and above items wich are Services
    i = 0
    while i < len(list_services):
        list_item_price[80 + i] = float(list_services[i][int(list_services[i].index("RM") + 3):])
        i += 1


def_file_sorter()


def def_food_drink_order():
    while True:
        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

        i = 0
        while i < len(list_foods) or i < len(list_drinks):
            # To fix up to space indention in console or terminal by applying detection rule to figure out
            # spacing for TWO DIGITS numbers
            var_space = 1
            if i <= 8:
                var_space = 2

            if i < len(list_foods):
                # Styling out the index number for the food or item and starting out from 1 for better human readability
                food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  | "
            else:
                # 36 is a constant for indention in console to fixup list in print
                food = " " * 36 + "| "
            if i < len(list_drinks):
                drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
            else:
                drink = ""
            print(food, drink)
            i += 1

        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

        input_1 = input("Please Select Your Operation: ").upper()  # Handling Menu Selection
        if (input_1 == 'M'):
            print("\n" * 10)
            # Return to main menu by calling it out
            def_main()
            break
        if (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            # Handling Exit and print out thank you
            break
        if (input_1 == 'P'):
            print("\n" * 10)
            # Handling payment || More details below
            def_payment()
            break
        try:
            # Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
            int(input_1)
            if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (
                    int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                try:
                    # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                    print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1]))
                except:
                    pass
                try:
                    print("\n" + "_" * 72 + "\n" + str(list_drinks[
                                                           int(input_1) - 41]))  # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                except:
                    pass

                input_2 = input("How Many You Want to Order?: ").upper()  # Handling Quantity input
                if int(input_2) > 0:
                    list_item_order[int(input_1) - 1] += int(input_2)  # adding item to Orders Array
                    print("\n" * 10)
                    print("Successfully Ordered!")
                    def_food_drink_order()  # Return food/drinks Menu
                    break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
        except:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def def_other_services():
    while True:
        # Services Menu Structure
        print("*" * 29 + "OTHER SERVICES" + "*" * 29)
        print(" |NO| |SERVICE NAME|      |PRICE|")

        i = 0
        while i < len(list_services):
            # Services starts from 81 + and now it is being enumarated into a list.
            print(" (" + str(81 + i) + ")" + " " + str(list_services[i]))

            i += 1

        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

        input_1 = input("Please Select Your Operation: ").upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            # Navigate Back to main menu
            def_main()
            break
        if (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        if (input_1 == 'P'):
            print("\n" * 10)
            # navigate to payment
            def_payment()
            break
        try:
            int(input_1)
            if (int(input_1) > 80) and (int(input_1) < 100):
                print("\n" * 10)
                print("Successfully Ordered: " + str(list_services[int(input_1) - 81]))
                # Adding services to orders array (AND) encapsulate errors  with try/except
                list_item_order[int(input_1) - 1] = 1
                def_other_services()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        except:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def def_report():
    while True:
        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
        # Reading out reports from report.fsd
        file_report = open('files' + navigator_symbol + 'report.fsd', 'r').read()
        print(file_report)
        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            # Navigate back to menu
            def_main()
            break
        elif (input_1 == 'E'):
            # Exit and break up the loop
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def def_payment():
    while True:
        # Header & Styling
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n")
        # alloc/init a variable to handle total_price
        total_price = 0

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[
                                                                                   :19] + "\n" + " " * 17 + "-" * 35  # building up report string header
        i = 0
        while i < len(list_item_order):
            # Enumarating order array items and summing up its prices * quantities
            if (list_item_order[i] != 0):
                if (i >= 0) and (i < 40):
                    # string appending the formated food name and formated order structure from quantity and final price
                    report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i])
                    print(" " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i]))
                    # Calculating the total price for food
                    total_price += list_item_price[i] * list_item_order[i]
                if (i >= 40) and (i < 80):
                    report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(list_item_order[i])
                    print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                    # Calculating the total price for drinks
                    total_price += list_item_price[i] * list_item_order[i]
                if (i >= 80) and (i < 100):
                    report_new += "\n" + " " * 17 + str(list_services[i - 80])
                    print(" " * 17 + str(list_services[i - 80]))
                    # Calculating the total price for services
                    total_price += list_item_price[i] * list_item_order[i]
                i += 1
            else:
                i += 1
        ### Applying Discounts Ruless
        if total_price > var_discount_3:  ### price > 5000
            total_price -= total_price * var_discount_3_rate  # Discount fees from the total_price by 0.15 or 15%
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                                                       "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                var_discount_3_rate * 100) + "\n" \
                                             "" + " " * 17 + "DISCOUNT AMOUNTS:   RM " + str(
                round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                                                                                            "" + " " * 17 + "TOTAL PRICES:       RM " + str(
                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35  # Round() to flour the float into an interger
            print(" " * 17 + "-" * 35 + "\n"
                                        "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                var_discount_3_rate * 100) + "\n"
                                             "" + " " * 17 + "DISCOUNT AMOUNTS:   RM " + str(
                round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                                                                                            "" + " " * 17 + "TOTAL PRICES:       RM " + str(
                round(total_price, 2)))
        elif total_price > var_discount_2:  ### price > 3000
            total_price -= total_price * var_discount_2_rate  # Discount fees from the total_price by 0.10 or 10%
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                                                       "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                var_discount_2_rate * 100) + "\n" \
                                             "" + " " * 17 + "DISCOUNT AMOUNTS:   RM " + str(
                round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                                                                                            "" + " " * 17 + "TOTAL PRICES:       RM " + str(
                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35  # Round() to flour the float into an interger
            print(" " * 17 + "-" * 35 + "\n"
                                        "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                var_discount_2_rate * 100) + "\n"
                                             "" + " " * 17 + "DISCOUNT AMOUNTS:   RM " + str(
                round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                                                                                            "" + " " * 17 + "TOTAL PRICES:       RM " + str(
                round(total_price, 2)))
        elif total_price > var_discount_1:  ### price > 200
            total_price -= total_price * var_discount_1_rate  # Discount fees from the total_price by 0.05 or 5%
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                                                       "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                var_discount_1_rate * 100) + "\n" \
                                             "" + " " * 17 + "DISCOUNT AMOUNTS:   RM " + str(
                round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                                                                                            "" + " " * 17 + "TOTAL PRICES:       RM " + str(
                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35  # Round() to flour the float into an interger
            print(" " * 17 + "-" * 35 + "\n"
                                        "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                var_discount_1_rate * 100) + "\n"
                                             "" + " " * 17 + "DISCOUNT AMOUNTS:   RM " + str(
                round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                                                                                            "" + " " * 17 + "TOTAL PRICES:       RM " + str(
                round(total_price, 2)))
        else:
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(
                round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       RM " + str(round(total_price, 2)))

        print("\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 10)
            print("Successfully Paid!")
            file_report = open('files' + navigator_symbol + 'report.fsd', 'a')  # Save it into a file
            file_report.write(report_new)
            file_report.close()
            # Reset the program for the name order
            def_default()
        elif (input_1 == 'M'):
            print("\n" * 10)
            # Navigate back to the main menu
            def_main()
            break
        elif (input_1 == 'R'):
            print("\n" * 10)
            # Navigate to the reports
            def_report()
            break
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def_main()
