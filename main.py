import pygame as pg


MY_EVENT_TYPE = pg.USEREVENT + 1


class Life:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Игра Жизнь')
        self.size = self.width, self.height = 30 + 30 * 15, 30 + 30 * 15
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill('black')
        self.display = pg.display
        self.board = Board(30, 30)
        self.fps = 60
        self.time = 1000
        pg.time.set_timer(MY_EVENT_TYPE, self.time)
        self.clock = pg.time.Clock()
        self.start = False
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == pg.BUTTON_LEFT and self.start is False:
                        self.board.get_click(event.pos)
                    elif event.button == pg.BUTTON_RIGHT:
                        if self.start is False:
                            self.start = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if self.start is False:
                            self.start = True
                        else:
                            self.start = False
                if event.type == pg.MOUSEWHEEL:
                    self.time += event.y * 100
                    if self.time <= 0:
                        self.time = 1
                    pg.time.set_timer(MY_EVENT_TYPE, self.time)
                if self.start is True and event.type == MY_EVENT_TYPE:
                    self.board.next_move()
            self.screen.fill('black')
            self.board.render(self.screen)
            self.clock.tick(self.fps)
            pg.display.set_caption(f'Игра "Жизнь"  Скорость: {self.time / 1000 :.1f} сек')
            self.display.flip()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 15
        self.top = 15
        self.cell_size = 15

    def next_move(self):
        b = [self.board[_].copy() for _ in range(len(self.board))]
        for j, row in enumerate(self.board):
            for i, value in enumerate(row):
                n = self.get_neighbors([i, j])
                if n == 3:
                    b[j][i] = 1
                elif n != 2:
                    b[j][i] = 0
        self.board = b.copy()

    def get_neighbors(self, coord):
        x, y = coord
        n = 0
        for i in range(8):
            try:
                if x == 0:
                    x = self.width + 10
                if y == 0:
                    y = self.width + 10
                if i == 0:
                    if self.board[y - 1][x - 1] == 1:
                        n += 1
                elif i == 1:
                    if self.board[y - 1][x] == 1:
                        n += 1
                elif i == 2:
                    if self.board[y - 1][x + 1] == 1:
                        n += 1
                elif i == 3:
                    if self.board[y][x - 1] == 1:
                        n += 1
                elif i == 4:
                    if self.board[y][x + 1] == 1:
                        n += 1
                elif i == 5:
                    if self.board[y + 1][x - 1] == 1:
                        n += 1
                elif i == 6:
                    if self.board[y + 1][x] == 1:
                        n += 1
                elif i == 7:
                    if self.board[y + 1][x + 1] == 1:
                        n += 1
            finally:
                continue
        return n

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for j in range(self.width):
            for i in range(self.height):
                if self.board[j][i] == 1:
                    pg.draw.rect(screen, 'green', (self.left + (self.cell_size * i), self.top + (self.cell_size * j),
                                                   self.cell_size, self.cell_size))
                pg.draw.rect(screen, 'white', (self.left + (self.cell_size * i), self.top + (self.cell_size * j),
                             self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        for j in range(self.width):
            for i in range(self.height):
                if (mouse_pos[0] in range(self.left + i * self.cell_size,
                                          self.left + (i + 1) * self.cell_size)
                        and mouse_pos[1] in range(self.top + j * self.cell_size,
                                                  self.top + (j + 1) * self.cell_size)):
                    return i, j
        return None

    def on_click(self, cell_coords):
        x = cell_coords[0]
        y = cell_coords[1]
        if self.board[y][x] == 0:
            self.board[y][x] = 1
        else:
            self.board[y][x] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    game = Life()
