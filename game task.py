# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:58:53 2020

@author: User
"""

import turtle
import random
from playsound import playsound

score=0
lives=10
main_window = turtle.Screen()
main_window.title("falling hearts")
main_window.bgpic("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\back.gif")
main_window.setup(width=600, height=600)
main_window.tracer(0)
main_window.register_shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\redheart.gif")
main_window.register_shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\blackheart.gif")
main_window.register_shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\left.gif")
main_window.register_shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\right.gif")

pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("purple")
font = ('Courier',26,'bold')
pen.goto(0,260)
pen.write('Score : {} -- lives : {} '.format(score,lives),align='center',font=font)


direction = 'stop'

actor = turtle.Turtle()
actor.shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\right.gif")
actor.speed(0)
actor.penup()
actor.goto(0, -270)

red_hearts=[]
for i in range (10) :
     red_heart = turtle.Turtle()
     red_heart.shape('C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\redheart.gif')
     red_heart.speed(random.randint(1, 4))
     red_heart.penup()
     red_heart.goto(-50, 270)
     red_hearts.append(red_heart)


black_hearts=[]
for i in range (10) :
     black_heart = turtle.Turtle()
     black_heart.shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\blackheart.gif")
     black_heart.speed(random.randint(1, 4))
     black_heart.penup()
     black_heart.goto(50, 270)
     black_hearts.append(black_heart)


def move_left():
    global direction
    direction = 'left'


def move_right():
    global direction
    direction = 'right'


def stop_actor():
    global direction
    direction = 'stop'


main_window.listen()
main_window.onkeypress(move_left, 'Left')
main_window.onkeypress(move_right, 'Right')
main_window.onkeypress(stop_actor, 'Down')

while True:
    main_window.update()
    if direction == 'left':
        actor.shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\left.gif")
        x = actor.xcor()
        x -= 0.7
        if x < -270:
            x = -270
        actor.setx(x)
    if direction == 'right':
        actor.shape("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\right.gif")
        x = actor.xcor()
        x += 0.7
        if x > 270:
            x = 270
        actor.setx(x)
    for red_heart in red_hearts:
         y=red_heart.ycor()
         y-=0.3*red_heart.speed()
         red_heart.sety(y)
         if y<-300:
           x=random.randint(-270,270)
           red_heart.goto(x,270)

         if red_heart.distance(actor)< 40 :
             playsound("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\red.wav",False)
             x = random.randint(-270, 270)
             red_heart.goto(x, 270)
             score+=10
             pen.clear()
             pen.write('Score : {} -- lives : {} '.format(score, lives), align='center', font=font)



    for black_heart in black_hearts:
         y=black_heart.ycor()
         y-=0.3*black_heart.speed()
         black_heart.sety(y)

         if y<-300:
           x=random.randint(-270,270)
           black_heart.goto(x,270)

         if black_heart.distance(actor)< 40 :
             playsound("C:\\Users\\User\\OneDrive\\Desktop\\game\\Game designs\\Game designs\\black.wav",False)
             x = random.randint(-270, 270)
             black_heart.goto(x, 270)
             score-=10
             lives-=1
             if lives<0:
                 main_window.bye()
                 exite(0)
             pen.clear()
             pen.write('Score : {} -- lives : {} '.format(score, lives), align='center', font=font)





main_window.mainloop()














