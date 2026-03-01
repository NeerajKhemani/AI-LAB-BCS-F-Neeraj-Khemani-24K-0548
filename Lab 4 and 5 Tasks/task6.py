import random

graph = {
 'A': {'B': 4, 'C': 3},
 'B': {'E': 12, 'F': 5},
 'C': {'D': 7, 'E': 10},
 'D': {'E': 2},
 'E': {'G': 5},
 'F': {'G': 16},
 'G': {}
}

heuristic = {'A':14,'B':12,'C':11,'D':6,'E':4,'F':11,'G':0}

def a_star_dynamic(graph, heuristic, start, goal, iterations=10):
    frontier = [(start, heuristic[start])]
    visited = set()
    g_costs = {start: 0}
    came_from = {start: None}

    for _ in range(iterations):
        if not frontier:
            print("Goal not reachable")
            return

        u = random.choice(list(graph.keys()))
        if graph[u]:
            v = random.choice(list(graph[u].keys()))
            old_cost = graph[u][v]
            graph[u][v] = random.randint(1, 20)
            print(f"Edge cost changed: {u}-{v} {old_cost} -> {graph[u][v]}")

        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")
        visited.add(current_node)

        if current_node == goal:
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"\nGoal found! Path: {path}, Total cost: {g_costs[goal]}")
            return

        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost
            f_cost = new_g_cost + heuristic[neighbor]
            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))

    print("\nGoal not found within iteration limit")

print("\nDynamic A* Search Execution:")
a_star_dynamic(graph, heuristic, 'A', 'G', iterations=20)
