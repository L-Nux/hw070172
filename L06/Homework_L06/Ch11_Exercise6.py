#Exercise 6 CH11 (Zelle 2017, Python Programming: An Introduction to Computer Science)
import random

def getList():
	items = []
	xStr = input("Enter a list item (<ENTER> to quit) >> ")
	while xStr != "":
		items.append(xStr)
		xStr = input("Enter a list item (<ENTER> to quit) >> ")
	return items

def shuffle_list(myList):
		for i in reversed(range(1, len(myList))):
			z = random.randint(0, i + 1)
			myList[i], myList[z] = myList[z], myList[i]
		return myList

def main():

	print("This program contains algorithms for Python operations.")

	myList = getList()

	print(myList.index)

	shuffled = shuffle_list(myList)

	print("This is your list randomly shuffled: ", shuffled)


if __name__ == '__main__':
	main()
