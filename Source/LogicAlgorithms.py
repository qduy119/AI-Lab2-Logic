
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
        self.agent_cell = None
        self.init_agent_cell = None
        self.KB = KnowledgeBase.KnowledgeBase()
        self.path = []
        self.action_list = []
        self.score = 0

        self.ReadMap(map_filename)

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
                if Cell.Object.AGENT.value in raw_map[ir][ic]:
                    self.agent_cell = self.cell_matrix[ir][ic]
                    self.agent_cell.update_parent(self.cave_cell)
                    self.init_agent_cell = copy.deepcopy(self.agent_cell)

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
        if self.agent_cell is None:
            return False, None
        return True, None

    def AppendEventToOutputFile(self, text: str):
        out_file = open(self.output_filename, "a")
        out_file.write(text + "\n")
        out_file.close()

    def AddAction(self, action):
        AddActionLogic(self, action)

    def AddNewPerceptIntoKB(self, cell):
        AddPerceptToKnowledgeBase(self, cell)

    def DirectionMove(self, next_cell):
        if next_cell.map_pos[0] == self.agent_cell.map_pos[0]:
            if next_cell.map_pos[1] - self.agent_cell.map_pos[1] == 1:
                self.AddAction(Action.TURN_UP)
            else:
                self.AddAction(Action.TURN_DOWN)
        elif next_cell.map_pos[1] == self.agent_cell.map_pos[1]:
            if next_cell.map_pos[0] - self.agent_cell.map_pos[0] == 1:
                self.AddAction(Action.TURN_RIGHT)
            else:
                self.AddAction(Action.TURN_LEFT)
        else:
            raise TypeError("Error: " + self.DirectionMove.__name__)

    def MoveTo(self, next_cell):
        self.DirectionMove(next_cell)
        self.AddAction(Action.MOVE_FORWARD)
        self.agent_cell = next_cell

    def BacktrackingSearch(self):
        BacktrackingSearchAlgorithm(self)

    def SolveWumpusWorld(self):
        out_file = open(self.output_filename, "w")
        out_file.close()

        self.BacktrackingSearch()

        victory_flag = True
        for cell_row in self.cell_matrix:
            for cell in cell_row:
                if cell.exist_gold() or cell.exist_wumpus():
                    victory_flag = False
                    break
        if victory_flag:
            self.AddAction(Action.KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD)

        if self.agent_cell.parent == self.cave_cell:
            self.AddAction(Action.CLIMB_OUT_OF_THE_CAVE)

        return self.action_list, self.init_agent_cell, self.init_cell_matrix
