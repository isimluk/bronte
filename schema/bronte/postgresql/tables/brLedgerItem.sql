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

CREATE TABLE brLedgerItem
(
    id                 NUMERIC NOT NULL
                           CONSTRAINT br_ledgeritem_id_pk PRIMARY KEY,
    statement_type_id  NUMERIC NOT NULL
                           CONSTRAINT br_ledgeritem_stype_fk
                               REFERENCES brFinancialStatementType (id)
                               ON DELETE CASCADE,
    name               VARCHAR(100) NOT NULL
);

CREATE UNIQUE INDEX br_ledgeritem_stype_name_uq
    ON brLedgerItem (statement_type_id, name);

CREATE SEQUENCE br_ledgeritem_id_seq;
