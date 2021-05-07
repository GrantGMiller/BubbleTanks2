from pygame import display


# screen
display.init()
SCR_W, SCR_H = display.list_modes()[0]  # The height MUST be a multiple of 6!
SCR_W2 = SCR_W // 2
SCR_H2 = SCR_H // 2
SCR_SIZE = (SCR_W, SCR_H)
HEIGHT_SCALE_FACTOR = SCR_H / 960
WIDTH_SCALE_FACTOR = SCR_W / 1280

# main menu and upgrade menu
OPEN = 1
WAIT = 0
CLOSE = -1
MAIN_MENU_ANIMATION_TIME = 1500
UPGRADE_MENU_ANIMATION_TIME = 350

# upgrade buttons
UPG_BUTTON_LEFT = 0
UPG_BUTTON_CENTER = 1
UPG_BUTTON_RIGHT = 2
UPG_BUTTON_WIDE_LEFT = 3
UPG_BUTTON_WIDE_RIGHT = 4

# pause_menu
STATS_WINDOW = 0
MAP_WINDOW = 1
OPTIONS_WINDOW = 2

# popup window
WINDOW_CLOSED = 0
WINDOW_OPENING = 1
WINDOW_CLOSING = 2
WINDOW_OPENED = 3

# game
ROOM_RADIUS = int(7/6 * SCR_H)
DIST_BETWEEN_ROOMS = 2 * ROOM_RADIUS + SCR_W2
TRANSPORTATION_TIME = 600
MU = 0.00064

# room
BOSS_IS_FAR_AWAY = 0
BOSS_IN_NEIGHBOUR_ROOM = 1
BOSS_IN_CURRENT_ROOM = 2


__all__ = [

    "SCR_W",
    "SCR_H",
    "SCR_W2",
    "SCR_H2",
    "SCR_SIZE",
    "OPEN",
    "CLOSE",
    "WAIT",
    "MAIN_MENU_ANIMATION_TIME",
    "STATS_WINDOW",
    "MAP_WINDOW",
    "OPTIONS_WINDOW",
    "UPGRADE_MENU_ANIMATION_TIME",
    "ROOM_RADIUS",
    "DIST_BETWEEN_ROOMS",
    "TRANSPORTATION_TIME",
    "MU",
    "BOSS_IS_FAR_AWAY",
    "BOSS_IN_NEIGHBOUR_ROOM",
    "BOSS_IN_CURRENT_ROOM",
    "WINDOW_CLOSED",
    "WINDOW_OPENING",
    "WINDOW_CLOSING",
    "WINDOW_OPENED",
    "UPG_BUTTON_LEFT",
    "UPG_BUTTON_CENTER",
    "UPG_BUTTON_RIGHT",
    "UPG_BUTTON_WIDE_LEFT",
    "UPG_BUTTON_WIDE_RIGHT"

]
