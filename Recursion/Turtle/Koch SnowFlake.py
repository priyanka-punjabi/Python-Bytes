import turtle

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400


def init():
    turtle.setworldcoordinates(-WINDOW_WIDTH / 1, -WINDOW_HEIGHT / 1,
                               WINDOW_WIDTH / 1, WINDOW_HEIGHT / 1)
    turtle.up()
    turtle.setheading(0)
    turtle.speed(0)
    turtle.title('Snow Flake')


def snowflak_rec(n):
    if n == 0:
        return
    turtle.down()
    for _ in range(3):
        for i in range(3):
            turtle.forward(30)
            turtle.right(120)
            turtle.forward(30)
            turtle.left(60)
        for _ in range(2):
            turtle.forward(30)
            turtle.left(60)

    for _ in range(2):
        turtle.forward(30)
        turtle.right(120)
        for _ in range(3):
            turtle.forward(30)
            turtle.left(60)

    snowflak_rec(n - 1)

    turtle.up()


def main():
    init()
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(100)
    snowflak_rec(6)
    turtle.mainloop()


if __name__ == '__main__':
    main()
