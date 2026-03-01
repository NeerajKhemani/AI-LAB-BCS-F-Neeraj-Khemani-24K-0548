graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': ['G'],
 'E': [],
 'F': ['H'],
 'G': [],
 'H': []
}

def dls(graph, start, goal, limit):
 visited = [ ]
 stack = [ (start, 0) ] 
 parent = { start: None }
 visited.append(start)

 while stack:
  node, depth = stack.pop()
  print(node, end=" ")
  
  if node == goal:
   print("\nGoal found!")
   path = [ ]
   while node is not None:
    path.append(node)
    node = parent[node]
   path.reverse()
   print("Path:", path)
   return True

  if depth < limit:
   for neighbour in reversed(graph[node]):
    if neighbour not in visited:
     visited.append(neighbour)
     parent[neighbour] = node
     stack.append( (neighbour, depth+1) )

 print("\ngoal not found within depth limit", limit)
 return False

print("running DLS with depth = 2")
dls(graph, 'A', 'H', 2)

print("\nrunning DLS with depth = 3")
dls(graph, 'A', 'H', 3)
