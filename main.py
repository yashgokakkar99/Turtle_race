from turtle import Turtle,Screen
import random

screen = Screen()
# By using screen.setup() here, we are specifying the height and width of screen.
screen.setup(width = 500, height = 400)

# declaring some important variables, lists, etc
is_race_on = False
turtle_pos = [-70,-40,-10,20,50,80]
colors = ["red","orange","purple","yellow","green","blue"]
all_turtles = []

# by using screen.textinput() we are taking user input which will be prompted on screen whe program will start executing.
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color : ")

# for loop to manage 6 turtles with different colors and character.
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y = turtle_pos[i]) # Understand the turtle graphics co-ordinate system and then give co-ordinates accordingly.
    all_turtles.append(new_turtle)

# if user is giving any input in bet then only race will start
if user_bet:
    is_race_on = True

# while loop for managing race and getting the winner
while(is_race_on):
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Hurray !! you won the bet, the turtle with {winning_color} color won the race.")
            else:
                print(f"Hard luck !!, bet better next time, {winning_color} color turtle won the race.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()

