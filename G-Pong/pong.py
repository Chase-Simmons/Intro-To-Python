import turtle 

win = turtle.Screen();
win.title("Pong by @Chase")
win.bgcolor(0, 0, 0)
win.setup(width=800, height=600)
win.tracer(0)

# Main Game Loop

while True:
    win.update()