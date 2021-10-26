from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

hp = HumanPlayer()
cp = ComputerPlayer()

cp.createShipGrid()
cp.gridShips.printGrid()
hp.createShipGrid()

while hp.stillHasShips() and cp.stillHasShips():
    print("Take your turn:")
    hp.takeTurn(cp)
    print("Computer's turn:")
    cp.takeTurn(hp)


if hp.stillHasShips() == False:
    print("Computer Won!")
if cp.stillHasShips() == True:
    print("You Won!")

print("Game over")