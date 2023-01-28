from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) - 1]
        self.up = 90
        self.down = 270
        self.left = 180
        self.right = 0
        self.forward = 10

    def create_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in self.starting_positions:
            self.create_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position_x = self.segments[seg_num - 1].xcor()
            new_position_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_position_x, y=new_position_y)
        self.head.forward(self.forward)

    def move_up(self):
        if self.head.heading() != self.down:
            self.head.setheading(self.up)

    def move_down(self):
        if self.head.heading() != self.up:
            self.head.setheading(self.down)

    def move_left(self):
        if self.head.heading() != self.right:
            self.head.setheading(self.left)

    def move_right(self):
        if self.head.heading() != self.left:
            self.head.setheading(self.right)

    def grow_snake(self):
        self.create_segment((self.tail.xcor(), self.tail.ycor()))
