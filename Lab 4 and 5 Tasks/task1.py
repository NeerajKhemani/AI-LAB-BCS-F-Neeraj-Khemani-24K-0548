building = [
 [1, 1, 0, 1],
 [0, 1, 1, 1],
 [1, 1, 0, 1],
 [1, 0, 1, 1]
]

rows = len(building)
cols = len(building[0])

graph = { }

for r in range(rows):
 for c in range(cols):
  if building[r][c] == 1:
   neighbors = [ ]
   for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr, nc = r+dr, c+dc
    if 0 <= nr < rows and 0 <= nc < cols and building[nr][nc]==1:
     neighbors.append((nr,nc))
   graph[(r,c)] = neighbors

def bfs(tree, start, goal):
 visited = [ ]
 queue = [ ]
 parent = { }

 visited.append(start)
 queue.append(start)
 parent[start] = None

 while queue:
  node = queue.pop(0)
  print(node, end=" ")
  
  if node == goal:
   print("\nGoal found!")
   path = [ ]
   while node is not None:
    path.append(node)
    node = parent[node]
   path.reverse()
   print("Shortest path:", path)
   return

  for neighbor in tree[node]:
   if neighbor not in visited:
    visited.append(neighbor)
    parent[neighbor] = node
    queue.append(neighbor)

bfs(graph, (0,0), (3,3))
