import random


class Grid:
    def __init__(self, n):
        """initialize object with a size of n by n matrix"""
        self.n = n
        self.grid = {i: {j: 0 for j in range(n)} for i in range(n)}
        self.start()

    def start(self):
        """randomly chosses three places on grid and set them to 2"""
        for _ in range(3):
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.n - 1)
            self.grid[i][j] = 2

    def gravityUp(self):
        """sets all blocks in the Up direction"""
        for pCol in range(self.n):
            q = []
            for pRow in range(self.n - 1, -1, -1):
                if self.grid[pRow][pCol]:
                    q.append(self.grid[pRow][pCol])
            for j in range(len(q), self.n):
                self.grid[j][pCol] = 0
            for i in range(len(q)):
                self.grid[i][pCol] = q.pop()

    def gravityDown(self):
        """sets all blocks in the Down direction"""
        for pCol in range(self.n):
            q = []
            for pRow in range(self.n):
                if self.grid[pRow][pCol]:
                    q.append(self.grid[pRow][pCol])
            for j in range(0, self.n - len(q)):
                self.grid[j][pCol] = 0
            for i in range(self.n - 1, self.n - len(q) - 1, -1):
                self.grid[i][pCol] = q.pop()

    def gravityLeft(self):
        """sets all blocks in the Left direction"""
        for pRow in range(self.n):
            q = []
            for pCol in range(self.n - 1, -1, -1):
                if self.grid[pRow][pCol]:
                    q.append(self.grid[pRow][pCol])
            for j in range(len(q), self.n):
                self.grid[pRow][j] = 0
            for i in range(len(q)):
                self.grid[pRow][i] = q.pop()

    def gravityRight(self):
        """sets all blocks in the Right direction"""
        for pRow in range(self.n):
            q = []
            for pCol in range(self.n):
                if self.grid[pRow][pCol]:
                    q.append(self.grid[pRow][pCol])
            for j in range(0, self.n - len(q)):
                self.grid[pRow][j] = 0
            for i in range(self.n - 1, self.n - len(q) - 1, -1):
                self.grid[pRow][i] = q.pop()

    def twitch(self):
        """set randomly one nonoccupied block to 2"""
        r = random.randint(0, self.n - 1)
        c = random.randint(0, self.n - 1)
        while self.grid[r][c] != 0:
            r = random.randint(0, self.n - 1)
            c = random.randint(0, self.n - 1)
        self.grid[r][c] = 2

    def show(self):
        """prints the grid"""
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j], end=" ")
            print()
        print("\n")

    def addUp(self):
        """add the block in the Up direction"""
        self.gravityUp()
        for pCol in range(self.n):
            pRow = 0
            while pRow + 1 < self.n:
                if self.grid[pRow][pCol] == self.grid[pRow + 1][pCol]:
                    self.grid[pRow][pCol] = self.grid[pRow][pCol] * 2
                    self.grid[pRow + 1][pCol] = 0
                    pRow += 1
                pRow += 1
        self.gravityUp()
        self.twitch()

    def addDown(self):
        """add the block in the Down direction"""
        self.gravityDown()
        for pCol in range(self.n):
            pRow = self.n - 1
            while pRow > 1:
                if self.grid[pRow][pCol] == self.grid[pRow - 1][pCol]:
                    self.grid[pRow][pCol] = self.grid[pRow][pCol] * 2
                    self.grid[pRow - 1][pCol] = 0
                    pRow -= 1
                pRow -= 1
        self.gravityDown()
        self.twitch()

    def addLeft(self):
        """add the block in the Left direction"""
        self.gravityLeft()
        for pRow in range(self.n):
            pCol = 0
            while pCol + 1 < self.n:
                if self.grid[pRow][pCol] == self.grid[pRow][pCol + 1]:
                    self.grid[pRow][pCol] = self.grid[pRow][pCol] * 2
                    self.grid[pRow][pCol + 1] = 0
                    pCol += 1
                pCol += 1
        self.gravityLeft()
        self.twitch()

    def addRight(self):
        """add the block in the Right direction"""
        self.gravityRight()
        for pRow in range(self.n):
            pCol = self.n - 1
            while pCol > 1:
                if self.grid[pRow][pCol] == self.grid[pRow][pCol - 1]:
                    self.grid[pRow][pCol] = self.grid[pRow][pCol] * 2
                    self.grid[pRow][pCol - 1] = 0
                    pCol -= 1
                pCol -= 1
        self.gravityRight()
        self.twitch()

    def shift(self, direction):
        """add blocks in the direction of gravity"""
        if direction == "up":
            self.addUp()
        elif direction == "down":
            self.addDown()
        elif direction == "left":
            self.addLeft()
        elif direction == "right":
            self.addRight()
        pass

    def terminate(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    return False, "GameOver"
                elif self.grid[i][j] == 2048:
                    return True, "Win"
        return True, "Running"
