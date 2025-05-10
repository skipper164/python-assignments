purchase = float(input('enter purchase amount: '))

if purchase >= 1000 and purchase < 10000:
    print(f'purchase between 1,000 to 10,000 receives {purchase * 0.05} discount for {purchase:,.2f} price, new price is {purchase - (purchase* 0.05):,.2f}' )
elif purchase >= 10000 and purchase <= 50000:
    print(f'purchase between 10,000 to 50,000 receives {purchase * 0.10} discount for  {purchase:,.2f} price , new price is {purchase - (purchase* 0.1):,.2f}')
elif purchase >= 50000:
    print(f'purchase above 50,000 receives {purchase * 0.2} discount for {purchase:,.2f} price, new price is {purchase - (purchase* 0.2):,.2f}')
else:
    print('theres no discount for this price')