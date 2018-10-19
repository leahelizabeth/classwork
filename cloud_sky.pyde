#while loop
#increase variable
#use draw() for animation
import time

ball = 0

def setup():
    size(640, 480)
    
def draw():
    global ball
    if ball >= 640:
        ball = 0
    ball += 4
    #to make background skyblue
    background(135,206,250)
    noStroke()
    ellipse(ball,height/2,50,50)
    #create a cluster of circles
    #to simulate a moving cloud
    ellipse(ball+25,height/2,50,50)
    ellipse(ball+50,height/2,50,50)
    ellipse(ball+25,height/2.25,50,50)
    rect(50, 200, 50, 300)
