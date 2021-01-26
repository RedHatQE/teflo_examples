#!/usr/bin/env python
import sys

if sys.argv:
        print('Hello World to %s ! Testing local script using teflo from IP %s' % (sys.argv[1], sys.argv[2]))
else:
        print ('Hello World ! Testing local script executing using teflo')
