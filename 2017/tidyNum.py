#num is a string
def getTidyNum(num):
	
	if(len(num) == 1):
		return num

	else:
		if(isDecreasing(num) == -1):
			return num
		else:
			num = list(num)
			while(isDecreasing(num) != -1):
				i = isDecreasing(num)
				num[i] = str(int(num[i])-1)
				if(num[i] == 0):
					num[i:] = '9'
				else:
					num[i+1] = '9'
				
			return int(''.join(num))
				

#num is string
#check if a number every decreases from the one before it
def isDecreasing(num):
	for i in range(1, len(num)):
		#print("%d: %s <? %s" % (i, num[i], num[i-1]))
		if int(num[i]) < int(num[i-1]):
			return i-1
	return -1		

def main():
		#Get number of inputs
		numTestCases = int(input())
		inputs = []
		#Get the inputs
		for x in range(numTestCases):
			inputs.append(input())

		#Get Outputs
		outputs = []
		for x in inputs:
			outputs.append(getTidyNum(x))

		for x in outputs:
			print(x)

main()
