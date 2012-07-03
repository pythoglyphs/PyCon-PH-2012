#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Waldemar Valdivia
#
# Created:     01/07/2012
# Copyright:   (c) Pythoglyphs 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

#print "Hello PyCon"
#a=1
#b=2
#print (a)
#a=10
#print (a)
#print (a+b)
#a="1"
#b="3"
#print (a+b)

#this is a comment

#print ("What is your name?")
#ame = raw_input()
#print ("Your name is " + name)

import turtle

turtle.penup()
turtle.goto(-70,50)
turtle.pensize(10)
turtle.right(90)

turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.backward(100)
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.pendown()
turtle.backward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.backward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.forward(50)

turtle.penup()

turtle.forward(25) # Space between letters

turtle.left(90)
turtle.forward(100)
turtle.pendown()
turtle.backward(100)
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.backward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.penup()


turtle.forward(25) # Space between letters

turtle.left(90)
turtle.forward(102)
turtle.left(90)
turtle.forward(90)
turtle.pencolor("#FF0000")

turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.pencolor("#0000FF")
turtle.pendown()
turtle.circle(120)


turtle.exitonclick()
