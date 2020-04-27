# The purpose of this program is to simulate the situation of a gas leak
#scenario 2
def main():
    import turtle
#square 1- big square
    
    turtle.speed('fastest')
    turtle.color('red')
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)

#square 2- left corner small square
    
    turtle.begin_fill()
    turtle.color('green')
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.end_fill()
#square 3- at 220, 120
    turtle.color('red')
    turtle.forward(300)
    turtle.color('red')
    turtle.penup()
    turtle.goto(220,120)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('green')
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()
# square 4- upper right corner at 300,300
    turtle.penup()
    turtle.goto(300,300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('green')
    turtle.left(180)
    turtle.color('red')
    turtle.forward(30)
    turtle.left(90)
    turtle.color('green')
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()

#square 5
    turtle.left(90)
    turtle.color('red')
    turtle.forward(300)
    turtle.left(90)
    turtle.color('red')
    turtle.forward(30)
    turtle.left(90)
    turtle.begin_fill()
    turtle.color('green')
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()

#number safety zones
    turtle.penup()
    turtle.color('black')
    style = ('Courier', 30, 'italic')
    turtle.goto(15,5)
    turtle.pendown()
    turtle.write('1', font=style, align='center')
    turtle.hideturtle()

    turtle.penup()
    turtle.color('black')
    style = ('Courier', 30, 'italic')
    turtle.goto(220,120)
    turtle.pendown()
    turtle.write('2', font=style, align='center')
    turtle.hideturtle()

    turtle.penup()
    turtle.color('black')
    style = ('Courier', 30, 'italic')
    turtle.goto(265,275)
    turtle.pendown()
    turtle.write('3', font=style, align='center')
    turtle.hideturtle()

    turtle.penup()
    turtle.color('black')
    style = ('Courier', 30, 'italic')
    turtle.goto(10,275)
    turtle.pendown()
    turtle.write('4', font=style, align='center')
    turtle.hideturtle()
    
#circle 1- representing oil worker 1
    turtle.penup()
    turtle.goto(270,220)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('brown')
    turtle.circle(10,360)
    turtle.end_fill()    
#circle 2- oil worker 2
    turtle.penup()
    turtle.goto(200,40)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('orange')
    turtle.circle(10,360)
    turtle.end_fill()
#blue circle 3- oil worker 3
    turtle.penup()
    turtle.goto(60,180)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('purple')
    turtle.circle(10,360)
    turtle.end_fill()
#blue circle 4- oil worker 4
    turtle.penup()
    turtle.goto(100,220)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('blue')
    turtle.circle(10,360)
    turtle.end_fill()
#blue circle 5- oil worker 5
    turtle.penup()
    turtle.goto(90,280)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(10,360)
    turtle.end_fill()
#contaminated area triangle
    turtle.penup()
    turtle.goto(0,300)
    turtle.pendown()
    turtle.color('red')
    turtle.left(50)
    turtle.forward(135)
    turtle.left(90)
    turtle.forward(113)
#worker 5 to to safety zone 4(top right corner)
    turtle.penup()
    turtle.goto(90,280)
    turtle.pendown()
    turtle.color('black')
    turtle.right(50)
    turtle.forward(195)
#worker 5 in safety zone
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(10,360)
    turtle.end_fill()
#worker 4 to safety zone 3 (bottom right)
    turtle.penup()
    turtle.goto(100,220)
    turtle.pendown()
    turtle.color('blue')
    turtle.right(45)
    turtle.forward(130)
#worker 4 in safety zone 3
    turtle.begin_fill()
    turtle.color('blue')
    turtle.circle(10,360)
    turtle.end_fill()


main()



























































    
