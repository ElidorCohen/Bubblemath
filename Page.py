import pygame

class Page():
    pygame.display.set_caption("BubbleMath")
    def __init__(self):
        self.PAGE_W = 1000
        self.PAGE_H = 720
        self.page_id = 0
        self.background_colour = (255, 207, 132)
        self.run_page = True
        self.display = pygame.Surface((self.PAGE_W, self.PAGE_H))
        self.window = pygame.display.set_mode(((self.PAGE_W, self.PAGE_H)))
        self.clock = pygame.time.Clock()


    def display_menu(self):
        self.run_page = True
        while self.run_page:
            self.window.fill(self.background_colour)
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check if Rage Quit
                    self.run_page = False
            pygame.display.update()




