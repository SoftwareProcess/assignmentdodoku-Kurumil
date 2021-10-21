from unittest import TestCase 
from urllib.parse import urlencode
import json
import random
import http.client

import dodoku.insert as insert
from dodoku.create import _get_integrity, _getcolumn, _get_grid_sha256

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