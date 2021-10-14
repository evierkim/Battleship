from Player import Player

class HumanPlayer:
    def __init__(self):
        super().__init__(self)


    #def takeTurn(self):
        #must have access to other player's grid, so player must be a parameter
        #compare shots against the other player's ship grid

    def placeShip(self, ship, size):
        #use createShipGrid
        #depending on the size, ask what column/row and place the ship
        #confirm that it's a legal placement using isSpaceWater
        direction = input("Input 0 for horizontal, 1 for vertical :")
        row = int(input("Input row 0-9:"))
        column = int(input("Input column 0-9:"))
        if direction == 0: #if horizontal placement
            for x in range (column, column+size):
                if isSpaceWater(self, row, x) == False:

            self.gridShips.changeRow(self, row, ship, column, size)
        else: #if vertical placement
            for x in range (row, row+size):
                if isSpaceWater(self, column, x) == False:

            self.gridShips.changeCol(self, column, ship, row, size)






