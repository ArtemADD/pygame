import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Я слежу за тобой!')
        self.size = self.width, self.height = 200, 200
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.num = Number(self)
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.WINDOWFOCUSLOST:
                    self.num.score += 1
            self.screen.fill('black')
            self.draw()
            self.display.flip()

    def draw(self):
        self.num.draw()


class Number:
    def __init__(self, game):
        self.screen = game.screen
        self.game = game
        self.score = 1
        self.font = pg.font.Font(None, 100)

    def draw(self):
        text = self.font.render(str(self.score), True, 'red')
        pos = self.game.width // 2 - text.get_width() // 2, self.game.height // 2 - text.get_height() // 2
        self.screen.blit(text, pos)


if __name__ == '__main__':
    game = Game()
