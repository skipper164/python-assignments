"""invest = int (input('enter amount of investment: '))
a = invest * (1 + 0.07) ** 10
b = invest * (1 + 0.07) ** 20
c = invest * (1 + 0.07) ** 30
print(f'youll have ${a:.2f} at the end of 10 years')
print(f'youll have ${b:.2f} at the end of 20 years')
print(f'youll have ${c:.2f} at the end of 30 years')"""






invest = int (input('enter amount of investment: '))
for loop in range(1,31):
    a = invest * (1 + 0.07) ** loop

    print(f'youll have ${a:.2f} at the end of {loop} years')
