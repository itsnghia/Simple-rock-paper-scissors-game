import random

while True:
  choices = ("rock", "paper", "scissors")

  computer = random.choice(choices)
  player = None

  while player not in choices:
    player = input("Decide to choose rock, paper or scisscors:? ").strip().lower()
      
  if player == computer:
    print("player: " + player)
    print("computer: " + computer)
    print("It's a tie")
  elif (player == "rock"):
    print("player: " + player)
    print("computer: " + computer)
    if (computer == "paper"):
      print("computer wins")
    elif (computer == "scissors"):
      print("player wins")
  elif (player =="paper"):
    print("player: " + player)
    print("computer: " + computer)
    if (computer == "rock"):
      print("player wins")
    elif (computer == "scissors"):
      print("computer wins")
  elif (player == "scissors"):
    print("player: " + player)
    print("computer: " + computer)
    if (computer == "paper"):
      print("player wins")
    elif (computer == "rock"):
      print("computer wins")

  play_again = input("Do you want to play again? (yes,no) ").strip().lower()
  if play_again != "yes":
    break  
print("Bye!")