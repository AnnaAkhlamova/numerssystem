def decimal_to_any_system(num):
    if 'x' not in num:
        return "Input should be in format '<decimal_number>x<base>'"
    num=num.split('x')
    if len(num) != 2 or not num[0].isdigit() or not num[1].isdigit():
        return "Input should be in format '<decimal_number>x<base>'"
    user_num=int(num[0])
    n=int(num[1])
    if n<2 or n>16:
        return "system must be in range 2-16"
    elif user_num==0:
        return num
    x = ''
    hex_digits = "0123456789ABCDEF"
    while user_num>0:
        zalushok=user_num%n
        x=hex_digits[zalushok]+x
        user_num=user_num//n
    return x
def system_to_decimal(num):
    if 'x' not in num:
        return "Input should be in format '<number>x<base>'"
    num = num.split('x')
    if len(num) != 2 or not num[1].isdigit():
        return "Input should be in format '<decimal_number>x<base>'"
    user_num = num[0]
    n = int(num[1])
    x = 0
    if n<2 or n>16:
        return "system must be in range 2-16"
    elif user_num==0:
        return user_num
    hex_digits = "0123456789ABCDEF"
    for digit in user_num.upper():
        if digit in hex_digits[:n]:
            value = hex_digits.index(digit)
            x = x * n + value
        else:
            return "Invalid digit for the given base"
    return x

while True:
    choice=input("What do you want to do? 1 for decimal to any system or 2 for system to decimal ")
    if choice=="1":
        number = input("Enter your decimal number\nat the end write x and number for which system you want to convert it ").lower()
        print(f'Converted number: {decimal_to_any_system(number)}')
    elif choice=="2":
        number=input("Enter your number\nat the end write x and number in which system it is ").lower()
        print(f'Converted number: {system_to_decimal(number)}')
    else:
        print("Uncorrect choice.")
    while True:
        choice = input("Do you wanna to enter another number? (yes, no) ").lower()
        if choice == "yes":
            break
        elif choice == "no":
            print("Thank you for using this app")
            exit()
        else:
            print("Uncorrect data!")