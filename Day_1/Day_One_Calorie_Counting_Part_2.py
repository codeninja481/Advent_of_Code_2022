"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might 
eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the 
most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth 
Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

Calories = open("Day_One_Calorie_Counting_Input.txt").read().split('\n')
#Calories = open("Day_One_Calorie_Counting_Test_Input.txt").read().split('\n')

topThree = [0, 0, 0]
CalCount = 0

def sortArray(r):
	f = 0
	if r[0] > r[1]:
		f = r[0]
		r[0] = r[1]
		r[1] = f

	if r[1] > r[2]:
		f = r[1]
		r[1] = r[2]
		r[2] = f

	return

print("Length of Calories: " + str(len(Calories)))
CalSize = len(Calories)
stepCount = 0

def buildTopThree(c):
	print("C value is: " + str(c))
	if topThree[0] == int(c) or topThree[1] == int(c) or topThree[2] == int(c):
		return

	if topThree[0] < int(c):
		topThree[0] = int(c)

	sortArray(topThree)

	return


for c in Calories:
	if str(c) != "":
		CalCount = CalCount + int(c)
	else:
		buildTopThree(CalCount)
		CalCount = 0

	stepCount = stepCount + 1

	if stepCount == CalSize:
		buildTopThree(CalCount)

print("Top Three Highest Calorie Counts: " + str(topThree[0]) + " : " + str(topThree[1]) + " : " + str(topThree[2]))
print("Total Count for all three is: " + str(int(topThree[0]) + int(topThree[1]) + int(topThree[2])))
print("Answer is NOT: 204701")
print("Answer is: 210367")