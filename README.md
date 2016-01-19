Bronte -- Stock Analysis Tool
=============================
Copyright (c) 2013--2014 Simon Lukasik

Mission Statement
-----------------
To provide open source data model supporting fundamential and technical
analysis of financial instruments (stocks and options).


Package Requirements
--------------------
backend: python-sqlalchemy python-psycopg2 ultra-finance
schema:  postgresql

How to build schema
-------------------
cd schema/bronte/postgresql
make clean main

How to install schema
---------------------
- Create new postgresql user called 'bronte'.
- Create new database called 'bronte'
- Grant all priviledges on this database to the user.
- Deploy schema/bronte/postgresql/main.sql into the database

How to configure backend
------------------------
cat > cat backend/bronte.cfg <<_END
[db]
connection_string = 'postgresql://bronte:changeme@localhost:5432/bronte'
_END

How to test
-----------
cd backend/tests/bronte
python tests.py

How to manually connect to the database
---------------------------------------
sudo systemctl start postgresql.service
psql -d myDb -U username -W

