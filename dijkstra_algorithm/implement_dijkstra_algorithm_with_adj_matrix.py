import heapq
import time
""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
"""
"""
input graph: graph represented by adj list [[(vertex, weight), ()],[()],[()]] dict(lists(tuples))

output: None (but please print the shortest distance from starting vertex to another vertex whenever you added to visited)

data structures:
- the unvisited should be priority queue implemented with min_heap.
- the unvisited should be implemented with starting vertex (0, v0), and other vertices as (inf, v_i)
"""

# debug = False
debug = True


def dprint(*args, **kwargs):
  if debug == True:
    print(*args, **kwargs)


class Priority_queue:

  def __init__(self):
    self.q = []

  def push(self, node, parent, cost):
    heapq.heappush(self.q, (cost, node, parent))

  def pop(self):
    # print("q still has", self.q)
    cost, node, parent = heapq.heappop(self.q)
    return node, parent, cost

  def peek(self):
    cost, parent, node = self.q[0]
    return node, parent, cost


class Dijkstra:

  def __init__(self):
    self.unvisited = Priority_queue()  # (cost, (x, y))
    self.visited = {}  # {(x, y): cost}

  def find_shortest_path(self, graph, src, dest):
    self.unvisited.push(src, None, 0)

    dprint("priority queue / min_heap", self.unvisited)
    """
    1) starting from the first grid: pop from min_heap; add to visited; update its neighbors' distances
    """
    while self.unvisited:
      min_node, _, _ = self.unvisited.peek()
      while min_node in self.visited:
        self.unvisited.pop()
        if not self.unvisited:
          return
      node, _, cost = self.unvisited.pop()  # (v, distance)
      if node == dest:
        dprint("Took a minimum distance of {} from src {} to dest {}".format(
            cost, src, dest))
        return True
      dprint("pop node {}: {}".format(node, cost))
      self.visited[node] = cost

      # debug print visited dict
      # for key, val in self.visited.items():
      #   dprint("node {}: {}".format(key, val))

      # update its neighbors' distance using d[i] = d[v] + w(v, i)
      # thus I need to find v's neighbors
      x, y = node
      neighbors = [
          (x - 1, y),
          (x + 1, y),
          (x, y + 1),
          (x, y - 1),
      ]
      valid_neighbors = [(xi, yi)
                         for (xi, yi) in neighbors
                         if xi >= 0 and xi < len(graph) and yi >= 0 and
                         yi < len(graph[0]) and graph[xi][yi] == 1]
      if valid_neighbors:
        for n in valid_neighbors:
          new_cost = cost + 1
          # compare this with the value in the min_heap
          """
          lazy implementation of the comparison: 
          1) push (new_distance, neighbor) into the priority queue
          2) each time whenever pop out the min_node, check if it has already by visited. 
          3) if the min_node has already been visited, keep pop() until a node has not been visited.
          """
          self.unvisited.push(n, None, new_cost)
          dprint("update vertex {}: {}".format(n, new_cost))


###############

# graph = [[1] * 30 for i in range(30)]
# src = (14, 14)
# dest = (29, 29)

graph = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
]
src = (0, 0)
dest = (2, 0)

start = time.time()
d = Dijkstra()
solution = d.find_shortest_path(graph, src, dest)
end = time.time()
run_time = end - start
print("dijkstra run time is", run_time)