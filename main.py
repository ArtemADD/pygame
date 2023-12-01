import pygame as pg

LEFT_UP = 1
LEFT_DOWN = 2
RIGHT_DOWN = 3
RIGHT_UP = 4


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Пра-пра-пра-крестики-нолики')
        self.size = self.width, self.height = 501, 501
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.v = 5
        self.board = Board(5, 7)
        self.board.set_view(100, 100, 50)
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
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.board.get_click(event.pos)
            self.screen.fill('black')
            self.board.render(self.screen)
            self.clock.tick(self.fps)
            self.display.flip()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.hod = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 0:
                    pg.draw.rect(screen, 'black', (self.left + (self.cell_size * i), self.top + (self.cell_size * j),
                                                   self.cell_size, self.cell_size))
                elif self.board[j][i] == 1:
                    pg.draw.line(screen, 'red', (self.left + (self.cell_size * i) + 2,
                                 self.top + (self.cell_size * j) + 2),
                                 (self.left + (self.cell_size * (i + 1)) - 4,
                                 self.top + (self.cell_size * (j + 1)) - 4), 1)
                    pg.draw.line(screen, 'red', (self.left + (self.cell_size * (i + 1)) - 4,
                                 self.top + (self.cell_size * j) + 2),
                                 (self.left + (self.cell_size * i) + 2,
                                 self.top + (self.cell_size * (j + 1)) - 4), 1)
                elif self.board[j][i] == 2:
                    pg.draw.ellipse(screen, 'blue', (self.left + (self.cell_size * i) + 2,
                                    self.top + (self.cell_size * j) + 2,
                                    self.cell_size - 4, self.cell_size - 4), 1)
                pg.draw.rect(screen, 'white', (self.left + (self.cell_size * i), self.top + (self.cell_size * j),
                             self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        for i in range(self.width):
            for j in range(self.height):
                if (mouse_pos[0] in range(self.left + i * self.cell_size,
                                          self.left + (i + 1) * self.cell_size)
                        and mouse_pos[1] in range(self.top + j * self.cell_size,
                                                  self.top + (j + 1) * self.cell_size)):
                    return i, j
        return None

    def on_click(self, cell_coords):
        x = cell_coords[0]
        y = cell_coords[1]
        if self.board[y][x] != 0:
            pass
        elif self.hod == 0:
            self.hod = 1
            self.board[y][x] = 1
        elif self.hod == 1:
            self.hod = 0
            self.board[y][x] = 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    game = Game()
