from ComputerPlayer import ComputerPlayer

cp1 = ComputerPlayer()
cp1.placeShip( "A" , 5 )
cp1.placeShip( "B", 4 )
cp1.placeShip( "C", 3 )
cp1.placeShip( "S", 3 )
cp1.placeShip( "D", 2 )

cp1.printGrids()
cp1.stillHasShips()