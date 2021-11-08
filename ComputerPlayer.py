from Player import Player
import random
class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.oHit = False
        self.shotHit = False # tells us if the current shot just made was a hit
        self.direction = 0
        self.r = 0
        self.c = 0
        self.belowOpen = False
        self.aboveOpen = False
        self.rightOpen = False
        self.leftOpen = False
        self.count = 0
        self.countMax = 4
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
    shot
    shoots at space
    self.shotHit is True if ship is hit, False if miss
    """
    def shot(self, otherPlayer, r, c):
        if otherPlayer.gridShips.returnLocation(r, c) == "~":  # if shot at water
            otherPlayer.gridShips.changeSingleSpace(r, c, "o")
            self.gridShots.changeSingleSpace(r, c, "o")
            self.shotHit = False
        elif otherPlayer.gridShips.returnLocation(r, c) != "~":  # if shot at ship
            otherPlayer.gridShips.changeSingleSpace(r, c, "x")
            self.gridShots.changeSingleSpace(r, c, "x")
            print("Hit")
            self.shotHit = True
    """
    checkSpaces
    checks the surrounding spaces to see if they are water and might have a ship
    """
    def checkSpaces(self):
        if self.r != 9 and self.gridShots.returnLocation(self.r, self.c) == "~":
            self.belowOpen = True
        if self.r != 0 and self.gridShots.returnLocation(self.r, self.c) == "~":
            self.aboveOpen = True
        if self.c != 0 and self.gridShots.returnLocation(self.r, self.c) == "~":
            self.leftOpen = True
        if self.c != 9 and self.gridShots.returnLocation(self.r, self.c) == "~":
            self.rightOpen = True
    """
    takeTurn
    takes shot at new space
    notifies if ship has been hit/sunk
    @param  otherPlayer  Player object of opposing player
    """
    def takeTurn(self,otherPlayer):
        if self.oHit: # if the previous turn hit a ship and it's not sunk yet
            if self.count == 0:
                self.checkSpaces()
            self.count += 1
            if (self.belowOpen == False and self.direction == 0) or self.count > self.countMax: # if space below isn't open
                self.direction = 2
                self.count = 0
            if (self.aboveOpen == False and self.direction == 2) or self.count > self.countMax: # if space above isn't open
                self.direction = 1
                self.count = 0
            if (self.leftOpen == False and self.direction == 1) or self.count > self.countMax: # if space to left isn't open
                self.direction = 3
                self.count = 0
            """ this will never be true/run
            if (self.rightOpen == False and self.direction == 3) or self.count > self.countMax: # if space to right isn't open
                self.direction = 0
                self.count = 0
            """
            if self.direction == 0: # space below
                self.shot(otherPlayer, self.r + self.count, self.c) # takes shot below
                if self.shotHit is False:  # miss
                    self.direction = 2 # changes direction to above
                    self.count = 0
            elif self.direction == 2:  # space above
                self.shot(otherPlayer, self.r - self.count, self.c)
                if self.shotHit is False:  # miss
                    self.direction = 1
                    self.count = 0
            elif self.direction == 1:  # space to left
                self.shot(otherPlayer,self.r, self.c - self.count)
                if self.shotHit is False:  # miss
                    self.direction = 3
                    self.count = 0
            elif self.direction == 3:  # space to right
                self.shot(otherPlayer,self.r, self.c + self.count)
                """ this will never be true/run
                if self.shotHit is False:  # miss
                    self.direction = 0
                    self.count = 0
                """
        else: # previous turn did not hit a ship5
            needNewSpace = True
            while needNewSpace: # runs until new index is generated
                self.r = random.randrange(0, 10)
                self.c = random.randrange(0, 10)
                if self.gridShots.returnLocation(self.r,self.c) == "~": # if space has not been shot at
                    self.shot(otherPlayer, self.r, self.c)
                    needNewSpace = False
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
                elif otherPlayer.gridShips.returnLocation(x,y) == "C": # there is a cruiser
                    c += 1
                elif otherPlayer.gridShips.returnLocation(x,y) == "D": # there is a destroyer
                    d += 1
                elif otherPlayer.gridShips.returnLocation(x,y) == "S": # there is a sub
                    s += 1
        if a == 0: # aircraft sunk
            print("aircraft carrier sunk")
            self.oHit = False
            self.direction = 0
            self.count = 0
            self.countMax = 3
        if b == 0: # battleship sunk
            print("battleship sunk")
            self.oHit = False
            self.direction = 0
            self.count = 0
            if a == 0: # aircraft and battleship sunk
                self.countMax = 2
        if c == 0: # cruiser sunk
            print("cruiser sunk")
            self.oHit = False
            self.direction = 0
            self.count = 0
            self.countMax = 1
            if a == 0 and b == 0 and s == 0: # aircraft, battleship, cruiser, and sub sunk
                self.countMax = 1
        if d == 0: # destroyer sunk
            print("destroyer sunk")
            self.oHit = False
            self.direction = 0
            self.count = 0
        if s == 0: # sub sunk
            print("submarine sunk")
            self.oHit = False
            self.direction = 0
            self.count = 0
            if a == 0 and b == 0 and c == 0: # aircraft, battleship, cruiser, and sub sunk
                self.countMax = 1
    """
    stillHasShips
    determines if you still have ships on your board
    @return  boolean  false if no more ships and vice versa
    """
    def stillHasShips(self):
        for x in range(10): # traverses rows
            for y in range(10): # traverses columns
                if self.gridShips.returnLocation(x,y) != "o" and self.gridShips.returnLocation(x,y) != "x" and self.gridShips.returnLocation(x,y) != "~": # if element has a ship
                    return True
        return False