import pygame
import sys
from utils import load_sprite, State
from entities import Entity
from menu import Menu

WINDOW_NAME = "Fish Story"
DEFAULT_WORLD_BG = "blue_bg.png"
DEFAULT_COMBAT_BG = "green_bg.png"
DEFAULT_WORLD_SPRITE = ""
DEFAULT_COMBAT_SPRITE = ""
DEFAULT_STATE = "combat"

PLAYER_SPRITE = ""


class Fishing_game:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 900, 900
        # set the initial coordinates for the player sprite in the world and in combat
        player_x_combat, player_y_combat = 0, 0
        player_x_world, player_y_world = 0, 0
        self.screen = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_NAME)
        # load the default game state background
        self.background = load_sprite(DEFAULT_WORLD_BG, False)
        # create the Player objects for each game state
        self.player_sprite_world = Entity(
            image="character0.png", entity_x=player_x_world, entity_y=player_y_world)
        self.player_sprite_combat = Entity(image="character1.png",
                                           entity_x=player_x_combat, entity_y=player_y_combat)
        # set the default game state
        self.game_state = State(DEFAULT_STATE)
        # create the combat menu Menu object
        self.combat_menu = Menu(menu_loc_x=0, menu_loc_y=self.WINDOW_HEIGHT*(2/3),
                                option_list=["FIGHT", "SKILLS", "MAGIC", "ITEM"])

    def main_loop(self):
        while True:
            # check which game state we are in and load the correct background and sprites
            self._check_game_state()
            # handle all keyboard and mouse inputs depending on the game state
            self._handle_input()
            # self._game_logic()
            # draw the sprites and backgrounds
            self._draw()
            # update all coordinates of objects to be drawn
            pygame.display.update()

    def _check_game_state(self):
        # change bg depending on the game state
        if self.game_state.state == "world":
            self.background = load_sprite("blue_bg.png", False)
        elif self.game_state.state == "combat":
            self.background = load_sprite(DEFAULT_COMBAT_BG, False)

        # change player sprite based on the game state
        if self.game_state.state == "world":
            self.player_sprite_world.image = load_sprite(
                "character0.png", True)
        elif self.game_state.state == "combat":
            self.player_sprite_combat.image = load_sprite(
                "character1.png", True)

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # handle key press inputs
            if event.type == pygame.KEYDOWN:
                # debug option to switch between game states
                if event.key == pygame.K_e:
                    if self.game_state.state == "combat":
                        self.game_state.state = "world"
                    elif self.game_state.state == "world":
                        self.game_state.state = "combat"
                # handle all world game state inputs
                if self.game_state.state == "world":
                    if event.key == pygame.K_a:
                        self.player_sprite_world.go_left()
                    if event.key == pygame.K_s:
                        self.player_sprite_world.go_down()
                    if event.key == pygame.K_d:
                        self.player_sprite_world.go_right()
                    if event.key == pygame.K_w:
                        self.player_sprite_world.go_up()
                # handle all combat game state inputs
                if self.game_state.state == "combat":
                    if event.key == pygame.K_s:
                        self.combat_menu.cursor.go_down()
                        self.combat_menu.current_option += 1
                    if event.key == pygame.K_w:
                        self.combat_menu.cursor.go_up()
                        self.combat_menu.current_option -= 1
                    if event.key == pygame.K_KP_ENTER:
                        print(
                            self.combat_menu._option_list[self.combat_menu.current_option-1] + " was selected!")

    def _draw(self):
        # draw the background
        self.screen.blit(self.background, (0, 0))

        # draw world game state objects
        if self.game_state.state == "world":
            self.player_sprite_world.update()
            self.screen.blit(self.player_sprite_world.image,
                             (self.player_sprite_world.rect.x, self.player_sprite_world.rect.y))

        # draw combat game state objects
        if self.game_state.state == "combat":
            self.player_sprite_combat.update()
            self.screen.blit(self.player_sprite_combat.image,
                             (self.player_sprite_combat.rect.x, self.player_sprite_combat.rect.y))
            # draw objects from the combat menu
            self.combat_menu.check_and_draw(self.screen)

        pygame.display.flip()
