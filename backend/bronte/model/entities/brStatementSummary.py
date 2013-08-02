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
from sqlalchemy.types import DateTime
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String

from entities_common import Base
from brCurrency import BrCurrency
from brDataSource import BrDataSource
from brFinancialStatement import BrFinancialStatement

class BrStatementSummary(Base):
    __tablename__ = 'brstatementsummary'

    id = Column(Integer, Sequence('br_statesum_id_seq'), primary_key=True)
    statement_id = Column(Integer, ForeignKey('brfinancialstatement.id'))
    datasource_id = Column(Integer, ForeignKey('brdatasource.id'))
    currency_id = Column(Integer, ForeignKey('brcurrency.id'))
    created = Column(DateTime)
    modified = Column(DateTime)
    notes = Column(String)
    statement = relationship(BrFinancialStatement, backref="summaries")
    datasource = relationship(BrDataSource)
    currency = relationship(BrCurrency)

    def __init__(self, statement, datasource, currency, notes=None):
        self.statement = statement
        self.datasource = datasource
        self.currency = currency
        self.notes = notes

    def __repr__(self):
        return "<BrStatementSummary(%s, %s, %s, '%s')>" % \
                (self.statement, self.datasource, self.currency, self.notes)
