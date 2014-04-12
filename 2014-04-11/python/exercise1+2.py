from larcc import *
from lar2psm import *
from mapper import *


#FUNZIONE PILASTRO#
def larKhalifaPillar(params):
   radius,height= params
   def larKhalifaPillar0(shape=[36,1]):
      V,CV = checkModel(larCylinder(params)(shape))
      return V,[range(len(V))]
   return larKhalifaPillar0
#END#

#FUNZIONE FLOOR (PIANO PARAMETRICO)#
def larKhalifaFloor(wingA = 0, wingB = 0, wingC = 0):
    Vwing = [[-2,-2],[2,-2],[2,10-wingA],[0,12.5-wingA],[-2,10-wingA],[2,0],[9-wingB,-7+wingB],[9.5-wingB,-10.5+wingB],[6-wingB,-10+wingB],[-2,0],[-9+wingC,-7+wingC],[-9.5+wingC,-10.5+wingC],[-6+wingC,-10+wingC]]
    FVwing = [[0,1,2,3,4,0],[5,6,7,8,0,5],[9,10,11,12,1,9]]
    pol =  SOLIDIFY(STRUCT(AA(POLYLINE)([[Vwing[v] for v in cell] for cell in FVwing])))
    solid = PROD([pol, Q(1)])
    mainPillar = STRUCT(MKPOLS(larKhalifaPillar([3,1.])([32,1])))
    main = T(2)(-2)(mainPillar)
    pillarAstar = STRUCT(MKPOLS(larKhalifaPillar([2,1])()))
    pillarA = T(2)(10-wingA)(pillarAstar)
    pillarBstar = STRUCT(MKPOLS(larKhalifaPillar([2,1])()))
    pillarB = (T(1)(7.5-wingB)(T(2)(-8.5+wingB)(pillarBstar)))
    pillarCstar = STRUCT(MKPOLS(larKhalifaPillar([2,1])()))
    pillarC = (T(1)(-7.5+wingC)(T(2)(-8.5+wingC)(pillarCstar)))
    floor = STRUCT([main, solid, pillarA, pillarB, pillarC])
    return COLOR([0.568,0.506,0.317])(floor)
#END#

#FUNZIONE FACCIATE ESTERNE PILASTRI#
def larKhalifaPillarsVerticalEnclosures(params):
    radius,height= params
    def larKhalifaPillarsVerticalEnclosures0(shape=[36,1]):
        domain = larIntervals(shape)([2*PI,1])
        V,CV = domain
        x = lambda V : [radius*COS(p[0]) for p in V]
        y = lambda V : [radius*SIN(p[0]) for p in V]
        z = lambda V : [height*p[1] for p in V]
        mapping = [x,y,z]
        model = larMap(mapping)(domain)
        return model
    return larKhalifaPillarsVerticalEnclosures0
#END#

#FUNZIONE FACCIATE ESTERNE (LUNGHEZZA PARAMETRICA)#
def larKhalifaVerticalEnclosures(wingA = 0, wingB = 0, wingC = 0):
    #FACCIATA EST
    V_EnclEST = [[2,10-wingA],[2,0],[9-wingB,-7+wingB]]
    FV_EnclEST = [[0,1,2]]
    pol_EST =  (STRUCT(AA(POLYLINE)([[V_EnclEST[v] for v in cell] for cell in FV_EnclEST])))
    solid_EST = PROD([pol_EST, QUOTE([0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.3])])
    #VIEW()
    #END
    #FACCIATA OVEST
    V_EnclWEST = [[-2,10-wingA],[-2,0],[-9+wingC,-7+wingC]]
    FV_EnclWEST = [[0,1,2]]
    pol_WEST =  (STRUCT(AA(POLYLINE)([[V_EnclWEST[v] for v in cell] for cell in FV_EnclWEST])))
    solid_WEST = PROD([pol_WEST, QUOTE([0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.3])])
    #END
    #FACCIATA SUD
    V_EnclSUD = [[6-wingB,-10+wingB],[0,-4],[-6+wingC,-10+wingC]]
    FV_EnclSUD = [[0,1,2]]
    pol_SUD =  (STRUCT(AA(POLYLINE)([[V_EnclSUD[v] for v in cell] for cell in FV_EnclSUD])))
    solid_SUD = PROD([pol_SUD, QUOTE([0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.2,-0.2,0.3])])
    #END
    #FACCIATA NORD
    pol_NORTH = STRUCT(MKPOLS(larKhalifaPillarsVerticalEnclosures([2,3.5])([32,1])))
    solid_NORTH = T(2)(10-wingA)(pol_NORTH)
    #END
    #FACCIATA SUD-EST
    pol_SUD_EST = STRUCT(MKPOLS(larKhalifaPillarsVerticalEnclosures([2,3.5])([32,1])))
    solid_SUD_EST = T(1)(7.5-wingB)(T(2)(-8.5+wingB)(pol_SUD_EST))
    #END
    #FACCIATA SUD-OVEST
    pol_SUD_WEST = STRUCT(MKPOLS(larKhalifaPillarsVerticalEnclosures([2,3.5])([32,1])))
    solid_SUD_WEST = T(1)(-7.5+wingC)(T(2)(-8.5+wingC)(pol_SUD_WEST))
    #END
    enclosures = STRUCT([solid_WEST, solid_EST, solid_SUD, solid_NORTH, solid_SUD_EST, solid_SUD_WEST])
    return COLOR([0.274,0.509,0.705])(enclosures)
