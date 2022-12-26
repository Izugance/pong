import pygame

from settings import Settings


class Ball:
    """Pong ball representation."""

    def __init__(self, pong):
        self.settings = Settings()
        self.settings.obj_color = (255, 0, 0)
        self.scr = pong.scr
        self.scr_rect = self.scr.get_rect()
        self.radius = self.settings.ball_radius
        self.x, self.y = self.scr_rect.center
        self.x_vel = self.settings.ball_vel
        self.y_vel = 0

    def reset(self):
        """Reset position and velocity metrics."""
        self.x, self.y = self.scr_rect.center
        self.x_vel *= -1
        self.y_vel = 0

    def move(self):
        """Move the ball's position based on the velocity."""
        self.x += self.x_vel
        self.y += self.y_vel

    def y_vel_by_red_factor(self, paddle):
        """
        Update upward velocity based on where the ball hits the paddle.
        """
        middle_y = paddle.y + self.settings.paddle_height / 2
        difference_in_y = middle_y - self.y
        reduction_factor = (self.settings.paddle_height / 2) / self.settings.ball_vel
        y_vel = difference_in_y / reduction_factor
        self.y_vel = -1 * y_vel

    def draw(self):
        """Draw the ball on the screen."""
        pygame.draw.circle(
            self.scr,
            self.settings.obj_color,
            (self.x, self.y),
            self.settings.ball_radius,
        )
