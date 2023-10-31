import turtle


class Button(turtle.Turtle):
    def __init__(self):
        super().__init__()
        window = turtle.Screen()
        window.addshape('button.gif')
        self.shape('button.gif')
