import macropy.activate
import JeevesLib
from smt.Z3 import *

# Example of circular dependnecy, x always evaluates
# to the "default" of true.  Tie this back to the discussion
# of \Delta in yang2012
JeevesLib.init()
# create label
x = JeevesLib.mkLabel()
# restrict variable to require context == True for high value
JeevesLib.restrict(x, lambda x: x == True)
# Create faceted value with low = False and high = True,
# guarded by x
facetedValue = JeevesLib.mkSensitive(x, True, False)
context = facetedValue
# circular dependency: facetedValue depends on context
print(JeevesLib.concretize(context, facetedValue))
# Output: True
