player_one = input("Player one choose between 'ROCK', 'PAPER','SCISSOR': ").lower()
player_two = input("Player two choose between 'ROCK', 'PAPER','SCISSORS': ").lower()

game = ("rock","paper","scissors")
if (player_one not in game or player_two not in game):
      print("INVALID OPTION!!")

elif (player_one == player_two):
     print("It's a tie")

if (player_one == "rock" and player_two == "scissors"):
     print("Hurray Player One wins")

if (player_one == "rock" and player_two == "paper"):
     print("Hurray Player Two wins")

if (player_one == "paper" and player_two == "scissors"):
     print("Hurray Player Two wins")

if (player_one == "paper" and player_two == "rock"):
     print("Hurray Player One wins")

if (player_one == "scissors" and player_two == "rock"):
     print("Hurray Player Two wins")

if (player_one == "scissors" and player_two == "paper"):
     print("Hurray Player One wins")

    
