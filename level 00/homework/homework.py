from turtle import*

speed(30)
width(4)

#square 
color("black")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#door
begin_fill()
forward(70)
color("gray")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200,200)
pendown()
color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#left window
left(30)
color("black")
begin_fill()
forward(30)
color("skyblue")
left(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()

#right window
penup()
goto(200,170)
pendown()
begin_fill()
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()

exitonclick()