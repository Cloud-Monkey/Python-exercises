number1 = int(input("Please input number to check if it is odd or even: "))
if (number1 % 2==0): # uses modulus to divide for remainder thus determining even or odd
    print(number1, "is an even number.")
else:
    print(number1, "is an odd number.")