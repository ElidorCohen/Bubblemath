import pygame
import button 
from enum import Enum

# Setup pygame/window ---------------------------------------- #
background = (255, 207, 132)
screen_w = 1000
screen_h = 720
pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('BubbleMath')
pygame.display.flip()

from InputBox import InputBox

# Pages ------------------------------------------------------ #
class PageName(Enum): 
    MAIN_PAGE = "main_page"
    LOGIN_PAGE = "login_page"
    ROLE_PAGE = "role_page"
    REGISTER_PAGE = "registeer_page"
    PROFILE_PAGE = "profile_page"
    GAME_MENU_PAGE = "game_menu_page"

# MainMenu - page 0 ------------------------------------------ #
login_image = pygame.image.load('login.png').convert_alpha()
register_image = pygame.image.load('Register.png').convert_alpha()
login_button = button.Button(360, 400, login_image, 0.3)
register_button = button.Button(360, 550, register_image, 0.3) 

# LoginPage - page 1 ------------------------------------------ #
connect_image = pygame.image.load('connect.png').convert_alpha()
back_image = pygame.image.load('back.png').convert_alpha()
connect_button = button.Button(395, 540, connect_image, 0.3)
back_button = button.Button(10, 620, back_image, 0.7)
user_id_input = InputBox(400, 440, 140, 32)
pass_input = InputBox(400, 490, 140, 32)
input_boxes = [user_id_input, pass_input]

# Choose role - page 2 -------------------------------------- #
student_image = pygame.image.load('student.png').convert_alpha()
counselor_image = pygame.image.load('counselor.png').convert_alpha()
student_button = button.Button(480, 300, student_image, 0.2)
counselor_button = button.Button(480, 400, counselor_image, 0.2)
role = ''

# RegisterPage - page 3 -------------------------------------- #
done_image = pygame.image.load('done.png').convert_alpha()
return_image = pygame.image.load('return.png').convert_alpha()
done_button = button.Button(500, 500, done_image, 0.3)
return_button = button.Button(5, 640, return_image, 0.3)
user_input = InputBox(250, 170, 140, 32)
password_input = InputBox(250, 220, 140, 32)
institute_input = InputBox(250, 260, 140, 32)
id_input = InputBox(250, 300, 140, 32)
gender_input = InputBox(250, 340, 140, 32)
age_input = InputBox(250, 380, 140, 32)
input_boxes1 = [user_input, password_input, institute_input, id_input, gender_input, age_input]

# Draw the text ---------------------------------------------- #
def draw_text(text, size, font, color, surface,x,y):
    font = pygame.font.Font(font, size)
    textobj = font.render(text, 1, color,)
    textrect = textobj.get_rect()
    surface.blit(textobj,(x,y))

def game_loop():
    current_screen = PageName.MAIN_PAGE
    run_MainMenu = True
    while run_MainMenu:
        mx, my = pygame.mouse.get_pos()
        screen.fill(background)
        match current_screen:                
            case PageName.MAIN_PAGE:
                draw_text('BubbleMate', 100, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 230, 200) 
                login_button.draw(screen)
                register_button.draw(screen)
                for event in pygame.event.get():
                    if login_button.is_clicked(event):
                        print("login")
                        current_screen = PageName.LOGIN_PAGE
                    if register_button.is_clicked(event):
                        print("register")
                        current_screen = PageName.ROLE_PAGE
            case PageName.LOGIN_PAGE:
                draw_text('BubbleMate', 100, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 230, 200) 
                draw_text('Name: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 290, 440) 
                draw_text('password: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 290, 490) 
                connect_button.draw(screen)
                back_button.draw(screen)
                for event in pygame.event.get():
                    for box in input_boxes:
                        box.handle_event(event)
                    if connect_button.is_clicked(event):
                        print("connect")
                        current_screen = PageName.GAME_MENU_PAGE
                        # go to game menu page
                        # pass
                    if back_button.is_clicked(event):
                        print("back")
                        current_screen = PageName.MAIN_PAGE
                        # go to main menu page
                        #pass
                for box in input_boxes:
                        box.update()
                for box in input_boxes:
                    box.draw(screen)
            
            case PageName.ROLE_PAGE:
                student_button.draw(screen)
                counselor_button.draw(screen)
                return_button.draw(screen)
                for event in pygame.event.get():
                    if done_button.is_clicked(event):
                        print("student")
                        current_screen = PageName.GAME_MENU_PAGE
                    if return_button.is_clicked(event):
                        print("counselor")
                        # set 
                        current_screen = PageName.MAIN_PAGE
                    if return_button.is_clicked(event):
                        print("return")
                        # set
                        current_screen = PageName.MAIN_PAGE
                
            case PageName.REGISTER_PAGE:
                draw_text('Register', 70, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 430, 30) # x , y
                draw_text('Name: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 100, 170) 
                draw_text('Password: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 100, 220)                 
                draw_text('Institute: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 100, 260)                 
                draw_text('Id: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 100, 300)                 
                draw_text('Gender: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 100, 340)                 
                draw_text('Age: ', 25, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), screen, 100, 380) 
                done_button.draw(screen)
                return_button.draw(screen)
                for event in pygame.event.get():
                    for box in input_boxes1:
                        box.handle_event(event)
                    if done_button.is_clicked(event):
                        print("done")
                        current_screen = PageName.GAME_MENU_PAGE
                        # go to game menu page
                        # pass
                    if return_button.is_clicked(event):
                        print("return")
                        current_screen = PageName.MAIN_PAGE
                        # go to main menu page
                        #pass
                for box in input_boxes1:
                    box.update()
                for box in input_boxes1:
                    box.draw(screen)     
            case _ :
                print("DEFAULT")
                current_screen = PageName.MAIN_PAGE
        if event.type == pygame.QUIT:
            run_MainMenu = False  
        pygame.display.update()
    pygame.quit()
game_loop()