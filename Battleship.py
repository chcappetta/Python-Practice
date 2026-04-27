#battleship
import random

def setup_grid():
    grid0 = ["-","-","-"]
    grid1 = ["-","-","-"]
    grid2 = ["-","-","-"]
    
    ship0 = random.randint(0,2)
    ship1 = random.randint(0,2)
    ship2 = random.randint(0,2)

    grid0[ship0] = "|"
    grid1[ship1] = "|"
    grid2[ship2] = "|"

    return [grid0,grid1,grid2]


def blank_grid():
    grid0 = ["-","-","-"]
    grid1 = ["-","-","-"]
    grid2 = ["-","-","-"]

    return [grid0,grid1,grid2]


def main():
    user_grid = blank_grid()
    actual_grid = setup_grid()

    print("Welcome to Battleship")
    print("Grid is 3x3, guesses will be X and Y:")
    print(user_grid[2][0],user_grid[2][1],user_grid[2][2])
    print(user_grid[1][0],user_grid[1][1],user_grid[1][2])
    print(user_grid[0][0],user_grid[0][1],user_grid[0][2])
    hit = 0

    while (hit < 3):
        guessx = int(input("X value: "))
        guessy = int(input("Y value: "))

        if (actual_grid[guessy-1][guessx-1] == "|"):
            hit+=1
            print("Hit!")
            print()
            user_grid[guessy-1][guessx-1] = "X"
            print(user_grid[2][0],user_grid[2][1],user_grid[2][2])
            print(user_grid[1][0],user_grid[1][1],user_grid[1][2])
            print(user_grid[0][0],user_grid[0][1],user_grid[0][2])
        else:
            print("Miss.")
            print()
            user_grid[guessy-1][guessx-1] = "O"
            print(user_grid[2][0],user_grid[2][1],user_grid[2][2])
            print(user_grid[1][0],user_grid[1][1],user_grid[1][2])
            print(user_grid[0][0],user_grid[0][1],user_grid[0][2])
            
    print()
    print()
    print("You win!!")
    return

main()
            
    
    
