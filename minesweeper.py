import random

# ***Define functions: ***************************


def create_solution_grid(mines, num_rows=5, num_cols=5):
    """
    Function to initialise a grid with mines in
    
    parameters: numbers of mines, rows and columns

    output: a 2d list, named "solution_grid" where "#" represents 
            a mined position and "-"an unmined position
    """

    grid = [["-"]*num_cols for _ in range(num_rows)]

    positions = list(range(num_rows * num_cols))
    # print(positions)
    mine_locations = random.sample(positions, mines)
    # print(mine_locations)

    for mine in mine_locations:
        grid[mine // num_cols][mine % num_cols] = "#"
    
    return grid


def print_grid(grid):
    for row in grid:
        print(row)


class Position:
    def __init__(self, row, col, num_rows=5, num_cols=5):
        self.row = row
        self.col = col
        self.num_rows = num_rows
        self.num_cols = num_cols
    
    def is_in_bounds(self):
        if (
            (self.row in range(self.num_rows)) 
            and (self.col in range(self.num_cols))
        ):
            return True
        else:
            return False


def search_for_mines(current_position: Position, solution_grid):
    adjacent_mines_count = 0
    
    north = Position(current_position.row - 1, current_position.col)
    north_east = Position(current_position.row - 1, current_position.col + 1)
    east = Position(current_position.row, current_position.col + 1)
    south_east = Position(current_position.row + 1, current_position.col + 1)
    south = Position(current_position.row + 1, current_position.col)
    south_west = Position(current_position.row + 1, current_position.col - 1)
    west = Position(current_position.row, current_position.col - 1)
    north_west = Position(current_position.row - 1, current_position.col - 1)
    
    for adjacent_position in [
                              north, north_east, east, south_east, 
                              south, south_west, west, north_west
                              ]:
        if adjacent_position.is_in_bounds() == False:
            pass
        elif adjacent_position.is_in_bounds() == True:
            if solution_grid[adjacent_position.row][adjacent_position.col] == "#":
                adjacent_mines_count += 1
            else:
                pass
    
    return adjacent_mines_count

def populate_question_grid(solution_grid, num_rows=5, num_cols=5):
    question_grid = [[None]*num_cols for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            current_position = Position(i,j)
            mine_count = search_for_mines(current_position, solution_grid)
            question_grid[i][j] = mine_count

    return question_grid    


#*************User inputs: *************************

num_mines = int(input("""
    Welcome to the Minesweeper Game!

    How many mines do you want in the grid? 
    (Please enter a number between zero and 25):
    """))

solution_grid = create_solution_grid(num_mines)

question_grid = populate_question_grid(solution_grid)

print(f"""
    Minesweeper Game:
    -----------------
    There are {num_mines} mines in the grid.
    The number displayed in each grid position denotes the number of mines """
    """present in adjacent positions.
    (Note that this can include horizontally, vertically and diagonally adjacent.)
    Can you locate all the mines?
    """)
print_grid(question_grid)

i=0
while i < 20:
    solution = input("""
        To view the solution grid, please type "view solution" and press enter:  """
        ).strip(" ").lower()

    if solution == "view solution":
        print_grid(solution_grid)
        print("""
              (The mines are in the positions with a hash symbol.)
              Thanks for playing!""")
        break
    else:
        i += 1