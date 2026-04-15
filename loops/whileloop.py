number = 0

while number < 10:
    print(number)
    number = number + 1


while True:
    number1 = int(input("Enter the number: "))
    number2 = int(input("Enter the number: "))
    print(number1+number2)


stored_num = 10
while True:
    number1 = int(input("Enter the number between 1 to 10: "))
    if number1 == stored_num:
        print("number found")
        break


# Complete guess number game with good response message to user


stored_n = 30
attempts = 0

while stored_n < 5:
    print(input("Enter a number 1 to 50: "))
    



