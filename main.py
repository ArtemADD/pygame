import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Курсор')
        pg.mouse.set_visible(False)
        self.size = self.width, self.height = 500, 500
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('black')
        self.fps = 100
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.cur = Curser(self.sprites)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEMOTION:
                    self.cur.update()
            self.screen.fill('black')
            if pg.mouse.get_focused():
                self.sprites.draw(self.screen)
            self.clock.tick(self.fps)
            self.display.flip()


class Curser(pg.sprite.Sprite):
    image = pg.image.load('data//arrow.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Curser.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 50, 50

    def update(self):
        self.rect.x, self.rect.y = pg.mouse.get_pos()


if __name__ == '__main__':
    game = Game()
