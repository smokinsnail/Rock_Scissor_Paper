#Kelly Mackey 18/08/2021

player_1_turn = ""
player_2_turn = ""

welcome_message = "Welcome to Rock, Scissor, Paper!!!!"
print(welcome_message)
print("player 1 enter your choice (rock, paper or scissors)")
player_1_turn = input()
print("************************************\n" * 50)
print("player 2 enter your choice (rock, paper or scissors)")
player_2_turn = input()

if (player_1_turn == "rock" or player_1_turn == "paper" or player_1_turn == "scissors") and (player_2_turn == "rock" or player_2_turn == "paper" or player_2_turn == "scissors"):
	
  if (player_1_turn == "rock" and player_2_turn == "scissors") or (player_1_turn == "scissors" and player_2_turn == "paper") or (player_1_turn == "paper" and player_2_turn == "rock"):
	  print("Player 1 WINS!!!")
  elif player_1_turn == player_2_turn:
	  print("It's a draw!")
  else:
      print("Player 2 WINS!!!")
else:
	print("Something went wrong!")
	

print(" GAME OVER ")