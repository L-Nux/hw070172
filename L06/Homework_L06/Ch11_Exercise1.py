#Exercise 1 CH11 (Zelle 2017, Python Programming: An Introduction to Computer Science)

import math

def getNumbers():
	nums = []
	xStr = input("Enter a number (<ENTER> to quit) >> ")
	while xStr != "":
		x = float(xStr)
		nums.append(x)
		xStr = input("Enter a number (<ENTER> to quit) >> ")
	return nums

def mean_N(nums):
	total = 0.0
	for num in nums:
		total = total + num
	return total/len(nums)

def std_N(nums):
	sumDevSq = 0.0
	x_m = mean_N(nums)
	for num in nums:
		dev = num - x_m
		sumDevSq = sumDevSq + dev * dev
	return math.sqrt(sumDevSq/(len(nums)-1))

def main():

	print("This program computes mean and/or standard deviation.")

	data = getNumbers()

	decision1 = input("Do you want to calculate only mean or the standard deviation [y/n]: ")

	if decision1 == 'y':
		d1 = input("Do you want to calculate the mean [m] or the standard deviation [s]: ")
		if d1 == 'm':
			print("The mean of the input data is", mean_N(data))
		if d1 == 's':
			print("The standard deviation of the input data is", std_N(data))
	else:
		decision2 = input("Do you want to calculate the mean and the standard deviation [y/n]: ")
		if decision2 == 'y':
			print("The mean of the input data is", mean_N(data))
			print()
			print("The standard deviation of the input data is", std_N(data))
		else:
			print("No statistical method chosen.")

if __name__ == '__main__':
	main()
