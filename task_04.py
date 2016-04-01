#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 10 Warmup Tasks. """

import data


data.BANDS['Buckingham Nicks'] = {'Lindsey Buckingham': ['guitar', 'vocals'],
                                  'Stevie Nicks': ['vocals', 'tambourine']}

data.BANDS['Fleetwood Mac'].update({k: v for k, v
                                    in data.BANDS['Buckingham Nicks']
                                    .iteritems() if v})
