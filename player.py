from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# turtle based object that moves forward based on player input
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.move_distance = MOVE_DISTANCE
        self.goto(0, -280)
        self.left(90)
        self.finish = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)
