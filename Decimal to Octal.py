# Decimal to Octal Converter
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

    # Whole Part Conversion
    whole_octal = ""
    temp_whole = whole_part

    if temp_whole == 0:
        whole_octal = "0"
    else:
        while temp_whole > 0:
            remainder = temp_whole % 8
            # The remainder will be between 0 and 7, which corresponds to the octal digits.
            whole_octal = str(remainder) + whole_octal
            temp_whole //= 8

    # Fractional Part Conversion
    fraction_octal = ""
    precision = 10
    temp_fraction = fraction_part

    while temp_fraction > 0 and precision > 0:
        temp_fraction *= 8
        digit = int(temp_fraction)
        fraction_octal += str(digit)
        temp_fraction -= digit
        precision -= 1

    if fraction_octal:
        print("Octal representation:", whole_octal + "." + fraction_octal)
    else:
        print("Octal representation:", whole_octal)

    # Y/N continuation input validation
    while True:
        User_Action = input("Do you want to enter again? [Y/N] ").strip().upper()

        if User_Action in ['Y', 'N']:
            break
        else:
            print("Invalid input! Please enter Y or N.")

print("Thank You")