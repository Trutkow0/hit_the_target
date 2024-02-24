# Timothy Rutkowski 02/15/2024 timothyRutkowski_lab3-4.py

# This program is an enhancement to the hit_the_target.py program by giving the 
# the user hints when they miss the target for how they can adjust their force
# and angle to more accuratley hit the target.

import turtle
  
# Named constants
SCREEN_WIDTH = 600     # Screen width
SCREEN_HEIGHT = 600    # Screen height
TARGET_LLEFT_X = 100   # Target's lower-left X
TARGET_LLEFT_Y = 250   # Target's lower-left Y
TARGET_WIDTH = 25      # Width of the target
FORCE_FACTOR = 30      # Arbitrary force factor
PROJECTILE_SPEED = 1   # Projectile's animation speed
NORTH = 90             # Angle of north direction
SOUTH = 270            # Angle of south direction
EAST = 0               # Angle of east direction
WEST = 180             # Angle of west direction
  
# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
  
# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
  
# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
  
# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))
  
# Calculate the distance.
distance = force * FORCE_FACTOR
  
# Set the heading.
turtle.setheading(angle)
  
# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
turtle.ycor() >= TARGET_LLEFT_Y and
turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Target hit!')
    
else:
    # Calculate the difference in x and y coordinates
    dx = TARGET_LLEFT_X + TARGET_WIDTH / 2 - turtle.xcor()
    dy = TARGET_LLEFT_Y + TARGET_WIDTH / 2 - turtle.ycor() 
    
    # Provide hints based on the differences
    if dx < 0 and dy < 0:
        print('You missed the target. \nTry a greater angle. \nUse less force.')
    elif dx < 0 and dy > 0:
        print('You missed the target. \nTry a greater angle. \nUse more force.')
    elif dx > 0 and dy < 0:
        print('You missed the target. \nTry a smaller angle. \nUse less force.')
    elif dx > 0 and dy > 0:
        print('You missed the target. \nTry a smaller angle. \nUse more force.')

turtle.done()
