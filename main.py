import pygame as pg

LEFT_UP = 1
LEFT_DOWN = 2
RIGHT_DOWN = 3
RIGHT_UP = 4


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Перетаскивание')
        self.size = self.width, self.height = 300, 300
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.v = 5
        self.balls = []
        self.fps = 30
        self.clock = pg.time.Clock()
        self.rect = Rect(self.screen)
        self.grap = False
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == pg.BUTTON_LEFT:
                        if (event.pos[0] in range(self.rect.x, self.rect.x + self.rect.w)
                                and event.pos[1] in range(self.rect.y, self.rect.y + self.rect.w)):
                            self.rect.pos_grap = event.pos
                            self.grap = True
                if event.type == pg.MOUSEBUTTONUP:
                    self.rect.x, self.rect.y = self.rect.pos
                    self.grap = False
                if event.type == pg.MOUSEMOTION and self.grap:
                    self.rect.move(event.pos)
            self.screen.fill('black')
            self.draw()
            self.clock.tick(self.fps)
            self.display.flip()

    def draw(self):
        self.rect.draw()


class Rect:
    def __init__(self, screen):
        self.screen = screen
        self.pos = 100, 100
        self.x, self.y = self.pos
        self.w = 100
        self.pos_grap = [0, 0]

    def move(self, pos):
        x, y = pos
        x -= self.pos_grap[0]
        y -= self.pos_grap[1]
        self.pos = [self.x + x, self.y + y]

    def draw(self):
        pg.draw.rect(self.screen, 'green', (*self.pos, self.w, self.w), border_radius=15)


if __name__ == '__main__':
    game = Game()
