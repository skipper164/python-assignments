gallon = 0
while gallon != -1:
    gallon = float(input('enter the gallons used (-1 to end):'))
    miles = int(input('enter the miles driven:'))
    miles_per_gallon = miles / gallon
    print(f'the miles per gallon for this tank was {miles_per_gallon:.6f}')

average = miles_per_gallon + average
print(f'the overal average miles per gallon was {average / 3}')