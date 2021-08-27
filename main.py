import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    for car in car_manager.all_cars:
        car_manager.move()
    car_manager.make_car()

    # check if player has passed boundary condition
    if player.finish < player.ycor():
        scoreboard.score()
        car_manager.score()
        player.goto(0, -280)

    # check if player has collided with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.lose()
            game_is_on = False

screen.exitonclick()
