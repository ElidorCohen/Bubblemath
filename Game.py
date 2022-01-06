# from _typeshed import Self
import pygame
import button
from Page import Page
import MainMenu
from random import *
from Database import Database as database
import os
import time
from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("bubble_pop.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
class AnswerBubble():
    def __init__(self,x,y,screen):
        self.xPos = x
        self.yPos = y
        self.bubble_image = pygame.image.load('bubble.png').convert_alpha()
        self.bubble_button = button.Button(x, y, self.bubble_image, 0.4)
        self.screen = screen
        self.answer = None
    
    def draw_text(self,text, size, font, color, surface, x, y):
        font = pygame.font.Font(font, size)
        textobj = font.render(text, 1, color)
        surface.blit(textobj, (x, y))

    def draw(self):
        self.bubble_button.draw(self.screen)
        if(self.answer is not None):
            self.draw_text('{}'.format(self.answer), 60, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, self.xPos+3, self.yPos)
            

class Game(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('game_background.png')), (self.PAGE_W, self.PAGE_H))
        self.sound_image = pygame.image.load('sound.png').convert_alpha()
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.sound_button = button.Button(940, 50, self.sound_image, 0.4)
        self.return_button = button.Button(5, 640, self.return_image, 0.3)
        self.a_b_sequence = [i for i in range(10)]
        self.answer_sequence = [i for i in range(100)]
        self.bubble_sequence = [i for i in range(4)]
        self.bubble1 = AnswerBubble(400,55,self.screen)
        self.bubble2 = AnswerBubble(500,55,self.screen)
        self.bubble3 = AnswerBubble(600,55,self.screen)
        self.bubble4 = AnswerBubble(700,55,self.screen)
        self.a = None
        self.b =  None
        self.num_of_correct = 0
        self.num_of_questions = 0
        self.score = 0
        self.start_question_time = 0
        self.time_remaining = 0
        self.delta_time = 0
        self.right_answer = None
        self.is_waiting_for_answer = False
        self.bubbles = [self.bubble1, self.bubble2, self.bubble3, self.bubble4]
        self.time_per_question = database.get_time_per_question()
        self.is_sound_enabled = True

    def draw_page(self):
        super(Game,self).draw_page()
        self.draw_text('Time: {}'.format(int(self.time_remaining)), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 10, 100)
        self.draw_text('Score: {}'.format(self.score), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 10, 150)
        self.draw_text('Correct answer: {0}/{1}'.format(self.num_of_correct, self.num_of_questions), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 10, 200)
        self.draw_text('{0} X {1}'.format(self.a, self.b), 60, 'david.ttf', (0, 0, 0), self.screen, 520, 250)
        self.return_button.draw(self.screen)
        self.sound_button.draw(self.screen)
        
    def draw_bubbles(self):
        for bubble in self.bubbles:
            bubble.draw()

    def start_new_question(self):
        seed()
        self.start_question_time = time.time()
        # make choices from the sequence
        self.a = choice(self.a_b_sequence)
        self.b = choice(self.a_b_sequence)
        self.right_answer = self.a * self.b
        right_bubble_num = choice(self.bubble_sequence)
        self.bubbles[right_bubble_num].answer = self.right_answer

        for i in range(4):
            if(i is not right_bubble_num):
                self.bubbles[i].answer = choice(self.answer_sequence)
        
    def check_ans(self,choice):
        if(choice == self.right_answer):
            return True
        return False

    def handle_bubbles(self):
        if(self.time_remaining <= 0):
            self.num_of_questions = self.num_of_questions + 1
            self.is_waiting_for_answer = False
        for event in pygame.event.get():
            for bubble in self.bubbles:
                if bubble.bubble_button.is_clicked(event):
                    if self.is_sound_enabled:
                        mixer.music.play()
                    if(self.check_ans(bubble.answer)):
                        print("correct")
                        self.num_of_correct = self.num_of_correct + 1
                        self.score = self.score + 10
                    else:
                        print("wrong answer")
                    self.num_of_questions = self.num_of_questions + 1
                    self.is_waiting_for_answer = False

    def handle_page(self):
        for event in pygame.event.get():
            if self.return_button.is_clicked(event):
                database.setUserScore(self.score,self.num_of_correct,self.num_of_questions)
                return MainMenu.MainMenu()
            if self.sound_button.is_clicked(event):
                self.is_sound_enabled = not self.is_sound_enabled
            if event.type == pygame.QUIT:
                pygame.quit()
        if(not self.is_waiting_for_answer):
            self.start_new_question()
            self.is_waiting_for_answer = True

        self.delta_time = time.time() - self.start_question_time
        self.time_remaining = self.time_per_question - self.delta_time
        self.draw_bubbles()
        self.handle_bubbles()

        return self

