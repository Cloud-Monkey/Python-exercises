number1 = input("Enter whole number: ") # a created variable
number2 = input("Enter decimal number: ") # a created variable
 
integer_number = int(number1) # number1 variable should be integer (int)
float_number = float(number2) # number2 variable should be decimal fraction
round_number = int(round(float_number))#rounds correctly number2 to nearest integer

print(number1) # prints first variable
print(number2) # prints second variable
print(round_number) # prints rounded float variable number2

number3 = int(5)
number4 = float(3.5)
print(number3 + number4)