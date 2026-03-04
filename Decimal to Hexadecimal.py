# Decimal to Hexadecimal Converter
User_Action = 'Y'
# This loops until the user decides to stop by entering 'N' or 'n'

while User_Action == 'Y':

    # Decimal input validation
    while True:
        try:
            Decimal_Number = float(input("Enter a Decimal number: "))
            break
        except ValueError:
            print("Input not recognized! Please enter a valid Decimal number.")

    # Conversion part
    whole_part = int(Decimal_Number)
    fraction_part = Decimal_Number - whole_part

    hex_chars = "0123456789ABCDEF"
    # The hex_chars string contains the characters for hexadecimal digits (0-9 and A-F) which correspond to the values 0-15.

    # Whole Part Conversion
    whole_hex = ""
    temp_whole = whole_part
    
    if temp_whole == 0:
        whole_hex = "0"
    else:
        while temp_whole > 0:
            remainder = temp_whole % 16
            # The remainder will be between 0 and 15, which corresponds to the hexadecimal digits.
            whole_hex = hex_chars[remainder] + whole_hex
            temp_whole //= 16
    
    # Fractional Part Conversion
    fraction_hex = ""
    precision = 10
    temp_fraction = fraction_part

    while temp_fraction > 0 and precision > 0:
        temp_fraction *= 16
        digit = int(temp_fraction)
        fraction_hex += hex_chars[digit]
        temp_fraction -= digit
        precision -= 1

    if fraction_hex:
        print("Hexadecimal representation:", whole_hex + "." + fraction_hex)
    else:
        print("Hexadecimal representation:", whole_hex)

    # Y/N continuation input validation
    while True:
        User_Action = input("Do you want to enter again? [Y/N] ").strip().upper()

        if User_Action in ['Y', 'N']:
            break
        else:
            print("Invalid input! Please enter Y or N.")

print("Thank You")