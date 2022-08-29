import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)

line_turtle = Turtle()
turtle_1 = Turtle(shape='turtle')
turtle_2 = Turtle(shape='turtle')
turtle_3 = Turtle(shape='turtle')
turtle_4 = Turtle(shape='turtle')
turtle_5 = Turtle(shape='turtle')

for turtle in screen.turtles():
    turtle.speed(4)
    turtle.penup()

line_turtle.hideturtle()
turtle_1.color('purple')
turtle_2.color('red')
turtle_3.color('blue')
turtle_4.color('green')
turtle_5.color('orange')

for i in range(0, 360, 60):
    line_turtle.speed(0)
    line_turtle.goto(-300, 150 - i)
    line_turtle.pendown()
    line_turtle.forward(600)
    line_turtle.penup()

line_turtle.goto(-270, 150)
line_turtle.pendown()
line_turtle.goto(-270, -150)
line_turtle.penup()


turtle_1.goto(-290, 120)
turtle_2.goto(-290, 60)
turtle_3.goto(-290, 0)
turtle_4.goto(-290, -60)
turtle_5.goto(-290, -120)

user_bet = screen.textinput("Make Your Bet", "Which turtle will win the race? Enter a color:")
bet_amount = screen.numinput("Make Your Bet", "If you win, you will double the money! How much do you want to bet:")

race = True
while race:
    for turtle in screen.turtles():
        turtle.forward(random.randint(0, 1) * 10)
        if turtle.pos()[0] == 280:
            winner_color = turtle.color()[0]
            race = False

if winner_color == user_bet:
    print(f"Congratulations! The winner is {winner_color} turtle.\nYou win {int(bet_amount * 2)}$ :)")
else:
    print(f"You Lose! The winner is {winner_color} turtle.\nYou lose {int(bet_amount)}$ :(")

screen.exitonclick()
