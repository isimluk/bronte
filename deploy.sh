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

for pkg in postgresql postgresql-server python-sqlalchemy python-psycopg2; do
	rpm -q --quiet $pkg || sudo dnf install $pkg
done

if ! sudo grep -q "local[[:space:]]*all[[:space:]]*all[[:space:]]*trust" /var/lib/pgsql/data/pg_hba.conf; then
	echo "Make sure your /var/lib/pgsql/data/pg_hba.conf contains:
	local	all	all	trust
	host	all	127.0.0.1/32	trust"
	exit 1
fi

if ! systemctl status postgresql.service > /dev/null; then
	if ! sudo systemctl start postgresql.service; then
		systemctl status postgresql.service
		exit 1
	fi
fi

username=bronte
dbname=bronte
if ! grep -q "^$username:" /etc/passwd; then
	sudo adduser $username
	echo "The applicaion will run under the $username. Set the password for the user."
	read password
	sudo passwd $username --stdin <<< $password
	cat > backend/bronte.cfg <<_END
[db]
connection_string = 'postgresql://$username:$password@localhost:5432/$dbname'
_END
fi

pcmd='sudo su - postgres -c psql template1'
if ! $pcmd <<< '\du' | grep -q $username; then
	$pcmd <<< "CREATE USER $username;"
fi

if ! $pcmd <<< '\l' | grep -q $dbname; then
	$pcmd <<_END
	CREATE DATABASE $dbname;
	GRANT ALL PRIVILEGES ON DATABASE $dbname to $username;
_END
fi

pushd schema/bronte/postgresql
make clean main
popd
$pcmd < schema/bronte/postgresql/main.sql
