import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle('square')
            
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.goto(300, random.randint(-250,250))
            
            # new_car.setheading(180) because car going backward and not forward

            self.all_cars.append(new_car)

    def car_speedup(self):
        self.car_speed += MOVE_INCREMENT