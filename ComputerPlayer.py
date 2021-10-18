from Player import Player
import random
class ComputerPlayer(Player):
    def __init__(self):
        super().__init__(self)
    def placeShip(self , ship , size):
        b = True
        while b: # ship still needs to be placed
            a = random.randrange(0,1)
            if a == 0: # horizontal
                r = random.randrange(0, 10)
                c = random.randrange(0, 11-size)
                for x in range(c,size): # checks if all spaces are legal
                    if self.gridShips.isSpaceWater(r,x) == False: # if space is illegal
                        b = True
                        break
                    else: # if space is legal
                        b = False
                if b == False:
                    self.gridShips.changeRow(r, ship, c, size)
            else: # if vertical
                r = random.randrange(0, 11-size)
                c = random.randrange(0, 10)
                for x in range(r, size):  # checks if all spaces are legal
                    if self.gridShips.isSpaceWater(x, c) == False:  # if space is illegal
                        b = True
                        break
                    else:  # if space is legal
                        b = False
                if b == False:
                    self.gridShips.changeCol(c, ship, r, size)
    def takeTurn(self,otherPlayer):