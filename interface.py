#Program interface should have all these:
#1. tell the user what the program is and what is can do
#2. tell the user make choices or select option
#3. Let the user enter information -you should include a helpful message
#4. Display result or answer
#5. Let the user close the program

teamlist = []
choice = ' '
while choice != 'x':
    print("TEAM MANAGER")
    print("===============")
    print("This program will help you manage your team")
    print("/n")
    print("A: Append a value")
    print("B: Print the team list")
    print("X: Exit the program")
    choice = input("Enter your choice: ")
    if choice == "A":
    name = input("Enter a name: ")
    teamlist.append(name)
print(teamlist)