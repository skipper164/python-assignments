number = int(input('enter a five digit numbeer: ')) 
ten_thous = number // 10000
thous = (number // 1000) % 10 
hund = (number // 100) % 10 
tens = (number // 10)  % 10 
unit = number % 10 
 
print(ten_thous,  thous,  hund,  tens,  unit)
