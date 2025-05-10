"""n = int(input('enter an input: '))
for n in range(1, n): 
    if n < 1:
        print('enter a positive number')
    print(n)"""

number = int(input('enter number:'))
while number < 1:
    number = int(input('enter number:'))
for n in range(number, 0, -1):
    print(n)
print('blast off')