from grid import Grid


class Control:

    def __init__(self, n):
        self.g = Grid(n)
        print("""
Commands:
Up [U or u]
Down [D or d]
Left [L or l]
Right [R or r]
        """)

    def getInput(self):
        self.g.show()

        s = self.g.terminate()
        if s[0]:
            print("Game Over")
            return False
        elif s[1] == "Win":
            print("Winner")
            return False
        else:
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
            return True


c = Control(4)
while c.getInput():
    pass
