from grid import Grid


class Control:
    def __init__(self, n):
        self.g = Grid(n)
        print(
            """
Commands:
Up [U or u]
Down [D or d]
Left [L or l]
Right [R or r]
        """
        )

    def getInput(self):
        self.g.show()

        w = input("Enter the input: ")

        if w.lower() == "u":
            self.g.addUp()
        elif w.lower() == "d":
            self.g.addDown()
        elif w.lower() == "l":
            self.g.addLeft()
        elif w.lower() == "r":
            self.g.addRight()
        else:
            print("Invalid Input")


c = Control(4)
while True:
    c.getInput()
