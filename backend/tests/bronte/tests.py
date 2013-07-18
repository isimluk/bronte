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
from bronte.model.entities import BrStockMarket, BrTicker

class CommonBase(unittest.TestCase):
    def setUp(self):
        db_engine = create_engine(db_connection_string)
        Session = sessionmaker()
        Session.configure(bind=db_engine)
        self.session = Session()

class TestBrStockMarket(CommonBase):
    def _ensure_exists(self, marker_acr):
        markets = self.session.query(BrStockMarket).filter(BrStockMarket.acronym == marker_acr)
        assert markets.count() == 1
        assert markets[0].acronym == marker_acr
    def test_ny_exists(self):
        self._ensure_exists('NASDAQ')
        self._ensure_exists('NYSE')
        self._ensure_exists('NasdaqNM')

class TestBrTicker(CommonBase):
    TEST_TICKER = 'BR_TESTING'
    def _test_exchange(self):
        return self.session.query(BrStockMarket).first()
    def _get_new_ticker(self):
        exchange = self._test_exchange()
        return BrTicker(self._test_exchange(), self.TEST_TICKER, "Bronte Testing Ticker")
    def _find_tickers(self):
        return self.session.query(BrTicker).filter(
            (BrTicker.exchange==self._test_exchange()) and (ticker==self.TEST_TICKER))
    def _count_tickers(self):
        return self._find_tickers().count()
    def _del_test_ticker(self):
        self._find_tickers().delete()
        self.session.commit()
        self.session.flush()
    def test_create(self):
        self._del_test_ticker()
        assert self._count_tickers() == 0
        self.session.add(self._get_new_ticker())
        self.session.commit()
        self.session.flush()
        assert self._count_tickers() == 1
        self._del_test_ticker()
        assert self._count_tickers() == 0

if __name__ == '__main__':
    unittest.main()
