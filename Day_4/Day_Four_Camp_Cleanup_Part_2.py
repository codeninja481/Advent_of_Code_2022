"""--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would 
  like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining 
  four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
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
	if (int(b[0]) <= int(a[1]) and b[1] >= a[0]) or (int(a[1]) <= int(b[1]) and b[0] <= a[1]):
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
print("The correct answer is NOT 955.  Too high.")
print("The correct answer is NOT 885.  Too low.")
print("The correct answer is 571")