number1 = int(input("Please enter first number: "))
number2 = int(input("Please input second number: "))
for i in range(0,number2):
    if i >= 15:
        break
    if number1 * i == 12:
        continue
    print(str(number1) + " " + 'x' + " " + str(i) + " "'=' + " " + str(number1 * i))