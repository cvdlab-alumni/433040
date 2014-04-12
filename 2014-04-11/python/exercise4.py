from pyplasm import *
from larcc import *
from lar2psm import *
from mapper import *

#FUNZIONE GENERA SUOLO
def background():
    ground = COLOR([0.957,0.643,0.376])(T(2)(-75)(T(1)(-75)(CUBOID([150,150,0.1]))))
    return ground
#END

#FUNZIONI DI SUPPORTO GENERA LAMPIONE STRADALE
def larLampRod(params):
   radius,height= params
   def larRod0(shape=[36,1]):
      V,CV = checkModel(larCylinder(params)(shape))
      return V,[range(len(V))]
   return larRod0

def larLampToroidal(params):
    r,R = params
    def larLampToroidal0(shape=[24,60]):
        domain = larIntervals(shape)([2*PI,PI])
        V,CV = domain
        x = lambda V : [(R + r*COS(p[0])) * COS(p[1]) for p in V]
        y = lambda V : [(R + r*COS(p[0])) * SIN(p[1]) for p in V]
        z = lambda V : [-r * SIN(p[0]) for p in V]
        return larMap([x,y,z])(domain)
    return larLampToroidal0

def larLampBall(radius=1):
   def larLampBall0(shape=[18,36]):
      V,CV = checkModel(larSphere(radius)(shape))
      return V,[range(len(V))]
   return larLampBall0
#END

#FUNZIONE GENERA LAMPIONE STRADALE
def street_lamp():
    rod = COLOR([0.440,0.502,0.565])(STRUCT(MKPOLS(larLampRod([.02,0.5])([32,1]))))
    tor = STRUCT(MKPOLS(checkModel(larLampToroidal([0.02,0.1])())))
    branch = COLOR([0.440,0.502,0.565])(T(3)(0.5)(T(1)(0.1)(R([1,3])(3*PI/2)(R([1,2])(PI/2)(R([1,3])(PI/2)(tor))))))
    ball = COLOR(YELLOW)(T(3)(0.5)(T(1)(0.2)(STRUCT(MKPOLS(larLampBall(0.03)([18,36]))))))
    return STRUCT([ball,rod,branch])
#END

#FUNZIONE GENERA STRADA (CON LAMPIONI)#
def street3D():
    ground3D = (T(2)(-45)(T(1)(-75)(CUBOID([150,10,0.1]))))
    line3D = STRUCT([T(3)(0.03)(T(2)(-40)(T(1)(-75)(CUBOID([1,0.53,0.1])))), T(1)(1.5)]*100)
    str = STRUCT([COLOR([0.823,0.823,0.823])(ground3D),line3D])
    return STRUCT([str])
#END

#FUNZIONE ALBERO
def tree():
    rod = COLOR([0.59,0.29,0])(STRUCT(MKPOLS(larLampRod([0.05,0.2])())))
    leaf = COLOR(GREEN)(T(3)(0.2)(CONE([0.25,0.5])(20)))
    return STRUCT([rod,leaf])
#

#FUNZIONE ISOLA VERDE#
def island():
    V0 = [[0,0],[8,0],[11,-3],[11,-12],[1,-17],[0,5]]
    FV0 = [[0,1,2,3,4,0]]
    pol0 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V0[v] for v in cell] for cell in FV0])))
    solid0 = PROD([pol0, Q(0.4)])
    isl = STRUCT([COLOR([0.59,0.29,0])(solid0)])
    V1 = [[12,3],[17,-6],[15,-18],[0,-25],[-3,-25],[-3,5]]
    FV1 = [[0,1,2,3,4,5,0]]
    pol1 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V1[v] for v in cell] for cell in FV1])))
    solid1 = PROD([pol1, Q(0.2)])
    water = STRUCT([COLOR(BLUE)(solid1)])
    trees = T(1)(1.5)(T(2)(-3)(STRUCT([(T(3)(0.6)(STRUCT([tree(), T(1)(1.4)]*7))), T(2)(-2)]*5)))
    return STRUCT([isl,water,trees])
#END

#OPERAZIONE ONEROSA!#
lamps = STRUCT([STRUCT([street_lamp(), T(1)(10)]*8), T(2)(-10)]*2)
#END#
#lamps = STRUCT([street_lamp(), T(1)(10)])


street = T(3)(0.1)(street3D())
lamps = T(2)(-35)(lamps)
back = background()
island = T(2)(5)(T(1)(25)(island()))

burjKhalifa_urban_fittings  = STRUCT([background(), street, lamps, island])

VIEW(burjKhalifa_urban_fittings)