value = int(input('Enter the number to check'))
day = input('Enter a day of the week ! = ')

if value > 0 and value % 2 == 0:
    print("This is positive")
elif value == 0:
    print('Zero')
else:
    print('This is negative')

if day == 'Sunday' or day == 'Saturday':
    print('Weekend')
else:
    print('Week')
