from pyplasm import *

#FUNZIONE TRIANGOLO########################################################################################
def triangolo(p):
    tPoints = p
    tCell = [[1,2,3]]
    return MKPOL([tPoints,tCell,None])
#END FUNZIONE TRIANGOLO####################################################################################

#FUNZIONE CERCHIO##########################################################################################
def disk2D(p):
    u,v = p
    return [v*COS(u), v*SIN(u)]
#END FUNZIONE CERCHIO######################################################################################

#FUNZIONE RETTANGOLO#######################################################################################
def rettangolo(p):
    rPoints = p
    rCells = [[1,2,3,4]]
    return MKPOL([rPoints,rCells,None])
#END FUNZIONE RETTANGOLO###################################################################################

#FUNZIONE WING#############################################################################################
def floor(raggio, wingA = 0, wingB = 0, wingC = 0, colorCerchio = BLUE, colorRect = YELLOW):
    r = raggio
    domain2D = PROD([INTERVALS(PI)(32), INTERVALS(r)(1)])
    rectA = None
    rectB = None
    rectC = None
    cBaseA = None
    cBaseB = None
    cBaseC = None
    if(wingA < 0) :
        cBaseA = COLOR(colorCerchio)((T(2)(5+wingA)(MAP(disk2D)(domain2D))))
        rectA = COLOR(colorRect)(rettangolo([[-r,-2],[r,-2],[r,5+wingA],[-r,5+wingA]]))
        w_A = STRUCT([cBaseA, rectA])
    else :
        cBaseA = COLOR(colorCerchio)(T(2)(5)(MAP(disk2D)(domain2D)))
        rectA = COLOR(colorRect)(rettangolo([[-r,-2],[r,-2],[r,5],[-r,5]]))
        w_A = STRUCT([cBaseA, rectA])
    if(wingB < 0) :
        cBaseB = COLOR(colorCerchio)(T(2)(5+wingB)(MAP(disk2D)(domain2D)))
        rectB = COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5+wingB],[-r,5+wingB]]))
        wB = STRUCT([cBaseB,rectB])
        w_B = R([1,2])(-(1.5*PI)+((1.5*PI)/2))(wB)
    else :
        cBaseB = COLOR(colorCerchio)(T(2)(5)(MAP(disk2D)(domain2D)))
        rectB = COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5],[-r,5]]))
        wB = STRUCT([cBaseB,rectB])
        w_B = R([1,2])(-(1.5*PI)+((1.5*PI)/2))(wB)
    if(wingC < 0) :
        cBaseC = COLOR(colorCerchio)(T(2)(5+wingC)(MAP(disk2D)(domain2D)))
        rectC =  COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5+wingC],[-r,5+wingC]]))
        wC = STRUCT([cBaseC,rectC])
        w_C = R([1,2])(((1.5*PI)-((1.5*PI)/2)))(wC)
    else :
        cBaseC = COLOR(colorCerchio)(T(2)(5)(MAP(disk2D)(domain2D)))
        rectC = COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5],[-r,5]]))
        wC = STRUCT([cBaseC,rectC])
        w_C = R([1,2])(-((1.5*PI)+((1.5*PI)/2)))(wC)
    return STRUCT([w_A,w_B,w_C])
#END#######################################################################################################

