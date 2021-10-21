'''
    
    Created to demonstrate the counting standard
    
    Created on Sept 29, 2121
    Updated on Sept 29, 2121
    
    @author: Mingcong Li
    
'''

from unittest import TestCase
import http.client
from urllib.parse import urlencode
import json
import random


class CreateTest(TestCase):
    def setUp(self) -> None:
        self.PATH = '/dodoku?'
        self.PORT = 5000
        self.URL = 'localhost'

    def microservice(self, parm=""):
        '''Issue HTTP Get and return result, which will be JSON string'''
        try:
            theParm = urlencode(parm)
            theConnection = http.client.HTTPConnection(self.URL, self.PORT)
            theConnection.request("GET", self.PATH + theParm)
            theStringResponse = str(theConnection.getresponse().read(), "utf-8")
        except Exception as e:
            theStringResponse = "{'diagnostic': '" + str(e) + "'}"

        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = theStringResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString) 
            for element in unicodeDictionary:
                if (isinstance(unicodeDictionary[element], str)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result

    def test_base(self):
        parms = {'op': 'create', 'level': 1}
        result = self.microservice(parms)
        self.assertIn('grid', result)
        self.assertIn('integrity', result)
        self.assertIn('status', result)

# Happy path create&level 1
    def test_level_1(self):
        parms = {'op': 'create', 'level': 1}
        result = self.microservice(parms)
        self.assertEqual(result['status'], 'ok')
        actual_grid = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        self.assertEqual(result['grid'], actual_grid)
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')

# Happy path create&level 2
    def test_level_2(self):
        parms = {'op': 'create', 'level': 2}
        result = self.microservice(parms)
        self.assertEqual(result['status'], 'ok')
        actual_grid = [0, -6, 0, 0, 0, 0, 0, -5, -9, -9, -3, 0, -4, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7, -3, 0, 0, 0,
                       -5, 0, 0, -1, 0, 0, -4, -6, 0, 0, 0, 0, 0, -6, 0, -9, 0, 0, -8, -1, -2, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, -8, 0, -4, 0, 0, -1, 0, 0, 0, -7, 0, 0, -6, 0, -2, 0,
                       -9, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, -5, -3, 0, 0, -7, 0, -4, 0, 0,
                       0, 0, 0, -5, -8, 0, 0, -1, 0, 0, -9, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, -8, 0,
                       -6, -1, -6, -1, 0, 0, 0, 0, 0, -7, 0]
        self.assertEqual(result['grid'], actual_grid)
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a')

# Happy path create&level 3
    def test_level_3(self):
        parms = {'op': 'create', 'level': 3}
        result = self.microservice(parms)
        self.assertEqual(result['status'], 'ok')
        actual_grid = [0, 0, 0, 0, -6, 0, 0, 0, 0, 0, 0, 0, -4, 0, -9, 0, 0, 0, 0, 0, -9, -7, 0, -5, -1, 0, 0, 0, -5,
                       -2, 0, -7, 0, -8, -9, 0, -9, 0, 0, -5, 0, -2, 0, 0, -4, 0, -8, -3, 0, -4, 0, -7, -2, 0, 0, 0,
                       -1, -2, 0, -8, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, -6, 0, -4, 0, 0, 0, -8, 0, -7, 0, 0, 0, 0,
                       0, 0, 0, -5, 0, 0, 0, 0, -1, 0, -6, -3, 0, 0, 0, -9, -8, 0, -5, 0, -1, -2, 0, -2, 0, 0, -7, 0,
                       -1, 0, 0, -3, 0, -4, -3, 0, -8, 0, -6, -5, 0, 0, 0, -7, -3, 0, -5, -9, 0, 0, 0, 0, 0, -4, 0,
                       -2, 0, 0, 0, 0, 0, 0, 0, -6, 0, 0, 0, 0]
        self.assertEqual(result['grid'], actual_grid)
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], 'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9')

# Happy path
    def test_empty_level(self):
        parms = {'op': 'create', 'level': ''}
        result = self.microservice(parms)
        actual_grid = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        self.assertEqual(result['grid'], actual_grid)
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')

# Happy path
    def test_extraneous(self):
        parms = {'op': 'create', 'extraneous': 3}
        result = self.microservice(parms)
        actual_grid = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        self.assertEqual(result['grid'], actual_grid)
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')

# Sad path a, 1.2, 0, 4
    def test_invalid_level(self):
        parms = {'op': 'create', 'level': random.choice(['a', '1.2', '0', '4'])}
        result = self.microservice(parms)
        self.assertEqual(result['status'][:6], 'error:')


