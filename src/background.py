"""Module containing classes to manage game background elements like Sky and Ground."""
import pygame


class Background:
    """Base class for all background objects in the game."""
    def __init__(self, filename, pos_x, pos_y, screen):
        """Initialize background with image, position, and screen reference."""
        self.screen = screen
        self.surface = pygame.image.load(f"../assets/Game Objects/{filename}")
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_width(self):
        """Return the width of the background surface."""
        return self.width

    def get_height(self):
        """Return the height of the background surface."""
        return self.height

    def get_pos_x(self):
        """Return the current X position."""
        return self.pos_x

    def get_pos_y(self):
        """Return the current Y position."""
        return self.pos_y

    def draw(self):
        """Abstract method to draw the object on the screen."""
        pass


class Sky(Background):
    """Class representing the sky background layer."""
    def __init__(self, filename, pos_X, pos_Y, screen):
        """Initialize the sky layer using the parent Background class."""
        super().__init__(filename, pos_X, pos_Y, screen)

    def draw(self):
        """Blit the sky surface onto the screen."""
        self.screen.blit(self.surface, (self.pos_x, self.pos_y))


class Ground(Background):
    """Class representing the scrolling ground with movement logic."""
    def __init__(self, filename, pos_x, sky_height, screen):
        """Initialize the ground and calculate its vertical position."""
        super().__init__(filename, pos_x, 0, screen)
        self.pos_y = sky_height - self.get_height()

    def draw(self):
        """Blit the ground surface onto the screen."""
        self.screen.blit(self.surface, (self.pos_x, self.pos_y))

    def move(self, velocity):
        """Update the X position to create a scrolling effect."""
        self.pos_x -= velocity
        if abs(self.pos_x) > (self.width / 7):
            self.pos_x = 0

    def update(self, velocity):
        """Draw the ground and move it according to game velocity."""
        self.draw()
        self.move(velocity)
