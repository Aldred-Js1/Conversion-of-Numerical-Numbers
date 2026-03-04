User_Action = 'Y'

while User_Action == 'Y':

    # Decimal input validation
    while True:
        try:
            Decimal_Number = float(input("Enter a Decimal number: "))
            # Enter a Desired Base from (2-36) :)
            Base = int(input("Enter the base you want to convert to (2-36): "))
            if Base < 2 or Base > 36:
                print("Invalid base! Please enter a base between 2 and 36.")
                continue
            break
        except ValueError:
            print("Input not recognized! Please enter a valid Decimal number.")

    # Conversion part
    whole_part = int(Decimal_Number)
    fraction_part = Decimal_Number - whole_part

    # Characters for bases up to 36
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Whole Part Conversion
    whole_result = ""
    temp_whole = whole_part
    
    if temp_whole == 0:
        whole_result = "0"
    else:
        while temp_whole > 0:
            remainder = temp_whole % Base
            # The remainder will be between 0 and Base minus 1, which corresponds to the digits/characters for that base.
            whole_result = chars[remainder] + whole_result
            temp_whole //= Base 
    
    # Fractional Part Conversion
    fraction_result = ""
    precision = 10
    temp_fraction = fraction_part

    while temp_fraction > 0 and precision > 0:
        temp_fraction *= Base
        digit = int(temp_fraction)
        fraction_result += chars[digit]
        temp_fraction -= digit
        precision -= 1

    if fraction_result:
        print(f"Base {Base} representation:", whole_result + "." + fraction_result)
    else:
        print(f"Base {Base} representation:", whole_result)

    # Y/N continuation input validation
    while True:
        User_Action = input("Do you want to enter again? [Y/N] ").strip().upper()

        if User_Action in ['Y', 'N']:
            break
        else:
            print("Invalid input! Please enter Y or N.")

print("Thank You") 