#END

#ASSEMBLO PIANI#

#BASE#
basement0 = T(3)(-1)(larKhalifaFloor(-2,-2,-2))
basement1 = T(3)(-2)(larKhalifaFloor(-3,-3,-3))
basement2 = T(3)(-3)(larKhalifaFloor(-4,-4,-4))
basement = STRUCT([basement0, basement1, basement2])
#END#

#TAMPONATURE PIANO 1#
Vwall0 = [[2,5],[1,5],[1,2],[0.7,2],[0.7,5.3],[2,5.3]]
FVwall0 = [[0,1,2,3,4,5,0]]
polWall0 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[Vwall0[v] for v in cell] for cell in FVwall0])))
solidWall0 = PROD([(polWall0), Q(3.5)])

Vwall1 = [[0.7,0],[0.7,-2],[4.7,-5.3],[6.2,-4.2],[5.8,-3.9],[4.7,-4.7], [1,-2],[1,0]]
FVwall1 = [[0,1,2,3,4,5,6,7,0]]
polWall1 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[Vwall1[v] for v in cell] for cell in FVwall1])))
solidWall1 = PROD([(polWall1), Q(3.5)])
#END#

ground0 = larKhalifaFloor()
roof0 = T(3)(3.5)(larKhalifaFloor(1,0,0))
encl0 = larKhalifaVerticalEnclosures(1,0,0)

#PIANO 1#
floor1 = STRUCT([ground0, roof0, solidWall0, solidWall1,encl0])
#END#

#TAMPONATURE PIANO 2#
solidWall2 = PROD([(polWall0), QUOTE([-3.5,3.5])])

solidWall3 = PROD([(polWall1), QUOTE([-3.5,3.5])])
#END#

ground1 = roof0
roof1 = T(3)(7)(larKhalifaFloor(1,1,0))
encl1 = T(3)(3.5)(larKhalifaVerticalEnclosures(1,1,0))

#PIANO 2#
floor2 = STRUCT([ground1, roof1, solidWall2, solidWall3,encl1])
#END#

#TAMPONATURE PIANO 3#
solidWall4 = PROD([(polWall0), QUOTE([-7,3.5])])

solidWall5 = PROD([(polWall1), QUOTE([-7,3.5])])
#END#

ground2 = roof1
roof2 = T(3)(10.5)(larKhalifaFloor(1,1,1))
encl2 = T(3)(7)(larKhalifaVerticalEnclosures(1,1,1))

#PIANO 3#
floor3 = STRUCT([ground2, roof2, solidWall4, solidWall5, encl2])
#END#

#TAMPONATURE PIANO 4#
solidWall6 = PROD([(polWall0), QUOTE([-10.5,3.5])])

solidWall7 = PROD([(polWall1), QUOTE([-10.5,3.5])])
#END#

ground3 = roof2
roof3 = T(3)(14)(larKhalifaFloor(2,1,1))
encl3 = T(3)(10.5)(larKhalifaVerticalEnclosures(2,1,1))

#PIANO 4#
floor4 = STRUCT([ground3, roof3, solidWall6, solidWall7, encl3])
#END#

#TAMPONATURE PIANO 5#
solidWall8 = PROD([(polWall0), QUOTE([-14,3.5])])

solidWall9 = PROD([(polWall1), QUOTE([-14,3.5])])
#END#

ground4 = roof3
roof4 = T(3)(17.5)(larKhalifaFloor(2,2,1))
encl4 = T(3)(14)(larKhalifaVerticalEnclosures(2,2,1))

#PIANO 5#
floor5 = STRUCT([ground4, roof4, solidWall8, solidWall9, encl4])
#END#

#TAMPONATURE PIANO 6#
solidWall10 = PROD([(polWall0), QUOTE([-17.5,3.5])])

solidWall11 = PROD([(polWall1), QUOTE([-17.5,3.5])])
#END#

ground5 = roof4
roof5 = T(3)(21)(larKhalifaFloor(2,2,2))
encl5 = T(3)(17.5)(larKhalifaVerticalEnclosures(2,2,2))

