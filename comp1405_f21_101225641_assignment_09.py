#Justin Yu 101225641
#Main Function
def central():
	#Asks user for input, if they don't enter a string, keeps asking
	flag = True
	while flag:
		userInput = input("Please input a string\n")
		if isinstance(userInput, str):
			flag = False
		else:
			print("Please enter a valid string")
	#Removes punctuation
	for i in userInput:
		asciiValue = ord(i)
		if not ((asciiValue >= 65 and asciiValue <= 90) or (asciiValue >= 97 and asciiValue <= 122) or asciiValue == 32):
			userInput = replace(userInput, chr(asciiValue), "")		
	print(userInput)
	#Calls the other functions and prints their return values
	userInput = lowUp(userInput)
	print(userInput)
	userInput = acronyms(userInput)
	print(userInput)
	userInput = homoglyphs(userInput)
	print(userInput)

#Function that replaces lowercase with uppercase
def lowUp(userInput):
	for i in userInput:
		asciiValue = ord(i)
		if (asciiValue >= 97 and asciiValue <= 122):
			userInput = replace(userInput, 	chr(asciiValue), chr(asciiValue-32))
	return userInput

#Function that replaces 4 words/phrases with acronyms
def acronyms(userInput):
	#Replaces BY THE WAY with BTW
	while "BY THE WAY" in userInput:
		userInput = replace(userInput, "BY THE WAY", "BTW")
	#Replaces AS SOON AS POSSIBLE with ASAP
	while "AS SOON AS POSSIBLE" in userInput:
		userInput = replace(userInput, "AS SOON AS POSSIBLE", "ASAP")
	#Replaces BE RIGHT BACK with BRB
	while "BE RIGHT BACK" in userInput:
		userInput = replace(userInput, "BE RIGHT BACK", "BRB")
	#Replaces MY BAD with MB
	while "MY BAD" in userInput:
		userInput = replace(userInput, "MY BAD", "MB")
	return userInput

#Function that replaces 4 letters with homoglyphs
def homoglyphs(userInput):
	#Replaces K with |<
	while "K" in userInput:
		userInput = replace(userInput, "K", "|<")
	#Replaces A with @
	while "A" in userInput:
		userInput = replace(userInput, "A", "@")
	#Replaces B with |3
	while "B" in userInput:
		userInput = replace(userInput, "B", "|3")
	#Replaces N with |\|
	while "N" in userInput:
		userInput = replace(userInput, "N", "|\|")
	return userInput
	
#Function that replaces characters and strings in strings
def replace(userInput, replaced, replacement):
	newInput = ""
	if userInput.index(replaced) == 0:
		newInput = replacement + userInput[slice(len(replaced), len(userInput))]
	else:
		x = userInput[slice(0, userInput.index(replaced))]
		y = userInput[slice((userInput.index(replaced)+len(replaced)),len(userInput))]
		newInput = x + replacement + y
	return newInput
	
#Main
central()









