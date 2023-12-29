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
    elif action == Action.GO_STRAIGHT:
        self.score -= 10
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.GET_GOLD:
        self.score += 100
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.PERCEIVE_BREEZE:
        pass
    elif action == Action.SMELL_STENCH:
        pass
    elif action == Action.SHOOT:
        self.score -= 100
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.KILL_WUMPUS:
        pass
    elif action == Action.WUMPUS_NOT_KILLED:
        pass
    elif action == Action.EATEN_BY_WUMPUS:
        self.score -= 10000
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.FALL_IN_HOLE:
        self.score -= 10000
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.KILL_ALL_WUMPUS_AND_GRAB_ALL_GOLD:
        pass
    elif action == Action.ESCAPE_FROM_THE_CAVE:
        self.score += 10
        print("Score: " + str(self.score))
        self.AppendEventToOutputFile("Score: " + str(self.score))
    elif action == Action.FIND_HOLE:
        pass
    elif action == Action.FIND_WUMPUS:
        pass
    elif action == Action.HOLE_NOT_FOUND:
        pass
    elif action == Action.WUMPUS_NOT_FOUND:
        pass
    elif action == Action.INFER_HOLE:
        pass
    elif action == Action.HOLE_NOT_INFERRED:
        pass
    elif action == Action.INFER_WUMPUS:
        pass
    elif action == Action.WUMPUS_NOT_INFERRED:
        pass
    elif action == Action.SAFE_FOUND:
        pass
    elif action == Action.INFER_SAFE:
        pass
    else:
        raise TypeError("Error: " + self.add_action.__name__)