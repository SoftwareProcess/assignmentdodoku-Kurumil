from unittest import TestCase 
from urllib.parse import urlencode
import json
import http.client

import dodoku.insert as insert
from dodoku.create import _get_integrity, _get_grid_sha256

class InsertTest(TestCase):
    def setUp(self) -> None:
        self.PATH = "/dodoku?"
        self.PORT = 5000
        self.URL = "localhost"
        self.gridKey = 'grid'
        self.integrityKey = 'integrity'
        self.statusKey = 'status'
        self.statusOk = 'ok' 
        self.statusWarning = 'warning'
        self.statusError = 'error:' 
    def microservice(self, parm=""):
        """Issue HTTP Get and return result, which will be JSON string"""
        try:
            # print('request params keys -->', parm.keys())
            theParm = urlencode(parm)
            theConnection = http.client.HTTPConnection(self.URL, self.PORT)
            theConnection.request("GET", self.PATH + theParm)
            # print('request param --->', str(theParm))
            responseContent = theConnection.getresponse().read()
            # print(responseContent)
            theStringResponse = str(responseContent, "utf-8")
        except Exception as e:
            theStringResponse = "{'diagnostic': '" + str(e) + "'}"

        """Convert JSON string to dictionary"""
        result = {}
        try:
            jsonString = theStringResponse.replace("'", '"')
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if isinstance(unicodeDictionary[element], str):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result["diagnostic"] = str(e)
        return result

    def _test_valid_insert(self, r, c, value):
        inputGrid = [ 0,-2, 0, 0,-1, 0, 0,-4, 0,
                     -8, 0,-1,-9, 0, 0, 0, 0,-5,
                      0, 0, 0, 0,-3, 0, 0,-1, 0,
                      0,-3, 0, 0, 0, 0,-4, 0,-6,
                     -5, 0,-9, 0, 0, 0, 0, 0,-7,
                      0, 0, 0, 0, 0, 0,-2,-8, 0,
                     -2, 0, 0,-6, 0, 0, 0, 0, 0, 0,-1,-4, 0,-6, 0,
                      0, 0,-6, 0, 0,-3, 0, 0, 0,-2, 0, 0,-1, 0,-9,
                      0,-4, 0,-5,-7, 0, 0, 0, 0, 0, 0,-7, 0, 0,-5,
                                        0, 0,-6, 0, 0, 0, 0,-9, 0,
                                       -2, 0, 0, 0, 0, 0,-4, 0,-8,
                                       -7, 0,-9, 0, 0, 0, 0, 0, 0,
                                        0,-5, 0, 0,-9, 0, 0, 0, 0,
                                       -4, 0, 0,-6, 0,-3,-9, 0, 0,
                                        0,-6, 0, 0,-5, 0, 0,-3,-1]
        inputParmDict = {
                            'op': 'insert',
                            'cell': f'r{r}c{c}',
                            'value': f'{value}',
                            'integrity': _get_integrity(inputGrid),
                            'grid': f'[{",".join(map(str, inputGrid))}]'
                         }

        board = insert._gridlist_to_board(inputGrid.copy())
        board[r-1][c-1] = value
        expectedOutputGrid = insert._board_to_grid_list(board)
        
        expectedIntegrity = _get_grid_sha256(expectedOutputGrid)
        expectedStatus = 'ok'
        exptectedKeyCount = 3

        actualResult = self.microservice(inputParmDict)
        # print(actualResult)
        
        actualKeyCount = len(actualResult)
        self.assertEqual(actualKeyCount, exptectedKeyCount)

        actualGridValue = actualResult.get(self.gridKey, [])
        self.assertEqual(actualGridValue, expectedOutputGrid)

        actualIntegrityValue = actualResult.get(self.integrityKey, '')
        self.assertEqual(8, len(actualIntegrityValue))
        self.assertIn(actualIntegrityValue, expectedIntegrity)

        actualStatusValue = actualResult.get(self.statusKey, '')
        self.assertEqual(actualStatusValue, expectedStatus)

    def test_valid_insert_1(self):
        self._test_valid_insert(1,  1,  6)

    def test_valid_insert_2(self):
        self._test_valid_insert(1,  3,  5)

    def test_valid_insert_3(self):
        self._test_valid_insert(15,  7,  9)

    def _test_invalid_insert_key_missing(self, key):
        inputGrid = [ 0,-2, 0, 0,-1, 0, 0,-4, 0,
                     -8, 0,-1,-9, 0, 0, 0, 0,-5,
                      0, 0, 0, 0,-3, 0, 0,-1, 0,
                      0,-3, 0, 0, 0, 0,-4, 0,-6,
                     -5, 0,-9, 0, 0, 0, 0, 0,-7,
                      0, 0, 0, 0, 0, 0,-2,-8, 0,
                     -2, 0, 0,-6, 0, 0, 0, 0, 0, 0,-1,-4, 0,-6, 0,
                      0, 0,-6, 0, 0,-3, 0, 0, 0,-2, 0, 0,-1, 0,-9,
                      0,-4, 0,-5,-7, 0, 0, 0, 0, 0, 0,-7, 0, 0,-5,
                                        0, 0,-6, 0, 0, 0, 0,-9, 0,
                                       -2, 0, 0, 0, 0, 0,-4, 0,-8,
                                       -7, 0,-9, 0, 0, 0, 0, 0, 0,
                                        0,-5, 0, 0,-9, 0, 0, 0, 0,
                                       -4, 0, 0,-6, 0,-3,-9, 0, 0,
                                        0,-6, 0, 0,-5, 0, 0,-3,-1]
        inputParmDict = {
                            'op': 'insert',
                            'cell': 'r1c1',
                            'value': '1',
                            'integrity': _get_integrity(inputGrid),
                            'grid': f'[{",".join(map(str, inputGrid))}]'
                         }

        del inputParmDict[key]


        expectedOutputGrid = inputGrid.copy()
        expectedOutputGrid[0] = 1
        expectedIntegrity = _grid2column(expectedOutputGrid)
        expectedStatus = 'error: missing'
        
        exptectedKeyCount = 1

        actualResult = self.microservice(inputParmDict)
        
        actualKeyCount = len(actualResult)
        self.assertEqual(actualKeyCount, exptectedKeyCount)

        actualStatusValue = actualResult.get(self.statusKey, '')
        self.assertEqual(actualStatusValue.startswith(expectedStatus), True)



    
    
