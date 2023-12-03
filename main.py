import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Кирпичи')
        self.size = self.width, self.height = 300, 200
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('white')
        self.display = pg.display
        self.bricks = Bricks(self)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.screen.fill('white')
            self.draw()
            self.display.flip()

    def draw(self):
        self.bricks.draw(self.screen)


class Bricks:
    def __init__(self, game):
        self.width = game.width
        self.height = game.height
        self.h = 15
        self.w = 30

    def draw(self, screen):
        q = self.width // self.w + 1
        k = self.height // self.h + 1
        for j in range(k):
            for i in range(q):
                if j == 0:
                    pg.draw.rect(screen, 'red', ((self.w * i) + (i * 2), self.h * j, self.w, self.h))
                    continue
                if j % 2 == 0 and j != 0:
                    pg.draw.rect(screen, 'red', ((self.w * i) + (i * 2), self.h * j + (j * 2), self.w, self.h))
                else:
                    if i == 0:
                        pg.draw.rect(screen, 'red', (0, self.h * j + (j * 2), self.w // 2, self.h))
                        pg.draw.rect(screen, 'red', ((self.w // 2) + (self.w * i) + (1 * 2),
                                                     self.h * j + (j * 2), self.w, self.h))
                    else:
                        pg.draw.rect(screen, 'red', ((self.w // 2) + (self.w * i) + ((i + 1) * 2),
                                                     self.h * j + (j * 2), self.w, self.h))


if __name__ == '__main__':
    game = Game()
