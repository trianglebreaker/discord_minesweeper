import random

# Boards are generated basically at random. No checking is done other than to
# ensure the center is free of mines.


MIN_DIMENSIONS = (7, 7)
MIN_MINES = 5
NUMBER_EMOJI_CODES = ["one", "two", "three", "four", "five", "six", "seven", "eight"]


# Representation of a minesweeper board.
# -1 is a mine, 0 to 8 is the number of mine cells surrounding that cell.
# (0, 0) is the top left cell.
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mines = 0
        self.grid = [[0] * width for i in range(height)]
    
    def get_adjacent_cells(self, x, y):
        candidates = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        cells = []
        for i in candidates:
            if 0 > i[0] or 0 > i[1] or self.width <= i[0] or self.height <= i[1]: continue
            cells.append(i)
        return cells
    
    def add_mine(self, x, y):
        if self.grid[y][x] == -1: return
        self.grid[y][x] = -1
        adjacent_cells = self.get_adjacent_cells(x, y)
        for i in adjacent_cells:
            if self.grid[i[1]][i[0]] != -1: self.grid[i[1]][i[0]] += 1
        self.mines += 1
    
    def __str__(self):
        rows = []
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if self.grid[y][x] == -1: row += "X"
                elif self.grid[y][x] == 0: row += "."
                else: row += str(self.grid[y][x])
            rows.append(row)
        return "\n".join(rows)


# Generates a board with mines.
# Automatically places a safe spot in the center.
def generate_board(width, height, mine_count):
    # Value handling
    width = max(width, MIN_DIMENSIONS[0])
    if width % 2 == 0: width += 1
    height = max(height, MIN_DIMENSIONS[0])
    if height % 2 == 0: height += 1
    # maybe there's a better way, but 50% mine density seems easiest
    mine_count = max(min(mine_count, (width * height - 9) // 2), MIN_MINES)
    
    board = Board(width, height)
    
    # maybe I could change the safe coordinate spot to be random in the future.
    # but for now it will always be in the center
    start_cell_coords = (width // 2, height // 2)
    safe_cell_range = (start_cell_coords[0] - 1, start_cell_coords[0] + 1, start_cell_coords[1] - 1, start_cell_coords[1] + 1) # min x, max x, min y, max y
    
    mines = random.sample(range(width * height - 9), mine_count)
    mines = dict.fromkeys(mines)
    
    n = 0
    for i in range(width * height):
        x = i % width
        y = i // height
        
        if x >= safe_cell_range[0] and x <= safe_cell_range[1] and y >= safe_cell_range[2] and y <= safe_cell_range[3]: continue
        
        if n in mines:
            board.add_mine(x, y)
        n += 1
    
    print(f"Generated a {width} by {height} board with {mine_count} mines")
    
    return board


# Given a board, returns a string representation of it in Discord Markdown format.
def board_to_discord_string(board, blank_emoji, mine_emoji):
    string_parts = []
    
    for y in range(board.height):
        row_string = ""
        for x in range(board.width):
            i = board.grid[y][x]
            if i == -1:
                row_string += f"||:{mine_emoji}:||"
            elif i == 0:
                row_string += f"||:{blank_emoji}:||"
            else:
                row_string += f"||:{NUMBER_EMOJI_CODES[i - 1]}:||"
        
        string_parts.append(row_string)
    
    return "\n".join(string_parts)
