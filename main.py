import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Жёлтый круг')
        self.size = self.width, self.height = 800, 600
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('blue')
        self.display = pg.display
        self.v = 1
        self.x = 1
        self.fps = 100
        self.clock = pg.time.Clock()
        self.draw_circle = False
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONUP:
                    self.screen.fill('blue')
                    self.draw_circle = True
                    self.x_pos = event.pos
                    self.x = 1
            self.draw()
            self.clock.tick(self.fps)
            self.display.flip()

    def draw(self):
        if self.draw_circle:
            self.x += self.v
            pg.draw.circle(self.screen, 'yellow', self.x_pos, self.x)


if __name__ == '__main__':
    game = Game()
