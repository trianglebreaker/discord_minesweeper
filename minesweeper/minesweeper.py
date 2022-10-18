# Boards are generated basically at random. No checking is done other than to
# ensure the center is free of mines.

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
    
    # I'm not using this in the real thing anyway
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

def generate_board():
    return


