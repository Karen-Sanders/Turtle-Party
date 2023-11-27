#Joy of Coding 5 Day Python Challenge.

#print("Hello, world!")  #first program.

name="Karebear"  #first variable.
print"Hello,", name +"!"  


import turtle
turtle.color("deep pink")


def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

#forward helper function
def move(len):
  back(-1*len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/num)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
  
spiral(75, 45)
move(150)
turtle.color("lawn green")
spiral(100, 90)
    
