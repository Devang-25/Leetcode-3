"""
purpose: implement an adjacent matrix to represent graph. 
Need to include below functions:
- add an edge

"""


class Node:

  def __init__(self, vertex):
    self.v = vertex
    self.next = None


class Graph:

  def __init__(self, num_of_vertex):
    self.num_of_vertex = num_of_vertex
    self.graph = [None] * self.num_of_vertex
    print("build graph:", self.graph)

  def add_edge(self, src, dest):
    dest_node = Node(dest)
    dest_node.next = self.graph[src]
    self.graph[src] = dest_node

    src_node = Node(src)
    src_node.next = self.graph[dest]
    self.graph[dest] = src_node


# TODO: implement remove_edge function
# def remove_edge(self, src, dest):

  def print_graph(self):
    for v in range(len(self.graph)):
      print("vertex {}".format(v), end="")
      if not self.graph[v]:
        print(" has NO neighbors")
        continue
      elif self.graph[v]:
        print(" has neighbor:", end="")
        neighbor = self.graph[v]
        print(neighbor.v, end="")
        while neighbor.next:
          neighbor = neighbor.next
          print(" -> ", neighbor.v, end="")
      print("\n")
    print("finish")

  def breadth_first_search(self, vertex):
    """
    purpose: implement breadth_first_search if start from a particular vertex v
    usage: the first all the vertices I can reach starting from this node

    key to implement a breadth_first_search is has memorization of: 1)visited 2)current_level 3)next_level


    input:
      vertex: int
    
    ouptut: 
      None
    """
    parents = {vertex: None}
    level = {vertex: 0}

    current_level = [vertex]
    i = 1
    while current_level:
      next_level = []
      for vs in current_level:
        print("vertex {}, ".format(vs), end="")
        # if not self.graph[v]:
        #   continue
        # print(vs, type(vs))
        if self.graph[vs]:
          neighbor = self.graph[vs]
          while neighbor:
            neighbor_v = neighbor.v
            if neighbor_v not in level:
              print("->", neighbor_v, end="")
              parents[neighbor_v] = vs
              level[neighbor_v] = i
              next_level.append(neighbor_v)
            neighbor = neighbor.next
      current_level = next_level
      i += 1
    print("finish bfs")

  # def depth_first_search(self):

graph = Graph(3)
graph.add_edge(0, 1)
# graph.print_graph()
graph.add_edge(1, 2)
graph.print_graph()

graph.breadth_first_search(1)
