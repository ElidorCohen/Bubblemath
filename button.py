import pygame

class Button():
    def __init__(self, x, y, image, scale):
        button_w = image.get_width()
        button_h = image.get_height()
        self.image = pygame.transform.scale(image, (int(button_w * scale), int(button_h * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        mouse_position = pygame.mouse.get_pos()  # get mouse position
        if self.rect.collidepoint(mouse_position):  # check mouseover and clicked conditions
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))  # draw button on screen
        return action

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)
