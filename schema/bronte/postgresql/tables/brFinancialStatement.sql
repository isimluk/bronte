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
    company_id         NUMERIC NOT NULL
                           CONSTRAINT br_finstatement_company_fk
                               REFERENCES brCompany (id)
                               ON DELETE CASCADE,
    period_id          NUMERIC NOT NULL
                           CONSTRAINT br_finstatement_period_fk
                               REFERENCES brFinancialPeriod (id)
                               ON DELETE CASCADE,
    period_end         DATE NOT NULL,
    release_date       DATE,
    notes              TEXT
);

CREATE UNIQUE INDEX br_finstatement_cpp_uq
    ON brFinancialStatement (company_id, period_id, period_end);

CREATE SEQUENCE br_finstatement_id_seq;
