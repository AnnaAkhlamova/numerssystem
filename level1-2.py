def decimal_to_binary(binary):
    if binary==0:
        return binary
    x = ''
    while int(binary)>0:
        zalushok=int(binary)%2
        binary=int(binary)//2
        x=str(zalushok)+x
    return x

def binary_to_decimal(decimal):
    decimal=decimal[2:]
    x=0
    for digit in decimal:
        x=x*2+int(digit)
    return x

def hexadecimal_to_binary(hexadecimal):
    hexadecimal=hexadecimal[2:]
    x_str = ''
    bin_values = ["0000", "0001", "0010", "0011","0100", "0101", "0110", "0111","1000", "1001", "1010", "1011","1100", "1101", "1110", "1111"]
    for char in hexadecimal:
        if '0' <= char <= '9':
            index = int(char)
        else:
            index = int(char, 16)
        x_str += bin_values[index]
    if x_str[0:3]=="000":
        return x_str[3:]
    elif x_str[0:2]=="00":
        return x_str[2:]
    else:
        return x_str

def hexadecimal_to_decimal(hexadecimal):
    hexadecimal=hexadecimal[2:]
    x=0
    for char in hexadecimal:
        if '0' <= char <= '9':
            index = int(char)
        else:
            index = int(char, 16)
        x=x*16+index
    return x

def decimal_to_hexadecimal(hexadecimal):
    if hexadecimal==0:
        return hexadecimal
    x = ''
    hex_digits = "0123456789ABCDEF"
    while int(hexadecimal)>0:
        zalushok=int(hexadecimal)%16
        hexadecimal=int(hexadecimal)//16
        x=hex_digits[zalushok]+x
    return x

def binary_to_hexadecimal(hexadecimal):
    hexadecimal = hexadecimal[2:]
    x = 0
    hex_digits = "0123456789ABCDEF"
    for digit in hexadecimal:
        x = x * 2 + int(digit)
    hex_value = ''
    while x > 0:
        zalushok = x % 16
        hex_value = hex_digits[zalushok] + hex_value
        x = x // 16
    return hex_value

def user_choice(choice,num):
    if choice=="binary" and (num[0:2]=='ox' or num[0:2]=='0x'):
       return hexadecimal_to_binary(num)
    elif choice=="decimal" and (num[0:2]=='ox' or num[0:2]=='0x'):
        return hexadecimal_to_decimal(num)
    elif (num[0:2]=='ob' or num[0:2]=='0b') and choice=="decimal":
        return binary_to_decimal(num)
    elif (num[0:2]=='ob' or num[0:2]=='0b') and (choice=="16" or choice=="hexadecimal"):
        return binary_to_hexadecimal(num)
    elif choice=="binary":
        return decimal_to_binary(num)
    elif choice=="hexadecimal" or choice=="16":
        return decimal_to_hexadecimal(num)

while True:
    number=input("Enter your number(decimal,binary,16)\n*if it's binary enter 0b, 16 enter 0x and then your number ").lower()
    answer = input("In which system you want to convert it?(decimal,binary,16) ").lower()
    answer=user_choice(answer,number)
    print(answer)
    while True:
        choice = input("Do you wanna to enter another number? (yes, no) ").lower()
        if choice == "yes":
            break
        elif choice == "no":
            print("Thank you for using this app")
            exit()
        else:
            print("Uncorrect data!")