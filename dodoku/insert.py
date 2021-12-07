'''    
    Created on Oct 21, 2021
    
    @author:    Mingcong Li
'''    

import json
import re

from dodoku import create


def _insert(parms):
    ok, result = _check_keys(parms)
    if not ok:
        return result

    raw_text_grid = parms["grid"]
    raw_text_cell = parms["cell"]
    if "value" in parms and parms["value"]=='0':
        return {'status':'error: invalid value'}
    raw_text_value = parms.get("value", "0")
    integrity = parms["integrity"]

    ok, grid = _parse_grid(raw_text_grid)
    if not ok:
        return {"status": "error: invalid grid"}
    if not _is_valid_grid(grid):
        return {"status": "error: invalid grid"}
    board = _gridlist_to_board(grid)

    ok, cell = _parse_cell(raw_text_cell)
    if not ok:
        return {"status": "error: invalid cell reference"}
    if not _is_valid_cell(board, cell):
        return {"status": "error: invalid cell reference"}

    ok, value = _parse_value(raw_text_value)
    if not ok:
        return {"status": "error: invalid value"}
    if not _is_valid_value(value):
        return {"status": "error: invalid value"}

    if not _is_valid_integrity(grid, integrity):
        return {"status": "error: integrity mismatch"}

    r, c = cell
    board = _gridlist_to_board(grid)
    if board[r - 1][c - 1] < 0:
        return {"status": "error: attempt to change fixed hint"}

    board[r - 1][c - 1] = value
    grid = _board_to_grid_list(board)
    integrity = create._get_integrity(grid)
    result = {"status": "ok", "grid": grid, "integrity": integrity}

    if _is_valid_board(board,r,c):
        result["status"] = "warning"

    return result


def _check_keys(parms):
    keys = ["cell", "integrity", "grid"]
    for key in keys:
        if key not in parms.keys():
            return False, {"status": f"error: missing {key} reference"}
    return True, None


def _parse_cell(raw_cell_text):
    pat = r"^[rR](\d\d?)[cC](\d\d?)$"
    m = re.fullmatch(pat, raw_cell_text)
    if m is None:
        return False, None
    r = int(m[1])
    c = int(m[2])
    return True, (r, c)


def _is_valid_cell(board, cell):
    r, c = cell
    if not 1 <= r <= 15:
        return False
    if not 1 <= c <= 15:
        return False
    if board[r - 1][c - 1] is None:
        return False
    return True


def _parse_grid(raw_grid_text):
    try:
        grid = json.loads(raw_grid_text)
        return True, grid
    except:
        return False, None


def _is_valid_grid(grid):
    try:
        assert isinstance(grid, list)
        assert len(grid) == 153
        assert all(isinstance(x, int) for x in grid)
        assert all(abs(x) <= 9 for x in grid)
        return True
    except:
        return False

def _is_valid_board(board,r,c):
    value = board[r-1][c-1]
    board[r-1][c-1] = 0
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
    return value in numbers

def _parse_value(raw_value_text):
    try:
        return True, int(raw_value_text)
    except:
        return False, None


def _is_valid_value(value):
    return 0 <= value <= 9


def _parse_integrity(integrity):
    return integrity


def _is_valid_integrity(grid, integrity):
    sha256_str = create._get_grid_sha256(grid)
    return (
        isinstance(integrity, str) and len(integrity) == 8 and integrity in sha256_str
    )


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


def _board_to_grid_list(board):
    grid = []
    for r in range(6):
        nums = board[r][:9]
        grid.extend(nums)
    for r in range(6, 9):
        nums = board[r][:]
        grid.extend(nums)
    for r in range(9, 15):
        nums = board[r][6:15]
        grid.extend(nums)
    return grid