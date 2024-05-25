# Original tool created in 2020
# Updated tool created in 2024 - same functionality, but with improved code quality

import os

value_hex_dict = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

hex_value_dict = {v: k for k, v in value_hex_dict.items()}

def value_to_hex_string(value): #Input a value (number), returns a hexadecimal string
    return value_hex_dict.get(value, value)

def hex_string_to_value(hexString): #Input a hex string (number or letter), returns an intsponding with the value
    return hex_value_dict.get(hexString.upper(), int(hexString))

def is_binary(string): #Checks if the string is a binary (only contains 1s and 0s)
    return set(string).issubset({'0', '1'})

def binary_to_decimal(): #Converts binary to decimal
    print("\nBinary to Decimal\n")
    decimal = 0
    binary = input("Enter the binary value you want to convert: ")

    if not is_binary(binary): #Checks if the string is a binary
        handle_error("Incorrect Format Entered.")
        print("_________________________________")
        input()
        return

    for i in range(len(binary)): #Loops through the length of the list adding 2 to the power of [length - i - 1] if the value is not 0
        if binary[i] == "0":
            continue
        decimal += 2 ** (len(binary) - i - 1)

    print(f">> {decimal}")
    print("_________________________________")
    input()

def decimal_to_binary(): #Converts decimal to binary
    print("Decimal to Binary\n")
    decimal = 0
    decimal = input("Enter the decimal value you want to convert: ")
    binary = ""

    if decimal.isdecimal(): #Checks if string is decimal
        decimal = int(decimal)
    else:
        handle_error("Incorrect Format Entered.")
        print("_________________________________")
        input()
        return
    
    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by two and adds it to the front of the string
        binary = str(decimal % 2) + binary[:]
        decimal //= 2

    print(f">> {binary}")
    print("_________________________________")
    input()

def hex_to_decimal(): #Converts hexadecimal to decimal
    print("Hexadecimal to Decimal\n")
    decimal = 0
    hexadecimal = ""
    hexadecimal = input("Enter the hexadecimal value you want to convert: ")

    for i in range(len(hexadecimal)): #Multiplies the hexadecimal value by 16 to the power of the length of the hex - i - 1, and then adds it to the decimal value
        decimal += hex_string_to_value(hexadecimal[i]) * (16 ** (len(hexadecimal) - i - 1))

    print(f">> {decimal}")
    print("_________________________________")
    input()

def decimal_to_hex(): #Converts decimal to hexadecimal
    print("Decimal to Hexadecimal\n")
    decimal = 0
    decimal = input("Enter the decimal value you want to convert: ")
    hexadecimal = ""

    if decimal.isdecimal(): #Checks if string is decimal
        decimal = int(decimal)
    else:
        handle_error("Incorrect Format Entered.")
        print("_________________________________")
        input()
        return

    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by sixteen and adds it to the front of the string
        value = value_to_hex_string(str(decimal % 16))
        hexadecimal = value + hexadecimal[:]
        decimal //= 16

    print(f">> {hexadecimal}")
    print("_________________________________")
    input()

def binary_to_hex(): #Converts Binary to Hexadecimal
    print("Binary to Hexadecimal\n")
    decimal = 0
    hexadecimal = ""
    binary = ""
    binary = input("Enter the binary value you want to convert: ")

    if not is_binary(binary): #Checks if the string is a binary
        handle_error("Incorrect Format Entered.")
        print("_________________________________")
        input()
        return

    for i in range(len(binary)): #Loops through the length of the list adding 2 to the power of [length - i - 1] if the value is not 0
        if binary[i] == "0":
            continue
        decimal += 2 ** (len(binary) - i - 1)

    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by sixteen and adds it to the front of the string
        value = value_to_hex_string(str(decimal % 16))
        hexadecimal = value + hexadecimal[:]
        decimal //= 16

    print(f">> {hexadecimal}")
    print("_________________________________")
    input()

def hex_to_binary(): #Converts hexadecimal to binary
    print("Hexadecimal to Binary\n")
    decimal = 0
    binary = ""
    hexadecimal = ""
    hexadecimal = input("Enter the hexadecimal value you want to convert: ")

    for i in range(len(hexadecimal)): #Multiplies the hexadecimal value by 16 to the power of the length of the hex - i - 1, and then adds it to the decimal value
        decimal += hex_string_to_value(hexadecimal[i]) * (16 ** (len(hexadecimal) - i - 1))

    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by two and adds it to the front of the string
        binary = str(decimal % 2) + binary[:]
        decimal //= 2

    print(f">> {binary}")
    print("_________________________________")
    input()

#Prints out the error message
def handle_error(error_str):
    print(f">> Error: {error_str}")

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def invalid_command():
    print("Invalid command entered. Please try again.")
    print("_________________________________")
    input()

def main():
    commands = {
        1: binary_to_decimal,
        2: decimal_to_binary,
        3: hex_to_decimal,
        4: decimal_to_hex,
        5: binary_to_hex,
        6: hex_to_binary,
        7: lambda: exit(0)
    }

    while True: #While the program is running, display the command menu and ask the user to enter a command
        clear_console()
        command = input(
        """This is a conversion tool. Enter the number of the command to execute.

    _________________________________

    1. Binary to Decimal
    2. Decimal to Binary
    3. Hexadecimal to Decimal
    4. Decimal to Hexadecimal
    5. Binary to Hexadecimal
    6. Hexadecimal to Binary
    7. Exit
    _________________________________
    > """
        )

        #Check if command is an int; if yes, parse to int
        if (command.isnumeric()):
            command = int(command)

        #Call the function corresponding to the command. If the command is not valid, print an error message.
        commands.get(command, invalid_command)()

if __name__ == "__main__":
    main()