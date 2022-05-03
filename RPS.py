from random import choice
objects = ["rock", "paper", "scissors"]
computer = choice(objects)
rps = input("What will you choose? Rock, Papper, or Scissors?").lower().strip()
if rps == computer:
    print("It is a tie! :p")
if rps == ("rock"):
    if computer == ("scissors"):
        print("Yay! you won! :)")
if rps == ("papper"):
    if computer == ("rock"):
        print("Yay! you won! :)")
if rps == ("scissors"):
    if computer == ("papper"):
        print("Yay! you won! :)")
if computer == ("scissors"):
    if rps == ("papper"):
        print("Nooo! you lost :(")
if computer == ("rock"):
    if rps == ("cissors"):
        print("Nooo! you lost :(")
if computer == ("papper"):
    if rps == ("rock"):
        print("Nooo! you lost :(")
