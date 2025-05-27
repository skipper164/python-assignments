

#ends = 0
#while ends != 'end':
print('''
1. add a task
2. view task
3. mark as complete
4. delete a task
5. exit''')


option = int(input())

lists = []

if(option == 1):
	
		print('add a task(5 to exit): ' )
		add = 0
		while add != '5': 
			add = input() 
			print(f'{add} has been added to list')
			lists.append(add)
			
if(option == 2):
		print(lists)

if(option == 3):
   		print(lists)
   
   
   
if(option == 4):
		print(list)
		adds = 0
		while adds != 'stop': 
			adds = input() 
			lists.pop(adds)

#print('task is ended')	


	
print(lists)	 

