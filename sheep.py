### Sheep Problem ###

numCases = int(input())
allCases = []
for case in range(numCases):
	allCases.append(int(input()))

#will never get INSOMNIA for any number other than 0,  because you'll 
#eventually get a left most digit that updates slowly at big enough numbers
for case in allCases:
	allDigitsFound = False
	digitString=""
	digitList=[]
	count = 0
	baseCase = case
	while(!allDigitsFound):
		digitString = str(case)
		#append all numbers from the input
		digitList += list(digitString)
		if(checkAllDigits(digitList)):
			print(count)
		case += baseCase #fix this
		count += 1
		
		
		
def checkAllDigits(digitList):
	for i in range(0, 11): #0 through 10
		if i not in digitList:
			return False
	return True
		
