# Ask the user to enter a day number (1-7) and print the corressponding day according to the number

num = int(input("Enter the Number: "))

match num:
    case 1:
        print("Today is SUNDAY")
    case 2:
        print("Today is MONDAY")
    case 3:
        print("Today is TUESDAY")
    case 4:
        print("Today is WEDNESDAY")
    case 5:
        print("Today is THURSDAY")
    case 6:
        print("Today is FRIDAY")
    case 7:
        print("Today is SATURDAY")