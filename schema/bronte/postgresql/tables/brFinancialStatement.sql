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

CREATE TABLE brFinancialStatement
(
    id                 NUMERIC NOT NULL
                           CONSTRAINT br_finstatement_id_pk PRIMARY KEY,
    report_id          NUMERIC NOT NULL
                           CONSTRAINT br_finstatement_report_fk
                               REFERENCES brFinancialReport (id)
                               ON DELETE CASCADE,
    statement_type     NUMERIC NOT NULL
                           CONSTRAINT br_finstatement_type_fk
                               REFERENCES brFinancialStatementType (id)
                               ON DELETE CASCADE,
    period_id          NUMERIC
                           CONSTRAINT br_finstatement_period_fk
                               REFERENCES brFinancialPeriod (id)
                               ON DELETE CASCADE,
    period_end         DATE NOT NULL,
    notes              TEXT
);

CREATE UNIQUE INDEX br_finstatement_rtp_uq
    ON brFinancialStatement (report_id, statement_type, period_id);

CREATE SEQUENCE br_finstatement_id_seq;
