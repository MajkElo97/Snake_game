from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()
screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.100)
    scoreboard.write_score()
    snake.move()

    if food.food_collision(snake.segments):
        snake.add_segment()
        scoreboard.add_score()
        food.generate_food()

    if snake.wall_collision() or snake.self_collision():
        # game_is_on = False
        # scoreboard.write_game_over()
        scoreboard.reset()
        snake.reset()
        time.sleep(2)
        # screen.clear()
screen.exitonclick()
