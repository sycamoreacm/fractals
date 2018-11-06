import turtle

t = turtle.Turtle()   # creates a turtle object
#t.ht()      # makes the turtle 'invisible' so you don't see it drawing
tick_length = 20
radius = 150

for i in range(12):     # executes the indented code 12 times
  t.left(90)            # rotates the turtle left 90 degrees
  t.fd(tick_length)     # moves the turtle forward tick_length units
  t.bk(tick_length)     # moves the turtle backward tick_length units
  t.right(90)           # rotates the turtle right 90 degrees
  t.circle(radius, 30)  # draws the first 30 degrees of a circle with a radius of 'radius'