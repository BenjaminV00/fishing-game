import pygame
import sys


class Fishing_game:
    def __init__(self):
        pygame.init()
        # creating display
        display = pygame.display.set_mode((300, 300))

    def main_loop(self):
        while True:
            self._handle_input()
            # self._game_logic()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    print("a")

                if event.key == pygame.K_s:
                    print("s")

                if event.key == pygame.K_d:
                    print("d")

                if event.key == pygame.K_w:
                    print("w")
