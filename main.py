import pygame


if __name__ == '__main__':
    pygame.init()
    n, k = list(map(lambda x: int(x), input().split(' ')))
    w = n * k * 2
    screen = pygame.display.set_mode((w, w))
    screen.fill('black')
    colors = ['red', 'green', 'blue']
    for i in range(1, k + 1):
        pygame.draw.circle(screen, colors[0], (w / 2, w / 2), n * i + 1, n + 1)
        c = colors.pop(0)
        colors.append(c)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
