import turtle

a = turtle.Turtle()



while True:
    a.color("black")
    a.begin_fill()
    a.forward(260)
    a.right(90)
    a.right(250)
    a.forward(50)
    a.right(250)
    a.forward(50)

    a.color("black", "red")
    a.begin_fill()
    r1 = 36
    a.circle(r1)
    a.end_fill()

    a.color("black")
    a.left(-10)
    a.forward(20)
    a.left(60)
    a.forward(90)
    a.right(420)
    a.forward(50)

    a.color("black", "yellow")
    a.begin_fill()
    r2 = 80
    a.circle(r2)
    a.end_fill()

    a.color("black")
    a.right(360)
    a.forward(50)
    a.right(-60)
    a.forward(60)

    a.color("black", "green")
    a.begin_fill()
    a.right(90)
    a.forward(20)
    a.right(90)
    a.forward(80)
    a.right(-90)
    a.forward(20)
    a.right(-90)
    a.forward(180)
    a.right(-90)
    a.forward(20)
    a.right(-90)
    a.forward(80)
    a.right(90)
    a.forward(20)
    a.right(-90)
    a.forward(20)
    a.right(180)
    a.forward(20)
    a.right(-90)
    a.end_fill()



    a.color("black")
    a.right(90)
    a.forward(80)
    a.right(-40)
    a.forward(70)

    a.color("black", "gray")
    a.begin_fill()
    r3 = 50
    a.circle(r3)
    a.end_fill()

    a.right(-40)
    a.forward(70)
    a.right(-40)
    a.forward(40)
    a.right(-40)
    a.forward(40)
    a.right(-22)
    a.forward(80)

    a.color("black", "blue")
    a.begin_fill()
    a.right(90)
    a.forward(30)
    a.right(90)
    a.forward(60)
    a.right(-90)
    a.forward(20)
    a.right(-90)
    a.forward(180)
    a.right(-90)
    a.forward(20)
    a.right(-90)
    a.forward(60)
    a.right(90)
    a.forward(30)
    a.right(90)
    a.forward(-10)
    a.right(90)
    a.forward(30)
    a.right(90)
    a.forward(40)
    a.right(90)
    a.forward(30)
    a.right(-90)
    a.forward(60)
    a.end_fill()




    turtle.done()