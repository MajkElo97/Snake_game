from turtle import Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.last_seg_x = 0
        self.last_seg_y = 0

    def create_snake(self):
        for k in range(3):
            self.segments.append(Turtle(shape="square"))
            self.segments[k].color("white")
            self.segments[k].penup()
            self.segments[k].goto(x=k * (-20), y=0)

    def move(self):
        self.last_seg_x = self.segments[len(self.segments) - 1].xcor()
        self.last_seg_y = self.segments[len(self.segments) - 1].ycor()
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)
        return

    def turn_left(self):
        self.segments[0].left(90)

    def turn_right(self):
        self.segments[0].right(90)

    def wall_collision(self):
        if self.segments[0].xcor() >= (SCREEN_WIDTH / 2) - 5 or self.segments[0].xcor() <= (-SCREEN_WIDTH / 2) + 5 or \
                self.segments[0].ycor() >= (SCREEN_HEIGHT / 2) - 5 or self.segments[0].ycor() <= (
                -SCREEN_HEIGHT / 2) + 5:
            return True
        else:
            return False

    def self_collision(self):
        if len(self.segments) >= 4:
            for seg in range(3, len(self.segments)):
                if self.segments[0].distance(self.segments[seg]) <= 19:
                    return True
            return False
        else:
            return False

    def add_segment(self):
        self.segments.append(Turtle(shape="square"))
        self.segments[-1].color("white")
        self.segments[-1].penup()
        self.segments[-1].goto(x=self.last_seg_x, y=self.last_seg_y)

    def reset(self):
        for seg in self.segments:
            seg.goto(800, 800)
        self.segments.clear()
        self.__init__()
