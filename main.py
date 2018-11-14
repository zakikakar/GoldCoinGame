#!/bin/python3

from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# Just return the actions we are interested in
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # red
Y = [255, 255, 0] # yellow
G = [0, 255, 0] # green
W = [255, 255, 255] # white
O = [0,0,0] #nothing
R = [255,40,0] #orange


score = 0

for turns in range(5):
  
  coinx = randint(0,7)
  coiny = randint(0,7)
  print (coinx, coiny)
  
  sense.set_pixel(coinx, coiny, Y)
  sleep(1)
  sense.clear()
  
  x = randint(0,7)
  y = randint(0,7)
  sense.set_pixel(x,y,W)
  
  while (True):
    e = wait_for_move()
    
    if (e.direction == DIRECTION_MIDDLE):
      if (x == coinx and y == coiny):
        sense.set_pixel(x,y,G)
        score += 1

        def coin():
          logo = [
          O, O, O, O, O, O, O, O,
          O, O, Y, Y, Y, Y, O, O,
          O, Y, Y, R, R, Y, Y, O,
          O, Y, R, Y, Y, Y, Y, O,
          O, Y, R, Y, Y, Y, Y, O,
          O, Y, Y, R, R, Y, Y, O,
          O, O, Y, Y, Y, Y, O, O,
          O, O, O, O, O, O, O, O,
          ]
          return logo
        
        images = [coin]
        count = 0

        sense.set_pixels(images[count % len(images)]())
        sleep(1)
        count += 1
        sense.clear()

      else:
        #sense.set_pixel(x,y,R)
        sense.clear(R)
      
      sleep(1)
      sense.clear()
      break;
  
    sense.clear()
  
    if (e.direction == DIRECTION_UP and y > 0):
      y = y - 1
    elif (e.direction == DIRECTION_DOWN and y < 7):
      y = y + 1
      
    if (e.direction == DIRECTION_LEFT and x > 0):
      x = x - 1
    elif (e.direction == DIRECTION_RIGHT and x < 7):
      x = x + 1
      
    sense.set_pixel(x,y,W)
    
sense.show_message("Score " + str(score) + "/5", scroll_speed = 0.05)
    
