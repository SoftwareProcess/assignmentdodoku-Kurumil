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
    result['status'] = 'ok'
    result['integrity'] = _get_integrity(result['grid'])
    return result


# integrity functions
def _get_integrity(grid):
    concat_columns = _getcolumn(grid)
    myHash = hashlib.sha256(concat_columns.encode()).hexdigest()
    random_start = random.randrange(0, 64 - 8)
    return myHash[random_start:random_start + 8]

def _getcolumn(grid):
    columns = []*15
    for col in range(1,16):
        for row in range(1,16):
            if(row>9 and col<=6): continue
            if(col>9 and row<=6): continue
            columns.append(grid[_getIndex(row,col)])
    return ''.join(map(str, columns))

def _getIndex(row,col):
    index = 0
    if(row<=6):
        index = (row-1)*9+col
    elif(row>6 and row<=9):
        index = 54 + (row-7)*15+col
    else:
        index = 99 + (row-10)*9 + (col-6)
    return index-1

def _get_grid_sha256(grid):
    concat_columns = _getcolumn(grid)
    hash_str = hashlib.sha256(concat_columns.encode()).hexdigest()
    return hash_str
