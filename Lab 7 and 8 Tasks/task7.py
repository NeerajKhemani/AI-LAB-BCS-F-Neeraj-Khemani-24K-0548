from ortools.sat.python import cp_model

def main():
    model = cp_model.CpModel()
    
    board_size = 4
    queens = [model.new_int_var(0, board_size - 1, f"Q{i}") for i in range(board_size)]
    
    model.add_all_different(queens)
    
  
    model.add_all_different([queens[i] + i for i in range(board_size)])
    model.add_all_different([queens[i] - i for i in range(board_size)])
    
   
    solver = cp_model.CpSolver()
    
    class NQueenSolutionPrinter(cp_model.CpSolverSolutionCallback):
        def __init__(self, queens):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.queens = queens
            self.solution_count = 0
        def on_solution_callback(self):
            self.solution_count += 1
            for i in range(board_size):
                for j in range(board_size):
                    if self.value(self.queens[j]) == i:
                        print("Q", end=" ")
                    else:
                        print("_", end=" ")
                print()
            print()
    
    solution_printer = NQueenSolutionPrinter(queens)
    
    solver.parameters.enumerate_all_solutions = True
    solver.solve(model, solution_printer)

if __name__ == "__main__":
    main()
