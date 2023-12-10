import pygame as pg
from random import randint


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Boom them all')
        self.size = self.width, self.height = 600, 300
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('blue')
        self.fps = 100
        self.v = 5
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.game_over = GameOver(self, self.sprites)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.screen.fill('blue')
            self.game_over.do()
            self.sprites.draw(self.screen)
            self.clock.tick(self.fps)
            self.display.flip()


class GameOver(pg.sprite.Sprite):
    image = pg.image.load('data//gameover.png')

    def __init__(self, game, *group):
        super().__init__(*group)
        self.game = game
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.w
        self.rect.y = 0

    def do(self):
        if self.rect.x != 0:
            self.rect.x += self.game.v


if __name__ == '__main__':
    game = Game()
