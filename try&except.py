while True:
 try:
     a=int(input('Enter the  first number'))
     b= int(input('Enter the second number'))
     print(a+b)
     print('You won!!!')
     break
 except:
    print('There is some error, please enter the correct value')