#FUNZIONE GROUND################################################################################################
def ground(raggioPilastro, raggio, wingA = 0, wingB = 0, wingC = 0, colorCerchio = BLUE, colorRect = YELLOW):
    r = raggio
    domain2D = PROD([INTERVALS(PI)(32), INTERVALS(r)(1)])
    rectA = None
    rectB = None
    rectC = None
    cBaseA = None
    cBaseB = None
    cBaseC = None
    if(wingA < 0) :
        cBaseA = COLOR(colorCerchio)((T(2)(5+wingA)(MAP(disk2D)(domain2D))))
        rectA = COLOR(colorRect)(rettangolo([[-r,-2],[r,-2],[r,5+wingA],[-r,5+wingA]]))
        w_A = STRUCT([cBaseA, rectA])
    else :
        cBaseA = COLOR(colorCerchio)(T(2)(5)(MAP(disk2D)(domain2D)))
        rectA = COLOR(colorRect)(rettangolo([[-r,-2],[r,-2],[r,5],[-r,5]]))
        w_A = STRUCT([cBaseA, rectA])
    if(wingB < 0) :
        cBaseB = COLOR(colorCerchio)(T(2)(5+wingB)(MAP(disk2D)(domain2D)))
        rectB = COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5+wingB],[-r,5+wingB]]))
        wB = STRUCT([cBaseB,rectB])
        w_B = R([1,2])(-(1.5*PI)+((1.5*PI)/2))(wB)
    else :
        cBaseB = COLOR(colorCerchio)(T(2)(5)(MAP(disk2D)(domain2D)))
        rectB = COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5],[-r,5]]))
        wB = STRUCT([cBaseB,rectB])
        w_B = R([1,2])(-(1.5*PI)+((1.5*PI)/2))(wB)
    if(wingC < 0) :
        cBaseC = COLOR(colorCerchio)(T(2)(5+wingC)(MAP(disk2D)(domain2D)))
        rectC =  COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5+wingC],[-r,5+wingC]]))
        wC = STRUCT([cBaseC,rectC])
        w_C = R([1,2])(((1.5*PI)-((1.5*PI)/2)))(wC)
    else :
        cBaseC = COLOR(colorCerchio)(T(2)(5)(MAP(disk2D)(domain2D)))
        rectC = COLOR(colorRect)(rettangolo([[-r,0],[r,0],[r,5],[-r,5]]))
        wC = STRUCT([cBaseC,rectC])
        w_C = R([1,2])(((1.5*PI)-((1.5*PI)/2)))(wC)
    domain2D_P = PROD([INTERVALS(2*PI)(32), INTERVALS(raggioPilastro)(1)])
    center = COLOR(BLACK)(MAP(disk2D)(domain2D_P))
    return STRUCT([w_A,w_B,w_C,center])
#END############################################################################################################

#DEFINIZIONE Piani##############################################################################################

ground0 = ground(3,0.8,0,0,0,BLACK,BLACK)

floor0 = floor(0.8,-1,-1,-1)

floor1 = floor(0.8,-2,-1,-1,RED,GREEN)

floor2 = floor(0.8,-2,-2,-1,ORANGE,WHITE)

floor3 = floor(0.8,-2,-2,-2,MAGENTA,CYAN)

floor4 = floor(0.8,-3,-2,-2,GRAY,BLUE)

floor5 = floor(0.8,-3,-3,-2,BLUE,GREEN)

floor6 = floor(0.8,-3,-3,-3,WHITE,YELLOW)

floor7 = floor(0.8,-4,-4,-3,CYAN)

floor8 = floor(0.8,-4,-4,-4,RED,GRAY)

#building_2D = STRUCT([ground0, floor0, floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8])

#END############################################################################################################

#VIEW(building_2D)

#QUOTO PIANI####################################################################################################

ground0 = PROD([ground0, QUOTE([1.5])])

floor0 = PROD([floor0, QUOTE([3])])

floor1 = PROD([floor1, QUOTE([-3,4])])

floor2 = PROD([floor2, QUOTE([-7,4])])

floor3 = PROD([floor3, QUOTE([-11,4])])

floor4 = PROD([floor4, QUOTE([-15,4])])

floor5 = PROD([floor5, QUOTE([-19,7])])

floor6 = PROD([floor6, QUOTE([-26,7])])

floor7 = PROD([floor7, QUOTE([-33,4])])

floor8 = PROD([floor8, QUOTE([-37,4])])

#ANTENNA
domain2D_P = PROD([INTERVALS(2*PI)(32), INTERVALS(1)(1)])
center = COLOR(RED)(MAP(disk2D)(domain2D_P))
center = PROD([center, QUOTE([-41,6])])
domain2D_P1 = PROD([INTERVALS(2*PI)(32), INTERVALS(0.5)(1)])
ant = COLOR(RED)(MAP(disk2D)(domain2D_P1))
ant = PROD([ant, QUOTE([-47,4])])
#END


#END##########################################################################################################

solid_model_3D = STRUCT([COLOR([0.67,0.8,0.93])(ant),COLOR([0.67,0.8,0.93])(center), COLOR([0.67,0.8,0.93])(ground0), COLOR([0.67,0.8,0.93])(floor0), COLOR([0.67,0.8,0.93])(floor1), COLOR([0.67,0.8,0.93])(floor2), COLOR([0.67,0.8,0.93])(floor3), COLOR([0.67,0.8,0.93])(floor4), COLOR([0.67,0.8,0.93])(floor5), COLOR([0.67,0.8,0.93])(floor6), COLOR([0.67,0.8,0.93])(floor7), COLOR([0.67,0.8,0.93])(floor8)])

VIEW(solid_model_3D)