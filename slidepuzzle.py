# Slide Puzzle
# This is a copy of the code
# from the book Making Games with Python 
# by Al Sweigart

import pygame, sys, random
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)
BOARDWIDTH = 4 # number of columns in the board
BOARDHEIGHT = 4 # number of rows in the board
TILESIZE = 80
WINDOWWIGHT = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

#                   R    G    B
BLACK =            (  0,    0,   0)
WHITE =            (255,  255, 255)
BRIGHTBLUE =       (  0,   50, 255)
DARKTURQUOISE =    (  3,   54,  73)
GREEN =            (  0,  204,   0)