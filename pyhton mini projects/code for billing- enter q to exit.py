sum = 0
while(True):
	userinput = input("enter the item price or press q to quit: \n")
	if (userinput != 'q') :
		sum = sum + int(userinput)
		print(f"order total so far: {sum}")

	else:
		print(f"Your bill total is {sum}. Thanks for shopping with us.")
		break