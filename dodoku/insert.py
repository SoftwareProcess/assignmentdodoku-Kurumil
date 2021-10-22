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

