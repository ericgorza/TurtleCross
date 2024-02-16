from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_Y = random.randint(-250,251)


class CarManager(Turtle):

    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color("black")
            random_y = random.randint(-250, 251)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.goto(290, random_y)
            self.car_list.append(new_car)


    def car_move(self):
        for car in self.car_list:
            car.forward(self.speed)

    def car_speedup(self):
        self.speed += MOVE_INCREMENT

    def clear_car(self):
        if self.xcor() < -290:
            self.clear()
            self.goto(290, RANDOM_Y)
            self.color(random.choice(COLORS))