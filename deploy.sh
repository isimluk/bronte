#!/bin/bash
#
# Copyright (c) 2013--2016 Simon Lukasik
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#

set -e -o pipefail
set -x

for pkg in postgresql postgresql-server; do
	rpm -q --quiet $pkg || sudo dnf install $pkg
done

if ! systemctl status postgresql.service > /dev/null; then
	if ! sudo systemctl start postgresql.service; then
		systemctl status postgresql.service
		exit 1
	fi
fi

username=bronte
if ! grep -q "^$username:" /etc/passwd; then
	sudo adduser $username
	echo "The applicaion will run under the $username. Set the password for the user."
	sudo passwd $username
fi

pcmd='sudo su - postgres -c psql template1'
if ! $pcmd <<< '\du' | grep -q $username; then
	$pcmd <<< "CREATE USER $username;"
fi

if ! $pcmd <<< '\l' | grep -q $username; then
	$pcmd <<_END
        CREATE DATABASE $username;
	GRANT ALL PRIVILEGES ON DATABASE $username to $username;
_END
fi

