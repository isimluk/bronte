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

import re

from bronte.crawler.common import CrawlerException

class GoogleDateParser(object):
    def __init__(self, date_string):
        self.date_string = date_string
        self.period = None
        self.date = None
        self._parse()

    def _parse(self):
        # Google give us a date in following formats:
        # 1) For balance sheet items 'As of 2013-03-31'
        # 2) For income/cashflow items '12 months ending 2010-12-31'
        if self.date_string[:6] == 'As of ':
            self.day = self.date_string[6:]
        else:
            r = re.match(r'(\d+) months ending (\d{4}-\d{2}-\d{2})$', self.date_string)
            if r:
                self.period = r.group(1)
                self.day = r.group(2)
            else:
                raise CrawlerException("Could not parse date: ", self.date_string[:16])
        if len(self.day) != 10 or not re.match(r'(\d{4}-\d{2}-\d{2})$', self.day):
            raise CrawlerException("Could not parse date: ", self.day)

    def getDay(self):
        return self.day

    def getPeriod(self):
        return self.period


