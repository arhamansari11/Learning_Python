week = int(input("Enter your Day Number : "))

match week:
    case 1 :
        print("Monday")
    case 2 :
        print("Tueday")
    case 3 :
        print("Wednesday")
    case 4 :
        print("Thursday")
    case 5 :
        print("Friday")
    case 6 :
        print("Saturday")
    case 7 :
        print("Sunday")
    case _:
        print("Please enter valid number of day.")
    