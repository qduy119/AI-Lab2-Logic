import Cell
from ActionEnum import Action

def BacktrackingSearchAlgorithm(self):
    if self.agent_cell.exist_pit():
        self.AddAction(Action.FALL_INTO_PIT)
        return False

    if self.agent_cell.exist_wumpus():
        self.AddAction(Action.BE_EATEN_BY_WUMPUS)
        return False

    if self.agent_cell.exist_gold():
        self.AddAction(Action.GRAB_GOLD)
        self.agent_cell.grab_gold()

    if self.agent_cell.exist_breeze():
        self.AddAction(Action.PERCEIVE_BREEZE)

    if self.agent_cell.exist_stench():
        self.AddAction(Action.PERCEIVE_STENCH)

    if not self.agent_cell.is_explored():
        self.agent_cell.explore()
        self.AddNewPerceptIntoKB(self.agent_cell)

    valid_adj_cell_list = self.agent_cell.get_adj_cell_list(self.cell_matrix)

    temp_adj_cell_list = []
    if self.agent_cell.parent in valid_adj_cell_list:
        valid_adj_cell_list.remove(self.agent_cell.parent)

    pre_agent_cell = self.agent_cell

    if not self.agent_cell.is_OK():
        temp_adj_cell_list = []
        for valid_adj_cell in valid_adj_cell_list:
            if valid_adj_cell.is_explored() and valid_adj_cell.exist_pit():
                temp_adj_cell_list.append(valid_adj_cell)
        for adj_cell in temp_adj_cell_list:
            valid_adj_cell_list.remove(adj_cell)

        temp_adj_cell_list = []

        if self.agent_cell.exist_stench():
            valid_adj_cell: Cell.Cell
            for valid_adj_cell in valid_adj_cell_list:
                print("Infer: ", end="")
                print(valid_adj_cell.map_pos)
                self.AppendEventToOutputFile(
                    "Infer: " + str(valid_adj_cell.map_pos)
                )
                self.DirectionMove(valid_adj_cell)

                self.AddAction(Action.INFER_WUMPUS)
                not_alpha = [[valid_adj_cell.get_literal(Cell.Object.WUMPUS, "-")]]
                have_wumpus = self.KB.infer(not_alpha)

                if have_wumpus:
                    self.AddAction(Action.DETECT_WUMPUS)
                    self.AddAction(Action.SHOOT)
                    self.AddAction(Action.KILL_WUMPUS)
                    valid_adj_cell.kill_wumpus(self.cell_matrix, self.KB)
                    self.AppendEventToOutputFile("KB: " + str(self.KB.KB))

                else:
                    self.AddAction(Action.INFER_NOT_WUMPUS)
                    not_alpha = [
                        [valid_adj_cell.get_literal(Cell.Object.WUMPUS, "+")]
                    ]
                    have_no_wumpus = self.KB.infer(not_alpha)

                    if have_no_wumpus:
                        self.AddAction(Action.DETECT_NO_WUMPUS)
                    else:
                        if valid_adj_cell not in temp_adj_cell_list:
                            temp_adj_cell_list.append(valid_adj_cell)

        if self.agent_cell.exist_stench():
            adj_cell_list = self.agent_cell.get_adj_cell_list(self.cell_matrix)
            if self.agent_cell.parent in adj_cell_list:
                adj_cell_list.remove(self.agent_cell.parent)

            explored_cell_list = []
            for adj_cell in adj_cell_list:
                if adj_cell.is_explored():
                    explored_cell_list.append(adj_cell)
            for explored_cell in explored_cell_list:
                adj_cell_list.remove(explored_cell)

            for adj_cell in adj_cell_list:
                print("Try: ", end="")
                print(adj_cell.map_pos)
                self.AppendEventToOutputFile("Try: " + str(adj_cell.map_pos))
                self.DirectionMove(adj_cell)

                self.AddAction(Action.SHOOT)
                if adj_cell.exist_wumpus():
                    self.AddAction(Action.KILL_WUMPUS)
                    adj_cell.kill_wumpus(self.cell_matrix, self.KB)
                    self.AppendEventToOutputFile("KB: " + str(self.KB.KB))

                if not self.agent_cell.exist_stench():
                    self.agent_cell.update_child_list([adj_cell])
                    break

        if self.agent_cell.exist_breeze():
            valid_adj_cell: Cell.Cell
            for valid_adj_cell in valid_adj_cell_list:
                print("Infer: ", end="")
                print(valid_adj_cell.map_pos)
                self.AppendEventToOutputFile(
                    "Infer: " + str(valid_adj_cell.map_pos)
                )
                self.DirectionMove(valid_adj_cell)

                self.AddAction(Action.INFER_PIT)
                not_alpha = [[valid_adj_cell.get_literal(Cell.Object.PIT, "-")]]
                have_pit = self.KB.infer(not_alpha)

                if have_pit:
                    self.AddAction(Action.DECTECT_PIT)
                    valid_adj_cell.explore()
                    self.AddNewPerceptIntoKB(valid_adj_cell)
                    valid_adj_cell.update_parent(valid_adj_cell)
                    temp_adj_cell_list.append(valid_adj_cell)

                else:
                    self.AddAction(Action.INFER_NOT_PIT)
                    not_alpha = [[valid_adj_cell.get_literal(Cell.Object.PIT, "+")]]
                    have_no_pit = self.KB.infer(not_alpha)

                    if have_no_pit:
                        self.AddAction(Action.DETECT_NO_PIT)

                    else:
                        temp_adj_cell_list.append(valid_adj_cell)

    temp_adj_cell_list = list(set(temp_adj_cell_list))

    for adj_cell in temp_adj_cell_list:
        valid_adj_cell_list.remove(adj_cell)
    self.agent_cell.update_child_list(valid_adj_cell_list)

    for next_cell in self.agent_cell.child_list:
        self.MoveTo(next_cell)
        print("Move to: ", end="")
        print(self.agent_cell.map_pos)
        self.AppendEventToOutputFile("Move to: " + str(self.agent_cell.map_pos))

        if not BacktrackingSearchAlgorithm(self):
            return False

        self.MoveTo(pre_agent_cell)
        print("Backtrack: ", end="")
        print(pre_agent_cell.map_pos)
        self.AppendEventToOutputFile(
            "Backtrack: " + str(pre_agent_cell.map_pos)
        )

    return True