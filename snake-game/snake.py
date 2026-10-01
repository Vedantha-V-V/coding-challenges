from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            


    def add_segment(self,position):
        segment=Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):  
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[i-1].forward(20)

    def up(self):
        headed=self.head.heading()
        if headed == 0.0 or headed == 180:
            self.head.setheading(90)

    def down(self):
        headed=self.head.heading()
        if headed == 0.0 or headed == 180:
            self.head.setheading(270)

    def left(self):
        headed=self.head.heading()
        if headed == 270:
            self.head.setheading(headed-90)
        else:
            self.head.setheading(headed+90)

    def right(self):
        headed=self.head.heading()
        if headed == 270:
            self.head.setheading(headed+90)
        else:
            self.head.setheading(headed-90)