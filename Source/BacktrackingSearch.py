import Cell
from ActionEnum import Action

def BacktrackingSearchAlgorithm(self):

    if self.AgentCell.exist_gold():
        self.AddAction(Action.GRAB_GOLD)
        self.AgentCell.grab_gold()


    if self.AgentCell.exist_wumpus():
        self.AddAction(Action.BE_EATEN_BY_WUMPUS)
        return False

    if not self.AgentCell.is_explored():
        self.AgentCell.explore()
        self.AddNewPerceptIntoKB(self.AgentCell)

    if self.AgentCell.exist_breeze():
        self.AddAction(Action.PERCEIVE_BREEZE)

    if self.AgentCell.exist_stench():
        self.AddAction(Action.PERCEIVE_STENCH)


    if self.AgentCell.exist_pit():
        self.AddAction(Action.FALL_INTO_PIT)
        return False

    ValidAdjCellList = self.AgentCell.get_adj_cell_list(self.cell_matrix)

    TempAdjCellList = []
    if self.AgentCell.parent in ValidAdjCellList:
        ValidAdjCellList.remove(self.AgentCell.parent)

    pre_agent_cell = self.AgentCell

    if not self.AgentCell.is_OK():
        TempAdjCellList = []
        for ValidAdjCell in ValidAdjCellList:
            if ValidAdjCell.is_explored() and ValidAdjCell.exist_pit():
                TempAdjCellList.append(ValidAdjCell)
        for AdjCell in TempAdjCellList:
            ValidAdjCellList.remove(AdjCell)

        TempAdjCellList = []

        if self.AgentCell.exist_stench():
            ValidAdjCell: Cell.Cell
            for ValidAdjCell in ValidAdjCellList:
                print("Infer: ", end="")
                print(ValidAdjCell.map_pos)
                self.AppendEventToOutputFile(
                    "Infer: " + str(ValidAdjCell.map_pos)
                )
                self.DirectionMove(ValidAdjCell)

                self.AddAction(Action.INFER_WUMPUS)
                not_alpha = [[ValidAdjCell.get_literal(Cell.Object.WUMPUS, "-")]]
                have_wumpus = self.KB.infer(not_alpha)

                if have_wumpus:
                    self.AddAction(Action.DETECT_WUMPUS)
                    self.AddAction(Action.SHOOT)
                    self.AddAction(Action.KILL_WUMPUS)
                    ValidAdjCell.kill_wumpus(self.cell_matrix, self.KB)
                    self.AppendEventToOutputFile("KB: " + str(self.KB.KB))

                else:
                    self.AddAction(Action.INFER_NOT_WUMPUS)
                    not_alpha = [
                        [ValidAdjCell.get_literal(Cell.Object.WUMPUS, "+")]
                    ]
                    have_no_wumpus = self.KB.infer(not_alpha)

                    if have_no_wumpus:
                        self.AddAction(Action.DETECT_NO_WUMPUS)
                    else:
                        if ValidAdjCell not in TempAdjCellList:
                            TempAdjCellList.append(ValidAdjCell)

        if self.AgentCell.exist_stench():
            AdjCellList = self.AgentCell.get_adj_cell_list(self.cell_matrix)
            if self.AgentCell.parent in AdjCellList:
                AdjCellList.remove(self.AgentCell.parent)

            explored_cell_list = []
            for AdjCell in AdjCellList:
                if AdjCell.is_explored():
                    explored_cell_list.append(AdjCell)
            for explored_cell in explored_cell_list:
                AdjCellList.remove(explored_cell)

            for AdjCell in AdjCellList:
                print("Try: ", end="")
                print(AdjCell.map_pos)
                self.AppendEventToOutputFile("Try: " + str(AdjCell.map_pos))
                self.DirectionMove(AdjCell)

                self.AddAction(Action.SHOOT)
                if AdjCell.exist_wumpus():
                    self.AddAction(Action.KILL_WUMPUS)
                    AdjCell.kill_wumpus(self.cell_matrix, self.KB)
                    self.AppendEventToOutputFile("KB: " + str(self.KB.KB))

                if not self.AgentCell.exist_stench():
                    self.AgentCell.update_child_list([AdjCell])
                    break

        if self.AgentCell.exist_breeze():
            ValidAdjCell: Cell.Cell
            for ValidAdjCell in ValidAdjCellList:
                print("Infer: ", end="")
                print(ValidAdjCell.map_pos)
                self.AppendEventToOutputFile(
                    "Infer: " + str(ValidAdjCell.map_pos)
                )
                self.DirectionMove(ValidAdjCell)

                self.AddAction(Action.INFER_PIT)
                not_alpha = [[ValidAdjCell.get_literal(Cell.Object.PIT, "-")]]
                have_pit = self.KB.infer(not_alpha)

                if have_pit:
                    self.AddAction(Action.DECTECT_PIT)
                    ValidAdjCell.explore()
                    self.AddNewPerceptIntoKB(ValidAdjCell)
                    ValidAdjCell.update_parent(ValidAdjCell)
                    TempAdjCellList.append(ValidAdjCell)

                else:
                    self.AddAction(Action.INFER_NOT_PIT)
                    not_alpha = [[ValidAdjCell.get_literal(Cell.Object.PIT, "+")]]
                    have_no_pit = self.KB.infer(not_alpha)

                    if have_no_pit:
                        self.AddAction(Action.DETECT_NO_PIT)

                    else:
                        TempAdjCellList.append(ValidAdjCell)

    TempAdjCellList = list(set(TempAdjCellList))

    for AdjCell in TempAdjCellList:
        ValidAdjCellList.remove(AdjCell)
    self.AgentCell.update_child_list(ValidAdjCellList)

    for next_cell in self.AgentCell.child_list:
        self.MoveTo(next_cell)
        print("Move to: ", end="")
        print(self.AgentCell.map_pos)
        self.AppendEventToOutputFile("Move to: " + str(self.AgentCell.map_pos))

        if not BacktrackingSearchAlgorithm(self):
            return False

        self.MoveTo(pre_agent_cell)
        print("Backtrack: ", end="")
        print(pre_agent_cell.map_pos)
        self.AppendEventToOutputFile(
            "Backtrack: " + str(pre_agent_cell.map_pos)
        )

    return True