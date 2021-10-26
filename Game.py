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
    cp.takeTurn(hp)

if hp.stillHasShips() == False:
    print("Computer Won!")
if cp.stillHasShips() == True:
    print("You Won!")
print("Game over")