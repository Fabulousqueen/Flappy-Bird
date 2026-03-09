import pygame


class Background:

    def __init__(self, filename, pos_X, pos_Y, screen):
        self.screen = screen
        self.surface = pygame.image.load(f"../assets/Game Objects/{filename}")
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.pos_X = pos_X
        self.pos_Y = pos_Y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_pos_X(self):
        return self.pos_X

    def get_pos_Y(self):
        return self.pos_Y

    def draw(self):
        pass


class Sky(Background):

    def __init__(self, filename, pos_X, pos_Y, screen):
        super().__init__(filename, pos_X, pos_Y, screen)

    def draw(self):
        self.screen.blit(self.surface, (self.pos_X, self.pos_Y))


class Ground(Background):

    def __init__(self, filename, pos_X, sky_height, screen):
        super().__init__(filename, pos_X, 0, screen)
        self.pos_Y = sky_height - self.get_height()

    def draw(self):
        self.screen.blit(self.surface, (self.pos_X, self.pos_Y))

    def move(self, velocity):
        self.pos_X -= velocity
        if abs(self.pos_X) > (self.width / 7):
            self.pos_X = 0

    def update(self, velocity):
        self.draw()
        self.move(velocity)
