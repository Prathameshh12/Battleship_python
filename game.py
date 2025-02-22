from components import Segment, Ship, Cell, InvalidPlacementException, InvalidPositionException, InvalidShipTypeException, Board
import string

if __name__ == "__main__":
    # Your code should start here
    obj = Board()
    print("Welcome to BATTLESHIP!")
    print()
    print("Setup Phase")
    print("Player 1 place your ships, Player 2 - no peeking.")
    print()
    print(obj.display_setup())

    for ship_type in ["battleship", "carrier", "destroyer", "submarine", "patrol boat"]:
        ship = Ship.createShip(ship_type)
        size = ship.length()
        while True:
            print(f"Where would you like to place your {ship.name()}?")
            position = input("Position: ").strip().lower()
            col = string.ascii_lowercase.index(position[0])
            row = int(position[1:]) - 1
            direction = input("Direction: ").strip().lower()
            if not (0 <= col < Board.SIZE) or not (0 <= row < Board.SIZE):
                print("That position does not exist.")
                continue
            try:
                obj.place_ship(ship, position, direction)
                break
            except (InvalidShipTypeException, InvalidPositionException, InvalidPlacementException):
                print("That is not a valid placement for that ship.")

        
        print(obj.display_setup())

    
    print("Attack Phase")
    print("Player 2, sink the fleet!")
    print()
    obj1 = Board()
    print(obj1.display_setup())
    obj2 = Ship.createShip(ship_type)
    obj3 = Cell()
    
    shots = 0
    coordinate = None
    attacked_positions = set()
    
    while any(not cell.has_been_hit() for row in obj._Board__board.values() for cell in row.values() if isinstance(cell, Cell) and cell.is_occupied() and not cell.has_been_hit()):
        
        try:
            coordinate = input("Enter a grid coordinate to attack: ").strip().lower()
        except EOFError:
            print("Invalid input. Please try again.")
            continue
        
        
        
        if len(coordinate) < 2 or len(coordinate) > 3:
            print("Invalid coordinate. Try again.")
            continue
        col = string.ascii_lowercase.index(coordinate[0])
        row = int(coordinate[1:]) - 1

        if (row, col) in attacked_positions:
            print("That position has already been attacked. Try again.")
            print(obj)
            continue
        
        if not (0 <= col < Board.SIZE) or not (0 <= row < Board.SIZE):
            print("That is not a valid position to attack.")
            print(obj)
            continue

        attacked_positions.add((row, col))
        

        try:
            result = obj.attack(coordinate)
            shots += 1
            print(obj)
            
        except InvalidPositionException:
            print("That is not a valid position to attack.")
            print(obj)

        
      
    
    print(f"The fleet has been sunk in {shots} shots!")

    print("GAME OVER")
