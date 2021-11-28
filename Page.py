import pygame

class Page():
    def __init__(self):
        self.PAGE_W = 640
        self.PAGE_H = 480
        self.page_id = 0
        self.background_colour = (255, 207, 132)
        self.run_page = True
        self.window = pygame.display.set_mode((self.PAGE_W, self.PAGE_H))
        self.clock = pygame.time.Clock()

    def blit_screen(self):
        self.display.fill(self.background_colour)
        pygame.display.flip()
        pygame.display.update()
        pygame.display.set_caption("BubbleMath")


    def display_menu(self):
        self.run_page = True
        while self.run_page:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check if Rage Quit
                    self.run_page = False



