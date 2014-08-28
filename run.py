# -*- coding: utf-8
import pprint
import qgis.utils
import os, sys
#import __builtin__
# Restore _builtin_import
#__builtin__.__import__ = qgis.utils._builtin_import

# Persistent ...
#try:
#    HelloServer.i = HelloServer.i+1
#except:
#    HelloServer.i = 0
#print "Call n° %s" % i

from processing.core.Processing import Processing
from processing.tools.general import *
Processing.initialize()
methods = Processing.algs

for i in methods:
    print i
    for m in methods[i]:
        print "---> %s" % m
