#
# Copyright (c) 2013 Simon Lukasik
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Make used to build the postgres schema.
#
# It uses the following tools:
#
#   blend    - A tool used to process the .deps files to produce
#              the main.sql.  It will inject the contents of a file
#              named "start.sql" at the beginning if it exits.
#

STYLE   := postgres
DIRS    := tables procs triggers data
BLEND   := ../blend -as $(STYLE)
MKFILES := $(shell find . -mindepth 2 -maxdepth 2 -name Makefile)


main :
	$(BLEND) $(DIRS)

clean :
	@rm -f main.sql
	@$(foreach m,$(MKFILES),$(MAKE) -C $(dir $(m)) $@;)

.PHONY: clean
