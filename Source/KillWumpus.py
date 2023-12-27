from ObjectEnum import Object

def KillWumpus(self, cell_matrix, kb):
        # Delete Wumpus.
        self.percept[2] = False

        # Delete Stench of adjacent cells.
        adj_cell_list_of_wumpus_cell = self.get_adj_cell_list(cell_matrix)
        for stench_cell in adj_cell_list_of_wumpus_cell:
            del_stench_flag = True
            adj_cell_list_of_stench_cell = stench_cell.get_adj_cell_list(cell_matrix)
            for adj_cell in adj_cell_list_of_stench_cell:
                if adj_cell.exist_wumpus():
                    del_stench_flag = False
                    break
            if del_stench_flag:
                stench_cell.percept[4] = False
                literal = self.get_literal(Object.STENCH, '+')
                kb.del_clause([literal])
                literal = self.get_literal(Object.STENCH, '-')
                kb.add_clause([literal])

                adj_cell_list = stench_cell.get_adj_cell_list(cell_matrix)
                # S => Wa v Wb v Wc v Wd
                clause = [stench_cell.get_literal(Object.STENCH, '-')]
                for adj_cell in adj_cell_list:
                    clause.append(adj_cell.get_literal(Object.WUMPUS, '+'))
                kb.del_clause(clause)

                # Wa v Wb v Wc v Wd => S
                for adj_cell in adj_cell_list:
                    clause = [stench_cell.get_literal(Object.STENCH, '+'),
                              adj_cell.get_literal(Object.WUMPUS, '-')]
                    kb.del_clause(clause)