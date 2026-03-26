import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None


class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        status = self.formulate_goal(node)
        if status == "Goal reached":
            return f"Minimax value for root: {node.minmax_value}"
        else:
            return environment.compute_minimax(node, self.depth)


class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    def compute_minimax(self, node, depth, maximizing_player=True):

        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value if isinstance(node.value, int) else 0

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                val = self.compute_minimax(child, depth - 1, False)
                value = max(value, val)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value

        else:
            value = math.inf
            for child in node.children:
                val = self.compute_minimax(child, depth - 1, True)
                value = min(value, val)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value


def run_agent(agent, env, start):
    p = env.get_percept(start)
    agent.act(p, env)

def reset_tree(node):
    node.minmax_value = None
    for child in node.children:
        reset_tree(child)


root = Node("Root")

n1 = Node("N1")
n2 = Node("N2")
root.children = [n1, n2]

n3 = Node("N3")
n4 = Node("N4")
n5 = Node("N5")
n6 = Node("N6")

n1.children = [n3, n4]
n2.children = [n5, n6]

n3.children = [Node(4), Node(7)]
n4.children = [Node(2), Node(5)]
n5.children = [Node(1), Node(8)]
n6.children = [Node(3), Node(6)]


depth = 3
agent = MinimaxAgent(depth)
env = Environment(root)

run_agent(agent, env, root)

print("Visit Order:", env.computed_nodes)

print("\nMinimax Values:")
print("Root:", root.minmax_value)
print("N1:", n1.minmax_value, "N2:", n2.minmax_value)
print("N3:", n3.minmax_value, "N4:", n4.minmax_value)
print("N5:", n5.minmax_value, "N6:", n6.minmax_value)


env.computed_nodes.clear()

reset_tree(root)

depth = 2
agent = MinimaxAgent(depth)
env2 = Environment(root)

run_agent(agent, env2, root)

print("\nDepth Limited (depth = 2):")
print("Visit Order:", env2.computed_nodes)
print("Root:", root.minmax_value)
print("N1:", n1.minmax_value, "N2:", n2.minmax_value)
