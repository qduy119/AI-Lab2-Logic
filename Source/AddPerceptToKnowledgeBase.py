
import Cell

def AddPerceptToKnowledgeBase(self, cell):
    adj_cell_list = cell.get_adj_cell_list(self.cell_matrix)

    # Note: Pit and Wumpus can not appear at the same cell.
    # Hence: * If a cell has Pit, then it can not have Wumpus.
    #        * If a cell has Wumpus, then it can not have Pit.

    # PL: Pit?
    sign = "-"
    if cell.exist_pit():
        sign = "+"
        self.KB.add_clause([cell.get_literal(Cell.Object.WUMPUS, "-")])
    self.KB.add_clause([cell.get_literal(Cell.Object.PIT, sign)])
    sign_pit = sign

    # PL: Wumpus?
    sign = "-"
    if cell.exist_wumpus():
        sign = "+"
        self.KB.add_clause([cell.get_literal(Cell.Object.PIT, "-")])
    self.KB.add_clause([cell.get_literal(Cell.Object.WUMPUS, sign)])
    sign_wumpus = sign

    # Check the above constraint.
    if sign_pit == sign_wumpus == "+":
        raise TypeError(
            "Logic Error: Pit and Wumpus can not appear at the same cell."
        )

    # PL: Breeze?
    sign = "-"
    if cell.exist_breeze():
        sign = "+"
    self.KB.add_clause([cell.get_literal(Cell.Object.BREEZE, sign)])

    # PL: Stench?
    sign = "-"
    if cell.exist_stench():
        sign = "+"
    self.KB.add_clause([cell.get_literal(Cell.Object.STENCH, sign)])

    # PL: This cell has Breeze iff At least one of all of adjacent cells has a Pit.
    # B <=> Pa v Pb v Pc v Pd
    if cell.exist_breeze():
        # B => Pa v Pb v Pc v Pd
        clause = [cell.get_literal(Cell.Object.BREEZE, "-")]
        for adj_cell in adj_cell_list:
            clause.append(adj_cell.get_literal(Cell.Object.PIT, "+"))
        self.KB.add_clause(clause)

        # Pa v Pb v Pc v Pd => B
        for adj_cell in adj_cell_list:
            clause = [
                cell.get_literal(Cell.Object.BREEZE, "+"),
                adj_cell.get_literal(Cell.Object.PIT, "-"),
            ]
            self.KB.add_clause(clause)

    # PL: This cell has no Breeze then all of adjacent cells has no Pit.
    # -Pa ^ -Pb ^ -Pc ^ -Pd
    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.PIT, "-")]
            self.KB.add_clause(clause)

    # PL: This cell has Stench iff At least one of all of adjacent cells has a Wumpus.
    if cell.exist_stench():
        # S => Wa v Wb v Wc v Wd
        clause = [cell.get_literal(Cell.Object.STENCH, "-")]
        for adj_cell in adj_cell_list:
            clause.append(adj_cell.get_literal(Cell.Object.WUMPUS, "+"))
        self.KB.add_clause(clause)

        # Wa v Wb v Wc v Wd => S
        for adj_cell in adj_cell_list:
            clause = [
                cell.get_literal(Cell.Object.STENCH, "+"),
                adj_cell.get_literal(Cell.Object.WUMPUS, "-"),
            ]
            self.KB.add_clause(clause)

    # PL: This cell has no Stench then all of adjacent cells has no Wumpus.
    # -Wa ^ -Wb ^ -Wc ^ -Wd
    else:
        for adj_cell in adj_cell_list:
            clause = [adj_cell.get_literal(Cell.Object.WUMPUS, "-")]
            self.KB.add_clause(clause)

    print(self.KB.KB)
    self.AppendEventToOutputFile(str(self.KB.KB))