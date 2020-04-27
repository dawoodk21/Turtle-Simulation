# The purpose of this program is to simulate the situation of a gas leak
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
#square 3- at 230, 70
    turtle.color('red')
    turtle.forward(300)
    turtle.color('red')
    turtle.penup()
    turtle.goto(230,70)
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
    
    '''
#square 3
    turtle.color('red')
    turtle.forward(300)
    turtle.left(90)
    turtle.color('green')
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
'''
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
    turtle.goto(215,75)
    turtle.pendown()
    turtle.write('2', font=style, align='center')
    turtle.hideturtle()

    turtle.penup()
    turtle.color('black')
    style = ('Courier', 30, 'italic')
    turtle.goto(285,270)
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


#triangle- to show gas contaminated area
    turtle.penup()
    turtle.goto(300,300)
    turtle.pendown()
    turtle.color('red')
    turtle.right(70)
    turtle.forward(120)
    turtle.left(120)
    turtle.forward(150)
#circle- representing oil worker
    turtle.penup()
    turtle.goto(270,220)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('blue')
    turtle.circle(10,360)
    turtle.end_fill()
    turtle.right(75)
    turtle.forward(155)
#blue circle 2- the oil worker in the safe zone
    turtle.begin_fill()
    turtle.color('blue')
    turtle.circle(10,360)
    turtle.end_fill()

    
    '''
    for i in range(5):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
        turtle.goto(235,75)
    '''
main()
    

































































    
















