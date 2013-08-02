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
from bronte.model.entities.brFinancialStatementType import BrFinancialStatementType

class BrLedgerItem(Base):
    __tablename__ = 'brledgeritem'

    id = Column(Integer, Sequence('br_ledgeritem_id_seq'), primary_key=True)
    statement_type_id = Column(Integer,
            ForeignKey('brfinancialstatementtype.id'))
    name = Column(String)
    statement_type = relationship(BrFinancialStatementType, backref="items")

    def __init__(self, statement_type, name):
        self.statement_type = statement_type
        self.name = name

    def __repr__(self):
        return "<BrLedgerItem(%s, '%s')>" % (self.statement_type, self.name)
