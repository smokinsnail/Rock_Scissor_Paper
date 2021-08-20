#Kelly Mackey 18/08/2021

from random import choice


player_1_turn = ""
computer_turn = choice(["rock", "scissors", "paper"])
play_again = "y"


while play_again.lower() == "y":

	welcome_message = "Welcome to Rock, Scissor, Paper!!!!"
	print(welcome_message)
	print("player 1 enter your choice (rock, paper or scissors)")
	player_1_turn = input()

	print("Your choice is" + player_1_turn.lower())
	print("Computer choice: " + computer_turn)


	if (player_1_turn == "rock" or player_1_turn == "paper" or player_1_turn == "scissors") and (computer_turn == "rock" or computer_turn == "paper" or computer_turn == "scissors"):
		
	  if (player_1_turn == "rock" and computer_turn == "scissors") or (player_1_turn == "scissors" and computer_turn == "paper") or (player_1_turn == "paper" and computer_turn == "rock"):
		  print("Player 1 WINS!!!")
		  
		  
	  elif player_1_turn == computer_turn:
		  print("It's a draw!")
	  else:
	      print("Computer WINS!!!")
	else:
		print("Something went wrong!")
	print("Do you want to play again?")	
	play_again = input()

print(" GAME OVER, Thanks for playing! ")