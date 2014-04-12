from larcc import *
from lar2psm import *
from mapper import *
from pyplasm import *

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

verticalEnclosuresModel = larKhalifaVerticalEnclosures()

VIEW(S(3)(1.7)(verticalEnclosuresModel))
