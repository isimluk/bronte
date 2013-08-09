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
import ConfigParser

main_config_file = '../../bronte.cfg'

class Configure(object):
    def __init__(self):
        self.__read(main_config_file)
        if 'config_addon' in self.__dict__:
            for file in self.config_addon:
                self.__read(file)

    def __read(self, filename):
        cp = ConfigParser.ConfigParser()
        cp.read(filename)
        for section in cp.sections():
            for option, value in cp.items(section):
                if section == 'general':
                    name = option
                else:
                    name = '%s_%s' % (section, option)
                self.__dict__[name] = self.parse(value)

    @classmethod
    def parse(self, content):
        content = content.replace('\n', '')
        if not len(content):
            return None
        elif re.match(r'^\d+$', content):
            return int(content)
        elif re.match(r'\d+\.\d*', content):
            return float(content)
        elif re.match(r'\[.*\]', content):
            return eval(content)
        elif re.match(r'{.*}', content):
            return eval(content)
        elif re.match(r'^["\'].*["\']$', content):
            return str(content)[1:-1]
        else:
            return str(content)

    def update(self, args):
        for key in args.__dict__:
            if args.__dict__[key] != None:
                self.__dict__[key] = args.__dict__[key]

conf = Configure()
