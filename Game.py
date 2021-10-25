from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

hp = HumanPlayer()
cp = ComputerPlayer()

cp.createShipGrid()
cp.gridShips.printGrid()
hp.createShipGrid()
hp.gridShips.printGrid()

while hp.stillHasShips() and cp.stillHasShips():
    hp.takeTurn(cp)
    hp.printGrids()
    cp.takeTurn(hp)
    cp.printGrids()

print("Game over")