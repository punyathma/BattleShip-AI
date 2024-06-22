import random

def create_battleship_grid(size=10):
    grid = [['o' for _ in range(size)] for _ in range(size)]
    ships = [(5, "Aircraft Carrier"), (4, "Battleship"), (3, "Cruiser"), (3, "Submarine"), (2, "Destroyer")]

    for ship_size, ship_name in ships:
        while True:
            direction = random.choice(['horizontal', 'vertical'])
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)

            if direction == 'horizontal' and col + ship_size <= size:
                if all(grid[row][col + i] == 'o' for i in range(ship_size)):
                    for i in range(ship_size):
                        grid[row][col + i] = ship_name[0]  # Use the first letter of the ship name as the symbol
                    break
            elif direction == 'vertical' and row + ship_size <= size:
                if all(grid[row + i][col] == 'o' for i in range(ship_size)):
                    for i in range(ship_size):
                        grid[row + i][col] = ship_name[0]  # Use the first letter of the ship name as the symbol
                    break

    return grid

def display_grid(grid):
    for row in range(len(grid)):
        print(" ".join(grid[row]))
    print()

def solve_battleship(grid):
    size = len(grid)
    hits = 0
    misses = 0
    max_hits = 17  # Maximum number of hits before stopping

    for row in range(size):
        for col in range(size):
            print(f"Checking cell [{row}][{col}]")
            if grid[row][col] != 'o':
                print(f"AI found a ship at [{row}][{col}] - It's a hit!")

                # Replace ship symbols based on their names
                if grid[row][col] == 'A':
                    grid[row][col] = 'A'  # Aircraft Carrier
                elif grid[row][col] == 'B':
                    grid[row][col] = 'B'  # Battleship
                elif grid[row][col] == 'C':
                    grid[row][col] = 'C'  # Cruiser
                elif grid[row][col] == 'S':
                    grid[row][col] = 'S'  # Submarine
                elif grid[row][col] == 'D':
                    grid[row][col] = 'D'  # Destroyer

                hits += 1

                # Check if the maximum number of hits is reached
                if hits >= max_hits:
                    print("\nFinal Grid:")
                    display_grid(grid)
                    print(f"Total cells checked: {hits + misses}")
                    print(f"Hits: {hits}")
                    print(f"Misses: {misses}")
                    return
            else:
                print(f"No ship found at [{row}][{col}] - It's a miss")
                grid[row][col] = '-'

                misses += 1

    print("\nFinal Grid:")
    display_grid(grid)
    print(f"Total cells checked: {hits + misses}")
    print(f"Hits: {hits}")
    print(f"Misses: {misses}")

battleship_grid = create_battleship_grid()

print("Initial Grid:")
display_grid([['o' for _ in range(10)] for _ in range(10)])

print("Solving Battleship:")
solve_battleship(battleship_grid)
