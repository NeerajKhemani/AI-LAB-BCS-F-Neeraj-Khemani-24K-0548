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
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)


class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []
        self.pruned_nodes = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):

        self.computed_nodes.append(node.value)

        if depth == 0 or not node.children:
            return node.value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value,
                    self.alpha_beta_search(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)

                if beta <= alpha:
                    self.pruned_nodes.append(child.value)
                    print("Pruned node:", child.value)
                    break

            node.minmax_value = value
            return value

        else:
            value = math.inf
            for child in node.children:
                value = min(value,
                    self.alpha_beta_search(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)

                if beta <= alpha:
                    self.pruned_nodes.append(child.value)
                    print("Pruned node:", child.value)
                    break

            node.minmax_value = value
            return value


def run_agent(agent, env, start):
    p = env.get_percept(start)
    agent.act(p, env)


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

print("\nVisited Nodes:", env.computed_nodes)
print("Pruned Nodes:", env.pruned_nodes)

print("\nMinimax Values:")
print("Root:", root.minmax_value)
print("N1:", n1.minmax_value, "N2:", n2.minmax_value)
print("N3:", n3.minmax_value, "N4:", n4.minmax_value)
print("N5:", n5.minmax_value, "N6:", n6.minmax_value)
