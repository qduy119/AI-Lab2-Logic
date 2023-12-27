import pygame
from ActionEnum import Action
from Specification import *
def DisplayActionLogic(self, action):
    if action == Action.TURN_LEFT:
        self.direct = self.agent.turn_left()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
    elif action == Action.TURN_RIGHT:
        self.direct = self.agent.turn_right()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
    elif action == Action.TURN_UP:
        self.direct = self.agent.turn_up()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
    elif action == Action.TURN_DOWN:
        self.direct = self.agent.turn_down()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
    elif action == Action.MOVE_FORWARD:
        self.agent.move_forward(self.direct)
        i, j = self.agent.get_pos()
        self.map.discover_cell_i_j(i, j)
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
    elif action == Action.GRAB_GOLD:
        self.agent.grab_gold()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        self.gold.grab_gold(self.screen, self.font)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
        pygame.time.delay(500)
    elif action == Action.PERCEIVE_BREEZE:
        pass
    elif action == Action.PERCEIVE_STENCH:
        pass
    elif action == Action.SHOOT:
        self.agent.shoot()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        i, j = self.agent.get_pos()
        self.arrow.Shoot(self.direct, self.screen, i, j)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
        pygame.time.delay(500)
    elif action == Action.KILL_WUMPUS:

        i, j = self.agent.get_pos()
        if self.direct == 0:
            i -= 1
        elif self.direct == 1:
            i += 1
        elif self.direct == 2:
            j -= 1
        elif self.direct == 3:
            j += 1
        self.wumpus.wumpus_killed(i, j)
        self.wumpus.wumpus_notification()
        i, j = self.agent.get_pos()
        if not self.wumpus.stench_i_j(i, j):
            self.wumpus.wumpus_kill(self.screen, self.font)
        temp = self.map.discovered()
        self.wumpus.update(self.screen, self.noti, temp)
        self.pit.update(self.screen, self.noti, temp)
        pygame.display.update()
        pygame.time.delay(500)
        pass
    elif action == Action.KILL_NO_WUMPUS:
        pass
    elif action == Action.BE_EATEN_BY_WUMPUS:
        self.agent.wumpus_or_pit_collision()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        self.state = GAMEOVER
    elif action == Action.FALL_INTO_PIT:
        self.agent.wumpus_or_pit_collision()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        self.state = GAMEOVER
    elif action == Action.KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD:
        #
        self.state = WIN
        pass
    elif action == Action.CLIMB_OUT_OF_THE_CAVE:
        self.agent.climb()
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        self.map.agent_climb(self.screen, self.font)
        pygame.display.update()
        pygame.time.delay(2000)
    elif action == Action.DECTECT_PIT:
        i, j = self.agent.get_pos()
        if self.direct == 0:
            i -= 1
        elif self.direct == 1:
            i += 1
        elif self.direct == 2:
            j -= 1
        elif self.direct == 3:
            j += 1
        self.map.pit_detect(i, j)
        self.all_sprites.update()
        self.RunningDraw()
        self.all_sprites.draw(self.screen)
        pygame.time.delay(1000)
    elif action == Action.DETECT_WUMPUS:
        pass
    elif action == Action.DETECT_NO_PIT:
        pass
    elif action == Action.DETECT_NO_WUMPUS:
        pass
    elif action == Action.INFER_PIT:
        pass
    elif action == Action.INFER_NOT_PIT:
        pass
    elif action == Action.INFER_WUMPUS:
        pass
    elif action == Action.INFER_NOT_WUMPUS:
        pass
    elif action == Action.DETECT_SAFE:
        pass
    elif action == Action.INFER_SAFE:
        pass
    else:
        raise TypeError("Error: " + self.DisplayAction.__name__)