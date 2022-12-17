"""--- Part Two ---
As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies 
their group. For efficiency, within each group of three Elves, the badge is the only item type 
carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will 
have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any 
other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. 
All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to 
tell which item type is the right one is by finding the one item type that is common between all 
three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different 
badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
In the first group, the only item type that appears in all three rucksacks is lowercase r; this 
must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, 
they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the 
priorities of those item types?
"""
RuckContents = open("Day_Three_Rucksack_Reorganization_Input.txt").read().split('\n')
#RuckContents = open("Day_Three_Rucksack_Reorganization_Test_Input.txt").read().split('\n')
scores = open("Day_Three_Rucksack_Reorganization_Scoring.txt").read().split('\n')

def getScore(m):
	tScore = 0
	print("Getting Score.")
	for s in scores:
		if str(s[0]) == str(m):
			if len(s) == 3:
				tScore = tScore + int(str(s[2]))
			elif len(s) == 4:
				tScore = tScore + int(str(s[2]+s[3]))
	
	return tScore


def compareRucks(ruck1, ruck2, ruck3):
	ruckMatch = ""
	for r2 in ruck2:
		match = ruck1.find(r2)
		if match != -1:
			if ruck3.find(r2) != -1:
				ruckMatch = ruck1[match]
			else:
				continue

	return ruckMatch

ruckRow = 0
ruckCount = len(RuckContents)
count = 0
sack = ['']*3
totalScore = 0

while ruckRow < ruckCount:
	while count != 3:
		sack[count] = RuckContents[ruckRow]
		count = count + 1
		ruckRow = ruckRow + 1

	count = 0
	totalScore = totalScore + getScore(compareRucks(sack[0], sack[1], sack[2]))

print("Score: " + str(totalScore))
print("The correct answer is: 2342")
