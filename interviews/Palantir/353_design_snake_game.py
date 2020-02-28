from collections import deque


class SnakeGame(object):

  def __init__(self, width, height, food):
    """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
    self.width = width  # cols
    self.height = height  # rows
    self.food = deque(food)
    self.snake = deque([[0, 0]])
    self.direct = {"U": [-1, 0], "L": [0, -1], "R": [0, +1], "D": [1, 0]}
    print("start from: 0, 0")

  def move(self, direction):
    """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
    r0, c0 = self.snake[0]
    r1, c1 = self.direct[direction]
    new_head = [r0 + r1, c0 + c1]
    # print("new_head:{}, food:{}".format(new_head, self.food[0]))

    if new_head[0] < 0 or new_head[0] >= self.height \
      or new_head[1] < 0 or new_head[1] >= self.width \
      or (new_head in self.snake and new_head != self.snake[-1]):
      print("move:{}, pos:{}, score:{}".format(direction, self.snake[0], -1))
      return -1

    if self.food and self.food[0] == new_head:
      self.snake.appendleft(new_head)
      self.food.popleft()
    else:
      self.snake.appendleft(new_head)
      self.snake.pop()

    print("move:{}, pos:{}, score:{}".format(direction, self.snake[0],
                                             len(self.snake) - 1))
    return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

food = [[1, 2], [0, 1]]
width = 3
height = 2

s = SnakeGame(width, height, food)
s.move("R")
s.move("D")
s.move("R")
s.move("U")
s.move("L")
s.move("U")
