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
        board = _gridlist_to_board(grid)
        assert _is_valid_board(board)
        return True
    except:
        return False

def _is_valid_nine_nums(nine_nums):

    for num in nine_nums:
        if not num <= 9:
            return False
    s = set()
    for num in nine_nums:
        if num == 0:
            continue
        if num in s:
            return False
        else:
            s.add(num)
    return True

def _is_valid_board(board):

    for i in range(9):
        row = board[i][:9]
        nine_nums = [abs(x) for x in row]
        if not _is_valid_nine_nums(nine_nums):
            return False

    for i in range(6, 15):
        row = board[i][6:15]
        nine_nums = [abs(x) for x in row]
        if not _is_valid_nine_nums(nine_nums):
            return False

    for c in range(9):
        col = []
        for r in range(9):
            col.append(board[r][c])
        nine_nums = [abs(x) for x in row]
        if not _is_valid_nine_nums(nine_nums):
            return False

    for c in range(6, 15):
        col = []
        for r in range(6, 15):
            col.append(board[r][c])
        nine_nums = [abs(x) for x in row]
        if not _is_valid_nine_nums(nine_nums):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nine_nums = []
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    nine_nums.append(abs(board[r][c]))
            if not _is_valid_nine_nums(nine_nums):
                return False

    for i in range(6, 15, 3):
        for j in range(6, 15, 3):
            nine_nums = []
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    nine_nums.append(abs(board[r][c]))
            if not _is_valid_nine_nums(nine_nums):
                return False

    return True

def _parse_value(raw_value_text):
    try:
        return True, int(raw_value_text)
    except:
        return False, None


def _is_valid_value(value):
    return -9 <= value <= 9


def _parse_integrity(integrity):
    return integrity


def _is_valid_integrity(grid, integrity):
    sha256_str = create._get_grid_sha256(grid)
    return (
        isinstance(integrity, str) and len(integrity) == 8 and integrity in sha256_str
    )


