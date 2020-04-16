import turtle
import random

wn = turtle.Screen()


num = ["turtle1", "turtle2", "turtle3", "turtle4", "turtle5", "turtle6"]

for x in range(0,len(num)):
    exec(f"{num[x]} = turtle.Turtle()")

line = turtle.Turtle()
wn.title("turtle race")
line.hideturtle()
line.up()
line.speed(0)
line.shape("arrow")
line.goto(250,300)
line.color("black")
line.down()
line.right(180)
line.forward(600)

color = ["green","blue","purple","gold","yellow","red"]

for x  in range(1,7):
    exec("turtle{}.shape(\"turtle\")".format(x))
    exec("turtle{}.up()".format(x))
    i=x-1
    exec("turtle{}.color(\"{}\")".format(x, color[i]))

ycor = [-200,-150,-100,-50,0,50]

for x in range(1,7):
    y = x-1
    exec("turtle{}.goto({},-150)".format(x, ycor[y]))
    exec ("turtle{}.left(90)".format(x))
    exec ("turtle{}.down()".format(x))


input("Ready?\n")
print("GO!!!")

while True:

    num = ["turtle1", "turtle2", "turtle3", "turtle4", "turtle5", "turtle6"]
    numr = random.choice(num)
    exec("yax= {}.ycor()".format(numr))
    if yax == 290:
        line2 = turtle.Turtle()
        line2.hideturtle()
        line2.speed(0)
        line2.up()
        line2.width(140)
        line2.goto(-150, 300)
        line2.down()
        write = f"{numr} won the race"
        line2.write(write)
        break

    else:
        exec("{}.forward(2)".format(numr))


wn.mainloop()
