#!/usr/bin/python
#
# Copyright (c) 2013 Simon Lukasik
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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
sys.path.insert(0, os.path.realpath('../../'))
from tests import db_connection_string
from bronte.model.entities import BrStockMarket

class TestBrStockMarket(unittest.TestCase):
    def setUp(self):
        db_engine = create_engine(db_connection_string)
        db_engine.echo = True
        Session = sessionmaker()
        Session.configure(bind=db_engine)
        self.session = Session()
    def test_listing(self):
        for market in self.session.query(BrStockMarket):
            print market.__repr__().encode('utf-8')
    def _ensure_exists(self, marker_acr):
        markets = self.session.query(BrStockMarket).filter(BrStockMarket.acronym == marker_acr)
        assert markets.count() == 1
        assert markets[0].acronym == marker_acr
    def test_ny_exists(self):
        self._ensure_exists('NASDAQ')
        self._ensure_exists('NYSE')
        self._ensure_exists('NasdaqNM')

if __name__ == '__main__':
    unittest.main()
