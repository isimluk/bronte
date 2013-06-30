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

CREATE TABLE brCurrency
(
    id                 NUMERIC NOT NULL
                           CONSTRAINT br_currency_id_pk PRIMARY KEY,
    code               VARCHAR(5) NOT NULL -- ISO 4217
                           CONSTRAINT br_currency_code_uq UNIQUE,
    sign               VARCHAR(5)
                           CONSTRAINT br_currency_sign_uq UNIQUE,
    name               VARCHAR(100)
);

CREATE SEQUENCE br_currency_id_seq;
