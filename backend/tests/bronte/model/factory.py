#!/usr/bin/python
#
# Copyright (c) 2013--2016 Simon Lukasik
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#

import os
import sys
import unittest
sys.path.insert(0, os.path.realpath('../../../'))
from tests.bronte import CommonBase
from bronte.model.brFactory import BrFactory

class TestBrFactory(CommonBase):
    def test_get_stock_market(self):
        f = BrFactory(self.session)
        nasdaq = f.get_stock_market('NYQ')
        assert nasdaq.acronym == 'NYSE'
