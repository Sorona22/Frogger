from turtle import Turtle
from scoreboard import Scoreboard
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = .1


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        super().__init__()
        self.ht()
        self.penup()

        self.total = 0

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2)
            car.penup()
            car.left(180)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)


    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + self.total * MOVE_INCREMENT)

    def score(self):
        self.total += 1
