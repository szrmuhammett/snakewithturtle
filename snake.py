from turtle import Turtle
STARTING_POSITIONS = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.color("black")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
      if self.head.heading() != DOWN:
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
          self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
          self.head.setheading(LEFT)



