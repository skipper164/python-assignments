principal = int(input('enter the principal amount: $'))
 
interest = int(input('enter the anual interest rate: '))
duration = float(input('enter the duration in years: '))
 
interest = interest / 100
interestRate = interest / 12
numberofpayment = duration * 12

monthly = principal * (interestRate * (1 + interestRate) ** numberofpayment) / (((1 + interestRate) ** numberofpayment) - 1)
print('monthly payment is: $', monthly)

