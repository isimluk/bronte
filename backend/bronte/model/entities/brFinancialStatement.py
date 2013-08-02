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
from sqlalchemy.types import Date
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String

from bronte.model.entities.entities_common import Base
from bronte.model.entities.brFinancialPeriod import BrFinancialPeriod
from bronte.model.entities.brFinancialReport import BrFinancialReport
from bronte.model.entities.brFinancialStatementType import BrFinancialStatementType

class BrFinancialStatement(Base):
    __tablename__ = 'brfinancialstatement'

    id = Column(Integer, Sequence('br_finstatement_id_seq'), primary_key=True)
    report_id = Column(Integer, ForeignKey('brfinancialreport.id'))
    statement_type_id = Column(Integer,
            ForeignKey('brfinancialstatementtype.id'))
    period_id = Column(Integer, ForeignKey('brfinancialperiod.id'))
    period_end = Column(Date)
    notes = Column(String)
    report = relationship(BrFinancialReport, backref="statements")
    statement_type = relationship(BrFinancialStatementType)
    period = relationship(BrFinancialPeriod)

    def __init__(self, report, statement_type, period, period_end):
        self.report = report
        self.statement_type = statement_type
        self.period = period
        self.period_end = period_end

    def __repr__(self):
        return "<BrFinancialStatement(%s, %s, %s, '%s')>" % \
                (self.report, self.statement_type, self.period, self.period_end)
