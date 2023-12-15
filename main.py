import sys

import pygame as pg
from random import randint


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Перемещение героя')
        self.size = self.width, self.height = 800, 800
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('black')
        self.fps = 100
        self.clock = pg.time.Clock()
        self.map = Map(self)
        self.sprites = pg.sprite.Group()
        self.player = Player(self, self.sprites)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    self.player.move()
            self.screen.fill('black')
            self.map.draw()
            self.sprites.draw(self.screen)
            self.clock.tick(self.fps)
            self.display.flip()


class Map:
    def __init__(self, game):
        self.game = game
        self.minimap = [[randint(0, 2) for m in range(game.width // 50)] for _ in range(game.height // 50)]
        self.grass_image = pg.image.load('data//grass.png')
        self.box_image = pg.image.load('data//box.png')

    def draw(self):
        for j in range(len(self.minimap)):
            for i in range(len(self.minimap[j])):
                if self.minimap[j][i] % 2 == 0:
                    self.game.screen.blit(self.grass_image, (i * 50, j * 50))
                else:
                    self.game.screen.blit(self.box_image, (i * 50, j * 50))


class Player(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('data//mar.png'), (50, 50))

    def __init__(self, game, *group):
        super().__init__(*group)
        self.game = game
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.x = randint(0, (game.width // 50) - 1)
        self.y = randint(0, (game.height // 50) - 1)
        while self.game.map.minimap[self.y][self.x] == 1:
            self.x = randint(0, (game.width // 50) - 1)
            self.y = randint(0, (game.height // 50) - 1)
        self.rect.x = self.x * 50
        self.rect.y = self.y * 50

    def move(self):
        keys = pg.key.get_pressed()
        x = self.x
        y = self.y
        if keys[pg.K_w]:
            y -= 1
        elif keys[pg.K_a]:
            x -= 1
        elif keys[pg.K_s]:
            y += 1
        elif keys[pg.K_d]:
            x += 1
        if (0 <= x < len(self.game.map.minimap) and 0 <= y < len(self.game.map.minimap)
                and self.game.map.minimap[y][x] != 1):
            print(x, y)
            self.x = x
            self.y = y
            self.rect.x = self.x * 50
            self.rect.y = self.y * 50


if __name__ == '__main__':
    game = Game()
    sys.exit()
