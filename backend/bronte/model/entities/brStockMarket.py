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

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, String

Base = declarative_base()

class BrStockMarket(Base):
    __tablename__ = 'brstockmarket'

    id = Column(Integer, Sequence('br_stockmarker_id_seq'), primary_key=True)
    acronym = Column(String)
    name = Column(String)

    def __init__(self, acronym, name):
        self.acronym = acronym
        self.name = name

    def __repr__(self):
        return "<BrStockMarket('%s','%s')>" % (self.acronym, self.name)
