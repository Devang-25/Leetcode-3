"""
You ave given a crossword puzzle of black and white squares. We need to determine whether the crossword puzzle is valid. Valid means that given any white square, you can reach any other white square by traversing a path in the puzzle going either up, down, left, or right. For simplicity, let's say the puzzle is represented by an int[][], where 0 = white and 1 = black.

For example, the follwoing gird is valid crossword puzzle:

0001
0010
0100
0000

#Valid

Ex 2:

0001
0010
0100
1000
# Invalid
# b/c if you pick a white from top left half of the puzzle, the diagnol of the black squares prevents me from traversing a path to any white square in the bottom right part of the puzzle.

"""

class CrossWordPuzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.whites = [(i, j) for i in range(len(puzzle)) for j in range(len(puzzle[i])) if puzzle[i][j] == 0]
        self.whites_set = set(self.whites)
        self.visited = set()


    def crossword_puzzle(self):
        """
        inputs:
            puzzle: [[int]]

        output:
            bool: True / False

        use self.white_set to keep track of which whites I have not yet visited

        start from a random white puzzle, use breadth first search, for all the next steps (up, down, left, right, and 0), i remove the next step from the whites_set

        And I should be able to travel to all the other 0/white puzzle in the puzzle if it  valid.
        """

        i, j = self.whites[0]
        self.travel(i, j)

        return not bool(self.whites_set)


    def travel(self, i, j):

        if i < 0 or i >= len(puzzle) or j < 0 or j >= len(puzzle):
            return

        elif puzzle[i][j] == 1:
            return

        elif puzzle[i][j] == 0:
            self.whites_set.remove((i, j))
            self.puzzle[i][j] = 1
            next_steps = [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]
            for step in next_steps:
                if tuple(step) not in self.visited:
                    r, c = step
                    self.travel(r, c)




puzzle = [
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[0,0,0,0],
]

results = CrossWordPuzzle(puzzle).crossword_puzzle()
print("Puzzle")
for row in puzzle:
    print(row)
print(results)


puzzle = [
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
]

results = CrossWordPuzzle(puzzle).crossword_puzzle()
print("Puzzle")
for row in puzzle:
    print(row)
print(results)
