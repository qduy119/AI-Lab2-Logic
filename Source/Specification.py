import pygame

# Speed
SPEED = 100

# Window
SCREEN_WIDTH = 970
SCREEN_HEIGHT = 710
CAPTION = 'Wumpus World'

# Cell
IMG_INITIAL_CELL = '../Assets/Images/initial_cell.png'
IMG_DISCOVERED_CELL = '../Assets/Images/discovered_cell.png'

# Object
IMG_WUMPUS_LOGO = '../Assets/Images/wumpus_logo.png'
IMG_PIT = '../Assets/Images/pit.png'
IMG_WUMPUS = '../Assets/Images/wumpus.png'
IMG_GOLD = '../Assets/Images/gold.png'
IMG_WINNER='../Assets/Images/win.png'
IMG_BG= '../Assets/Images/bg.jpg'

# Hunter
IMG_AGENT_RIGHT = '../Assets/Images/agent_right.png'
IMG_AGENT_LEFT = '../Assets/Images/agent_left.png'
IMG_AGENT_UP = '../Assets/Images/agent_up.png'
IMG_AGENT_DOWN = '../Assets/Images/agent_down.png'

IMG_WEAPON_RIGHT = '../Assets/Images/weapon_right.png'
IMG_WEAPON_LEFT = '../Assets/Images/weapon_left.png'
IMG_WEAPON_UP = '../Assets/Images/weapon_up.png'
IMG_WEAPON_DOWN = '../Assets/Images/weapon_down.png'

# Map
MAP_LIST = ['../Assets/Input/map_1.txt',
            '../Assets/Input/map_2.txt',
            '../Assets/Input/map_3.txt',
            '../Assets/Input/map_4.txt',
            '../Assets/Input/map_5.txt']
MAP_NUM = len(MAP_LIST)

# Output
OUTPUT_LIST = ['../Assets/Output/result_1.txt',
               '../Assets/Output/result_2.txt',
               '../Assets/Output/result_3.txt',
               '../Assets/Output/result_4.txt',
               '../Assets/Output/result_5.txt']

# Fonts
FONT_MRSMONSTER = '../Assets/Fonts/mrsmonster.ttf'

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREY = (150, 150, 150)
DARK_GREY = (190, 190, 190)
RED = (0, 0, 0)

# state
HOME = 'home'
ABOUT = 'about'
RUNNING = 'running'
GAMEOVER = 'gameover'
WIN = 'win'
TRYBEST = 'trybest'
MAP = 'map'

PLAY_POS = pygame.Rect(235, 380, 500, 50)
ABOUT_POS = pygame.Rect(235, 460, 500, 50)
EXIT_POS = pygame.Rect(235, 540, 500, 50)

LEVEL_1_POS = pygame.Rect(235, 120, 500, 50)
LEVEL_2_POS = pygame.Rect(235, 200, 500, 50)
LEVEL_3_POS = pygame.Rect(235, 280, 500, 50)
LEVEL_4_POS = pygame.Rect(235, 360, 500, 50)
LEVEL_5_POS = pygame.Rect(235, 440, 500, 50)
BACK_POS = pygame.Rect(760, 550, 100, 50)

TITLE_POS = pygame.Rect(235, 120, 500, 50)
MEMBER_1_POS = pygame.Rect(235, 220, 500, 30)
MEMBER_2_POS = pygame.Rect(235, 280, 500, 30)
MEMBER_3_POS = pygame.Rect(235, 340, 500, 30)
MEMBER_4_POS = pygame.Rect(235, 400, 500, 30)
MEMBER_5_POS = pygame.Rect(235, 460, 500, 30)
MEMBER_BACK_POS = pygame.Rect(235, 540, 500, 50)