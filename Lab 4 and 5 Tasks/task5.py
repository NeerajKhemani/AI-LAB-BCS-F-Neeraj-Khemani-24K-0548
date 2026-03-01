from queue import PriorityQueue

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = 0   
        self.h = 0   
        self.f = 0   

    def __lt__(self, other):
        return self.f < other.f

def best_first_multi_goals(graph, start, goals):
    path_total = []
    current_start = start
    remaining_goals = goals.copy()
    
    while remaining_goals:
        frontier = PriorityQueue()
        start_node = Node(current_start)
        frontier.put(start_node)
        visited = set()
        goal_reached = None
        
        while not frontier.empty():
            current_node = frontier.get()
            current_name = current_node.name
            
            if current_name in remaining_goals:
                goal_reached = current_name
                path_segment = []
                temp = current_node
                while temp:
                    path_segment.append(temp.name)
                    temp = temp.parent
                path_total += path_segment[::-1][1:] if path_total else path_segment[::-1]
                remaining_goals.remove(goal_reached)
                current_start = goal_reached
                break
            
            visited.add(current_name)
            
            for neighbor, cost in graph[current_name]:
                if neighbor not in visited:
                    new_node = Node(neighbor, current_node)
                    new_node.g = current_node.g + cost
                    new_node.h = 0
                    new_node.f = new_node.h
                    frontier.put(new_node)
                    visited.add(neighbor)
        
        if goal_reached is None:
            return None
    
    return path_total

graph = {
 'S': [('A',3), ('B',6), ('C',5)],
 'A': [('D',9), ('E',8)],
 'B': [('F',12), ('G',14)],
 'C': [('H',7)],
 'H': [('I',5), ('J',6)],
 'I': [('K',1), ('L',10), ('M',2)],
 'D': [], 'E': [], 'F': [], 'G': [], 'J': [], 'K': [], 'L': [], 'M': []
}

start = 'S'
goals = ['D','K','M']  

path = best_first_multi_goals(graph, start, goals)

if path:
    print("Path covering all goals:", path)
else:
    print("No path found covering all goals")
