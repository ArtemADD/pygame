import pygame as pg


class Game:
    def __init__(self):
        self.set_cube()
        pg.init()
        pg.display.set_caption('Куб')
        self.size = self.width, self.height = 300, 300
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.cube = Cube(self)
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
        self.cube.draw(self.screen)

    def set_cube(self):
        n = input().split()
        if int(n[0]) > 100 or int(n[0]) % 4 != 0 or int(n[1]) > 360:
            print('Неправильный формат ввода')
            pg.quit()
        self.w = int(n[0])
        self.c = int(n[1])


class Cube:
    def __init__(self, game):
        self.w = game.w
        self.width = game.width
        self.height = game.height
        c_1 = pg.Color(0, 0, 0)
        c_2 = pg.Color(0, 0, 0)
        c_3 = pg.Color(0, 0, 0)
        c_1.hsva = (game.c, 100, 100, 100)
        self.c_1 = c_1
        c_2.hsva = (game.c, 100, 75, 100)
        self.c_2 = c_2
        c_3.hsva = (game.c, 100, 50, 100)
        self.c_3 = c_3

    def draw(self, screen):
        pg.draw.rect(screen, self.c_2, (self.width // 2 - self.w // 2, self.height // 2,
                                        self.w, self.w))
        pg.draw.polygon(screen, self.c_1, [(self.width // 2 - self.w // 2, self.height // 2),
                                           (self.width // 2 + self.w // 2, self.height // 2),
                                           (self.width // 2 + self.w, self.height // 2 - self.w // 2),
                                           (self.width // 2, self.height // 2 - self.w // 2)
                                           ])
        pg.draw.polygon(screen, self.c_3, [(self.width // 2 + self.w // 2, self.height // 2),
                                           (self.width // 2 + self.w, self.height // 2 - self.w // 2),
                                           (self.width // 2 + self.w, self.height // 2 + self.w // 2),
                                           (self.width // 2 + self.w // 2, self.height // 2 + self.w)
                                           ])


if __name__ == '__main__':
    game = Game()
