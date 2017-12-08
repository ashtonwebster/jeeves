import macropy.activate
import JeevesLib
from smt.Z3 import *


JeevesLib.init()
#c = 7
b = JeevesLib.mkLabel()
JeevesLib.restrict(b, lambda _: c == 7)
b_s = JeevesLib.mkSensitive(b, True, False)

# interestingly, c can be defined afer the 
# restrict statement
c = 7
print(JeevesLib.concretize(None, b_s))
c = 6
print(JeevesLib.concretize(None, b_s))

#print(JeevesLib.concretize(True, a_s))
#print(JeevesLib.concretize(False, a_s))
