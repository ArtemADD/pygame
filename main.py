import pygame as pg
from random import randint


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Boom them all')
        self.size = self.width, self.height = 500, 500
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('black')
        self.fps = 100
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        [Bomb(self, self.sprites) for i in range(20)]
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                self.sprites.update(event)
            self.screen.fill('black')
            self.sprites.draw(self.screen)
            self.clock.tick(self.fps)
            self.display.flip()


class Bomb(pg.sprite.Sprite):
    image_bomb = pg.image.load('data//bomb.png')
    image_boom = pg.image.load('data//boom.png')

    def __init__(self, game, *group):
        super().__init__(*group)
        self.game = game
        self.image = Bomb.image_bomb
        self.image_boom = Bomb.image_boom
        self.rect = self.image_bomb.get_rect()
        self.r_boom = self.image_boom.get_rect()
        self.rect.x = randint(0, self.game.width - self.rect.w)
        self.rect.y = randint(0, self.game.height - self.rect.h)
        self.r_boom.x = self.rect.x - ((self.r_boom.w - self.rect.w) / 2)
        self.r_boom.y = self.rect.y - ((self.r_boom.h - self.rect.h) / 2)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.rect = self.r_boom
            self.image = self.image_boom


if __name__ == '__main__':
    game = Game()
