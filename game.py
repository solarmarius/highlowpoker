import sys
import pygame
import time


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("High-low")
        self.screen = pygame.display.set_mode((1024, 768))

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("Assets/Poppins-Light.ttf", 32)
        self.mus = pygame.mixer.music.load("Assets/sounds/whip-110235.mp3")

        self.img = pygame.image.load("Assets/highbet.png")
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [0, 0]
        self.movement = [False, False]

    def run(self):
        pygame.mixer.music.play(-1, 0.0)
        textSurf = self.font.render("Hello World!", True, (255, 255, 255))
        textRect = textSurf.get_rect()
        textRect.center = (200, 150)

        while True:
            self.screen.blit(self.img, self.img_pos)
            self.screen.blit(textSurf, textRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

            pygame.display.update()
            self.clock.tick(60)


Game().run()
