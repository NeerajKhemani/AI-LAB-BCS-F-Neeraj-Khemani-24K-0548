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
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
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
                child_val = self.alpha_beta_search(child, depth-1, alpha, beta, False)
                value = max(value, child_val)
                alpha = max(alpha, value)
                if beta <= alpha:
                    self.pruned_nodes.append(child.value)
                    break
            node.minmax_value = value
            return value
        else:
            value = math.inf
            for child in node.children:
                child_val = self.alpha_beta_search(child, depth-1, alpha, beta, True)
                value = min(value, child_val)
                beta = min(beta, value)
                if beta <= alpha:
                    self.pruned_nodes.append(child.value)
                    break
            node.minmax_value = value
            return value

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)

root = Node('Root')
n1 = Node('N1')
n2 = Node('N2')
root.children = [n1, n2]

n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(4)
n8 = Node(9)    
n9 = Node(1)    
n10 = Node(5)
n15 = Node(6)    

n3.children = [n7, n8]
n4.children = [n9, n10, n15]

n11 = Node(1)
n12 = Node(8)   
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)

run_agent(agent, environment, root)

# Print computed values and pruning
print("Visited Nodes:", environment.computed_nodes)
print("Pruned Nodes:", environment.pruned_nodes)
print("\nMinimax Values:")
print(f"Root: {root.minmax_value}")
print(f"N1: {n1.minmax_value}  N2: {n2.minmax_value}")
print(f"N3: {n3.minmax_value}  N4: {n4.minmax_value}  N5: {n5.minmax_value}  N6: {n6.minmax_value}")

def find_optimal_path(node, maximizing=True):
    path = [node.value]
    if not node.children:
        return path
    valid_children = [child for child in node.children if child.minmax_value is not None]
    if not valid_children:
        return path
    if maximizing:
        best_val = max(child.minmax_value for child in valid_children)
    else:
        best_val = min(child.minmax_value for child in valid_children)
    for child in valid_children:
        if child.minmax_value == best_val:
            path.extend(find_optimal_path(child, not maximizing))
            break
    return path

optimal_path = find_optimal_path(root)
print("\nOptimal Path for Max from Root:", " -> ".join(map(str, optimal_path)))
