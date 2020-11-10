from turtle import Turtle, Screen
import random as rand

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("lightgreen")
winner = "none"


class Racer:
    def __init__(self):
        self.id = Turtle()
        self.id.shape("turtle")
        self.name = "none"
        self.id.penup()
        self.id.color("black")

    def turtle_run(self):
        self.id.forward(rand.randint(2,8))
        if self.id.xcor() == 200:
            winner = self.name

            return winner


def create_racer(color, lane):
    new_racer = Racer()
    new_racer.id.color(color)
    new_racer.id.setpos(-200, lane)
    new_racer.name = color

    return new_racer


lanes = [-150, -100, -50, 0, 50, 100, 150]
colors = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]
user_choice = screen.textinput("Make your Choice", f"Choose a color. ({colors})").lower()
racers = []
for i in range(7):
    racers.append(create_racer(colors[i], lanes[i]))

while winner == "none":

    for racer in range(7):
        if racers[racer].id.xcor() >= 200:
            winner = racers[racer].name
        racers[racer].turtle_run()


if winner == user_choice:
    print(f"Congratulations, your {user_choice} turtle has won!")
else:
    print(f"Too bad, the {winner} turtle beat your {user_choice} turtle.")

screen.mainloop()
