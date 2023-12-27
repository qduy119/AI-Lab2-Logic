
from ActionEnum import Action

def AddActionLogic(self, action):
    self.action_list.append(action)
    print(action)
    self.AppendEventToOutputFile(action.name)

    if action == Action.TURN_LEFT:
        pass
    elif action == Action.TURN_RIGHT:
        pass
    elif action == Action.TURN_UP:
        pass
    elif action == Action.TURN_DOWN:
        pass
    elif action == Action.MOVE_FORWARD:
        self.score -= 10
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.GRAB_GOLD:
        self.score += 100
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.PERCEIVE_BREEZE:
        pass
    elif action == Action.PERCEIVE_STENCH:
        pass
    elif action == Action.SHOOT:
        self.score -= 100
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.KILL_WUMPUS:
        pass
    elif action == Action.KILL_NO_WUMPUS:
        pass
    elif action == Action.BE_EATEN_BY_WUMPUS:
        self.score -= 10000
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.FALL_INTO_PIT:
        self.score -= 10000
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD:
        pass
    elif action == Action.CLIMB_OUT_OF_THE_CAVE:
        self.score += 10
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.DECTECT_PIT:
        pass
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
        raise TypeError("Error: " + self.add_action.__name__)