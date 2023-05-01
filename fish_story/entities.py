import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, image="character0.png", entity_x=0, entity_y=0, MAX_WIN_WIDTH=900, MAX_WIN_HEIGHT=600, MIN_WIN_WIDTH=0, MIN_WIN_HEIGHT=0, velocity_x=30, velocity_y=15):
        super().__init__()
        from utils import load_sprite
        self.image = load_sprite(image, True)
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.rect.x = entity_x
        self.rect.y = entity_y
        self._change_x = 0
        self._change_y = 0
        self._MAX_WIN_WIDTH = MAX_WIN_WIDTH
        self._MAX_WIN_HEIGHT = MAX_WIN_HEIGHT
        self._MIN_WIN_WIDTH = MIN_WIN_WIDTH
        self._MIN_WIN_HEIGHT = MIN_WIN_HEIGHT
        self._velocity_x = velocity_x
        self._velocity_y = velocity_y

        # List of sprites we can bump against
        self.level = None

    def update(self):
        self.rect.y += self._change_y
        self.rect.x += self._change_x
        if self.rect.x < self._MIN_WIN_WIDTH:
            self.rect.x = self._MIN_WIN_WIDTH
        if self.rect.right > self._MAX_WIN_WIDTH:
            self.rect.x = self._MAX_WIN_WIDTH  # - self.rect.width
        if self.rect.y < self._MIN_WIN_HEIGHT:
            self.rect.y = self._MIN_WIN_HEIGHT
        if self.rect.y > self._MAX_WIN_HEIGHT:
            self.rect.y = self._MAX_WIN_HEIGHT  # - self.rect.height

        self._change_x = 0
        self._change_y = 0

    def update_velocity_x(self, vel_x):
        self._velocity_x = vel_x

    def update_velocity_y(self, vel_y):
        self._velocity_y = vel_y

    def go_left(self):
        self._change_x = -self._velocity_x

    def go_right(self):
        self._change_x = self._velocity_x

    def go_up(self):
        self._change_y = -self._velocity_y

    def go_down(self):
        self._change_y = self._velocity_y
