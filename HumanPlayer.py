from Player import Player

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    """
    takeTurn
    allows player to shoot at opponent's ships
    tells player if ship has been sunk and what kind
    also tells player if all ships are sunk and are the winner
    "x" marks a hit, "o" marks a miss
    parameters: otherPlayer Player object of opponent
    """
    def takeTurn(self, otherPlayer):

        invalid = True
        while invalid: #runs while space inputted is invalid/illegal
            row = int(input("Input row 0-9:"))
            if row < 0 or row > 9: #if user inputs something not between 0 and 9
                print("Space is illegal. Try again.")
                continue
            column = int(input("Input column 0-9:"))
            if column < 0 or column > 9: #if user inputs something not between 0 and 9
                print("Space is illegal. Try again")
                continue
            else:
                invalid = False

        if otherPlayer.gridShips.returnLocation(row,column) != "~": #if hit/if it's not water (assuming that they wouldn't shoot at the same place more than once)
            shipType = otherPlayer.gridShips.returnLocation(row, column)
            print("Hit!")
            otherPlayer.gridShips.changeSingleSpace(row, column, "x")  # mark as a hit on otherPlayer's gridShips
            self.gridShots.changeSingleSpace(row, column, "x")  # mark as a hit on player's gridShots

            sunk = True #helps check if ship is sunk or not
            for col in range(0, 10): #traverses through the columns
                for r in range(0, 10): #traverses through each row of the column
                    if otherPlayer.gridShips.returnLocation(r,col) == shipType: #if the ship is still not sunk
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

            self.printGrids()

        else: #if not hit
            print("Miss!")
            otherPlayer.gridShips.changeSingleSpace(row, column, "o")
            self.gridShots.changeSingleSpace(row, column, "o")
            self.printGrids()

    """
    placeShip
    places a ship onto the player's own grid
    parameters: type of ship, char
    parameters: size of the ship, int
    """
    def placeShip(self, ship, size):
        notPlaced = True
        while notPlaced: #while ship has not been placed

            direction = int(input("Input 0 for horizontal, 1 for vertical"))
            if direction != 0 and direction != 1: #if user inputs something other than 0 or 1
                print("Illegal input. Try again.")
                continue
            row = int(input("Input row 0-9:"))
            if row < 0 or row > 9: #if user inputs something not between 0 and 9
                print("Space is illegal. Try again.")
                continue
            column = int(input("Input column 0-9:"))
            if column < 0 or column > 9: #if user inputs something not between 0 and 9
                print("Space is illegal. Try again")
                continue

            if direction == 0: #if horizontal placement
                allSpacesOpen = True
                for x in range(column, column+size): #loops through the column's rows, "size" number of times
                    if column+size > 9:
                        print("Invalid position")
                        allSpacesOpen = False
                        break
                    if self.gridShips.isSpaceWater(row, x) == False: #if the space is not open/water
                        allSpacesOpen = False
                        print("Space is illegal")
                        break
                if allSpacesOpen == True: #if the spaces are legal
                    self.gridShips.changeRow(row, ship, column, size)
                    notPlaced = False
                    self.gridShips.printGrid()
            else: #if vertical placement
                allSpacesOpen = True

                for x in range(row, row+size): #loops through the row's columns, "size" number of times
                    if row+size > 9:
                        print("Invalid position")
                        allSpacesOpen = False
                        break
                    if self.gridShips.isSpaceWater(x, column) == False: #if the space is not open/water
                        allSpacesOpen = False
                        print("Space is illegal")
                        break
                if allSpacesOpen == True: #if the spaces are legal
                    self.gridShips.changeCol(column, ship, row, size)
                    notPlaced = False
                    self.printGrids()
    """
    stillHasShips
    checks a grid to see if it still has ships or not
    returns a boolean: false if it doesn't have ships, true if it has ships
    """

    def stillHasShips(self):
        for x in range(10): # traverses rows
            for y in range(10): # traverses columns
                if self.gridShips.returnLocation(x,y) != "o" and self.gridShips.returnLocation(x,y) != "x" and self.gridShips.returnLocation(x,y) != "~": # if element has a ship
                    return True
        return False