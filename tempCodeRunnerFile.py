import pygame
from MainPage import MainPage
import button
from enum import Enum
from Database import Database as database

pygame.init()
page = MainPage()
pygame.display.set_caption('BubbleMath')
pygame.display.flip()