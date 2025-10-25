#Grade Calculator
marks=float(input('Enter your marks:'))
if marks>=85 and marks<100:
    print('Congrats!, you scored Grade A')
elif marks>=60 and marks<84:
    print('You scored Grade B')
elif marks>=40 and marks<59:
    print('You scored Grade C')
elif marks>=30 and marks<39:
    print('You scored Grade D')
else:
    print('Sorry! you are Failed')
