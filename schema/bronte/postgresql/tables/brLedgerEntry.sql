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

CREATE TABLE brLedgerEntry
(
    id                 NUMERIC NOT NULL
                           CONSTRAINT br_ledgerentry_id_pk PRIMARY KEY,
    statement_id       NUMERIC NOT NULL
                           CONSTRAINT br_ledgerentry_statement_fk
                               REFERENCES brStatementSummary (id)
                               ON DELETE CASCADE,
    item_id            NUMERIC NOT NULL
                           CONSTRAINT br_ledgerentry_item_fk
                               REFERENCES brLedgerItem (id)
                               ON DELETE CASCADE,
    amount             DECIMAL(64,3) NOT NULL, -- anticipates some hyperinflation
    modified           TIMESTAMP with time zone
                            DEFAULT (current_timestamp) NOT NULL
);

CREATE UNIQUE INDEX br_ledgerentry_state_item_uq
    ON brLedgerEntry (statement_id, item_id);

CREATE SEQUENCE br_ledgerentry_id_seq;