#PIANO 6#
floor6 = STRUCT([ground5, roof5, solidWall10, solidWall11,encl5])
#END#

#TAMPONATURE PIANO 7#
solidWall12 = PROD([(polWall0), QUOTE([-21,3.5])])

solidWall13 = PROD([(polWall1), QUOTE([-21,3.5])])
#END#

ground6 = roof5
roof6 = T(3)(24.5)(larKhalifaFloor(3,2,2))
encl6 = T(3)(21)(larKhalifaVerticalEnclosures(3,2,2))

#PIANO 7#
floor7 = STRUCT([ground6, roof6, solidWall12, solidWall13, encl6])
#END#

#TAMPONATURE PIANO 8#
solidWall14 = PROD([(polWall0), QUOTE([-24.5,3.5])])

solidWall15 = PROD([(polWall1), QUOTE([-24.5,3.5])])
#END#

ground7 = roof6
roof7 = T(3)(28)(larKhalifaFloor(3,3,2))
encl7 = T(3)(24.5)(larKhalifaVerticalEnclosures(3,3,2))

#PIANO 8#
floor8 = STRUCT([ground7, roof7, solidWall14, solidWall15,encl7])
#END#

#TAMPONATURE PIANO 9#
solidWall16 = PROD([(polWall0), QUOTE([-28,3.5])])

solidWall17 = PROD([(polWall1), QUOTE([-28,3.5])])
#END#

ground8 = roof7
roof8 = T(3)(31.5)(larKhalifaFloor(3,3,3))
encl8 = T(3)(28)(larKhalifaVerticalEnclosures(3,3,3))

#PIANO 9#
floor9 = STRUCT([ground8, roof8, solidWall16, solidWall17,encl8])
#END#

ground9 = roof8
roof9 = T(3)(35)(larKhalifaFloor(4,3,3))
encl9 = T(3)(31.5)(larKhalifaVerticalEnclosures(4,3,3))

#PIANO 10#
floor10 = STRUCT([ground9, roof9,encl9])
#END#

ground10 = roof9
roof10 = T(3)(38.5)(larKhalifaFloor(5,3,3))
encl10 = T(3)(35)(larKhalifaVerticalEnclosures(5,3,3))

#PIANO 11#
floor11 = STRUCT([ground10, roof10, encl10])
#END#

ground11 = roof10
roof11 = T(3)(42)(larKhalifaFloor(6,3,3))
encl11 = T(3)(38.5)(larKhalifaVerticalEnclosures(6,3,3))

#PIANO 12#
floor12 = STRUCT([ground11, roof11, encl11])
#END#

ground12 = roof11
roof12 = T(3)(45.5)(larKhalifaFloor(7,4,4))
encl12 = T(3)(42)(larKhalifaVerticalEnclosures(7,4,4))

#PIANO 13#
floor13 = STRUCT([ground12, roof12, encl12])
#END#

ground13 = roof12
roof13 = T(3)(49)(larKhalifaFloor(8,5,5))
encl13 = T(3)(45.5)(larKhalifaVerticalEnclosures(8,5,5))

#PIANO 14#
floor14 = STRUCT([ground13, roof13, encl13])
#END#

ground14 = roof13
roof14 = T(3)(52.5)(larKhalifaFloor(9,6,6))
encl14 = T(3)(49)(larKhalifaVerticalEnclosures(9,6,6))

#PIANO 15#
floor15 = STRUCT([ground14, roof14, encl14])
#END#

#ANTENNA#
baseAntennaStar = STRUCT(MKPOLS(larKhalifaPillar([3,2])([32,1])))
baseAntenna = COLOR([0.274,0.509,0.705])(T(3)(52.5)(T(2)(-2)(baseAntennaStar)))
baseAntennaStar1 = STRUCT(MKPOLS(larKhalifaPillar([1.5,2])([32,1])))
baseAntenna1 = COLOR([0.274,0.509,0.705])(T(3)(54.5)(T(2)(-2)(baseAntennaStar1)))
baseAntennaStar2 = STRUCT(MKPOLS(larKhalifaPillar([1,2])([32,1])))
baseAntenna2 = COLOR([0.274,0.509,0.705])(T(3)(56.5)(T(2)(-2)(baseAntennaStar2)))
antennaStar = STRUCT(MKPOLS(larKhalifaPillar([0.3,7])([32,1])))
antenna = COLOR([0.274,0.509,0.705])(T(3)(58.5)(T(2)(-2)(antennaStar)))
#END#

#END#

building3D = STRUCT([basement, floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8, floor9, floor10, floor11, floor12, floor13, floor14, floor15, baseAntenna, baseAntenna1, baseAntenna2, antenna])
VIEW(S(3)(1.7)(building3D))
