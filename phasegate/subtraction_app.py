import random

count = 0;
point = 0;

while (True):  
	count_2 = 0;

	number_1 = random.randint(1,50) 
	number_2 = random.randint(1,50) 

	if(number_1 > number_2):
		loop = 0
		while loop != 2:
			print(number_1, "-", number_2)
			score = number_1 - number_2
			option = int (input("input your answer " ))
			loop+=1
			if(option == score):
				point += 1
				loop = 2
	

	
       

	count+= 1
	




	if (count == 10): break;

print("your score is: ", point);
