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

floor0 = T(3)(3)(floor0)

floor1 = T(3)(7)(floor1)

floor2 = T(3)(11)(floor2)

floor3 = T(3)(15)(floor3)

floor4 = T(3)(19)(floor4)

floor5 = T(3)(26)(floor5)

floor6 = T(3)(33)(floor6)

floor7 = T(3)(37)(floor7)

floor8 = T(3)(41)(floor8)


#END##########################################################################################################

#SHELL NORD 1##################################################################################################

def sphere1(p):
    return [0.8*COS(p[0]), 0.8*SIN(p[0])] # point function
def domain(n): 
    return INTERVALS(PI)(n) # generator of domain decomp

nord = T(2)(4)(MAP(sphere1)(domain(32)))

shellNORD = PROD([nord, QUOTE([4])])


#END##########################################################################################################

#CUSTODIA VERTICALE SUD PIANO 1

verts_1f = [[-3.8,-4],[-0.2,-1.2]]
cells_1f = [[1,2]]
shellSUD1 = MKPOL([verts_1f,cells_1f,None])

verts_2f = [[-0.2,-1.2],[3.8,-3.1]]
cells_2f = [[1,2]]
shellSUD2 = MKPOL([verts_2f,cells_2f,None])

shellSUD1 = (PROD([shellSUD1, QUOTE([4])]))

shellSUD2 = PROD([shellSUD2, QUOTE([4])])
shellSUD2 = T(1)(3)(T(2)(-5.4)(R([1,2,3])((3/2)*PI)(shellSUD2)))

#END

#CUSTODIA VERTICALE OVEST PIANO 2
shellOVEST1 = T(1)(-0.5)(T(2)(1.55)(shellSUD1))

verts = [[-0.7,0],[-0.7,4]]
cells = [[1,2]]
shellOVEST2 = MKPOL([verts,cells,None])

shellOVEST2 = PROD([shellOVEST2, QUOTE([4])])

#END

#CUSTODIA VERTICALE EST PIANO 2

shellEST1 = T(1)(1.5)(shellOVEST2)

shellEST2 = T(2)(1.5)(shellSUD2)

#END

#CUSTODIA VERTICALE SUD-OVEST PIANO 2

shellSUDOVEST = (T(2)(4)(MAP(sphere1)(domain(32))))

shellSUDOVEST = (R([1,2])(-(1.5*PI)+((1.5*PI)/2))(shellNORD))

#END

#CUSTODIA VERTICALE SUD-EST PIANO 2

#shellSUDOVEST = (T(2)(4)(MAP(sphere1)(domain(32))))

shellSUDEST = (T(2)(0.5)(R([1,2])(-(1.5*PI)+((1.5*PI)/2))(shellSUDOVEST)))

#END

mock_up_3D = STRUCT([ground0, floor0, floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8, shellNORD, shellSUD1, shellSUD2, shellOVEST1, shellOVEST2, shellEST1, shellEST2, shellSUDEST])

VIEW(mock_up_3D)