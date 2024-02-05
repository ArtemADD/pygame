import sys
import pygame as pg


def read_points_from_file(file_path):
    with open(file_path, 'r') as file:
        points_str = file.read()
    points_str = points_str.replace('(', '').replace(')', '')
    points = [tuple(map(lambda x: float(x.replace(',', '.')), point.split(';'))) for point in points_str.split(', ')]
    return points


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Zoom')
        self.size = self.width, self.height = 501, 501
        self.screen = pg.display.set_mode(self.size)
        self.display = pg.display
        self.screen.fill('black')
        self.fps = 100
        self.clock = pg.time.Clock()
        self.points = read_points_from_file('points.txt')
        self.scale = 20
        self.run()
        pg.quit()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Колесо вверх
                        self.scale *= 1.1
                    elif event.button == 5:  # Колесо вниз
                        self.scale /= 1.1
            self.screen.fill('black')
            self.draw_polygon([(int(x * self.scale) + self.width // 2, int(-y * self.scale) + self.height // 2)
                               for x, y in self.points])
            self.clock.tick(self.fps)
            self.display.flip()

    def draw_polygon(self, points):
        pg.draw.polygon(self.screen, 'white', points, 1)


if __name__ == '__main__':
    game = Game()
    sys.exit()
