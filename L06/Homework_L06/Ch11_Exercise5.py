#Exercise 5 CH11 (Zelle 2017, Python Programming: An Introduction to Computer Science)

def count_new(myList, x):
	c=0
	for i in myList:
		if i == x:
			c+=1
	return c

def isin_new(myList, x):
	j=0
	for i in myList:
		if i == x:
			j+=1
	if j>=1:
		return True

def index_new(myList, x):
	for i, j in enumerate(myList):
		if j == x:
			return i

def reverse_new(myList):
	reversed_l = myList[::-1]
	return reversed_l

def getList():
	items = []
	xStr = input("Enter a list item (<ENTER> to quit) >> ")
	while xStr != "":
		items.append(xStr)
		xStr = input("Enter a list item (<ENTER> to quit) >> ")
	return items

def main():

	print("This program contains algorithms for Python operations.")

	myList = getList()

	x = input("Choose one item of your list: ")

	if isin_new(myList, x) == True:
		print("The count of the item {} in the entered List is: {}".format(x, count_new(myList, x)))
		print("The index of the item {} in the entered List is: {}".format(x, index_new(myList, x)))
		print("The  entered list{} in reversed order is {}".format(myList, reverse_new(myList)))
	else:
		print("{} is not an item in your list!".format(x))


if __name__ == '__main__':
	main()
