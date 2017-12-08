import macropy.activate
import JeevesLib
from smt.Z3 import *
import pdb
from sourcetrans.macro_module import macros, jeeves

JeevesLib.init()
x = JeevesLib.mkLabel()
JeevesLib.restrict(x, lambda q: q == True)
fv = JeevesLib.mkSensitive(x, True, False)

@JeevesLib.supports_jeeves
def foo(fv_p):
    if fv_p == True:
        return 0
    else:
        return 1

print("fv:",str(fv))
myif = JeevesLib.jif(fv, 
    lambda: JeevesLib.jeevesState.pathenv.getEnv(), 
    lambda: JeevesLib.jeevesState.pathenv.getEnv())
print("myif, context=True", JeevesLib.concretize(True, myif))
print("myif, context=False", JeevesLib.concretize(False, myif))

def mythen():
    return JeevesLib.jif(fv, lambda: 1, lambda: 2)

def myelse():
    return JeevesLib.jif(fv, lambda: 3, lambda: 4)

myif = JeevesLib.jif(fv, mythen, myelse)
print(myif)
#< v0 ? const:1 : const:4 >

# can't get the automatic source rewritng working, but this
# shows the path condition examples
# we can observe that this prints 1 and 4 because these are
# the only "consistent" responses given the path conditions.

