from ortools.sat.python import cp_model

model = cp_model.CpModel()


x = model.new_int_var(0, 3, "x")
y = model.new_int_var(0, 3, "y")
z = model.new_int_var(0, 3, "z")


model.add(x != y)
model.add(y != z)
model.add(x + y <= 4)


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.Value(v)}", end="  ")
        print()

    @property
    def solution_count(self):
        return self.__solution_count


solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x, y, z])
solver.parameters.enumerate_all_solutions = True

status = solver.Solve(model, solution_printer)

print(f"Total solutions found: {solution_printer.solution_count}")
