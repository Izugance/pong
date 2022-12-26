import sys
import time

import pygame

from settings import Settings
from paddle import Paddle
from ball import Ball
from score import Score


class Pong:
    """Representation of the Pong game."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.scr = pygame.display.set_mode(
            (self.settings.scr_width, self.settings.scr_height)
        )
        pygame.display.set_caption("Pong!")

        self.left_paddle = Paddle(self)
        self.right_paddle = Paddle(self, left=False)
        self.ball = Ball(self)
        self.left_score = Score(self)
        self.right_score = Score(self)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.left_paddle.moving_up = True
        elif event.key == pygame.K_s:
            self.left_paddle.moving_down = True

        if event.key == pygame.K_UP:
            self.right_paddle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.right_paddle.moving_down = True

        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.left_paddle.moving_up = False
        elif event.key == pygame.K_s:
            self.left_paddle.moving_down = False

        if event.key == pygame.K_UP:
            self.right_paddle.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.right_paddle.moving_down = False

    def _draw_center_line(self):
        pygame.draw.rect(
            self.scr,
            self.settings.obj_color,
            (self.settings.scr_width // 2 - 5, 10, 10, self.settings.scr_height - 20),
        )

    def _handle_ball_collisions(self):
        if self.ball.y - self.ball.radius <= 0:
            self.ball.y_vel *= -1
        elif self.ball.y + self.ball.radius >= self.settings.scr_height:
            self.ball.y_vel *= -1

        if self.ball.x_vel < 0:
            if (
                self.ball.y >= self.left_paddle.rect.y
                and self.ball.y <= self.left_paddle.rect.y + self.left_paddle.height
            ):
                if (
                    self.ball.x - self.ball.radius
                    <= self.left_paddle.rect.x + self.left_paddle.width
                ):
                    self.ball.x_vel *= -1
                    self.ball.y_vel_by_red_factor(self.left_paddle.rect)
        else:
            if (
                self.ball.y >= self.right_paddle.rect.y
                and self.ball.y <= self.right_paddle.rect.y + self.right_paddle.height
            ):
                if self.ball.x + self.ball.radius >= self.right_paddle.rect.x:
                    self.ball.x_vel *= -1
                    self.ball.y_vel_by_red_factor(self.right_paddle.rect)

    def _handle_resets(self, ball, left_paddle, right_paddle):
        ball.reset()
        left_paddle.reset()
        right_paddle.reset()

    def _handle_scoring(self):
        if self.ball.x + self.ball.radius <= -0.1:
            self.right_score.score += 1
            self._handle_resets(self.ball, self.left_paddle, self.right_paddle)
            time.sleep(0.5)
        elif self.ball.x - self.ball.radius >= self.settings.scr_width + 0.1:
            self.left_score.score += 1
            self._handle_resets(self.ball, self.left_paddle, self.right_paddle)
            time.sleep(0.5)

    def _handle_win(self):
        win = False
        if self.left_score.score >= self.settings.winning_score:
            win_msg = "Left Player Won!"
            win = True
        elif self.right_score.score >= self.settings.winning_score:
            win_msg = "Right Player Won!"
            win = True

        if win:
            win_text = self.settings.font.render(win_msg, True, self.settings.obj_color)
            self.scr.blit(
                win_text,
                (
                    self.settings.scr_width // 2 - win_text.get_width() // 2,
                    self.settings.scr_height // 2 - win_text.get_height() // 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(5000)
            self._handle_resets(self.ball, self.left_paddle, self.right_paddle)
            self.left_score.reset_score()
            self.right_score.reset_score()

    def check_events(self):
        """Handle keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def update_screen(self):
        """Draw objects on the screen based on recent game actions."""
        self.scr.fill(self.settings.bg_color)
        self.left_paddle.draw()
        self.right_paddle.draw()
        self._draw_center_line()
        self.ball.draw()
        self.left_score.draw()
        self.right_score.draw(left=False)
        self._handle_ball_collisions()
        self._handle_scoring()
        self._handle_win()

        pygame.display.flip()

    def play(self):
        """The game's main loop."""
        while True:
            self.check_events()
            self.left_paddle.move()
            self.right_paddle.move()
            self.ball.move()
            self.update_screen()


if __name__ == "__main__":
    Pong().play()
