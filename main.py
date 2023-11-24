import pygame


if __name__ == '__main__':
    pygame.init()
    w, n = list(map(lambda x: int(x), input().split(' ')))
    screen = pygame.display.set_mode((w, w))
    screen.fill('white')
    s = w / n
    flag = True
    for i in range(n):
        for j in range(n):
            if flag:
                pygame.draw.rect(screen, 'black', (i * s, j * s, s, s))
                flag = False
            else:
                flag = True
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
