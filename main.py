import pygame as pg

RIGHT_UP = 1
LEFT_UP = 2
LEFT_DOWN = 3
RIGHT_DOWN = 4
LINE = 5


class Game:
    def __init__(self):
        self.set_n()
        pg.init()
        pg.display.set_caption('Ромбики')
        self.size = self.width, self.height = 300, 300
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('yellow')
        self.display = pg.display
        self.loz = Lozenges(self)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.screen.fill('yellow')
            self.draw()
            self.display.flip()

    def draw(self):
        self.loz.draw(self.screen)

    def set_n(self):
        n = input()
        if ',' in n:
            print('Неправильный формат ввода')
            pg.quit()
        self.n = int(n)


class Lozenges:
    def __init__(self, game):
        self.n = game.n
        self.width = game.width
        self.height = game.height

    def draw(self, screen):
        k = self.width // self.n
        q = self.height // self.n
        half_n = self.n // 2
        for i in range(k):
            for j in range(q):
                pg.draw.polygon(screen, 'orange', [
                    (half_n + self.n * i, self.n * j),
                    (self.n * i, half_n + self.n * j),
                    (half_n + self.n * i, self.n + self.n * j),
                    (self.n + self.n * i, half_n + self.n * j)
                ])


if __name__ == '__main__':
    game = Game()
