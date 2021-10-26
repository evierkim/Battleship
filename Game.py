from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

hp = HumanPlayer()
cp = ComputerPlayer()

cp.createShipGrid()
cp.gridShips.printGrid()
hp.createShipGrid()
print("Human Player, Make First Move:")

while hp.stillHasShips() and cp.stillHasShips():
    hp.takeTurn(cp)
    cp.takeTurn(hp)

print("Game over")