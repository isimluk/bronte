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

import HTMLParser
import os
import pickle
import sys

from ultrafinance.dam.googleFinance import GoogleFinance
from ultrafinance.dam.yahooFinance import YahooFinance

sys.path.insert(0, os.path.realpath('../../'))

from bronte.crawler.common import CrawlerException
from bronte.crawler.google.model import GoogleLedgerItem
from bronte.crawler.google.parser import GoogleDateParser
from bronte.model import Session
from bronte.model.BrFactory import BrFactory

session = Session()
factory = BrFactory(session)

class UFGoogleDataSerializer(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def fetch(self):
        self.financials = GoogleFinance().getFinancials(self.symbol)

    def serialize_financials(self):
        self.result = {}
        h = HTMLParser.HTMLParser()
        for item_name, values in self.financials.iteritems():
            item_name = h.unescape(item_name)
            statement_type = GoogleLedgerItem.get_statement_type(item_name)
            for date, value in values.iteritems():
                if value:
                    d = GoogleDateParser(date)
                    self._store_result(d, statement_type, item_name, value)
        print self.result

    def _store_result(self, date, statement_type, item_name,
            value):
        day = date.getDay()
        period = date.getPeriod()
        if day not in self.result:
            self.result[day] = {}
        if statement_type not in self.result[day]:
            self.result[day][statement_type] = {}
        if period not in self.result[day][statement_type]:
            self.result[day][statement_type][period] = {}
        assert item_name not in self.result[day][statement_type][period]
        self.result[day][statement_type][period][item_name] = value

class UFYahooDataSerializer(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def fetch(self):
        self.info = YahooFinance().getAll(self.symbol)

    def store(self):
        print self._get_ticker()

    def _get_ticker(self):
        market = self._get_stock_exchange()
        return factory.get_ticker(market, symbol)

    def _get_stock_exchange(self):
        acronym =  self.info['stock_exchange']
        if acronym.startswith('"'):
            acronym = acronym[1:-1]
        return factory.get_stock_market(acronym)



class StockSerializer(object):
    def __init__(self, symbol):
        self.symbol = symbol
        self.ys = UFYahooDataSerializer(symbol)
        self.gs = UFGoogleDataSerializer(symbol)

    def fetch(self):
        self.ys.fetch()
        self.gs.fetch()

    def store(self):
        self.ys.store()
        self.gs.serialize_financials()

ss = StockSerializer("GOOG")
ss.fetch()
ss.store()

