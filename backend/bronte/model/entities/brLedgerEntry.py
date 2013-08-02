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
from sqlalchemy import Column, ForeignKey, Integer, Sequence

from entities_common import Base
from brLedgerItem import BrLedgerItem
from brStatementSummary import BrStatementSummary

class BrLedgerEntry(Base):
    __tablename__ = 'brledgerentry'

    id = Column(Integer, Sequence('br_ledgerentry_id_seq'), primary_key=True)
    statement_id = Column(Integer, ForeignKey('brstatementsummary.id'))
    item_id = Column(Integer, ForeignKey('brledgeritem.id'))
    amount = Column(Integer)
    modified = Column(DateTime)
    statement = relationship(BrStatementSummary, backref="entries")
    item = relationship(BrLedgerItem)

    def __init__(self, statement, item, amount):
        self.statement = statement
        self.item = item
        self.amount = amount

    def __repr__(self):
        return "<BrLedgerEntry(%s, %s, %s)>" % \
                (self.statement, self.item, self.amount)
