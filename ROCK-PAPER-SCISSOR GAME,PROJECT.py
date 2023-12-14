import random
print("-----------------------------------------------------------")
print("                        HI THERE!!!                                ")
print("                 My name is PrincessPixel 👩 \n                          ")
print("            LETS'PLAY ROCK-PAPER-SCISSOR GAME!!!                  \n")
print('👩- Winning rules of the game ROCK-PAPER-SCISSORS are :\n')
print("...........................................................")
print(".              Rock vs Paper -> Paper wins                .")
print(".             Rock vs Scissors -> Rock wins               .")
print(".           Paper vs Scissors -> Scissor wins             .")
print("...........................................................\n")
print("-----------------------------------------------------------")
while True:
	
	print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
	
	choice=int(input("                 👩- Enter your choice.... \n-----------------------------------------------------------\n"))
	while choice > 3 or choice <1:
         choice=int(input('Enter a valid choice please '))#re enter correct value
	if choice == 1:
		choice_name= 'ROCK'
	elif choice == 2:
		choice_name= 'PAPER'
	else:
		choice_name= 'SCISSOR'
	print('User choice is -',choice_name,"\n-----------------------------------------------------------")#user input
	print("             \nNow its PrincessPixel's Turn....\n ")
	comp_choice = random.randint(1,3)
	while comp_choice == choice:
		comp_choice = random.randint(1,3)
	if comp_choice == 1:
		comp_choice_name = 'ROCK'
	elif comp_choice == 2:
		comp_choice_name = 'PAPER'
	else:
		comp_choice_name = 'SCISSOR'
	print("👩 -", comp_choice_name,"\n-----------------------------------------------------------")#computer turn
	print("                      ",choice_name,'VS',comp_choice_name)
	if choice == comp_choice:
		print('Its a Draw',end="")#draw game
	if (choice==1 and comp_choice==2):
		print('Paper wins =>',end="")
		result='Paper'
	elif (choice==2 and comp_choice==1):
		print('Paper wins =>',end="")
	if (choice==1 and comp_choice==3):
		print('Rock wins =>\n',end= "")
		result='Rock'
	elif (choice==3 and comp_choice==1):
		print('Rock wins =>\n',end= "")
	if (choice==2 and comp_choice==3):
		print('Scissors wins =>',end="")
		result='Scissor'
	elif (choice==3 and comp_choice==2):
		print('Scissors wins =>',end="")
		result='Rock'
	if result == 'DRAW':
		print("<== Its a tie ==>")
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== 👩 wins ==>")
	print("-----------------------------------------------------------\nDo you want to play again?\n \n(PRESS ANY KEY FOR YES AND 'N' FOR NO)")
	ans = input().lower()
	if ans =="n":
		break
print("                      Thanks for playing🥰.... \n                                BYE👩🤚\n-----------------------------------------------------------")
print('Developed by: ROHAN JACOBS.')
