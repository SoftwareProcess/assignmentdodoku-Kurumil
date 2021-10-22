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

    
    
