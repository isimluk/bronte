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

CREATE TABLE brTicker
(
    id                 NUMERIC NOT NULL
                           CONSTRAINT br_ticker_id_pk PRIMARY KEY,
    exchange_id        NUMERIC NOT NULL
                           CONSTRAINT br_ticker_exchange_fk
                               REFERENCES brStockMarket (id)
                               ON DELETE CASCADE,
    ticker             VARCHAR(10) NOT NULL,
    name               VARCHAR(100)
);

CREATE UNIQUE INDEX br_ticker_exchange_ticker_uq
    ON brTicker (exchange_id, ticker);

CREATE SEQUENCE br_ticker_id_seq;
