#Game Higher-Lower

#get the data and art from the other files'
import random
from art import logo,vs
from replit import clear
from game_data import data

score=0
game=True

#function to assign random data for A and B
def select_data(data):
  return random.choice(data)
  
#assigning data for A and B
A=select_data(data)
B=select_data(data)

#write a function to print both the values of A and B
def printing_values(A,B):
  print(f"Compare A: {A['name']}, a { A['description']}, from {A['country']}")
  print(vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

#write a function now to compare those values
def compare(a,b):
  if a>b:
    return 'A'
  else:
    return 'B'
    
#function to get new data for next rounds    
def exchange_data(B):
    return B,select_data(data)

#loop to continue running the game
while game: 
  print(logo)
  if score!=0:
    print(f"You're right! Current score: {score}.")
  printing_values(A,B)
  guess=input("Who has more followers?? Type 'A' or 'B':: ")
  X=compare(A['follower_count'],B['follower_count'])
  
  #If statement to check to check the guess is right or wrong and challenge with new data  
  if X==guess:
    score+=1
    A,B=exchange_data(B)
    clear()
  else:
  #end the game if player got it wrong and display the score
    game=False
    clear()
    print(f"Sorry thats wrong!! The final score is {score}")


