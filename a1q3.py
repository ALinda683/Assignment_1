# Name: Alinda Kumar Mazumder
# NSID: ugj683
# Student ID: 11342454
# Course: CMPT 145

def initialRead_state(filename):
    """ Reads a file's contents and returns the starting state as a list of lists.
           Args: filename (str): The name of the file to read.
           Returns: list: A collection of lists representing the initial state. Each row of the initial state is represented by an inner list.
       with open("input_1.txt", 'r') as file:
           lines = file.readlines()
       initialState = [list(line.strip()) for line in lines]
       return initialState
       """
    with open("input_3.txt", 'r') as file:
        lines = file.readlines()
    initialState = [list(line.strip()) for line in lines]
    return initialState

def neighboursCounting(grid_display, i, j):
    """ Updates the status of a grid display based on the Game of Life rules.
            Args: grid_display (list): A list of lists representing the current state of the grid display.
                                     Each inner list represents a grid display row.
                                     The characters in each row are saved as distinct inner list components.
                                     The grid display can include the characters '*' to denote live cells
                                     and '-' to represent dead cells.

            Returns: list: The updated status of the grid display after applying the Game of Life rules.
            """
    neighbours = []
    rows, cols = len(grid_display), len(grid_display[0])
    if i > 0:
        neighbours.append(grid_display[i - 1][j])
    if i < rows - 1:
        neighbours.append(grid_display[i + 1][j])
    if j > 0:
        neighbours.append(grid_display[i][j - 1])
    if j < cols - 1:
        neighbours.append(grid_display[i][j + 1])
    return neighbours

def update_state(grid_display):

    new_grid_display = []
    for i, row in enumerate(grid_display):
        new_row = []
        for j, cell in enumerate(row):
            neighbours = neighboursCounting(grid_display, i, j)
            surviving_neighbours = neighbours.count('*')
            if cell == '*':
                if surviving_neighbours < 2 or surviving_neighbours > 3:
                    new_row.append('-')
                else:
                    new_row.append('*')
            else:
                if surviving_neighbours == 3:
                    new_row.append('*')
                else:
                    new_row.append('-')
        new_grid_display.append(new_row)
    return new_grid_display

def Conway(input_3):
    """
    Args:
    filename (str): The path to a text file containing the initial state.
    Returns: None
    """
    initialState = initialRead_state(input_3)
    state_updated = update_state(initialState)
    n = len(initialState)
    textfile_updated = f"{n}x{n}_updated.txt"
    with open(textfile_updated, 'w') as file:
        for row in state_updated:
            file.write(''.join(row) + '\n')
    print(f"The updated state has been saved to {textfile_updated}.")

Conway("input_3.txt")
