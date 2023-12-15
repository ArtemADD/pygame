import sys
import pygame as pg


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Перемещение героя')
        self.map = Map(self)
        self.size = self.width, self.height = self.map.size[0] * 50 , self.map.size[1] * 50
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('black')
        self.fps = 100
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.start_screen = pg.sprite.Group()
        self.player = Player(self, self.sprites)
        self.ss = StartScreen(self)
        self.start = True
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if self.start is False:
                        self.player.move()
                    if self.start:
                        self.start = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.start = False
            self.screen.fill('black')
            self.map.draw()
            self.sprites.draw(self.screen)
            if self.start:
                self.start_screen.draw(self.screen)
            self.clock.tick(self.fps)
            self.display.flip()


class Map:
    def __init__(self, game):
        self.game = game
        self.minimap = load_level('map.txt')
        self.grass_image = pg.image.load('data//grass.png')
        self.box_image = pg.image.load('data//box.png')
        self.size = len(self.minimap), len(self.minimap[0])

    def draw(self):
        for j in range(len(self.minimap)):
            for i in range(len(self.minimap[j])):
                if self.minimap[j][i] == '@':
                    self.game.player.set_pos(i, j)
                if self.minimap[j][i] != '#':
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
        self.x, self.y = None, None

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
                and self.game.map.minimap[y][x] != '#'):
            self.x = x
            self.y = y
            self.rect.x = self.x * 50
            self.rect.y = self.y * 50
        print(x, y)

    def set_pos(self, x, y):
        if self.x is None and self.y is None:
            self.x = x
            self.y = y
            self.rect.x = x * 50
            self.rect.y = y * 50


class StartScreen(pg.sprite.Sprite):
    img = pg.image.load('data//fon.jpg')

    def __init__(self, game):
        super().__init__(game.start_screen)
        self.image = pg.transform.scale(StartScreen.img, game.size)
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    game = Game()
    sys.exit()
