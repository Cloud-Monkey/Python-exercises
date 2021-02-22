number1 = int(input('Please enter your number: ')) #variable int input
for i in range(1,number1+1): #index in range plus one
    if i*i >=200: # conditional to break the loop
        break #break statement
    print(i,i*i) #print function index, space, index squared