import pygame
import sys
from utils import load_sprite, State, Menu
from entities import Player

WINDOW_NAME = "Fish Story"
DEFAULT_WORLD_BG = "blue_bg"
DEFAULT_COMBAT_BG = "green_bg"
DEFAULT_WORLD_SPRITE = ""
DEFAULT_COMBAT_SPRITE = ""
DEFAULT_STATE = "combat"

PLAYER_SPRITE = ""


class Fishing_game:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 900, 900
        player_x, player_y = 0, 0
        self.screen = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_NAME)
        self.background = load_sprite(DEFAULT_WORLD_BG, False)
        self.player_sprite_world = Player(player_x, player_y)
        self.game_state = State(DEFAULT_STATE)
        self.combat_menu = Menu(menu_loc_x=0, menu_loc_y=self.WINDOW_HEIGHT*(2/3),
                                option_list=["FIGHT", "SKILLS", "MAGIC", "ITEM"])

    def main_loop(self):
        while True:
            self._check_game_state()
            self._handle_input()
            # self._game_logic()
            self._draw()
            pygame.display.update()

    def _check_game_state(self):
        # change bg depending on the game state
        if self.game_state.state == "world":
            self.background = load_sprite("blue_bg", False)
        elif self.game_state.state == "combat":
            self.background = load_sprite(DEFAULT_COMBAT_BG, False)

        if self.game_state.state == "world":
            self.player_sprite_world.image = load_sprite("character0", True)
        elif self.game_state.state == "combat":
            self.player_sprite_world.image = load_sprite("character1", True)

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if self.game_state.state == "combat":
                        self.game_state.state = "world"
                    elif self.game_state.state == "world":
                        self.game_state.state = "combat"
                if event.key == pygame.K_a:
                    self.player_sprite_world.go_left()
                if event.key == pygame.K_s:
                    self.player_sprite_world.go_down()
                if event.key == pygame.K_d:
                    self.player_sprite_world.go_right()
                if event.key == pygame.K_w:
                    self.player_sprite_world.go_up()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        if self.game_state.state == "world":
            self.player_sprite_world.update()
        self.screen.blit(self.player_sprite_world.image,
                         (self.player_sprite_world.rect.x, self.player_sprite_world.rect.y))
        if self.game_state.state == "combat":
            self.combat_menu.draw(self.screen)

        pygame.display.flip()
