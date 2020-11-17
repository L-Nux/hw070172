#Exercise 7 CH11 (Zelle 2017, Python Programming: An Introduction to Computer Science)

def getList():
	items = []
	xStr = input("Enter a list item (<ENTER> to quit) >> ")
	while xStr != "":
		xStr = float(xStr)
		items.append(xStr)
		xStr = input("Enter a list item (<ENTER> to quit) >> ")
	return items

def innerProd(x,y):
	product= 0
	for i in range(0, len(x)):
		product += x[i]*y[i]
	return product

def main():

	print("This program computes the inner product of two lists.")

	myList1 = getList()
	myList2 = getList()

	if len(myList1) == len(myList2):
		print("The inner product for the two entered lists is: ", innerProd(myList1, myList2))
	else:
		print("The entered lists do not have the same length! ")

if __name__ == '__main__':
	main()
