import os

def valueToHexString(value): #Input a value (number), returns a hexadecimal string
    if value == "10":
        return "A"
    elif value == "11":
        return "B"
    elif value == "12":
        return "C"
    elif value == "13":
        return "D"
    elif value == "14":
        return "E"
    elif value == "15":
        return "F"
    else:
        return value

def hexStringToValue(hexString): #Input a hex string (number or letter), returns an intsponding with the value
    if hexString.lower() == "a":
        return 10
    elif hexString.lower() == "b":
        return 11
    elif hexString.lower() == "c":
        return 12
    elif hexString.lower() == "d":
        return 13
    elif hexString.lower() == "e":
        return 14
    elif hexString.lower() == "f":
        return 15
    else:
        return int(hexString)

def checkBinary(string): #Checks if the string is a binary (only contains 1s and 0s)
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        return True
    else : 
        return False

def binaryToDec(): #Converts binary to decimal
    print("\nBinary to Decimal\n")
    decimal = 0
    binary = input("Enter the binary value you want to convert: ")

    if not checkBinary(binary): #Checks if the string is a binary
        handleError("Incorrect Format Entered.")
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

def decToBinary(): #Converts decimal to binary
    print("Decimal to Binary\n")
    decimal = 0
    decimal = input("Enter the decimal value you want to convert: ")
    binary = ""

    if decimal.isdecimal(): #Checks if string is decimal
        decimal = int(decimal)
    else:
        handleError("Incorrect Format Entered.")
        print("_________________________________")
        input()
        return
    
    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by two and adds it to the front of the string
        binary = str(decimal % 2) + binary[:]
        decimal //= 2

    print(f">> {binary}")
    print("_________________________________")
    input()

def hexToDec(): #Converts hexadecimal to decimal
    print("Hexadecimal to Decimal\n")
    decimal = 0
    hexadecimal = ""
    hexadecimal = input("Enter the hexadecimal value you want to convert: ")

    for i in range(len(hexadecimal)): #Multiplies the hexadecimal value by 16 to the power of the length of the hex - i - 1, and then adds it to the decimal value
        decimal += hexStringToValue(hexadecimal[i]) * (16 ** (len(hexadecimal) - i - 1))

    print(f">> {decimal}")
    print("_________________________________")
    input()

def decToHex(): #Converts decimal to hexadecimal
    print("Decimal to Hexadecimal\n")
    decimal = 0
    decimal = input("Enter the decimal value you want to convert: ")
    hexadecimal = ""

    if decimal.isdecimal(): #Checks if string is decimal
        decimal = int(decimal)
    else:
        handleError("Incorrect Format Entered.")
        print("_________________________________")
        input()
        return

    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by sixteen and adds it to the front of the string
        value = valueToHexString(str(decimal % 16))
        hexadecimal = value + hexadecimal[:]
        decimal //= 16

    print(f">> {hexadecimal}")
    print("_________________________________")
    input()

def binaryToHex(): #Converts Binary to Hexadecimal
    print("Binary to Hexadecimal\n")
    decimal = 0
    hexadecimal = ""
    binary = ""
    binary = input("Enter the binary value you want to convert: ")

    if not checkBinary(binary): #Checks if the string is a binary
        handleError("Incorrect Format Entered.")
        print("_________________________________")
        input()
        return

    for i in range(len(binary)): #Loops through the length of the list adding 2 to the power of [length - i - 1] if the value is not 0
        if binary[i] == "0":
            continue
        decimal += 2 ** (len(binary) - i - 1)

    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by sixteen and adds it to the front of the string
        value = valueToHexString(str(decimal % 16))
        hexadecimal = value + hexadecimal[:]
        decimal //= 16

    print(f">> {hexadecimal}")
    print("_________________________________")
    input()

def hexToBinary(): #Converts hexadecimal to binary
    print("Hexadecimal to Binary\n")
    decimal = 0
    binary = ""
    hexadecimal = ""
    hexadecimal = input("Enter the hexadecimal value you want to convert: ")

    for i in range(len(hexadecimal)): #Multiplies the hexadecimal value by 16 to the power of the length of the hex - i - 1, and then adds it to the decimal value
        decimal += hexStringToValue(hexadecimal[i]) * (16 ** (len(hexadecimal) - i - 1))

    while decimal > 0: #While the decimal is greater than 0, takes the remainder of int dividing the decimal by two and adds it to the front of the string
        binary = str(decimal % 2) + binary[:]
        decimal //= 2

    print(f">> {binary}")
    print("_________________________________")
    input()

#Prints out the error message
def handleError(error_str):
    print(f">> Error: {error_str}")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

while True: #While the program is running, display the command menu and ask the user to enter a command
    clearConsole()
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
    if command == 1:
        binaryToDec()
    elif command == 2:
        decToBinary()
    elif command == 3:
        hexToDec()
    elif command == 4:
        decToHex()
    elif command == 5:
        binaryToHex()
    elif command == 6:
        hexToBinary()
    elif command == 7:
        break
    else:
        handleError("Invalid Command.")
        print("_________________________________")
        input()
