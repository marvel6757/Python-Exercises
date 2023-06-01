#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
#from art import logo

#print(logo)
print("Welcome to the Number Guessing Game!!!\nI'm thinking of a number between 1 and 100")
#user choice of difficulty
difficulty=input('Choose a difficulty. Type "easy" or "hard": ')

#pick a random number
number=random.randint(1,100)

#setting up the level
if difficulty=='easy':
  level=10
elif difficulty=='hard':
  level=5
else:
  print("Sorry!! Invalid input.")

#while loop to count the attempts and guess the number
while level:
  print(f"You have {level} attempts to make a guess")
  guess=int(input("Make a guess: "))
  
  if guess==number:
    print(f"You got it!! The answer is {number}")
    break;
  elif guess>number:
    print("Too High")
  elif guess<number:
    print("Too Low")
    
  level-=1;
  if level:
    print("Guess again")

#if the player loses the game reveal the answer
if level==0:
  print(f"you lost the game!! The answer is {number}")
