import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=700, height=400)
guess = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race?Enter the color:: ")
print(guess)
screen.listen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-330, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if guess:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 340:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == guess:
                print("You won the bet")
            else:
                print(f"you lost the bet. The winner is {winning_color}")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
