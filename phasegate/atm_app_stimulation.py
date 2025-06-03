print('welcome to semicolon bank ATM')

balance = int(input('enter your account ballance: '))

total_balance = []
count = 0

loop = 0
while (True):
	withdrawal = int(input('enter withdrawal ammount multiples of N500 or N1,000: '))
	total_balance[count] = total_balance.append(withdrawal)



	if (withdrawal >= 500 and withdrawal % 10 == 0 and withdrawal >= withdrawal * 0.9  and balance - withdrawal > 100 and withdrawal < 20000 ):
		charges = 100
		count += 1
		print('Transaction successful!')
		new_balance =  balance - withdrawal - charges
		
		print(f'withdrawal amount: N{withdrawal}')
		print(f'withrawal fee: N{charges}')
		print(f'Remaining balance: N{new_balance}')
		print(' ')

		balance = new_balance
		


	else: print('invalid withdrawal amount')
	loop = input('Do you want to make another withdrawal?  YES(0)/NO(1) or press (3) to view transactions: ')
	
		
	if(loop ==3): print(f'your transaction history is {total_balance}')
	if(loop == 1): 
		break
	