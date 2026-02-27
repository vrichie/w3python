day=39
match day:
    case 0:
        print("Sunday")
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case _:
        print('Not a valid day')

match day:
    case 1|2|3|4|5:
        print("This is a weekday")
    case 0|6:
        print("its the weekend")
    case _:
        print("NOt valid")