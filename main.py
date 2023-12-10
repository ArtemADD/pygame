import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Машинка')
        self.size = self.width, self.height = 600, 95
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('white')
        self.fps = 100
        self.v = 1
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
            self.clock.tick(self.fps)
            self.display.flip()


class Hero(pg.sprite.Sprite):
    image = pg.image.load('data//car.png')

    def __init__(self, game, size, *group):
        super().__init__(*group)
        self.game = game
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (size[0] // 2) - (self.rect.width // 2), (size[1] // 2) - (self.rect.height // 2)
        self.m = 0

    def check_pos(self):
        x = self.rect.x
        w = self.rect.w
        speed = self.game.v
        if self.m == 0:
            if x + speed + w > self.game.width:
                self.image = pg.transform.flip(self.image, self.rect.x, self.rect.y)
                self.m = 1
                return False
        if self.m == 1:
            if x - speed < 0:
                self.image = pg.transform.flip(self.image, self.rect.x + self.rect.w, self.rect.y)
                self.m = 0
                return False
        return True

    def move(self):
        speed = self.game.v
        if self.m == 0 and self.check_pos():
            self.rect.x += speed
        if self.m == 1 and self.check_pos():
            self.rect.x -= speed


if __name__ == '__main__':
    game = Game()
