#Name
#Period
MENU = '''
\t\t\t ____
\t\t\t|Menu|
\t\t0 - Quit
\t\t1 - View Attributes and Pool
\t\t2 - Add to Attribute
\t\t3 - Remove from Attribute'''
atts = {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Wisdom": 0, "Intelligence": 0, "Charisma": 0, "Pool": 72}

def main():
	print(MENU)
	choice = input("What's your choice?\n")
	while choice != "0":
		if choice == "1":
			print(table(atts))
		elif choice == "2":
			attribute = input("What attribute would you like to add points to?\n").capitalize()
			amount = int(input("How many points would you like to add?\n"))
			print(add(attribute, amount, atts))
		elif choice == "3":
			attribute = input("What attribute would you like to remove points from?\n").capitalize()
			amount = int(input("How many points would you like to remove?\n"))
			print(table(atts))
			print(remove(attribute, amount, attss))
			#message, atts = (remove(attribute, amount, atts))
			#print(message)
		else:
			print(f"'{choice}' is not a valid menu option.")
		print(MENU)
		choice = input("What's your choice?\n")
	else:
		print("Goodbye.")
def table(atts):
	return(f'''
______________________________
Strength    |	{atts["Strength"]}
Dexterity   |	{atts["Dexterity"]}
Constitution|	{atts["Constitution"]}
Wisdom      |	{atts["Wisdom"]}
Intelligence|	{atts["Intelligence"]}
Charisma    |	{atts["Charisma"]}
Pool        |	{atts["Pool"]}
______________________________''')
def add(attribute, amount, atts):
	if attribute in atts:
		if (amount) <= (atts["Pool"]):
			atts["Pool"] -= amount
			atts[attribute] += amount
			return (f"{amount} added to {attribute}")
		else:
			return (f"{amount} is more points than you have left in your pool")
	else:
		return (f"'{attribute}' is not a valid attribute")
def remove(attribute, amount, atts):
	if attribute in atts:
		if (amount) <= atts[attribute]:
			atts[attribute] -= amount
			atts["Pool"] += amount
			return (f"{amount} removed from {attribute}")
		else:
			return (f"{amount} is more points than you have left in {attribute}")
	else:
		 return (f"'{attribute}' is not a valid attribute")

#elif choice is 0 than say "Goodbye"
#elif choice is not given numbers
#print choice is not a valid menu option.

#keep this at the bottom of your program
if __name__ == "__main__":
	main()
