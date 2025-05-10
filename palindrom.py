number = int(input('enter a five digit numbeer: ')) 
thous = number // 1000 
hund = (number // 100) % 10 
tens = (number // 10)  % 10 
unit = number // 10 
 
print(unit, tens, hund, thous)
