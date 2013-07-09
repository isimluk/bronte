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

CREATE OR REPLACE FUNCTION brledgerentry_mod_trig_fun() RETURNS TRIGGER
AS
$$
BEGIN
    new.modified := current_timestamp;
    RETURN new;
end;
$$ language plpgsql;

CREATE TRIGGER brledgerentry_mod_trig
    BEFORE INSERT OR UPDATE ON brLedgerEntry
    FOR EACH ROW
        EXECUTE PROCEDURE brledgerentry_mod_trig_fun();
