import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Герой двигается!')
        self.size = self.width, self.height = 300, 300
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('white')
        self.fps = 0
        self.v = 1
        self.delta_time = 1
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.hero = Hero(self, self.size, self.sprites)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.hero.move()
            self.screen.fill('white')
            self.sprites.draw(self.screen)
            self.delta_time = self.clock.tick(self.fps)
            self.display.flip()


class Hero(pg.sprite.Sprite):
    image = pg.image.load('data//creature.png')

    def __init__(self, game, size, *group):
        super().__init__(*group)
        self.game = game
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (size[0] // 2) - (self.rect.width // 2), (size[1] // 2) - (self.rect.height // 2)

    def check_pos(self, keys):
        x = self.rect.x
        y = self.rect.y
        w = self.rect.w
        h = self.rect.h
        speed = self.game.v * self.game.delta_time
        if keys[pg.K_LEFT]:
            if x - speed < 0:
                return False
        if keys[pg.K_RIGHT]:
            if x + speed + w > self.game.width:
                return False
        if keys[pg.K_UP]:
            if y - speed < 0:
                return False
        if keys[pg.K_DOWN]:
            if y + speed + h > self.game.height:
                return False
        return True

    def move(self):
        speed = self.game.v * self.game.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.check_pos(keys):
            self.rect.x -= speed
        if keys[pg.K_RIGHT] and self.check_pos(keys):
            self.rect.x += speed
        if keys[pg.K_UP] and self.check_pos(keys):
            self.rect.y -= speed
        if keys[pg.K_DOWN] and self.check_pos(keys):
            self.rect.y += speed


if __name__ == '__main__':
    game = Game()
