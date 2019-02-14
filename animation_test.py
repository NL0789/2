import sys
import random
import itertools
import enum
import copy
import pygame as pg
import pygame.freetype


SCREEN_SIZE = (800, 600)


class GameTile(pg.sprite.Sprite):
    def __init__(self, tile_size, tile_color, tile_pos, font, value=0, text_color=(255, 255, 255),
                 border_color=(0, 0,0 ), border_width=20):
        super().__init__()

        self.font = font

        self.tile_size = tile_size
        self.surface = pg.Surface(tile_size)

        self.tile_color = tile_color
        self.rect = self.surface.get_rect(center=tile_pos)
        self.value = value

        self.border_color = border_color
        self.border_width = border_width

        self.text_color = text_color

        #self.label = self.font.render(str(self.value), fgcolor=(255, 255, 255))

        self.update()


    def update(self):
        self.surface.fill(self.border_color)
        surface_rect = self.surface.get_rect()
        pg.draw.rect(self.surface, self.tile_color,
                     (self.border_width, self.border_width,
                      self.tile_size[0]-2*self.border_width,
                      self.tile_size[0] - 2 * self.border_width))
        text_surf, text_rect = self.font.render(str(self.value), fgcolor=self.text_color)
        self.surface.blit(text_surf, ((surface_rect.width-text_rect.width)/2, (surface_rect.height-text_rect.height)/2))





class AnimationUI():
    BACKGROUND_COLOR = (0, 0, 0)
    TILE_COLOR_INACTIVE = (127, 127, 127)
    TILE_COLORS = [(247, 112, 137),
     (248, 118, 59),
     (210, 142, 49),
     (184, 153, 49),
     (158, 162, 49),
     (124, 170, 49),
     (49, 179, 69),
     (51, 176, 129),
     (53, 174, 155),
     (54, 172, 173),
     (55, 170, 193),
     (58, 166, 221),
     (118, 153, 245),
     (176, 135, 245),
     (224, 109, 245),
     (246, 98, 216),
     (246, 106, 179)]
    TILE_COLORS_ACTIVE = [(138, 22, 15),
     (138, 66, 15),
     (138, 109, 15),
     (123, 138, 15),
     (80, 138, 15),
     (36, 138, 15),
     (15, 138, 37),
     (15, 138, 80),
     (15, 138, 123),
     (15, 109, 138),
     (15, 65, 138),
     (15, 22, 138),
     (51, 15, 138),
     (95, 15, 138),
     (138, 15, 138),
     (138, 15, 94),
     (138, 15, 51)]


    def __init__(self, screen_size, grid_size=(4, 4)):
        pg.init()
        self.font = pg.freetype.SysFont("Arial", 48)

        self.screen_size = screen_size
        self.screen = pg.display.set_mode(self.screen_size)

        self.grid_width = min(*self.screen_size)
        self.play_area = None

        self.tiles = []

        self.running = False


    def run(self):
        self.play_area = pg.Surface((self.grid_width, self.grid_width))
        self.play_area.fill(self.BACKGROUND_COLOR)

        # Add random tiles
        num_tiles = 2
        for i in range(num_tiles):
            tile = GameTile(
                    tile_size = (100, 100), tile_color = self.TILE_COLORS[1],
                    tile_pos = (random.randint(0, self.grid_width), random.randint(0, self.grid_width)),
                    font=self.font, value=i, text_color=(255, 255, 255),
                    border_color=(255, 255, 255), border_width=10
                )
            print("Created tile: {}".format(tile))
            self.tiles.append(tile)

        self.running = True
        self._main_loop()

    def update(self):
        """Update tiles and stuff."""
        pass

    def draw(self):
        """Draw the screen."""
        self.play_area.fill(self.BACKGROUND_COLOR)
        for tile in self.tiles:
            tile.update()
            self.play_area.blit(tile.surface, tile.rect)

        self.screen.blit(self.play_area, (0, 0))
        pg.display.flip()

    def _main_loop(self):
        """Blocking main event loop."""
        while self.running:
            self.update()
            self.draw()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                        sys.exit()

                elif event.type == pg.QUIT:
                    self.running = False
                    sys.exit()

        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit()
                elif event.type == pg.QUIT:
                    sys.exit()



def main():
    animation_ui = AnimationUI(SCREEN_SIZE)
    animation_ui.run()



if __name__ == "__main__":
    main()
