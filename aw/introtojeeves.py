import macropy.activate
import JeevesLib
from smt.Z3 import *

JeevesLib.init()
x = JeevesLib.mkLabel()
JeevesLib.restrict(x, lambda _: False)
print(JeevesLib.concretize(x, None))

x = JeevesLib.mkLabel()
JeevesLib.restrict(x, lambda y: y == 2)
value = JeevesLib.mkSensitive(x, 42, 41)
print(1, JeevesLib.concretize(1, value), 41)
print(2, JeevesLib.concretize(2, value), 42)
print(3, JeevesLib.concretize(3, value), 41)

b = value + 3
print('b, 3', JeevesLib.concretize(3, b))
print('b, 2', JeevesLib.concretize(2, b))
