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

from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String

from bronte.model.entities.entities_common import Base
from bronte.model.entities.brStockMarket import BrStockMarket

class BrTicker(Base):
    __tablename__ = 'brticker'

    id = Column(Integer, Sequence('br_ticker_id_seq'), primary_key=True)
    exchange_id = Column(Integer, ForeignKey('brstockmarket.id'))
    ticker = Column(String)
    name = Column(String)
    exchange = relationship(BrStockMarket)

    def __init__(self, exchange, ticker, name):
        self.exchange = exchange
        self.ticker = ticker
        self.name = name

    def __repr__(self):
        return "<BrTicker(%s, '%s','%s')>" % \
                (self.exchange, self.ticker, self.name)
