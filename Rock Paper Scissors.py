#Brendan Li
#Rock Paper Scissors game; Nice and easy start to Python Programming

#necessary Libraries
import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
#Infinite game loop
loop=False
while (loop==False):
          #Get User Input for game  
          print("\n")
          RPS = input("What is your choice???? [R]ock, [P]aper, or [S]cissors: ")
          print("Rock, Paper, Scissors.....SHOOT!")
          
          #If the input isn't an option
          if not re.match("[SsRrPp]", RPS):
              print("SORRY, that's not a choice. Please choose one of the following: ")
              print("[R]ock, [P]aper or [S]cissors. ")
              continue
          print("You threw: " + RPS)

          #randomized opponent choice...
          choices = ['R', 'P', 'S']
          bot = random.choice(choices)

          #Who won????
          if bot == str.upper(RPS):
              print("Dang, that was a TIE!")
          elif bot == 'R' and RPS.upper() == 'S':
              print("I threw Rock, so you LOSE!")
              continue
          elif bot == 'S' and RPS.upper() == 'P':
              print("I threw Scissors, so you LOSE!")
              continue
          elif bot == 'P' and RPS.upper() == 'R':
              print("I threw paper, so you LOSE!")
              continue
          else:
              print("you WIN!")

          print("Let's keep playing...")  
