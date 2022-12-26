import pygame

from settings import Settings


class Paddle:
    """Pong paddle representation."""

    def __init__(self, pong, left=True):
        self.settings = Settings()
        self.scr = pong.scr
        self.scr_rect = self.scr.get_rect()
        self.width = self.settings.paddle_width
        self.height = self.settings.paddle_height
        self.left = left
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.moving_up = False
        self.moving_down = False
        self.reset()

    def reset(self):
        """Reset the paddle to the midpoint of the screen's side."""
        if self.left:
            self.rect.midleft = (
                self.scr_rect.midleft[0] + 10,
                self.scr_rect.midright[1],
            )
        else:
            self.rect.midright = (
                self.scr_rect.midright[0] - 10,
                self.scr_rect.midright[1],
            )
        self.y = float(self.rect.y)

    def move(self):
        """Move the paddle's position."""
        if self.moving_up and self.rect.top >= self.scr_rect.top:
            self.y -= self.settings.paddle_vel
        if self.moving_down and self.rect.bottom <= self.scr_rect.bottom:
            self.y += self.settings.paddle_vel
        self.rect.y = self.y

    def draw(self):
        """Draw the paddle on the screen."""
        pygame.draw.rect(self.scr, self.settings.obj_color, self.rect)
