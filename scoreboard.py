from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL = (-250, 250)

# scoreboard class that draws a level onto the screen and increments it each time a boundary is past


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.pencolor("black")
        self.ht()
        self.goto(LEVEL)
        self.total = 0
        self.write("Level: 1", font=FONT)

    def score(self):
        self.goto(LEVEL)
        self.total += 1
        self.clear()
        self.write(f"Level: {self.total+1}", font=FONT)

    def lose(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT)