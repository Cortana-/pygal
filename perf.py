# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2013 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.


from pygal import CHARTS_NAMES, CHARTS_BY_NAME
from pygal.test import adapt
from random import sample

import timeit
import sys


rands = list(zip(
    sample(range(1000), 1000),
    sample(range(1000), 1000)))


def perf(chart_name, length, series):
    chart = CHARTS_BY_NAME.get(chart_name)()
    for i in range(series):
        chart.add('s %d' % i, adapt(chart, rands[:length]))
    return chart


def prt(s):
    sys.stdout.write(s)
    sys.stdout.flush()

charts = CHARTS_NAMES if '--all' in sys.argv else 'Line',


for chart in charts:
    prt('%s\n' % chart)
    prt('s\\l\t1\t10\t100')

    for series in (1, 10, 100):
        prt('\n%d\t' % series)
        for length in (1, 10, 100):
            times = []
            time = timeit.timeit(
                "c.render()",
                setup="from __main__ import perf; c = perf('%s', %d, %d)" % (
                    chart, length, series),
                number=10)
            prt('%d\t' % (1000 * time))
    prt('\n')
