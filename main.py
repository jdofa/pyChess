import pygame
import os

#fully capitalized variables will be constants

pygame.display.set_caption("chess")
WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#load images
LIGHT_SQUARE_JPG = pygame.image.load(os.path.join('Assets','light_square.jpg'))
DARK_SQUARE_JPG = pygame.image.load(os.path.join('Assets','dark_square.jpg'))

#scale images according to window screen size to have 8x8 board
#added 1 pixel to width & height to fix rounding error - maybe switch away from images later
LIGHT_SQUARE = pygame.transform.scale(LIGHT_SQUARE_JPG, (WIDTH/8 + 1, HEIGHT/8 + 1)) 
DARK_SQUARE = pygame.transform.scale(DARK_SQUARE_JPG, (WIDTH/8 + 1, HEIGHT/8 + 1))

def drawBoard():
    for rows in range(4):
        #Top Row Pattern | Light -> Dark 
        for i in range(8):
            if i%2 == 0:
                WINDOW.blit(LIGHT_SQUARE, ((WIDTH/8)*i, (HEIGHT/8)*rows*2))
            else:
                WINDOW.blit(DARK_SQUARE, ((WIDTH/8)*i, (HEIGHT/8)*rows*2))
        #Bottom Row Pattern | Dark -> Light
        for i in range(8):
            if i%2 == 0:
                WINDOW.blit(DARK_SQUARE, ((WIDTH/8)*i, (HEIGHT/8)*(rows*2+1)))
            else:
                WINDOW.blit(LIGHT_SQUARE, ((WIDTH/8)*i, (HEIGHT/8)*(rows*2+1)))

    pygame.display.update()

def main():

    gameLoop = True

    while gameLoop:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                gameLoop = False

        drawBoard()

    pygame.quit()


if __name__ == "__main__":
    main()