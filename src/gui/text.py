import pygame as pg

from data.config import OPEN


class Text:
    """Widget that stores text on multiple lines. """
    def __init__(self, x, y, font, font_size, color, align=0, width_limit=9001):
        pg.font.init()
        self.font_name = font
        self.font = pg.font.Font(font, font_size)
        self.x = x
        self.y = y
        self.h = 0
        self.w = 0
        self.color = color
        self.align = align
        self.width_limit = width_limit
        self.lines = []   # list of text surfaces with their coords
        self.text = None


    def set_font_size(self, font_size):
        pg.font.init()
        self.font = pg.font.Font(self.font_name, font_size)

    def replace_with(self, text_widget):
        self.lines = text_widget.lines

    def clear(self):
        self.lines = []

    def set_text(self, text=''):
        """Receives a string as input and makes a list of text
        surfaces with their coords.
        """
        self.text = text
        self.lines = []
        letter_height = self.font.size('A')[1]
        current_string = ''
        for i, word in enumerate(text.split() + ['@$']):
            new_word = (' ' if i else '') + word
            line_width = self.font.size(current_string + new_word)[0]
            if word == '@$' or (line_width > self.width_limit and current_string != ''):
                # make new surface with line of text and append it with its coords to the list of surfaces
                line = self.font.render(current_string.replace('~', ' '), True, self.color)

                if self.align == 0: x = 0
                elif self.align == 1: x = -line.get_width() / 2
                else: x = -line.get_width()
                y = len(self.lines) * letter_height
                self.lines.append([line, x, y])
                current_string = word
            else:
                current_string += new_word
        self.h = letter_height * len(self.lines)
        self.w = max(line.get_width() for line,_,_ in self.lines)

    def set_alpha(self, alpha):
        """Sets alpha-value for all text surfaces. """
        for surface, _, _ in self.lines:
            surface.set_alpha(alpha)

    def update_alpha(self, animation_state, time_elapsed):
        if animation_state == OPEN:
            alpha = round(255 * time_elapsed)
        else:
            alpha = round(255 - 255 * time_elapsed)
        self.set_alpha(alpha)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, dx=0, dy=0):
        for surface, x, y in self.lines:
            screen.blit(surface, (round(self.x + x - dx), round(self.y + y - dy)))


__all__ = ["Text"]
