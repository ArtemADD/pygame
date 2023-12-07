import pygame as pg
from random import randint


class Game:
    def __init__(self):
        self.n = 8  # int(input())
        pg.init()
        pg.display.set_caption('Недореверси')
        self.size = self.width, self.height = 40 + (self.n * 30), 40 + (self.n * 30)
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.v = 5
        self.fps = 30
        self.board = Board(self.n, self.n)
        self.board.set_view(20, 20, 30)
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
            self.board.check()
            self.clock.tick(self.fps)
            self.display.flip()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[randint(0, 1) for _ in range(width)] for __ in range(height)]
        print(self.board)
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
                    pg.draw.ellipse(screen, 'blue', (self.left + (self.cell_size * i) + 2,
                                    self.top + (self.cell_size * j) + 2,
                                    self.cell_size - 4, self.cell_size - 4))
                elif self.board[j][i] == 1:
                    pg.draw.ellipse(screen, 'red', (self.left + (self.cell_size * i) + 2,
                                    self.top + (self.cell_size * j) + 2,
                                    self.cell_size - 4, self.cell_size - 4))
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
        print(x, y)
        print(self.board[y][x])
        print(self.hod)
        if self.hod == 0:
            if self.board[y][x] == 1:
                self.hod = 1
                self.fill_x(cell_coords)
                self.fill_y(cell_coords)
                print('red')
        else:
            if self.board[y][x] == 0:
                self.hod = 0
                self.fill_x(cell_coords)
                self.fill_y(cell_coords)
                print('blue')

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def fill_x(self, cell):
        x = cell[0]
        y = cell[1]
        c = self.board[y][x]
        for i in range(self.width):
            if self.board[y][i] != c:
                self.board[y][i] = c

    def fill_y(self, cell):
        x = cell[0]
        y = cell[1]
        c = self.board[y][x]
        for i in range(self.width):
            if self.board[i][x] != c:
                self.board[i][x] = c


if __name__ == '__main__':
    game = Game()
