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

from entities_common import Base
from brCompany import BrCompany

class BrFinancialReport(Base):
    __tablename__ = 'brfinancialreport'

    id = Column(Integer, Sequence('br_finreport_id_seq'), primary_key=True)
    company_id = Column(Integer, ForeignKey('brcompany.id'))
    period_end = Column(Date)
    release_date = Column(Date)
    notes = Column(String)
    company = relationship(BrCompany)

    def __init__(self, company, period_end, release_date=None, notes=None):
        self.company = company
        self.period_end = period_end
        self.release_date = release_date
        self.notes = notes

    def __repr__(self):
        return "<BrFinancialReports(%s, '%s')>" % \
                (self.company, self.period_end)
