--
-- Copyright (c) 2013 Simon Lukasik
--
-- This software is licensed to you under the GNU General Public License,
-- version 2 (GPLv2). There is NO WARRANTY for this software, express or
-- implied, including the implied warranties of MERCHANTABILITY or FITNESS
-- FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
-- along with this software; if not, see
-- http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
--

CREATE TABLE brFinancialStatementType
(
    id                 NUMERIC NOT NULL
                           CONSTRAINT br_finstatetype_id_pk PRIMARY KEY,
    name               TEXT NOT NULL
                           CONSTRAINT br_finstatetype_name_uq UNIQUE
);

CREATE SEQUENCE br_finstatetype_id_seq;
