import pygame


if __name__ == '__main__':
    pygame.init()
    size = width, height = list(map(lambda x: int(x), input().split(' ')))
    screen = pygame.display.set_mode(size)
    screen.fill('black')
    pygame.draw.rect(screen, 'red', (1, 1, width - 2, height - 2))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
