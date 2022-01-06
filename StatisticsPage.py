import pygame
from pymongo.database import Database
from User import UserType
import button
import os
from Database import Database as database
from Page import Page
import MainPage
import MainMenu
from InputBox import InputBox

ITEM_Y = 400
OFFSET_Y = 30

FEEDBACK_X = 320
GRADE_X = 560
NAME_GRADE_X = 50
FEED_BUTTON_X = 800

class UserStatistic():
    def __init__(self,user_id, user_name,user_score,item_y):
        self.is_sent = False
        self.item_y = item_y
        self.user_id = user_id
        self.user_name = user_name
        self.user_score = user_score
        self.feedback_input = InputBox(FEEDBACK_X, self.item_y, 0, 32)
        self.grades_input = InputBox(GRADE_X, self.item_y, 0, 32)
        self.send_feedback_image = pygame.image.load('send_feedback.png').convert_alpha()
        self.send_feedback_button = button.Button(FEED_BUTTON_X, self.item_y, self.send_feedback_image, 0.15)

    def handle_stat_item(self, event):
        if self.send_feedback_button.is_clicked(event):
            database.send_feedback(self.user_id,self.feedback_input.text,self.user_score)
            self.is_sent = True


class StatisticsPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('myprofile.png')), (self.PAGE_W, self.PAGE_H))
        self.return_image = pygame.image.load('return.png').convert_alpha()
        self.return_button = button.Button(20, 15, self.return_image, 0.3)
        self.user = database.getUser(database.user_id)
        self.institute = database.getInstitute(self.user.institute)
        self.users_list = database.get_all_users()
        self.user_stats_list = []
        self.count = 0
        for user in self.users_list:
            self.user_stats_list.append(UserStatistic(user.user_id,user.full_name,user.score, ITEM_Y + self.count * OFFSET_Y))
            self.count = self.count + 1
        self.input_boxes1 = []
        for item in self.user_stats_list:
            self.input_boxes1.append(item.grades_input)
            self.input_boxes1.append(item.feedback_input)

    def draw_page(self):
        super(StatisticsPage,self).draw_page()
        self.screen.blit(self.background, (0, 0))
        self.draw_text('Statistics', 70, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 400, 20)
        self.draw_text('Number Of Student: {}'.format(self.institute.num_of_students), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 170)
        self.draw_text('Rank Of The Institute: {}'.format(self.institute.rank), 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 100, 220)
        self.draw_text('Students:', 30, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, 450, 285)
        self.draw_text('Feedback', 20, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, FEEDBACK_X, 340)
        self.draw_text('Grades', 20, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, GRADE_X, 340)
        self.return_button.draw(self.screen)
        for item in self.user_stats_list:
            self.draw_text('Name: {},      Score: {}'.format(item.user_name,item.user_score), 20, 'Harlow Solid Italic Italic.ttf', (0, 0, 0), self.screen, NAME_GRADE_X, item.item_y)
            if not item.is_sent:
                item.send_feedback_button.draw(self.screen)
    # def draw_student(self):
    #     count = 0
    #     for i in self.reports:
    #         self.draw_text('{}'.format(i), 25, 'david.ttf', (0, 0, 0), self.screen, 100, REPORT_Y_OFFSET * count + 250)
    #         count = count + 1 

    def handle_page(self):
        for event in pygame.event.get():
            for box in self.input_boxes1:
                box.handle_event(event)
            if self.return_button.is_clicked(event):
                return MainMenu.MainMenu()
            if event.type == pygame.QUIT:
                pygame.quit()
            for item in self.user_stats_list:
                item.handle_stat_item(event)
        for box in self.input_boxes1:
            box.update()
        for box in self.input_boxes1:
            box.draw(self.screen)
        return self
