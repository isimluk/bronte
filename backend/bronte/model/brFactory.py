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

from bronte import BronteException
from bronte.model.entities.brStockMarket import BrStockMarket
from bronte.model.entities.brTicker import BrTicker

class BrFactory(object):
    def __init__(self, session):
        self.s = session

    def get_ticker(self, br_market, ticker):
        existing_tickers = self.s.query(BrTicker) \
                .filter(BrTicker.exchange_id == br_market.id, BrTicker.ticker == ticker)
        if existing_tickers.count() == 1:
            return existing_tickers[0]
        elif existing_tickers.count() == 0:
            t = BrTicker(br_market, ticker, None)
            self.s.add(t)
            self.s.commit()
            self.s.flush()
            return t
        else:
            raise BronteException("Expecting single ticket but got %s" % existing_tickers.all())
            assert False

    def get_stock_market(self, market_acronym):
        market_acronym = self._market_acronym_override(market_acronym)
        markets = self.s.query(BrStockMarket) \
                .filter(BrStockMarket.acronym == market_acronym)
        assert markets.count() == 1
        return markets[0]

    @staticmethod
    def _market_acronym_override(market_acronym):
        acronym_map = {
          'NYQ': 'NYSE'
        }
        if market_acronym in acronym_map:
            return acronym_map[market_acronym]
        return market_acronym
