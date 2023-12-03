import pygame as pg

RIGHT_UP = 1
LEFT_UP = 2
LEFT_DOWN = 3
RIGHT_DOWN = 4
LINE = 5


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('К щелчку')
        self.size = self.width, self.height = 501, 501
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.v = 5
        self.circle = Circle(20, (self.width // 2, self.height // 2), self.v)
        self.fps = 30
        self.clock = pg.time.Clock()
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.circle.go_to(event.pos)
            self.screen.fill('black')
            self.draw()
            self.clock.tick(self.fps)
            self.display.flip()

    def draw(self):
        self.circle.draw(self.screen)


class Circle:
    def __init__(self, r, pos, v):
        self.r = r
        self.pos = pos
        self.v = v
        self.x, self.y = pos
        self.to_pos = 0, 0
        self.go = False

    def go_to(self, pos):
        self.to_pos = pos
        self.go = True

    def draw(self, screen):
        self.movement()
        pg.draw.circle(screen, 'red', self.pos, self.r)

    def movement(self):
        if self.go:
            m = self.define_move()
            if m is True:
                self.go = False
                return
            if m[0] == RIGHT_UP:
                self.x += self.v
                self.y -= self.v
            if m[0] == LEFT_UP:
                self.x -= self.v
                self.y -= self.v
            if m[0] == LEFT_DOWN:
                self.x -= self.v
                self.y += self.v
            if m[0] == RIGHT_DOWN:
                self.x += self.v
                self.y += self.v
            if m[0] == 5:
                if m[1] == 1:
                    self.x += self.v
                if m[1] == 2:
                    self.y -= self.v
                if m[1] == 3:
                    self.x -= self.v
                if m[1] == 4:
                    self.y += self.v
            self.x = self.speed_corrected(self.x, self.to_pos[0])
            self.y = self.speed_corrected(self.y, self.to_pos[1])
            self.pos = self.x, self.y

    def define_move(self):
        to_x = self.to_pos[0]
        to_y = self.to_pos[1]
        x = self.x
        y = self.y
        if self.pos == self.to_pos:
            return True
        if to_x > x and to_y < y:
            return RIGHT_UP, 0
        if to_x < x and to_y < y:
            return LEFT_UP, 0
        if to_x < x and to_y > y:
            return LEFT_DOWN, 0
        if to_x > x and to_y > y:
            return RIGHT_DOWN, 0
        if to_x - x > 0 and y == to_y:
            return LINE, 1
        elif to_y - y < 0 and x == to_x:
            return LINE, 2
        elif to_x - x < 0 and y == to_y:
            return LINE, 3
        elif to_y - y > 0 and x == to_x:
            return LINE, 4

    def speed_corrected(self, n, to):
        if self.v > abs(n - to):
            return to
        return n


if __name__ == '__main__':
    game = Game()
