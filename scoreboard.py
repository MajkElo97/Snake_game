from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.score = 0
        with open(file="data.txt") as file:
            self.high_score = int(file.read())
        self.turtle = Turtle()
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(x=0, y=280)
        self.turtle.clear()

    def add_score(self):
        self.score += 1

    def write_score(self):
        self.turtle.goto(x=-100, y=280)
        self.turtle.clear()
        self.turtle.write(f"Score = {self.score}", align="center", font=('Arial', 12, 'normal'))
        self.turtle.goto(x=100, y=280)
        self.turtle.write(f"Highest score = {self.high_score}", align="center", font=('Arial', 12, 'normal'))

    # def write_game_over(self):
    #     self.turtle.goto(x=0, y=0)
    #     self.turtle.write("Game over", align="center",font=('Arial', 36, 'bold'))
    #     self.turtle.goto(x=0, y=-100)
    #     self.turtle.write("Press 'Space' to start again", align="center", font=('Arial', 12, 'bold'))
    #     self.turtle.goto(x=0, y=280)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()
    #     self.turtle.goto(x=0, y=0)
    #     self.turtle.write("Game over", align="center",font=('Arial', 36, 'bold'))
    #     self.turtle.goto(x=0, y=-100)