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

from entities_common import Base

class BrTickerCompanyMap(Base):
    __tablename__ = 'brtickercompanymap'

    id = Column(Integer, Sequence('br_ticco_id_seq'), primary_key=True)
    ticker_id = Column(Integer, ForeignKey('brticker.id'))
    company_id = Column(Integer, ForeignKey('brcompany.id'))
    description = Column(String)
    company = relationship("BrCompany", backref="tickers")
    ticker = relationship("BrTicker", backref="company", uselist=False)

    def __repr__(self):
        return "<BrTicker(%s, %s)>" % (self.company, self.ticker)
