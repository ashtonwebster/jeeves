import macropy.activate
import JeevesLib
from smt.Z3 import *

JeevesLib.init()
x = JeevesLib.mkLabel()
JeevesLib.restrict(x, lambda _: False)
print(JeevesLib.concretize(x, None))

x = JeevesLib.mkLabel()
JeevesLib.restrict(x, lambda y: y > 0)
value = JeevesLib.mkSensitive(x, True, False)
y = JeevesLib.mkLabel()
JeevesLib.restrict(y, lambda z: z < 0)
context = JeevesLib.mkSensitive(y, 1, 1)
print(context, JeevesLib.concretize(context, value))
context = JeevesLib.mkSensitive(y, -1, 1)
print(context, JeevesLib.concretize(context, value))
context = JeevesLib.mkSensitive(y, -1, -1)
print(context, JeevesLib.concretize(context, value))
context = JeevesLib.mkSensitive(y, 1, -1)
print(context, JeevesLib.concretize(context, value))
# There is no context which satisfies both faceted values in some cases! 

b = value + 3
print('b, 3', JeevesLib.concretize(3, b))
print('b, 2', JeevesLib.concretize(2, b))
