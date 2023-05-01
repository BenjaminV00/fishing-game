import pygame
from entities import Entity


class Menu():
    def __init__(self, menu_size_x=900, menu_size_y=300, menu_loc_x=0, menu_loc_y=600, option_list=list(),
                 border_color=(255, 255, 255), menu_bg_color=(100, 155, 100)):
        self._option_list = option_list
        self._menu_size_x = menu_size_x
        self._menu_size_y = menu_size_y
        self._menu_loc_x = menu_loc_x
        self._menu_loc_y = menu_loc_y
        self._border_color = border_color
        self._bg_color = menu_bg_color
        self._FONT_SIZE = 32
        self._items_to_be_drawn = dict()

        # vertical space between each menu option
        self._menu_option_cushion_between = self._menu_size_y / \
            (len(self._option_list))
        # vertical space before the first menu option
        self._menu_option_cushion_top = self._menu_size_y / \
            (len(self._option_list) * 2)
        # horizontal space before left side of menu options
        menu_cushion_factor_left = 0.1
        self._menu_option_cushion_left = self._menu_size_x * menu_cushion_factor_left

        space_between_text_and_cursor = 25
        # initial x, y positions for the cursor
        cursor_init_x = self._menu_loc_x + \
            self._menu_option_cushion_left - space_between_text_and_cursor
        cursor_init_y = (self._menu_loc_y + (self._menu_option_cushion_top - (
            self._FONT_SIZE / 2)))

        # maximum y position for the cursor
        cursor_max_y = (self._menu_loc_y + (self._menu_option_cushion_top - (
            self._FONT_SIZE / 2)) + (self._menu_option_cushion_between * (len(self._option_list)-1)))

        # create cursor Entity object
        self.cursor = Entity(image="menu-cursor.gif",
                             entity_x=cursor_init_x, entity_y=cursor_init_y, MAX_WIN_HEIGHT=cursor_max_y, MIN_WIN_HEIGHT=cursor_init_y, velocity_y=self._menu_option_cushion_between)
        self.current_option = 1

    def check_and_draw(self, surface):
        self._check_menu_option_position()
        self._draw(surface)

    def _check_menu_option_position(self):
        if self.current_option < 1:
            self.current_option = 1
        if self.current_option > len(self._option_list):
            self.current_option = len(self._option_list)

    def _draw(self, surface):
        # Draw the menu and menu options
        # draw rectangle with filled in color
        pygame.draw.rect(surface, self._bg_color, pygame.Rect(
            self._menu_loc_x, self._menu_loc_y, self._menu_size_x, self._menu_size_y), 0, 3)
        # draw rectangle with border
        pygame.draw.rect(surface, self._border_color, pygame.Rect(
            self._menu_loc_x, self._menu_loc_y, self._menu_size_x, self._menu_size_y), 5, 3)

        # find the correct positions for all menu options
        self._set_positions_for_menu_options()
        # draw all menu options
        for menu_text, menu_text_rect in self._items_to_be_drawn.items():
            surface.blit(menu_text, menu_text_rect)

        # update the cursor and draw it
        self.cursor.update()
        # debug print
        # print(self.current_option)
        surface.blit(self.cursor.image, self.cursor.rect)
        # empty the items_to_be_drawn dict
        self._items_to_be_drawn.clear()
        pygame.display.flip()

    def _set_positions_for_menu_options(self):
        # tries to set the menu positions based on the menu size
        COMBAT_FONT = "freesansbold.ttf"
        font = pygame.font.Font(COMBAT_FONT, self._FONT_SIZE)

        white = (255, 255, 255)
        green = (0, 255, 0)
        light_green = (100, 255, 100)
        blue = (0, 0, 128)

        # find all the x, y coordinates for the menu options
        for item_count, item in enumerate(self._option_list):
            # create the two items that we will add to the draw dictionary
            menu_option = font.render(item, True, white)
            menu_option_rect = menu_option.get_rect()
            # determine the x, y coord for each option
            font_w, font_h = font.size(item)
            menu_option_rect.x = self._menu_loc_x + self._menu_option_cushion_left
            menu_option_rect.y = (self._menu_loc_y + (self._menu_option_cushion_top - (
                font_h / 2)) + (self._menu_option_cushion_between * item_count))
            # add each item to the draw dict
            self._items_to_be_drawn[menu_option] = menu_option_rect
