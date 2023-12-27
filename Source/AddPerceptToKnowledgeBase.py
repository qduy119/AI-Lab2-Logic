import Cell

def AddPerceptToKnowledgeBase(self, cell):
    adj_cell_list = cell.get_adj_cell_list(self.cell_matrix)

    # Propositional Logic: Pit
    sign = "-"
    if cell.exist_pit():
        sign = "+"
        self.KB.add_clause([cell.get_literal(Cell.Object.WUMPUS, "-")])
    self.KB.add_clause([cell.get_literal(Cell.Object.PIT, sign)])
    sign_pit = sign

    # Propositional Logic: Wumpus
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

    # Propositional Logic: Breeze?
    sign = "-"
    if cell.exist_breeze():
        sign = "+"
    self.KB.add_clause([cell.get_literal(Cell.Object.BREEZE, sign)])

    # Propositional Logic: Stench?
    sign = "-"
    if cell.exist_stench():
        sign = "+"
    self.KB.add_clause([cell.get_literal(Cell.Object.STENCH, sign)])

    # Propositional Logic: This cell has Breeze iff At least one of all of adjacent cells has a Pit.
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

    # Propositional Logic: This cell has no Breeze then all of adjacent cells has no Pit.
    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.PIT, "-")]
            self.KB.add_clause(clause)

    # Propositional Logic: This cell has Stench iff At least one of all of adjacent cells has a Wumpus.
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

    # Propositional Logic: This cell has no Stench then all of adjacent cells has no Wumpus.
    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.WUMPUS, "-")]
            self.KB.add_clause(clause)

    print(self.KB.KB)
    self.AppendEventToOutputFile(str(self.KB.KB))