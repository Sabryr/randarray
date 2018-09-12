import random

def getrandarray(origsize , number):
	listoflist = []
	while number > 0:
		print number
		size = origsize
		arrayList = []
		while size > 0:
			cnum = getrand(1,34)
			if cnum not in arrayList:
				arrayList.append(cnum)
				size =  size - 1
		arrayList.sort()
		if not listcontain(listoflist , arrayList):
			listoflist.append(arrayList)
			number =  number - 1
	return  listoflist

def listcontain(listoflist, list):
	if len(listoflist) == 0:
		return  False
	for i in listoflist:
		i.sort()
                if  i == list:
			return True
		difs = 0
		for j in i:
			if j in list:
				difs = difs +1 
		if difs > 4:
			return True
	return False


def getrand(a,b):
	return random.randint(1,10)


def main():
	for i in getrandarray(10, 10):
		print i

if __name__ == '__main__':
	main()
