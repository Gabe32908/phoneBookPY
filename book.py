
from os import system
#this is the dictionary where all the numbers and names gets stored 
numbers = {}
#this is the display contact function that displays the contacts name and number
def display_contact():
#this prints "name" and 'and number' the "\t" is used to represent a tab space 
	print('name\t\tcontact number')
#this is the start of a for loop that retrives a key value from the dictionary using a get request and then displays that information using the .format method which formats the curly bracketss
	for key in numbers:
		print('{}\t\t{}'.format(key,numbers.get(key)))
#this while loop make sure that the program doesnt end unless the user wants it to 
while True: 
#this variable is where the user inputs what they want the program to accomplish 
	tod0= int(input("""welcome to the python phonebook.
  >>>> what would you like to do?<<<<
1. display your existising contacts
2. create a new contacts
3. edit an entry
4. delete an entry 
5. exit
enter here: """))
			#this if statement make sure the input the user puts in matches the result they want 
	if tod0 == 4: 
#Clears the screen 
		print('\n')
#the variable takes uer input so it can find the user within the dictionary 
		delete = input('enter contact name you would like to delete: ')
#this if statement says that if the name user is looking for which was inputed right above is in the dictionary numbers then go to the confrim variable
		if delete in numbers:
#this variable confrims that the user would like to delete the number 
			confirm = input('are you sure you want to delete this contact?(y/n)')
#this "if" statement says the if the user choses yes then to go to the next line 
		if confirm.lower() == 'y' or confirm.lower() == 'yes':
			system('clear')
#this line uses the ".pop" function to delete the number and name from the numbers dictionary. this is based on the user input from the delete variable which is why delete is in parathenses 
			del numbers[delete]
		else:
			print('contact not found')
#this calls to the display contact funtion which displays the users contacts 
			display_contact()
			#system('clear')
#this elif statment tells the program what to do when the user inputs 1 in the todo variable
	elif tod0 ==1:
#this if statement says that if there is nothing within the numbers dictionary then print the statement below
		if not numbers:
			system('clear')
			print('empty contact book')
			print('\n')
#this is saying that if there is or something else then display the contacts. this is done thru the display contact funtion.
		else:
			system('clear')
			display_contact()
			print('\n')
#this elif statment tells the program what to do when the user inputs 2 in the todo variable
	elif tod0 ==2: 
		print('\n')
#this variable named name asks the user whos name they will be saving
		name = input('whos number will you be saving: ')
#this variable named phone is asking the user what is the number of the person they are looking to save to their phonebook
		phone = input('what is '+name+'s number: ')
#this saves the their name and number to the dictionary and correlates them using the = phone 
		numbers[name] =phone
		system('clear')
##this elif statment tells the program what to do when the user inputs 3 in the todo variable
	elif tod0 == 3:
#this variable asks the user whos number they would like to edit
		print('\n')
		edit= input('enter user you would like to edit:')
#and this if statement checks if the name the user inputed is in the dictionary 
		if edit in numbers:
#this variable has the user input the user they are looking to edits new number in 
			number = input('enter new number: ')
#then this updates the list by completley replacing the name and number 
			numbers[edit] = number
#and this ensures to the user that the contact was updated sucesfully 
			system('clear')
			print('contact updated')
#then we once again call to this display contact function to display the contact
			print('\n')
			display_contact()
#then this says that if the name isnt found then to display that the name wasnt found
		else:
			print('\n')
			print('name was not found')
	if tod0 == 5:
		system('clear')
		print("hope to see you soon!!!!")
		exit()