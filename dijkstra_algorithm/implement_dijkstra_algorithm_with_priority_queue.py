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


def find_shortest_path(graph):
  unvisited = []
  visited = set()
  visited_list = []

  for v in range(len(graph)):
    if v == 0:
      heapq.heappush(unvisited, (0, v))
    else:
      heapq.heappush(unvisited, (float("inf"), v))

  print("priority queue / min_heap", unvisited)
  """
  1) starting from the first vertex: pop from min_heap; add to visited; update its neighbors' distances
  """

  while unvisited:
    while unvisited[0][1] in visited:
      heapq.heappop(unvisited)
      if not unvisited:
        return
    distance, v = heapq.heappop(unvisited)  # (v, distance)
    print("pop vertex {}: {}".format(v, distance))
    visited.add(v)
    visited_list.append((v, distance))
    print("visited", visited_list)

    # update its neighbors' distance using d[i] = d[v] + w(v, i)
    # thus I need to find v's neighbors
    neighbors = graph[v]
    if neighbors:
      for neighbor, weight in neighbors:
        new_distance = distance + weight
        # compare this with the value in the min_heap
        """
        lazy implementation of the comparison: 
        1) push (new_distance, neighbor) into the priority queue
        2) each time whenever pop out the min_node, check if it has already by visited. 
        3) if the min_node has already been visited, keep pop() until a node has not been visited.
        """
        heapq.heappush(unvisited, (new_distance, neighbor))
        print("update vertex {}: {}".format(neighbor, distance))


graph = [
    [(1, 10), (2, 3)],
    [(3, 1)],
    [(1, 1), (3, 10)],
    [],
]

find_shortest_path(graph)
