import pygame as pg

RIGHT_UP = 1
LEFT_UP = 2
LEFT_DOWN = 3
RIGHT_DOWN = 4
LINE = 5


class Game:
    def __init__(self):
        n = input()
        if ',' in n:
            print('Неправильный формат ввода')
            return
        self.n = int(n)
        pg.init()
        pg.display.set_caption('Сфера')
        self.size = self.width, self.height = 300, 300
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.circle = Circle(self)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.screen.fill('black')
            self.draw()
            self.display.flip()

    def draw(self):
        self.circle.draw(self.screen)


class Circle:
    def __init__(self, game):
        self.n = game.n
        self.width = game.width
        self.height = game.height
        self.half_width = game.width // 2
        self.half_height = game.height // 2

    def draw(self, screen):
        q = self.width // self.n
        for i in range(1, self.n + 1):
            pg.draw.ellipse(screen, 'white', (0, self.half_height - (q * i // 2), self.width, q * i), 1)
        for i in range(1, self.n + 1):
            pg.draw.ellipse(screen, 'white', (self.half_width - (q * i // 2), 0, q * i, self.height), 1)


if __name__ == '__main__':
    game = Game()
