"""--- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several 
  Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique 
  ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed 
  that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated 
  effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), 
  while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, 
  while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might 
  contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 
  2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully 
  contains the other, one Elf in the pair would be exclusively cleaning sections their partner will 
  already be cleaning, so these seem like the most in need of reconsideration. In this example, there 
  are 2 such pairs.

In how many assignment pairs does one range fully contain the other?
"""

Sections = open("Day_Four_Camp_Cleanup_Input.txt").read().split('\n')
#Sections = open("Day_Four_Camp_Cleanup_Test_Input.txt").read().split('\n')

def compareAssignments(a1, a2):
	a = [0]*2
	b = [0]*2
	a[0] = a1[0:a1.index('-')]
	a[1] = a1[(a1.index('-')+1):len(a1)]
	b[0] = a2[0:a2.index('-')]
	b[1] = a2[(a2.index('-')+1):len(a2)]
	print("a: " + a[0] + " - " + a[1])
	print("b: " + b[0] + " - " + b[1])
	match = 0
	if (int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])) or (int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1])):
		print("MATCH")
		match = 1
	else:
		print("not a match")

	return match

totalMatches = 0
for s in Sections:
	assignment1 = s[0:(s.index(','))]
	assignment2 = s[(s.index(',')+1):len(s)]
	totalMatches = totalMatches + compareAssignments(assignment1, assignment2)


print("Total Matches: " + str(totalMatches))
print("The correct answer is NOT 199.  Too low.")
print("The correct answer is NOT 590.  Too high.")
print("The correct answer is 571")