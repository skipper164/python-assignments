"""
for skipper in range(2, 11, 2):
    print(skipper)

total_score = 0
for number in range(4):
    score = int(input("enter the student score: "))
    total_score = total_score + score

average = total_score / number

print("the total score is: ", total_score, "average is: ", average)
"""




total_score = 1
score = 0
number = -1
while score != -1:
    score = int(input("enter the student score (and -1 to stop): "))
    total_score = total_score + score
    number += 1

average = total_score / number

print("the total score is: ", total_score, "average is: ", average)
