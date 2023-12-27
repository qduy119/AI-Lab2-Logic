
import Cell
from ActionEnum import Action



def BacktrackingSearchAlgorithm(self):
    # If there is a Pit, Agent dies.
    if self.agent_cell.exist_pit():
        self.AddAction(Action.FALL_INTO_PIT)
        return False

    # If there is a Wumpus, Agent dies.
    if self.agent_cell.exist_wumpus():
        self.AddAction(Action.BE_EATEN_BY_WUMPUS)
        return False

    # If there is Gold, Agent grabs Gold.
    if self.agent_cell.exist_gold():
        self.AddAction(Action.GRAB_GOLD)
        self.agent_cell.grab_gold()

    # If there is Breeze, Agent perceives Breeze.
    if self.agent_cell.exist_breeze():
        self.AddAction(Action.PERCEIVE_BREEZE)

    # If there is Stench, Agent perceives Stench.
    if self.agent_cell.exist_stench():
        self.AddAction(Action.PERCEIVE_STENCH)

    # If this cell is not explored, mark this cell as explored then add new percepts to the KB.
    if not self.agent_cell.is_explored():
        self.agent_cell.explore()
        self.AddNewPerceptIntoKB(self.agent_cell)

    # Initialize valid_adj_cell_list.
    valid_adj_cell_list = self.agent_cell.get_adj_cell_list(self.cell_matrix)

    # Discard the parent_cell from the valid_adj_cell_list.
    temp_adj_cell_list = []
    if self.agent_cell.parent in valid_adj_cell_list:
        valid_adj_cell_list.remove(self.agent_cell.parent)

    # Store previos agent's cell.
    pre_agent_cell = self.agent_cell

    # If the current cell is OK (there is no Breeze or Stench), Agent move to all of valid adjacent cells.
    # If the current cell has Breeze or/and Stench, Agent infers base on the KB to make a decision.
    if not self.agent_cell.is_OK():
        # Discard all of explored cells having Pit from the valid_adj_cell_list.
        temp_adj_cell_list = []
        for valid_adj_cell in valid_adj_cell_list:
            if valid_adj_cell.is_explored() and valid_adj_cell.exist_pit():
                temp_adj_cell_list.append(valid_adj_cell)
        for adj_cell in temp_adj_cell_list:
            valid_adj_cell_list.remove(adj_cell)

        temp_adj_cell_list = []

        # If the current cell has Stench, Agent infers whether the valid adjacent cells have Wumpus.
        if self.agent_cell.exist_stench():
            valid_adj_cell: Cell.Cell
            for valid_adj_cell in valid_adj_cell_list:
                print("Infer: ", end="")
                print(valid_adj_cell.map_pos)
                self.AppendEventToOutputFile(
                    "Infer: " + str(valid_adj_cell.map_pos)
                )
                self.DirectionMove(valid_adj_cell)

                # Infer Wumpus.
                self.AddAction(Action.INFER_WUMPUS)
                not_alpha = [[valid_adj_cell.get_literal(Cell.Object.WUMPUS, "-")]]
                have_wumpus = self.KB.infer(not_alpha)

                # If we can infer Wumpus.
                if have_wumpus:
                    # Dectect Wumpus.
                    self.AddAction(Action.DETECT_WUMPUS)

                    # Shoot this Wumpus.
                    self.AddAction(Action.SHOOT)
                    self.AddAction(Action.KILL_WUMPUS)
                    valid_adj_cell.kill_wumpus(self.cell_matrix, self.KB)
                    self.AppendEventToOutputFile("KB: " + str(self.KB.KB))

                # If we can not infer Wumpus.
                else:
                    # Infer not Wumpus.
                    self.AddAction(Action.INFER_NOT_WUMPUS)
                    not_alpha = [
                        [valid_adj_cell.get_literal(Cell.Object.WUMPUS, "+")]
                    ]
                    have_no_wumpus = self.KB.infer(not_alpha)

                    # If we can infer not Wumpus.
                    if have_no_wumpus:
                        # Detect no Wumpus.
                        self.AddAction(Action.DETECT_NO_WUMPUS)

                    # If we can not infer not Wumpus.
                    else:
                        # Discard these cells from the valid_adj_cell_list.
                        if valid_adj_cell not in temp_adj_cell_list:
                            temp_adj_cell_list.append(valid_adj_cell)

        # If this cell still has Stench after trying to infer,
        # the Agent will try to shoot all of valid directions till Stench disappear.
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

        # If the current cell has Breeze, Agent infers whether the adjacent cells have Pit.
        if self.agent_cell.exist_breeze():
            valid_adj_cell: Cell.Cell
            for valid_adj_cell in valid_adj_cell_list:
                print("Infer: ", end="")
                print(valid_adj_cell.map_pos)
                self.AppendEventToOutputFile(
                    "Infer: " + str(valid_adj_cell.map_pos)
                )
                self.DirectionMove(valid_adj_cell)

                # Infer Pit.
                self.AddAction(Action.INFER_PIT)
                not_alpha = [[valid_adj_cell.get_literal(Cell.Object.PIT, "-")]]
                have_pit = self.KB.infer(not_alpha)

                # If we can infer Pit.
                if have_pit:
                    # Detect Pit.
                    self.AddAction(Action.DECTECT_PIT)

                    # Mark these cells as explored.
                    valid_adj_cell.explore()

                    # Add new percepts of these cells to the KB.
                    self.AddNewPerceptIntoKB(valid_adj_cell)

                    # Update parent for this cell.
                    valid_adj_cell.update_parent(valid_adj_cell)

                    # Discard these cells from the valid_adj_cell_list.
                    temp_adj_cell_list.append(valid_adj_cell)

                # If we can not infer Pit.
                else:
                    # Infer not Pit.
                    self.AddAction(Action.INFER_NOT_PIT)
                    not_alpha = [[valid_adj_cell.get_literal(Cell.Object.PIT, "+")]]
                    have_no_pit = self.KB.infer(not_alpha)

                    # If we can infer not Pit.
                    if have_no_pit:
                        # Detect no Pit.
                        self.AddAction(Action.DETECT_NO_PIT)

                    # If we can not infer not Pit.
                    else:
                        # Discard these cells from the valid_adj_cell_list.
                        temp_adj_cell_list.append(valid_adj_cell)

    temp_adj_cell_list = list(set(temp_adj_cell_list))

    # Select all of the valid nexts cell from the current cell.
    for adj_cell in temp_adj_cell_list:
        valid_adj_cell_list.remove(adj_cell)
    self.agent_cell.update_child_list(valid_adj_cell_list)

    # Move to all of the valid next cells sequentially.
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