import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
screen.tracer(0)

x_time = 0.09

turtle = Player()

car = CarManager()

screen.listen()
screen.onkeypress(turtle.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(x_time)
    screen.update()
    car.create_car()
    car.car_move()

    for carro in car.car_list:
        if carro.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() > 270:
        turtle.reset_pos()
        scoreboard.increase_score()
        scoreboard.write_score()
        car.car_speedup()


screen.exitonclick()
