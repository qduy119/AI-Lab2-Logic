import Cell

def AddPerceptToKnowledgeBase(self, cell):
    adj_cell_list = cell.get_adj_cell_list(self.cell_matrix)


    sign = "-"
    if cell.exist_hole():
        sign = "+"
        self.KB.InsertClause([cell.get_literal(Cell.Object.WUMPUS, "-")])
    self.KB.InsertClause([cell.get_literal(Cell.Object.PIT, sign)])
    sign_hole = sign

 
    sign = "-"
    if cell.exist_wumpus():
        sign = "+"
        self.KB.InsertClause([cell.get_literal(Cell.Object.PIT, "-")])
    self.KB.InsertClause([cell.get_literal(Cell.Object.WUMPUS, sign)])
    sign_wumpus = sign

    if sign_hole == sign_wumpus == "+":
        raise TypeError(
            "Logic Error: Pit and Wumpus can not appear at the same cell."
        )


    sign = "-"
    if cell.exist_breeze():
        sign = "+"
    self.KB.InsertClause([cell.get_literal(Cell.Object.BREEZE, sign)])


    sign = "-"
    if cell.exist_stench():
        sign = "+"
    self.KB.InsertClause([cell.get_literal(Cell.Object.STENCH, sign)])


    if cell.exist_breeze():
        clause = [cell.get_literal(Cell.Object.BREEZE, "-")]
        for adj_cell in adj_cell_list:
            clause.append(adj_cell.get_literal(Cell.Object.PIT, "+"))
        self.KB.InsertClause(clause)

        for adj_cell in adj_cell_list:
            clause = [
                cell.get_literal(Cell.Object.BREEZE, "+"),
                adj_cell.get_literal(Cell.Object.PIT, "-"),
            ]
            self.KB.InsertClause(clause)


    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.PIT, "-")]
            self.KB.InsertClause(clause)


    if cell.exist_stench():
        clause = [cell.get_literal(Cell.Object.STENCH, "-")]
        for adj_cell in adj_cell_list:
            clause.append(adj_cell.get_literal(Cell.Object.WUMPUS, "+"))
        self.KB.InsertClause(clause)

        for adj_cell in adj_cell_list:
            clause = [
                cell.get_literal(Cell.Object.STENCH, "+"),
                adj_cell.get_literal(Cell.Object.WUMPUS, "-"),
            ]
            self.KB.InsertClause(clause)


    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.WUMPUS, "-")]
            self.KB.InsertClause(clause)

    #print(self.KB.KB)
    self.AppendEventToOutputFile(str(self.KB.KB))
