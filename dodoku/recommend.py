import json
import re
def _recommend(parms):
    raw_text_grid = parms["grid"]
    raw_text_cell = parms["cell"]
    ok, grid = _parse_grid(raw_text_grid)
    board = _gridlist_to_board(grid)

    ok, cell = _parse_cell(raw_text_cell)
    if not ok:
        return {"status": "error: invalid cell reference"}
    if not _is_valid_cell(board, cell):
        return {"status": "error: invalid cell reference"}    
    r, c = cell
    recommend_numbers = _get_recommendation_numbers(board,r,c)
    result = {'recommendation': recommend_numbers,'status':'ok'}
    return result

def _parse_grid(raw_grid_text):
    try:
        grid = json.loads(raw_grid_text)
        return True, grid
    except:
        return False, None

def _parse_cell(raw_cell_text):
    pat = r"^[rR](\d\d?)[cC](\d\d?)$"
    m = re.fullmatch(pat, raw_cell_text)
    if m is None:
        return False, None
    r = int(m[1])
    c = int(m[2])
    return True, (r, c)

def _gridlist_to_board(grid):
    board = []
    cur_index = 0
    for _ in range(6):
        row = grid[cur_index : cur_index + 9]
        row = row + [None] * 6
        board.append(row)

        cur_index += 9
    for _ in range(3):
        board.append(grid[cur_index : cur_index + 15])
        cur_index += 15
    for _ in range(6):
        row = grid[cur_index : cur_index + 9]
        row = [None] * 6 + row
        board.append(row)
        cur_index += 9
    return board

def _get_recommendation_numbers(board,r,c):
    if board[r-1][c-1]<0:
        return []
    board[r-1][c-1] = 0
    all_numbers = set(range(1,10))
    row_numbers = set()
    for num in board[r-1]:
        if num:
            row_numbers.add(abs(num))
    col_numbers = set()
    for row in range(0,15):
        if board[row][c-1]:
            col_numbers.add(abs(board[row][c-1]))
    subgrid_numbers = set()
    row_start_index = (r-1)//3*3
    col_start_index = (c-1)//3*3
    for row in range(row_start_index, row_start_index+3):
        for col in range(col_start_index, col_start_index+3):
            if board[row][col]:
                subgrid_numbers.add(abs(board[row][col]))
    numbers = row_numbers.union(col_numbers).union(subgrid_numbers)
    recommend_numbers = (all_numbers - numbers)
    return sorted(list(recommend_numbers))

def _is_valid_cell(board, cell):
    r, c = cell
    if not 1 <= r <= 15:
        return False
    if not 1 <= c <= 15:
        return False
    if board[r - 1][c - 1] is None:
        return False
    return True 