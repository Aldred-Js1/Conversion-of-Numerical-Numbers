# Decimal to Binary Converter
User_Action = 'Y'
# This loops until the user decides to stop by entering 'N' or 'n'

while User_Action == 'Y':

    # Decimal input validation
    while True:
        try:
            Decimal_Number = float(input("Enter a decimal number: "))
            break
        except ValueError:
            print("Input not recognized! Please enter a valid decimal number.")

    # Conversion part
    whole_part = int(Decimal_Number)
    fraction_part = Decimal_Number - whole_part

    # Whole Part Conversion
    whole_binary = ""
    temp_whole = whole_part

    if temp_whole == 0:
        whole_binary = "0"
    else:
        while temp_whole > 0:
            remainder = temp_whole % 2
            # The remainder will be either 0 or 1, which are the binary digits.
            whole_binary = str(remainder) + whole_binary
            temp_whole //= 2

    # Fractional Part Conversion
    fraction_binary = ""
    precision = 10
    temp_fraction = fraction_part

    while temp_fraction > 0 and precision > 0:
        temp_fraction *= 2
        bit = int(temp_fraction)
        fraction_binary += str(bit)
        temp_fraction -= bit
        precision -= 1

    if fraction_binary:
        print("Binary representation:", whole_binary + "." + fraction_binary)
    else:
        print("Binary representation:", whole_binary)

    # Y/N continuation input validation
    while True:
        User_Action = input("Do you want to enter again? [Y/N] ").strip().upper()

        if User_Action in ['Y', 'N']:
            break
        else:
            print("Invalid input! Please enter Y or N.")

print("Thank You")