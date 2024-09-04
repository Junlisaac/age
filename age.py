ans = input("Do you have a driving lisense?(Y/N): ")

if ans.upper() == "Y":
	age = int(input("What is your age now? "))

	if age >= 0 and age < 18:
		print("Why you can drive???")
	elif age >= 18:
		print("Enjoy your driving!")
	else:
		print("You may enter a wrong age!")

elif ans.upper() == "N":
	age = int(input("What is your age now? "))

	if age >= 18:
		print("You can get a driving lisense.")
	elif age >=0 and age < 18:
		print("You are still young.")
	else:
		print("You may enter a wrong age!")
else:
	print("You enter a wrong answer!")