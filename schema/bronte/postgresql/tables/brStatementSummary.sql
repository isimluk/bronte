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

CREATE TABLE brStatementSummary
(
    id                 NUMERIC NOT NULL
                           CONSTRAINT br_statesum_id_pk PRIMARY KEY,
    statement_id       NUMERIC NOT NULL
                           CONSTRAINT br_statesum_statement_fk
                               REFERENCES brFinancialStatement (id)
                               ON DELETE CASCADE,
    datasource_id      NUMERIC NOT NULL
                           CONSTRAINT br_statesum_source_fk
                               REFERENCES brDataSource (id)
                               ON DELETE CASCADE,
    currency_id        NUMERIC NOT NULL
                           CONSTRAINT br_legerentry_currency_fk
                               REFERENCES brCurrency (id)
                               ON DELETE CASCADE,
    created            TIMESTAMP with time zone
                            DEFAULT (current_timestamp) NOT NULL,
    modified           TIMESTAMP with time zone
                            DEFAULT (current_timestamp) NOT NULL,
    notes              TEXT
);

CREATE UNIQUE INDEX br_statesum_state_source_uq
    ON brStatementSummary (statement_id, datasource_id);

CREATE SEQUENCE br_statesum_id_seq;
