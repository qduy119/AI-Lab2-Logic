import Cell

def AddPerceptToKnowledgeBase(self, cell):
    adj_cell_list = cell.get_adj_cell_list(self.cell_matrix)


    sign = "-"
    if cell.exist_pit():
        sign = "+"
        self.KB.add_clause([cell.get_literal(Cell.Object.WUMPUS, "-")])
    self.KB.add_clause([cell.get_literal(Cell.Object.PIT, sign)])
    sign_pit = sign

 
    sign = "-"
    if cell.exist_wumpus():
        sign = "+"
        self.KB.add_clause([cell.get_literal(Cell.Object.PIT, "-")])
    self.KB.add_clause([cell.get_literal(Cell.Object.WUMPUS, sign)])
    sign_wumpus = sign

    if sign_pit == sign_wumpus == "+":
        raise TypeError(
            "Logic Error: Pit and Wumpus can not appear at the same cell."
        )


    sign = "-"
    if cell.exist_breeze():
        sign = "+"
    self.KB.add_clause([cell.get_literal(Cell.Object.BREEZE, sign)])


    sign = "-"
    if cell.exist_stench():
        sign = "+"
    self.KB.add_clause([cell.get_literal(Cell.Object.STENCH, sign)])


    if cell.exist_breeze():
        clause = [cell.get_literal(Cell.Object.BREEZE, "-")]
        for adj_cell in adj_cell_list:
            clause.append(adj_cell.get_literal(Cell.Object.PIT, "+"))
        self.KB.add_clause(clause)

        for adj_cell in adj_cell_list:
            clause = [
                cell.get_literal(Cell.Object.BREEZE, "+"),
                adj_cell.get_literal(Cell.Object.PIT, "-"),
            ]
            self.KB.add_clause(clause)


    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.PIT, "-")]
            self.KB.add_clause(clause)


    if cell.exist_stench():
        clause = [cell.get_literal(Cell.Object.STENCH, "-")]
        for adj_cell in adj_cell_list:
            clause.append(adj_cell.get_literal(Cell.Object.WUMPUS, "+"))
        self.KB.add_clause(clause)

        for adj_cell in adj_cell_list:
            clause = [
                cell.get_literal(Cell.Object.STENCH, "+"),
                adj_cell.get_literal(Cell.Object.WUMPUS, "-"),
            ]
            self.KB.add_clause(clause)


    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.WUMPUS, "-")]
            self.KB.add_clause(clause)

    print(self.KB.KB)
    self.AppendEventToOutputFile(str(self.KB.KB))