"""--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""

RPS = open("Day_Two_Rock_Paper_Scissors_Input.txt").read().split('\n')
#RPS = open("Day_Two_Rock_Paper_Scissors_Test_Input.txt").read().split('\n')

"""
A - Rock
B - Paper
C - Scissors
X - Lose
Y - Draw
Z - Win
"""
myScore = 0

def getScore(opp, me, score):

	if opp == "A":
		if me == "X":
			print("opp threw rock, so you threw scissors.  Scored as a loss")
			score = score + (3 + 0)
		elif me == "Y":
			print("opp threw rock, so you threw rock.  Scored as a draw")
			score = score + (1 + 3)
		elif me == "Z":
			print("opp threw rock, so you threw paper.  Scored as a win")
			score = score + (2 + 6)
	elif opp == "B":
		if me == "X":
			print("opp threw paper, so you threw rock.  Scored as a loss")
			score = score + (1 + 0)
		elif me == "Y":
			print("opp threw paper, so you threw paper.  Scored as a draw")
			score = score + (2 + 3)
		elif me == "Z":
			print("opp threw paper, so you threw scissors.  Scored as a win")
			score = score + (3 + 6)
	elif opp == "C":
		if me == "X":
			print("opp threw scissors, so you threw paper.  Scored as a loss")
			score = score + (2 + 0)
		elif me == "Y":
			print("opp threw scissors, so you threw scissors.  Scored as a draw")
			score = score + (3 + 3)
		elif me == "Z":
			print("opp threw scissors, so you threw rock.  Scored as a win")					
			score = score + (1 + 6)

	return score

for r in RPS:
	print(r)
	print(r[0])
	#print(r[1])
	print(r[2])
	myScore = getScore(r[0], r[2], myScore)

print("Your final score is: " + str(myScore))
print("The right answer is 11186")