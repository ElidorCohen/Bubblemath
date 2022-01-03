import pygame
from MainPage import MainPage
import button
from enum import Enum
from Database import Database as database

pygame.init()
page = MainPage()
pygame.display.set_caption('BubbleMath')
pygame.display.flip()
from InputBox import InputBox
database.connectToServer()

def game_loop():
    run_MainMenu = True
    page = MainPage()
    
    while run_MainMenu:
        mx, my = pygame.mouse.get_pos()
        page.draw_page()
        page = page.handle_page()
        pygame.display.update()

    pygame.quit()


game_loop()