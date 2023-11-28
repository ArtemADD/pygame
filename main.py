import pygame as pg

LEFT_UP = 1
LEFT_DOWN = 2
RIGHT_DOWN = 3
RIGHT_UP = 4


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Шарики')
        self.size = self.width, self.height = 400, 200
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('blue')
        self.display = pg.display
        self.v = 5
        self.balls = []
        self.fps = 30
        self.clock = pg.time.Clock()
        self.draw_balls = False
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == pg.BUTTON_LEFT:
                        self.draw_balls = True
                        self.balls.append(Ball(event.pos, self.v, self.screen))
            self.screen.fill('black')
            self.draw()
            self.clock.tick(self.fps)
            self.display.flip()

    def draw(self):
        if self.draw_balls:
            for ball in self.balls:
                ball.move()
                ball.draw()


class Ball:
    def __init__(self, pos, v, screen, m=LEFT_UP):
        self.r = 10
        self.screen = screen
        self.pos = list(pos)
        self.x, self.y = pos
        self.v = v
        self.color = 'white'
        self.moving = m

    def move(self):
        if self.moving == LEFT_UP:
            self.x -= self.v
            self.y -= self.v
        if self.moving == LEFT_DOWN:
            self.x -= self.v
            self.y += self.v
        if self.moving == RIGHT_UP:
            self.x += self.v
            self.y -= self.v
        if self.moving == RIGHT_DOWN:
            self.x += self.v
            self.y += self.v
        self.ball_touch_wall()

    def ball_touch_wall(self):
        r = self.r
        h = self.screen.get_height()
        w = self.screen.get_width()
        if self.x - r < 0 and self.moving == LEFT_UP:
            self.moving = RIGHT_UP
            self.x = r
        elif self.y - r < 0 and self.moving == LEFT_UP:
            self.moving = LEFT_DOWN
            self.y = r
        elif self.x - r < 0 and self.moving == LEFT_DOWN:
            self.moving = RIGHT_DOWN
            self.x = r
        elif self.y + r > h and self.moving == LEFT_DOWN:
            self.moving = LEFT_UP
            self.y = h - r
        elif self.x + r > w and self.moving == RIGHT_UP:
            self.moving = LEFT_UP
            self.x = w - r
        elif self.y - r < 0 and self.moving == RIGHT_UP:
            self.moving = RIGHT_DOWN
            self.y = r
        elif self.x + r > w and self.moving == RIGHT_DOWN:
            self.moving = LEFT_DOWN
            self.x = w - r
        elif self.y + r > h and self.moving == RIGHT_DOWN:
            self.moving = RIGHT_UP
            self.y = h - r
        self.pos = [self.x, self.y]

    def draw(self):
        pg.draw.circle(self.screen, self.color, self.pos, self.r)


if __name__ == '__main__':
    game = Game()
