import pygame
import os

#fully capitalized variables will be constants

pygame.display.set_caption("chess")
WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def drawGraph():
    WINDOW.fill((0, 0, 255)) #fill bg color
    pygame.display.update()

def main():

    gameLoop = True

    while gameLoop:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                gameLoop = False

        drawGraph()

    pygame.quit()


if __name__ == "__main__":
    main()