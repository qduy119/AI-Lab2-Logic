
import copy
import Cell
import KnowledgeBase
from BacktrackingSearch import * 
from AddPerceptToKnowledgeBase import *
from ActionEnum import Action
from AddAction import *

class AgentBrain:
    def __init__(self, map_filename, output_filename):
        self.output_filename = output_filename
        self.map_size = None
        self.cell_matrix = None
        self.init_cell_matrix = None

        self.cave_cell = Cell.Cell((-1, -1), 10, Cell.Object.EMPTY.value)
        self.AgentCell = None
        self.wumpus_list = []
        self.gold_list = []

        self.init_agent_cell = None
        self.KB = KnowledgeBase.KnowledgeBase()
        self.path = []
        self.action_list = []
        self.score = 0

        self.ReadMap(map_filename)

    def BacktrackingSearch(self):
        BacktrackingSearchAlgorithm(self)

    def SolveWumpusWorld(self):
        OutputFile = open(self.output_filename, "w")
        OutputFile.close()

        self.BacktrackingSearch()

        WinFlag = True
        '''for row in self.cell_matrix:
            for cell in row:
                if cell.exist_gold() or cell.exist_wumpus():
                    WinFlag = False
                    break
        if WinFlag:
            self.AddAction(Action.KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD)
'''
        if self.AgentCell.parent == self.cave_cell:
            self.AddAction(Action.CLIMB_OUT_OF_THE_CAVE)

        return self.action_list, self.init_agent_cell, self.init_cell_matrix

    def AddNewPerceptIntoKB(self, cell):
        AddPerceptToKnowledgeBase(self, cell)


    def AppendEventToOutputFile(self, text: str):
        OutputFile = open(self.output_filename, "a")
        OutputFile.write(text + "\n")
        OutputFile.close()

    def AddAction(self, action):
        AddActionLogic(self, action)


    def DirectionMove(self, next_cell):
        if next_cell.map_pos[0] == self.AgentCell.map_pos[0]:
            if next_cell.map_pos[1] - self.AgentCell.map_pos[1] == 1:
                self.AddAction(Action.TURN_UP)
            else:
                self.AddAction(Action.TURN_DOWN)
        elif next_cell.map_pos[1] == self.AgentCell.map_pos[1]:
            if next_cell.map_pos[0] - self.AgentCell.map_pos[0] == 1:
                self.AddAction(Action.TURN_RIGHT)
            else:
                self.AddAction(Action.TURN_LEFT)
        else:
            raise TypeError("Error: " + self.DirectionMove.__name__)

    def MoveTo(self, next_cell):
        self.DirectionMove(next_cell)
        self.AddAction(Action.MOVE_FORWARD)
        self.AgentCell = next_cell


    def ReadMap(self, map_filename):
        file = open(map_filename, "r")

        self.map_size = int(file.readline())
        raw_map = [line.split(".") for line in file.read().splitlines()]

        self.cell_matrix = [
            [None for _ in range(self.map_size)] for _ in range(self.map_size)
        ]
        for ir in range(self.map_size):
            for ic in range(self.map_size):
                self.cell_matrix[ir][ic] = Cell.Cell(
                    (ir, ic), self.map_size, raw_map[ir][ic]
                )
                if self.cell_matrix[ir][ic].exist_gold():
                    self.gold_list.append(self.cell_matrix[ir][ic])
                if self.cell_matrix[ir][ic].exist_wumpus():
                    self.wumpus_list.append(self.cell_matrix[ir][ic])
                if Cell.Object.AGENT.value in raw_map[ir][ic]:
                    self.AgentCell = self.cell_matrix[ir][ic]
                    self.AgentCell.update_parent(self.cave_cell)
                    self.init_agent_cell = copy.deepcopy(self.AgentCell)

        file.close()
        self.init_cell_matrix = copy.deepcopy(self.cell_matrix)

        result, pos = self.IsValidMap()
        if not result:
            if pos is None:
                raise TypeError("Input Error: The map is invalid! There is no Agent!")
            raise TypeError(
                "Input Error: The map is invalid! Please check at row "
                + str(pos[0])
                + " and column "
                + str(pos[1])
                + "."
            )
        
    def IsValidMap(self):
        for cell_row in self.cell_matrix:
            for cell in cell_row:
                adj_cell_list = cell.get_adj_cell_list(self.cell_matrix)
                if cell.exist_pit():
                    for adj_cell in adj_cell_list:
                        if not adj_cell.exist_breeze():
                            return False, cell.matrix_pos
                if cell.exist_wumpus():
                    for adj_cell in adj_cell_list:
                        if not adj_cell.exist_stench():
                            return False, cell.matrix_pos
        if self.AgentCell is None:
            return False, None
        return True, None
