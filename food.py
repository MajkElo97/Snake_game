from random import choice
from turtle import Turtle


class Food:
    def __init__(self):
        self.food_positions = []
        for f in range(-280, 280, 20):
            self.food_positions.append(f)

        self.food = Turtle(shape="circle")
        self.food.color("red")
        self.food.penup()
        self.generate_food()

    def generate_food(self):
        self.food.goto(x=choice(self.food_positions), y=choice(self.food_positions))

    def food_collision(self, segments):
        if segments[0].distance(self.food) <= 19:
            return True
        else:
            return False