#Simple Calculator

number1=int(input('Enter Number 1:'))
number2=int(input('Enter Number 2:'))
op=input('Enter Operator[+,-,/,*,%]:')
if op=='+':
    print('Sum of Number 1 & Number 2 is =',number1+number2,)
elif op=='-':
    print('Substraction of Number 1 & Number 2 is =',number1-number2)
elif op=='*':
    print('Multiplication of Number 1 & Number 2 is =',number1*number2)
elif op=='/':
    print('Division of Number 1 & Number 2 is =',number1/number2)
elif op=='%':
    print('Reminder of Number 1 & Number 2 is =',number1%number2)
else:
    print('Invalid Operator')
