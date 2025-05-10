investment = float(input('enter the investment amount: '))
years = int(input('enter number of year(s):'))
rate = float(input('what is your interest rate:'))
 
rate = rate / 100

for loop in range(years):
   interest = (loop + 1) * rate * investment + investment
   print(f'return of investment for year:{loop + 1} is {interest}')    
    

