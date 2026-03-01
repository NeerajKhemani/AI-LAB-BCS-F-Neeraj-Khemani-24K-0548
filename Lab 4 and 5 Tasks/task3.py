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

def dls(node, goal, depth, path):
 if depth < 0:
  return False
 path.append(node)
 if node == goal:
  return True
 if depth == 0:
  path.pop()
  return False
 if node not in graph:
  path.pop()
  return False
 for child in graph[node]:
  if dls(child, goal, depth-1, path):
   return True
 path.pop()
 return False

def iterative_deepening(start, goal, max_depth):
 for depth in range(max_depth+1):
  print(f"\nDepth = {depth}")
  path = [ ]
  visited = [ ]
  def dfs_visit(n, d):
   visited.append(n)
   if dls(n, goal, d, path):
    return True
   return False
  found = dfs_visit(start, depth)
  print("Visited nodes:", visited)
  if found:
   print("Goal found!")
   print("Path:", path)
   return
 print("Goal not found within max depth", max_depth)

iterative_deepening('A', 'G', 4)
