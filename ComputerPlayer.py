from Player import Player
import random
class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
    """
    placeShip
    randomly places parameter ship in clear spaces
    @param  ship  char ship
    @param  size  int size of ship
    """
    def placeShip(self , ship , size):
        shipNotPlace = True
        while shipNotPlace: # ship still needs to be placed
            shipNotPlace = False
            a = random.randrange(0,2)
            if a == 0: # horizontal
                r = random.randrange(0, 10)
                c = random.randrange(0, 11-size)
                for col in range(size): # checks if all spaces are legal
                    if self.gridShips.isSpaceWater(r,col+c) == False: # if space is illegal
                        shipNotPlace = True
                        break
                if shipNotPlace == False: # area is clear
                    self.gridShips.changeRow(r, ship, c, size)
            else: # if vertical
                r = random.randrange(0, 11-size)
                c = random.randrange(0, 10)
                for row in range(size):  # checks if all spaces are legal
                    if self.gridShips.isSpaceWater(row+r, c) == False:  # if space is illegal
                        shipNotPlace = True
                        break
                if shipNotPlace == False: # area is clear
                    self.gridShips.changeCol(c, ship, r, size)

    """
    takeTurn
    takes shot at random new space
    notifies if ship has been hit/sunk
    @param  otherPlayer  Player object of opposing player
    """
    def takeTurn(self,otherPlayer):
        b = True
        while b: # runs until new index is generated
            r = random.randrange(0, 10)
            c = random.randrange(0, 10)
            if otherPlayer.gridShips.returnLocation(r,c) != "o" and otherPlayer.gridShips.returnLocation(r,c) != "x": # if space has not been shot at
                b = False
        if otherPlayer.gridShips.returnLocation(r,c) != "~": # if shot at water
            otherPlayer.gridShips.changeSingleSpace(r,c,"o")
            self.gridShots.changeSingleSpace(r,c,"o")
        else: # if shot at ship
            otherPlayer.gridShips.changeSingleSpace(r,c,"x")
            self.gridShots.changeSingleSpace(r,c,"x")
            print("Hit")
        self.printGrids()
        a = 0
        b = 0
        c = 0
        d = 0
        s = 0
        for x in range(10): # traverses rows
            for y in range(10): # traverses columns
                if otherPlayer.gridShips.returnLocation(x,y) == "A": # there is an aircraft carrier
                    a += 1
                elif otherPlayer.gridShips.returnLocation(x,y) == "B": # there is a battleship
                    b += 1
                elif otherPlayer.gridShips.returnLocation(x, y) == "C": # there is a cruiser
                    c += 1
                elif otherPlayer.gridShips.returnLocation(x, y) == "D": # there is a destroyer
                    d += 1
                elif otherPlayer.gridShips.returnLocation(x, y) == "S": # there is a sub
                    s += 1
        if a == 0: # aircraft sunk
            print("aircraft carrier sunk")
        if b == 0: # battleship sunk
            print("battleship sunk")
        if c == 0: # cruiser sunk
            print("cruiser sunk")
        if d == 0: # destroyer sunk
            print("destroyer sunk")
        if s == 0: # sub sunk
            print("submarine sunk")
    """
    stillHasShips
    determines if you still have ships on your board
    @return  boolean  false if no more ships and vice versa
    """
    def stillHasShips(self):
        b = False
        for x in range(10): # traverses rows
            for y in range(10): # traverses columns
                if self.gridShips.returnLocation(x,y) != "o" or self.gridShips.returnLocation(x,y) != "x" or self.gridShips.returnLocation(x,y) != "~": # if element has a ship
                    b = True
        return b