from settings import Settings


class Score:
    def __init__(self, pong):
        self.settings = Settings()
        self.scr = pong.scr
        self.reset_score()

    def reset_score(self):
        """Reset score statistics."""
        self.score = 0

    def draw(self, left=True):
        """Draw the score on the screen."""
        score_text = self.settings.font.render(
            f"{self.score}", 1, self.settings.obj_color
        )
        if left:
            self.scr.blit(
                score_text,
                (self.settings.scr_width // 4 - score_text.get_width() // 2, 20),
            )
        else:
            self.scr.blit(
                score_text,
                (self.settings.scr_width * (3 / 4) - score_text.get_width() // 2, 20),
            )
