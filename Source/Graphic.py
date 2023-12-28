import sys
from Map import *
from Agent import *
import LogicAlgorithms
from DisplayActionLogic import *

class Graphic:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load(IMG_BG).convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.logo = pygame.image.load(IMG_WUMPUS_LOGO).convert()
        self.caption = pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.map = None
        self.agent = None
        self.gold = None
        self.wumpus = None
        self.pit = None
        self.arrow = None
        self.font = pygame.font.Font(FONT_MRSMONSTER, 30)
        self.noti = pygame.font.Font(FONT_MRSMONSTER, 15)
        self.victory = pygame.font.Font(FONT_MRSMONSTER, 50)
        self.all_sprites = pygame.sprite.Group()

        self.state = HOME
        self.map_i = 1
        self.mouse = None
        self.bg = pygame.image.load(IMG_WINNER).convert()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.direct = 3

        self.message = ""

    def running_draw(self):
        self.screen.blit(self.background, (0, 0))
        self.map.draw(self.screen)
        score = self.agent.get_score()
        text = self.font.render('Your score: ' + str(score), True, WHITE)
        textRect = text.get_rect()
        textRect.center = (830, 50)
        self.screen.blit(text, textRect)

    def DrawButton(self, surf, rect, button_color, text_color, text):
        pygame.draw.rect(surf, button_color, rect)
        text_surf = self.font.render(text, True, text_color)
        text_rect = text_surf.get_rect()
        text_rect.center = rect.center
        self.screen.blit(text_surf, text_rect)
    def map_draw(self):
        self.screen.fill(WHITE)

    def home_draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.logo, (410, 50))

    def home_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 235 <= self.mouse[0] <= 735 and 380 <= self.mouse[1] <= 430:
                    self.state = MAP
                elif 235 <= self.mouse[0] <= 735 and 460 <= self.mouse[1] <= 510:
                    self.state = ABOUT
                elif 235 <= self.mouse[0] <= 735 and 540 <= self.mouse[1] <= 590:
                    pygame.quit()
                    sys.exit()

            self.mouse = pygame.mouse.get_pos()
            if 235 <= self.mouse[0] <= 735 and 380 <= self.mouse[1] <= 430:
                self.DrawButton(self.screen, PLAY_POS, DARK_GREY, RED, "PLAY")
            else:
                self.DrawButton(self.screen, PLAY_POS, LIGHT_GREY, BLACK, "PLAY")
            if 235 <= self.mouse[0] <= 735 and 460 <= self.mouse[1] <= 510:
                self.DrawButton(self.screen, ABOUT_POS, DARK_GREY, RED, "ABOUT US")
            else:
                self.DrawButton(self.screen, ABOUT_POS, LIGHT_GREY, BLACK, "ABOUT US")
            if 235 <= self.mouse[0] <= 735 and 540 <= self.mouse[1] <= 590:
                self.DrawButton(self.screen, EXIT_POS, DARK_GREY, RED, "EXIT")
            else:
                self.DrawButton(self.screen, EXIT_POS, LIGHT_GREY, BLACK, "EXIT")
            pygame.display.update()

    def draw_info(self, text, text_color, rect):
        text_surf = self.font.render(text, True, text_color)
        text_rect = text_surf.get_rect()
        text_rect.center = rect.center
        self.screen.blit(text_surf, text_rect)

    def about_draw(self):
        self.screen.fill(WHITE)
        self.draw_info('GROUP MEMBERS', BLACK, TITLE_POS)
        self.draw_info('21120184 - LE THI MINH THU', BLACK, MEMBER_1_POS)
        self.draw_info('21120198 - NGUYEN THI LAN ANH', BLACK, MEMBER_2_POS)
        self.draw_info('21120408 - Dang Tuan Anh', BLACK, MEMBER_3_POS)
        self.draw_info('21120426 - Huynh Phat Dat', BLACK, MEMBER_4_POS)
        self.draw_info('21120440 - Chu Quang Duy', BLACK, MEMBER_5_POS)
        self.DrawButton(self.screen, MEMBER_BACK_POS, LIGHT_GREY, BLACK, "BACK")

    def about_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 235 <= self.mouse[0] <= 735 and 540 <= self.mouse[1] <= 590:
                    self.state = HOME

        self.mouse = pygame.mouse.get_pos()
        if 235 <= self.mouse[0] <= 735 and 540 <= self.mouse[1] <= 590:
            self.DrawButton(self.screen, MEMBER_BACK_POS, DARK_GREY, RED, "BACK")
        else:
            self.DrawButton(self.screen, MEMBER_BACK_POS, LIGHT_GREY, BLACK, "BACK")
        pygame.display.update()

    def map_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 235 <= self.mouse[0] <= 735 and 120 <= self.mouse[1] <= 170:
                    self.state = RUNNING
                    self.map_i = 1
                elif 235 <= self.mouse[0] <= 735 and 200 <= self.mouse[1] <= 250:
                    self.state = RUNNING
                    self.map_i = 2
                elif 235 <= self.mouse[0] <= 735 and 280 <= self.mouse[1] <= 330:
                    self.state = RUNNING
                    self.map_i = 3
                elif 235 <= self.mouse[0] <= 735 and 360 <= self.mouse[1] <= 410:
                    self.state = RUNNING
                    self.map_i = 4
                elif 235 <= self.mouse[0] <= 735 and 440 <= self.mouse[1] <= 490:
                    self.state = RUNNING
                    self.map_i = 5
                elif 760 <= self.mouse[0] <= 860 and 550 <= self.mouse[1] <= 600:
                    self.state = HOME

            self.mouse = pygame.mouse.get_pos()
            if 235 <= self.mouse[0] <= 735 and 120 <= self.mouse[1] <= 170:
                self.DrawButton(self.screen, LEVEL_1_POS, DARK_GREY, RED, "MAP 1")
            else:
                self.DrawButton(self.screen, LEVEL_1_POS, LIGHT_GREY, BLACK, "MAP 1")
            if 235 <= self.mouse[0] <= 735 and 200 <= self.mouse[1] <= 250:
                self.DrawButton(self.screen, LEVEL_2_POS, DARK_GREY, RED, "MAP 2")
            else:
                self.DrawButton(self.screen, LEVEL_2_POS, LIGHT_GREY, BLACK, "MAP 2")
            if 235 <= self.mouse[0] <= 735 and 280 <= self.mouse[1] <= 330:
                self.DrawButton(self.screen, LEVEL_3_POS, DARK_GREY, RED, "MAP 3")
            else:
                self.DrawButton(self.screen, LEVEL_3_POS, LIGHT_GREY, BLACK, "MAP 3")
            if 235 <= self.mouse[0] <= 735 and 360 <= self.mouse[1] <= 410:
                self.DrawButton(self.screen, LEVEL_4_POS, DARK_GREY, RED, "MAP 4")
            else:
                self.DrawButton(self.screen, LEVEL_4_POS, LIGHT_GREY, BLACK, "MAP 4")
            if 235 <= self.mouse[0] <= 735 and 440 <= self.mouse[1] <= 490:
                self.DrawButton(self.screen, LEVEL_5_POS, DARK_GREY, RED, "MAP 5")
            else:
                self.DrawButton(self.screen, LEVEL_5_POS, LIGHT_GREY, BLACK, "MAP 5")
            if 760 <= self.mouse[0] <= 860 and 550 <= self.mouse[1] <= 600:
                self.DrawButton(self.screen, BACK_POS, DARK_GREY, RED, "BACK")
            else:
                self.DrawButton(self.screen, BACK_POS, LIGHT_GREY, BLACK, "BACK")

            pygame.display.update()

    def DrawStatusWin(self):
        self.screen.blit(self.bg, (0, 0))

        if self.state == WIN:
            text = self.victory.render('VICTORY!!!', True, WHITE)
        elif self.state == TRYBEST:
            text = self.victory.render('TRY BEST!!!', True, WHITE)
        textRect = text.get_rect()
        textRect.center = (500, 50)
        self.screen.blit(text, textRect)

        text = self.victory.render(self.message, True, BLACK)        
        textRect.center = (350, 125)
        self.screen.blit(text, textRect)
        
        score = self.agent.GetPoint()
        text = self.victory.render('Your score: ' + str(score), True, WHITE)
        textRect.center = (450, 100)
        self.screen.blit(text, textRect)

    def EventWin(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.state = MAP
        pygame.display.update()
        pygame.time.delay(200)
        self.state = HOME

    def Running(self):
        while True:
            if self.state == HOME:
                self.home_draw()
                self.home_event()
            elif self.state == ABOUT:
                self.about_draw()
                self.about_event()
            elif self.state == MAP:
                self.map_draw()
                self.map_event()
            elif self.state == RUNNING:
                self.state = TRYBEST

                action_list, cave_cell, cell_matrix = LogicAlgorithms.AgentBrain(MAP_LIST[self.map_i - 1], OUTPUT_LIST[self.map_i - 1]).SolveWumpusWorld()
                map_pos = cave_cell.map_pos

                self.map = Map((len(cell_matrix) - map_pos[1] + 1, map_pos[0]))
                self.arrow = Arrow()
                self.gold = Gold()
                self.agent = Agent(len(cell_matrix) - map_pos[1] + 1, map_pos[0])
                self.agent.load_image()
                self.all_sprites = pygame.sprite.Group()
                self.all_sprites.add(self.agent)

                x = []
                y = []
                for ir in range(len(cell_matrix)):
                    for ic in range(len(cell_matrix)):
                        if cell_matrix[ir][ic].exist_pit():
                            x.append(ir)
                            y.append(ic)
                self.pit = Pit(x, y)
                self.pit.pit_notification()

                x = []
                y = []
                for ir in range(len(cell_matrix)):
                    for ic in range(len(cell_matrix)):
                        if cell_matrix[ir][ic].exist_wumpus():
                            x.append(ir)
                            y.append(ic)
                self.wumpus = Wumpus(x, y)
                self.wumpus.wumpus_notification()

                self.RunningDraw()

                for action in action_list:
                    pygame.time.delay(SPEED)
                    self.DisplayAction(action)

                    if action == LogicAlgorithms.Action.KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD:
                        self.state = WIN


                    if action == LogicAlgorithms.Action.FALL_INTO_PIT or action == LogicAlgorithms.Action.BE_EATEN_BY_WUMPUS:
                        self.state = GAMEOVER
                        break

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

            elif self.state == WIN or self.state == TRYBEST:
                self.DrawStatusWin()
                self.EventWin()

            self.clock.tick(60)

    def DisplayAction(self, action: LogicAlgorithms.Action):
       DisplayActionLogic(self, action)
        
    def RunningDraw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        score = self.agent.GetPoint()
        text = self.font.render('Score: ' + str(score), True, BLACK)
        textRect = text.get_rect()
        textRect.center = (820, 25)
        self.screen.blit(text, textRect)
