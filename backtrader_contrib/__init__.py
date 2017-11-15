#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2017 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

from .version import __version__, __sversion__

from .loadmodule import loader

from . import analyzers as analyzers
from . import brokers as brokers
from . import commissions as commissions
from . import feeds as feeds
from . import filters as filters
from . import indicators as indicators
from . import observers as observers
from . import signals as signals
from . import sizers as sizers
from . import stores as stores
from . import strategies as strategies
from . import studies as studies


# Replace itself with backtrader
import backtrader as bt
sys.modules[__name__] = bt
