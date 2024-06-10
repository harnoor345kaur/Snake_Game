from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]
        list_cor = [(0, 0), (-20, 0), (-40, 0)]

    def create_snake(self):
        i = 0
        for j in range(3):
            tim = Turtle()
            tim.color("white")
            tim.pencolor("black")
            tim.shape("square")
            tim.setpos(i, 0)
            self.all_turtle.append(tim)
            i -= 20

    def add_segment(self, position):
        new_tim = Turtle()
        new_tim.color("white")
        new_tim.pencolor("black")
        new_tim.shape("square")
        new_tim.setpos(position)
        self.all_turtle.append(new_tim)

    def extend(self):
        self.add_segment((self.all_turtle[-1].xcor()-20,self.all_turtle[-1].ycor()-20))

    def move(self):
        for num in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[num - 1].xcor()
            new_y = self.all_turtle[num - 1].ycor()
            self.all_turtle[num].setpos(new_x, new_y)
        self.all_turtle[0].forward(20)

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


