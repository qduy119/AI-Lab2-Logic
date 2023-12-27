from ObjectEnum import Object

def KillWumpus(self, cell_matrix, kb):
    self.percept[2] = False

    AdjCellListOfWumpus = self.get_adj_cell_list(cell_matrix)
    for StenchCell in AdjCellListOfWumpus:
        DeleteStenchFlag = True
        AdjCellListOfStench = StenchCell.get_adj_cell_list(cell_matrix)
        for AdjCell in AdjCellListOfStench:
            if AdjCell.exist_wumpus():
                DeleteStenchFlag = False
                break
        if DeleteStenchFlag:
            StenchCell.percept[4] = False
            literal = self.get_literal(Object.STENCH, '+')
            kb.DeleteClause([literal])
            literal = self.get_literal(Object.STENCH, '-')
            kb.InsertClause([literal])

            AdjCellList = StenchCell.get_adj_cell_list(cell_matrix)
            clause = [StenchCell.get_literal(Object.STENCH, '-')]
            for AdjCell in AdjCellList:
                clause.append(AdjCell.get_literal(Object.WUMPUS, '+'))
            kb.DeleteClause(clause)

            for AdjCell in AdjCellList:
                clause = [StenchCell.get_literal(Object.STENCH, '+'),
                            AdjCell.get_literal(Object.WUMPUS, '-')]
                kb.DeleteClause(clause)