#Done by: Yousif aljabri, Khaled Khader , Sama Nimer , Bachar Altajer

import turtle

turtle.color("Black")
turtle.fillcolor("White")
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
x=-315
y=315
# Global Variables

def reposition(x1,y1,headingV):
    turtle.penup()
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.setheading(headingV)
# Function for deciding positions along with heading

def singlePixel(colors1):
    turtle.fillcolor(colors1)
    turtle.begin_fill()
    for i in range(4):    
        turtle.forward(PIXEL_SIZE)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)
# Function used for drawing and filling the color of the pixel.

def pixelColoring(pixelMultiColors):
    for inputColor in pixelMultiColors:
        if (inputColor=="0"):
                singlePixel("black")
        elif (inputColor=="1"):
                singlePixel("white")
        elif (inputColor=="2"):
                singlePixel("red")
        elif (inputColor=="3"):
                singlePixel("yellow")
        elif (inputColor=="4"):
                singlePixel("orange")
        elif (inputColor=="5"):
                singlePixel("green")
        elif (inputColor=="6"):
                singlePixel("yellowgreen")
        elif (inputColor=="7"):
                singlePixel("sienna")
        elif (inputColor=="8"):
                singlePixel("tan")
        elif (inputColor=="9"):
                singlePixel("gray")
        elif (inputColor=="A"):
                singlePixel("darkgray")
        else:
            return False
#Function to allign each character given by pixart() function with its color

def pixart():
    reposition(x,y,0)
    chosenFile=input("Enter the absolute path of the file you want to draw: ")
    with open(chosenFile) as currentFile:
        for line in currentFile:
            for i in line:
                pixelColoring(i)
            reposition(x,turtle.ycor()-PIXEL_SIZE,0)
#function to repoisition and take out data from the file given by the user

def main():
    turtle.tracer(False)
    pixart()
    turtle.tracer(True)

main()
turtle.exitonclick()
