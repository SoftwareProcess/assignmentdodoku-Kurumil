from unittest import TestCase 
from urllib.parse import urlencode
import json
import random
import http.client

import dodoku.insert as insert
from dodoku.create import _get_integrity, _getcolumn, _get_grid_sha256

    def test_valid_insert_1(self):
        self._test_valid_insert(1,  1,  6)
 
