import numpy as np
import time
import heapq
import math

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


class Comparison:

  def __init__(self):
    self.visited = {}  # dict {node: cost}
    self.unvisited = Priority_queue()
    self.g_cost_cache = {}  # dict[(x1,x2): real_cost]
    # self.problem = problem
    # self.cost = cost
    # self.rows = len(problem)
    # self.cols = len(problem[0])

  def h_cost(self, current, dest):
    """
    goal: to calculate the heuristic cost h(i) of a node;
    plan to use euclidean distance as the heuristic cost for this problem.

    input: 
    current: (x_i: int; y_i:int)
    dest: (x_dest: int; y_dest: int)
    
    output: heuristic cost: float.
    """
    x_i, y_i = current
    x_dest, y_dest = dest

    x = (x_i - x_dest)**2.0
    y = (y_i - y_dest)**2.0
    h = math.sqrt(x + y)
    return h

  def g_cost(self, parent, current):
    """
    inputs:
    prev: coordiantes of previous location, tuple(int, int)
    current: coordinates of current location, tuple(int, int)
    
    return the real cost
    """
    g_prev = self.g_cost_cache[parent]
    print("current", current)
    row, col = current
    # if has cost function:
    # weight = self.cost[row][col]

    # if has unform cost of 1
    weight = 1
    return g_prev + weight

  def total_cost(self, prev, current, dest):
    """
    inputs:
    prev: coordiantes of previous location, tuple(int, int)
    current: the coordinate of current location; tuple(int, int)

    return the total  cost of reaching current location: int
    """
    g_cost = self.g_cost(prev, current)
    h_cost = self.h_cost(current, dest)

    return g_cost + h_cost

  def find_best_route(self, graph, src, dest):
    """
    goal: start from a node, find out the best route from one node to another node.

    inputs:
    src: the coordinate of the source (x0, y0), tuple(int, int)
    dest: the destination of the source (x_dest, y_dest), tuple(int, int)
    
    outputs:
    the best route from src to dest. [loc1, loc2 ...] list[tuple(int), tuple(int),...]
    """
    self.unvisited.push(src, src, 0)
    self.g_cost_cache[src] = 0
    while self.unvisited.q:
      current, parent, f_cost = self.unvisited.pop()

      # update the g_cost(src, current) in to the cache
      g_cost = self.g_cost(parent, current)
      if current not in self.g_cost_cache:
        self.g_cost_cache[current] = g_cost
      elif current in self.g_cost_cache and g_cost < self.g_cost_cache[current]:
        self.g_cost_cache[current] = g_cost

      dprint("I pop node {}, parent {}, cost {}".format(current, parent,
                                                        f_cost))
      dprint("after pop:", self.unvisited, "\n")

      if current == dest:
        print("I found the best cost for to reach dest {}: {}".format(
            dest, f_cost))
        return f_cost

      if current not in self.visited:
        dprint("enter")
        xi, yi = current
        candidates = [
            (xi - 1, yi),
            (xi + 1, yi),
            (xi, yi - 1),
            (xi, yi + 1),
        ]

        dprint("candidates", candidates)
        next_steps = [(x, y)
                      for x, y in candidates
                      if x >= 0 and x < len(graph) and y >= 0 and
                      y < len(graph[0]) and graph[x][y] == 1]
        dprint("next", next_steps)
        for loc in next_steps:
          if loc not in self.visited:
            # calculate the f(loc)
            f_cost_loc = self.total_cost(current, loc, dest)
            self.unvisited.push(loc, current, f_cost_loc)
            dprint("newly added to unvisited: {}".format(loc))
        self.visited[current] = f_cost
    return ("I cannot find a path")

  def generate_graph(self):
    graph = np.random.randint(0, 2, (30, 30))

    dprint("graph:")
    for row in graph:
      dprint(row)

    return graph

  def generate_src_dest(self):
    src = None
    dest = None
    while src == dest:
      src = np.random.randint(0, 30, (1, 2))
      dest = np.random.randint(0, 30, (1, 2))

      src = tuple(src[0])
      dest = tuple(dest[0])

    dprint("src", src)
    dprint("dest", dest)
    return src, dest

  def is_solvable(self, graph, src, dest):
    """
    see if this is solvable
    """
    solution = self.find_best_route(graph, src, dest)

    if type(solution) == int:
      print("take minimum cost of {} to reach destination".format(solution),
            "\n\n")
      return True
    elif solution == "I cannot find a path":
      return False

  def generate_valid_solution(self):
    graph = self.generate_graph()
    src, dest = self.generate_src_dest()
    workable = self.is_solvable(graph, src, dest)
    i = 1
    while not workable:
      i += 1
      src, dest = self.generate_src_dest()
      workable = self.is_solvable(graph, src, dest)
    print("i: ", i)
    return graph, src, dest

  def calculate_a_star_run_time(self):
    # graph, src, dest = self.generate_valid_solution()

    graph = [[1] * 30 for i in range(30)]
    src = (14, 14)
    dest = (29, 29)

    start_time = time.time()
    a_star_solution = self.find_best_route(graph, src, dest)
    end_time = time.time()
    a_star_runtime = end_time - start_time
    print("start: {} \n end: {}".format(start_time, end_time))
    print("A* needs {} seconds to finsh".format(a_star_runtime))
    return a_star_runtime


c = Comparison()
# print(c.calculate_a_star_run_time())

# graph, src, dest = c.generate_valid_solution()
# print("src", src)
# print("dest", dest)
# print(c.find_best_route(graph, src, dest))
print(c.calculate_a_star_run_time())