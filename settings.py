from dataclasses import dataclass

from pygame import font


class Settings:
    """Configurable settings for the game."""

    def __init__(self):
        self.font = font.SysFont("comicsans", 50)

        # Screen concerns.
        self.scr_width = 700
        self.scr_height = 500
        self.bg_color = (0, 0, 0)
        self.obj_color = (255, 255, 255)

        # Paddle concerns.
        self.paddle_width = 20
        self.paddle_height = 100
        self.paddle_vel = 0.5

        # Ball concerns.
        self.ball_radius = 7
        self.ball_vel = 0.35  # 0.2

        # Score concerns.
        self.winning_score = 10
