# Project 6 - Image Art
# CS 111, Reckinger
# Iancarlo Trejo

import turtle
import image

"""Opens the file and gets the width and height of the image"""
filename = "Galaxy.gif" 
img = image.FileImage(filename)
width = img.get_width() 
height = img.get_height()
print("Image Width: " + str(width))
print("Image Height: " + str(height))

"""Turtle Settings"""
t = turtle.Turtle()
s = turtle.getscreen()
s.colormode(255) 
t.penup()
t.hideturtle()
s.tracer(0)

"""Drawing the image"""
for row in range(0, height, 3):
  for col in range(0, width, 3):
    p = img.get_pixel(col, row) # get pixel from image
    r, g, b = p.red, p.green, p.blue   
    x = col - width / 2 # x coordinate of the center of the image 
    y = height / 2 - row # -300 is to make the image look right
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(r, g, b) 
    for i in range(4): 
     t.forward(10)
     t.right(90)
    t.end_fill()
    t.penup()
  
turtle.mainloop()