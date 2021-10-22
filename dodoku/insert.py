import re
import json

from dodoku import create


def _insert(parms):
    # parms:
    # {
    #     "op": "insert",
    #     "cell": "r1c1",
    #     "value": "1",
    #     "integrity": "5f3e8318",
    #     "grid": "[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]",
    # }

    ok, result = _check_keys(parms)
    if not ok:
        return result

    raw_text_grid = parms["grid"]
    raw_text_cell = parms["cell"]
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

    if not _is_valid_board(board):
        result["status"] = "warning"

    return result

def _check_keys(parms):
    keys = ["cell", "integrity", "grid"]
    for key in keys:
        if key not in parms.keys():
            return False, {"status": f"error: missing {key} reference"}
    return True, None

