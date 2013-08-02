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

from sqlalchemy import Column, Integer, Sequence, String

from entities_common import Base

class BrCurrency(Base):
    __tablename__ = 'brcurrency'

    id = Column(Integer, Sequence('br_currency_id_seq'), primary_key=True)
    code = Column(String)
    sign = Column(String)
    name = Column(String)

    def __init__(self, code, sign, name):
        self.code = code
        self.sign = sign
        self.name = name

    def __repr__(self):
        return "<BrCurrency('%s', '%s','%s')>" % \
            (self.code, self.sign, self.name)
