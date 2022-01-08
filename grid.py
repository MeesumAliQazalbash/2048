import random


class Grid:
    def __init__(self, n):
        self.n = n
        self.grid = {i: {j: 0 for j in range(n)} for i in range(n)}
        self.start()

    def start(self):
        for _ in range(3):
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.n - 1)
            self.grid[i][j] = 2

    def gravityUp(self):
        for pointerCol in range(self.n):
            q = []
            for pointerRow in range(self.n - 1, -1, -1):
                if self.grid[pointerRow][pointerCol]:
                    q.append(self.grid[pointerRow][pointerCol])
            for j in range(len(q), self.n):
                self.grid[j][pointerCol] = 0
            for i in range(len(q)):
                self.grid[i][pointerCol] = q.pop()

    def gravityDown(self):
        for pointerCol in range(self.n):
            q = []
            for pointerRow in range(self.n):
                if self.grid[pointerRow][pointerCol]:
                    q.append(self.grid[pointerRow][pointerCol])
            for j in range(0, self.n - len(q)):
                self.grid[j][pointerCol] = 0
            for i in range(self.n - 1, self.n - len(q) - 1, -1):
                self.grid[i][pointerCol] = q.pop()

    def gravityLeft(self):
        for pointerRow in range(self.n):
            q = []
            for pointerCol in range(self.n - 1, -1, -1):
                if self.grid[pointerRow][pointerCol]:
                    q.append(self.grid[pointerRow][pointerCol])
            for j in range(len(q), self.n):
                self.grid[pointerRow][j] = 0
            for i in range(len(q)):
                self.grid[pointerRow][i] = q.pop()

    def gravityRight(self):
        for pointerRow in range(self.n):
            q = []
            for pointerCol in range(self.n):
                if self.grid[pointerRow][pointerCol]:
                    q.append(self.grid[pointerRow][pointerCol])
            for j in range(0, self.n - len(q)):
                self.grid[pointerRow][j] = 0
            for i in range(self.n - 1, self.n - len(q) - 1, -1):
                self.grid[pointerRow][i] = q.pop()

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j], end=" ")
            print()
