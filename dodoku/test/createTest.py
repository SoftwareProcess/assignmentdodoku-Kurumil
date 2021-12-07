'''
    
    Created to demonstrate the counting standard
    
    Created on Sept 29, 2121
    Updated on Sept 29, 2121
    
    @author: Mingcong Li
    
'''

from unittest import TestCase
import dodoku.create as create

class CreateTest(TestCase):

    #Happy path test
    def test100_010ShouldReturnLevel1Grid(self):
        parms = {'op':'create','level': '1'}
        expectedResult = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        result = create._create(parms)
        self.assertEqual(result['grid'], expectedResult)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')
    
    def test100_020ShouldReturnLevel2Grid(self):
        parms = {'op':'create','level': '2'}
        expectedResult = [0, -6, 0, 0, 0, 0, 0, -5, -9, -9, -3, 0, -4, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7, -3, 0, 0, 0,
                       -5, 0, 0, -1, 0, 0, -4, -6, 0, 0, 0, 0, 0, -6, 0, -9, 0, 0, -8, -1, -2, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, -8, 0, -4, 0, 0, -1, 0, 0, 0, -7, 0, 0, -6, 0, -2, 0,
                       -9, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, -5, -3, 0, 0, -7, 0, -4, 0, 0,
                       0, 0, 0, -5, -8, 0, 0, -1, 0, 0, -9, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, -8, 0,
                       -6, -1, -6, -1, 0, 0, 0, 0, 0, -7, 0]
        result = create._create(parms)
        self.assertEqual(result['grid'], expectedResult)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a')
    
    def test100_030ShouldReturnLevel3Grid(self):
        parms = {'op':'create','level': '3'}
        expectedResult = [0, 0, 0, 0, -6, 0, 0, 0, 0, 0, 0, 0, -4, 0, -9, 0, 0, 0, 0, 0, -9, -7, 0, -5, -1, 0, 0, 0, -5,
                       -2, 0, -7, 0, -8, -9, 0, -9, 0, 0, -5, 0, -2, 0, 0, -4, 0, -8, -3, 0, -4, 0, -7, -2, 0, 0, 0,
                       -1, -2, 0, -8, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, -6, 0, -4, 0, 0, 0, -8, 0, -7, 0, 0, 0, 0,
                       0, 0, 0, -5, 0, 0, 0, 0, -1, 0, -6, -3, 0, 0, 0, -9, -8, 0, -5, 0, -1, -2, 0, -2, 0, 0, -7, 0,
                       -1, 0, 0, -3, 0, -4, -3, 0, -8, 0, -6, -5, 0, 0, 0, -7, -3, 0, -5, -9, 0, 0, 0, 0, 0, -4, 0,
                       -2, 0, 0, 0, 0, 0, 0, 0, -6, 0, 0, 0, 0]
        result = create._create(parms)
        self.assertEqual(result['grid'], expectedResult)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], 'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9')
        
    def test100_040ShouldReturnEmptyLevelGrid(self):
        parms = {'op':'create','level': ''}
        expectedResult = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        result = create._create(parms)
        self.assertEqual(result['grid'], expectedResult)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')
        
    def test100_050ShouldReturnEmptyLevelParm(self):
        parms = {'op':'create','': ''}
        expectedResult = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        result = create._create(parms)
        self.assertEqual(result['grid'], expectedResult)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')
        
    def test100_060ShouldIgnoreCaseSensitiveLevel(self):
        parms = {'op':'create','Level': '3'}
        expectedResult = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        result = create._create(parms)
        self.assertEqual(result['grid'], expectedResult)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')

    def test100_060ShouldIgnoreExtraneous(self):
        parms = {'op':'create','extraneous': '3'}
        expectedResult = [0, -2, 0, 0, -1, 0, 0, -4, 0, -8, 0, -1, -9, 0, 0, 0, 0, -5, 0, 0, 0, 0, -3, 0, 0, -1, 0, 0,
                       -3, 0, 0, 0, 0, -4, 0, -6, -5, 0, -9, 0, 0, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, -2, -8, 0, -2, 0,
                       0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0, 0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9,
                       0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -6, 0, 0, 0, 0, -9, 0, -2, 0, 0, 0, 0,
                       0, -4, 0, -8, -7, 0, -9, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, -9, 0, 0, 0, 0, -4, 0, 0, -6, 0, -3,
                       -9, 0, 0, 0, -6, 0, 0, -5, 0, 0, -3, -1]
        result = create._create(parms)
        self.assertEqual(result['grid'], expectedResult)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(len(result['integrity']), 8)
        self.assertIn(result['integrity'], '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd')
    
    #Sad path test
    
    def test110_010ShouldErrorWithNonIntLevel(self):
        parms = {'op':'create','level': 'a'}
        result = create._create(parms)
        self.assertEqual(result['status'][:6], 'error:')
    
    def test110_020ShouldErrorWithNonNumericLevel(self):
        parms = {'op':'create','level': '1.2'}
        result = create._create(parms)
        self.assertEqual(result['status'][:6], 'error:')
    
    def test110_030ShouldErrorWithBelowBoundLevel(self):
        parms = {'op':'create','level': '0'}
        result = create._create(parms)
        self.assertEqual(result['status'][:6], 'error:')
    
    def test110_040ShouldErrorWithAboveBoundLevel(self):
        parms = {'op':'create','level': '4'}
        result = create._create(parms)
        self.assertEqual(result['status'][:6], 'error:')
        
    def test110_050ShouldReturn57IntegrityValue(self):
        totalIntegrity = "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"
        parms = {'op': 'create', 'level': '1'}
        number = 5700
        set1 = set()
        while(number>0):
            integrity = create._create(parms)['integrity']
            set1.add(integrity)
            number -= 1
        for key in set1:
            self.assertIn(key, totalIntegrity)
            self.assertEqual(len(key), 8)
        self.assertEqual(len(set1),56)