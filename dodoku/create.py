'''
    
    Created to demonstrate the counting standard
    
    Created on Sept 29, 2121
    Updated on Sept 29, 2121
    
    @author: Mingcong Li
    
'''

import hashlib
import random

# main
def _create(parms):
    result = {'status': 'create stub'}
    level = parms.get('level')
    if level == '1' or not level:
        result['grid'] = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                          -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                          0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                          0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                          0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                          -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
    elif level == '2':
        result['grid'] = [0, -6, 0, 0, 0, 0, 0, -5, -9, -9, -3, 0, -4, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7, -3, 0, 0, 0,
                          -5, 0, 0, -1, 0, 0, -4, -6, 0, 0, 0, 0, 0, -6, 0, -9, 0, 0, -8, -1, -2, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, -8, 0, -4, 0, 0, -1, 0, 0, 0, -7, 0, 0, -6, 0, -2, 0,
                          -9, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, -5, -3, 0, 0, -7, 0, -4, 0, 0,
                          0, 0, 0, -5, -8, 0, 0, -1, 0, 0, -9, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, -8, 0,
                          -6, -1, -6, -1, 0, 0, 0, 0, 0, -7, 0]
    elif level == '3':
        result['grid'] = [0, 0, 0, 0, -6, 0, 0, 0, 0, 0, 0, 0, -4, 0, -9, 0, 0, 0, 0, 0, -9, -7, 0, -5, -1, 0, 0, 0, -5,
                          -2, 0, -7, 0, -8, -9, 0, -9, 0, 0, -5, 0, -2, 0, 0, -4, 0, -8, -3, 0, -4, 0, -7, -2, 0, 0, 0,
                          -1, -2, 0, -8, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, -6, 0, -4, 0, 0, 0, -8, 0, -7, 0, 0, 0, 0,
                          0, 0, 0, -5, 0, 0, 0, 0, -1, 0, -6, -3, 0, 0, 0, -9, -8, 0, -5, 0, -1, -2, 0, -2, 0, 0, -7, 0,
                          -1, 0, 0, -3, 0, -4, -3, 0, -8, 0, -6, -5, 0, 0, 0, -7, -3, 0, -5, -9, 0, 0, 0, 0, 0, -4, 0,
                          -2, 0, 0, 0, 0, 0, 0, 0, -6, 0, 0, 0, 0]
    else:
        return {'status': 'error: invalid level!'}

# return grid, status
    result['integrity'] = _get_integrity(result['grid'])
    result['status'] = 'ok'
    return result

# integrity functions
def _get_integrity(grid):
    concat_columns = _getcolumn(grid)
    hash_str = hashlib.sha256(concat_columns.encode()).hexdigest()
    random_start = random.randrange(0, 64 - 8)
    return hash_str[random_start:random_start + 8]

# get column
def _getcolumn(grid):
    columns = []
    for i in range(9):
        columns.append(grid[:54][i::9])
    for i in range(9):
        columns[i].extend(grid[54:99][i::15])
    for i in range(3):
        columns[i + 6].extend(grid[99:][i::9])
    for i in range(6):
        columns.append(grid[54:99][(i + 9)::15])
    for i in range(6):
        columns[i + 9].extend(grid[99:][(i + 3)::9])
    flat_columns = [j for i in columns for j in i]
    return ''.join(map(str, flat_columns))



