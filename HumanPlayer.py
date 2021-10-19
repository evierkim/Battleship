from Player import Player

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    """
    TAKE TURN
    """
    def takeTurn(self, otherPlayer):
        #must have access to other player's grid, so player must be a parameter
        #compare shots against the other player's ship grid

        #x is hit, o is miss

        #ask for shot coordinates from player
        #compare shot with the otherPlayer's gridShips
            #if hit, player is allowed to go again; mark it as a hit on both otherPlayer's gridShips and player's gridShots
                #check if ship is sunk, or if all the ships are sunk (stillHasShips)
            #if miss, mark it as an o on player's gridShots

        row = input("Input row 0-9:")
        column = input("Input column 0-9:")

        if otherPlayer.gridShips.returnLocation(row, column ) is not "~": #if hit/if it's not water (assuming that they wouldn't shoot at the same place more than once)
            shipType = otherPlayer.gridShips.returnLocation(row, column)
            print("Hit!")

            sunk = True #helps check if ship is sunk or not
            for col in range(0, 10): #traverses through the columns
                for r in range(0, 10): #traverses through each row of the column
                    if otherPlayer.gridShips[r][col] is shipType: #if the ship is still not sunk
                        sunk = False
                        break
            if sunk is True: #if the ship is sunk
                if shipType == "A": #if value is A, aircraft carrier
                    print("Aircraft Carrier is sunk.")
                elif shipType == "B": #if value is B, battleship
                    print("Battleship is sunk.")
                elif shipType == "C": #if value is C, cruiser
                    print("Cruiser is sunk.")
                elif shipType == "S": #if value is S, submarine
                    print("Submarine is sunk.")
                else: #if shipType is D, destroyer
                    print("Destroyer is sunk.")

            otherPlayer.gridShips.changeSingleSpace(row, column, "x") #mark as a hit on otherPlayer's gridShips
            self.gridShots.changeSingleSpace(row,column, "x") #mark as a hit on player's gridShots
            if otherPlayer.gridShips.stillHasShips() is False: #if there are no more ships on otherPlayer's grid
                print("You win!")

            self.printGrids()

        else: #if not hit
            print("Miss!")
            otherPlayer.gridShips.changeSingleSpace(row, column, "o")
            self.gridShots.changeSingleSpace(row, column, "o")
            self.printGrids()

    """
    placeShip
    
    """
    def placeShip(self, ship, size):
        placed = True
        while placed: #run until p

            direction = input("Input 0 for horizontal, 1 for vertical")
            row = int(input("Input row 0-9:"))
            column = int(input("Input column 0-9:"))

            if direction == 0: #if horizontal placement
                allSpacesOpen = False

                for x in range(column, column+size): #loops through the row, "size" number of times
                    if self.gridShips.isSpaceWater(self, row, x) == False: #if the space is not open/water
                        allSpacesOpen = False
                        break
                    else: #if the space is water
                        allSpacesOpen = True

                if allSpacesOpen is True: #if
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


    def stillHasShips(self, row, column):
        #if isSpaceWater(self, row, column) == False: #if the space
        #use a double for loop to traverse every single spot

        hasShips = True
        for r in range(0,10): #traverses through the rows
            for c in range(0,10): #traverses through the columns of each row
                if self.gridShips.isSpaceWater(r, c) is True: #if the space is water
                    hasShips = False
                elif self.gridShips.returnLocation(r,c) is "o" or "x": #if the space is already marked a hit/miss
                    hasShips = False
                else: #if the space has a ship value
                    hasShips = True
                    break
            if hasShips is True:
                break










