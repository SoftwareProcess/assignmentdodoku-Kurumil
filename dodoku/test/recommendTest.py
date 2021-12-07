from unittest import TestCase
import dodoku.status as recommend 
import dodoku.recommend as recommend 

class RecommendTest(TestCase):
        pass
    #Happy path test
    def test100_010NormalInput(self):
        expectedResult = {'recommendation': [3,8],'status':'ok'}      
        parms = {'op': 'recommend', 'cell': 'r7c9', 
                 'grid': '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]', 
                 'integrity': '5a3f0c31'}
        result = recommend._recommend(parms)
        self.assertEqual(expectedResult['recommendation'], result['recommendation'])
        self.assertEqual(expectedResult['status'], result['status'])

    #Happy path test
    def test100_020NormalInput(self):
        expectedResult = {'recommendation': [],'status':'ok'}      
        parms = {'op': 'recommend', 'cell': 'r1c1', 
                 'grid': '[0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]', 
                 'integrity': '8b3504ae'}
        result = recommend._recommend(parms)
        self.assertEqual(expectedResult['recommendation'], result['recommendation'])
        self.assertEqual(expectedResult['status'], result['status'])     

    #Happy path test
    def test100_030NormalInput(self):
        expectedResult = {'recommendation': [],'status':'ok'}      
        parms = {'op': 'recommend', 'cell': 'r1c2', 
                 'grid': '[0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]', 
                 'integrity': '8b3504ae'}
        result = recommend._recommend(parms)
        self.assertEqual(expectedResult['recommendation'], result['recommendation'])
        self.assertEqual(expectedResult['status'], result['status']) 

    #Happy path test
    def test100_040NormalInput(self):
        expectedResult = {'recommendation': [5],'status':'ok'}      
        parms = {'op': 'recommend', 'cell': 'r1c3', 
                 'grid': '[0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]', 
                 'integrity': '8b3504ae'}
        result = recommend._recommend(parms)
        self.assertEqual(expectedResult['recommendation'], result['recommendation'])
        self.assertEqual(expectedResult['status'], result['status'])