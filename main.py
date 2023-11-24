import pygame


if __name__ == '__main__':
    pygame.init()
    size = width, height = list(map(lambda x: int(x), input().split(' ')))
    screen = pygame.display.set_mode(size)
    pygame.draw.line(screen, 'white', (0, 0), size, 5)
    pygame.draw.line(screen, 'white', (width, 0), (0, height), 5)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
