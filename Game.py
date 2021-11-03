from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

hp = HumanPlayer()
cp = ComputerPlayer()

cp.createShipGrid()
cp.gridShips.printGrid()
hp.createShipGrid()

while hp.stillHasShips() and cp.stillHasShips():
    print("Take your turn:")
    hp.takeTurn(cp)
    print("Computer's turn:")
    cp.takeTurn(hp)

if not hp.stillHasShips():
    print("Computer Won!")
else:
    print("You Won!")

print("Game over")

"""
        if self.hit == True: # previous turn hit ship
            if self.r >= 9: # bottom element
                self.direction = 1
            elif self.r <= 0: # top element
                self.direction = 2
            elif self.c >= 9: # rightmost element
                self.direction = 3
            elif self.c <= 0: # leftmost element
                self.direction = 0
            # account for corner elements - evie
            if self.direction == 0 and self.r != 9: # space below
                if self.gridShots.returnLocation(self.r+1,self.c) == "~": # space below is not shot at
                    #self.shot(otherPlayer, self.r + 1, self.c)
                    if self.shot(otherPlayer,self.r+1,self.c) == False: # miss
                        self.direction = 1
            elif self.direction == 1 and self.r+1 >= 0: # space above
                if self.gridShots.returnLocation(self.r-1,self.c) == "~": # space above is not shot at
                    #self.shot(otherPlayer, self.r - 1, self.c)
                    if self.shot(otherPlayer,self.r - 1, self.c) == False: # miss
                        self.direction = 2
            elif self.direction == 2 and self.c >= 0: # space to left
                if self.gridShots.returnLocation(self.r, self.c - 1) == "~":  # space to left is not shot at
                    #self.shot(otherPlayer,self.r, self.c - 1)
                    if self.shot(otherPlayer,self.r, self.c - 1) == False: # miss
                        self.direction = 3
            elif self.direction == 3 and self.c <= 9: # space to right
                if self.gridShots.returnLocation(self.r,self.c+1) == "~": # space to right is not shot at
                    #self.shot(otherPlayer,self.r, self.c + 1)
                    if self.shot(otherPlayer,self.r, self.c + 1) == False: # miss
                        self.hit == False
                        self.direction = 0



        else: # previous turn did not hit ship
"""