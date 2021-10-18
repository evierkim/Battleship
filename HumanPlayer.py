from Player import Player

class HumanPlayer:
    def __init__(self):
        super().__init__(self)


    #def takeTurn(self):
        #must have access to other player's grid, so player must be a parameter
        #compare shots against the other player's ship grid

    def placeShip(self, ship, size):
        placed = True
        while placed:

            direction = input("Input 0 for horizontal, 1 for vertical")
            row = int(input("Input row 0-9:"))
            column = int(input("Input column 0-9:"))

            if direction == 0: #if horizontal placement
                allSpacesOpen = False

                for x in range(column, column+size): #loops through the row, "size" number of times
                    if self.gridShips.isSpaceWater(self, row, x) == False: #if the space is not open/water
                        allSpacesOpen = False
                        break
                    else:
                        allSpacesOpen = True

                if allSpacesOpen is True:
                    self.gridShips.changeRow(self, row, ship, column, size)
                placed = False

            else: #if vertical placement
                allSpacesOpen = False

                for x in range(row, row+size):
                    if self.gridShips.isSpaceWater(self, x, row) == False: #if the space is not open/water
                        allSpacesOpen = False
                        break
                    else:
                        allSpacesOpen = True

                if allSpacesOpen is True:
                    self.gridShips.changeCol(self, column, ship, row, size)


    #def stillHasShips(self, row, column):
        #if isSpaceWater(self, row, column) == False: #if the space






