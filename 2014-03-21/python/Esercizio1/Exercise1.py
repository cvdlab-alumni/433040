from pyplasm import *

#FUNZIONI (per mapping)
def x (p):
    u,v = p
    return -u +2

def y (p):
    u,v = p
    return v
#END FUNZIONI

#FUNZIONE TRIANGOLO
def triangolo(p):
    tPoints = p
    tCell = [[1,2,3]]
    return MKPOL([tPoints,tCell,None])
#END FUNZIONE TRIANGOLO

#FUNZIONE CERCHIO
def disk2D(p):
    u,v = p
    return [v*COS(u), v*SIN(u)]
#END FUNZIONE CERCHIO

#FUNZIONE RETTANGOLO
def rettangolo(p):
    rPoints = p
    rCells = [[1,2,3,4]]
    return MKPOL([rPoints,rCells,None])
#END FUNZIONE RETTANGOLO

#DIMENSIONO CERCHIO 0
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(1)(1)])
cBase = T(2)(5)(T(1)(1)(MAP(disk2D)(domain2D))) #Cerchio Componente
#END

#ALI PIANO 0
ala0 = STRUCT([COLOR(RED)(cBase),COLOR(GREEN)(triangolo([[0,5],[1,5.5 + SQRT(3)],[2,5]])),COLOR(BLUE)(rettangolo([[0,0],[2,0],[2,5],[0,5]]))])
ala1 = T(1)(0.5)(T(2)(-2.5)(R([1,2])(90)(ala0)))
ala2 = R([1,2])(PI+(PI/3)+(PI/40))((ala0))
ala2 = T(2)(-0.7)(T(1)(2.5)(ala2))
#END ALI PIANO 0

#PILASTRO PIANO 0
domain2D_P = PROD([INTERVALS(2*PI)(32), INTERVALS(4.3)(3)])
center = COLOR(YELLOW)(T(2)(-1)(T(1)(1)(MAP(disk2D)(domain2D_P))))
#END PILASTRO PIANO 0

# PIANO 0
floor0 = T(1)(-1)(T(2)(1)(STRUCT([ala0,ala1,ala2,center]))) #ALI PIANO 0 + BASE PIANO 0 = FLOOR 0
#END PIANO 0

#DIMENSIONO CERCHIO 1
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(0.7)(1)])
cBase = (T(2)(5)(MAP(disk2D)(domain2D))) #Cerchio Componente
#END

#ALI PIANO 1
ala3 = T(3)(3)(STRUCT([COLOR(BLACK)(cBase),COLOR(CYAN)(rettangolo([[-0.7,-1],[0.7,-1],[0.7,5],[-0.7,5]]))]))
ala4 = (T(1)(-0.5)(T(2)(-0.5)(R([1,2])(90)(ala3))))
ala5 = (R([1,2])(PI+(PI/3)+(PI/40))((ala3)))
ala5 = (T(2)(-0.7)(T(1)(0.5)(ala5)))
#END ALI PIANO 1

# PIANO 1
floor1 = STRUCT([ala3,ala4,ala5])
#END PIANO 1

#DIMENSIONO CERCHIO 2
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(0.7)(1)])
cBase = (T(2)(4)(MAP(disk2D)(domain2D)))
#END

#ALI PIANO 2
ala6 = T(3)(8)(STRUCT([COLOR(WHITE)(cBase),COLOR(GREEN)(rettangolo([[-0.7,-1],[0.7,-1],[0.7,4],[-0.7,4]]))]))
ala7 = (T(1)(-0.5)(T(2)(-0.5)(R([1,2])(90)(ala6))))
ala8 = (R([1,2])(PI+(PI/3)+(PI/40))((ala6)))
ala8 = (T(2)(-0.7)(T(1)(0.5)(ala8)))
#END ALI PIANO 2

# PIANO 2
floor2 = STRUCT([ala6,ala7,ala8])
#END PIANO 2

#DIMENSIONO CERCHIO 3
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(0.7)(1)])
cBase = (T(2)(4)(MAP(disk2D)(domain2D)))
#END

#ALI PIANO 3
ala9 = T(3)(14)(STRUCT([COLOR(GRAY)(cBase),COLOR(ORANGE)(rettangolo([[-0.7,-1],[0.7,-1],[0.7,4],[-0.7,4]]))]))
ala9_mod = T(3)(14)(STRUCT([COLOR(GRAY)(cBase),COLOR(ORANGE)(rettangolo([[-0.7,-0.2],[0.7,-0.2],[0.7,4],[-0.7,4]]))]))
ala10 = R([1,2])(90)((ala9_mod))
ala11 = (R([1,2])(PI+(PI/3)+(PI/40))((ala9)))
#END ALI PIANO 3

# PIANO 3
floor3 = STRUCT([ala9,ala10,ala11])
#END PIANO 3

#DIMENSIONO CERCHIO 4
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(0.4)(1)])
cBase = (T(2)(3)(MAP(disk2D)(domain2D)))
#END

#ALI PIANO 4
ala12 = T(3)(22)(STRUCT([COLOR(MAGENTA)(cBase),COLOR(BLUE)(rettangolo([[-0.4,-0.5],[0.4,-0.5],[0.4,3],[-0.4,3]]))]))
ala12_mod = T(3)(22)(STRUCT([COLOR(MAGENTA)(cBase),COLOR(BLUE)(rettangolo([[-0.4,-0.2],[0.4,-0.2],[0.4,3],[-0.4,3]]))]))
ala13 = (R([1,2])(90)((ala12_mod)))
ala14 = (R([1,2])(PI+(PI/3)+(PI/40))((ala12)))
#END ALI PIANO 4

# PIANO 4
floor4 = STRUCT([ala12,ala13,ala14])
#END PIANO 4

#DIMENSIONO CERCHIO 5
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(0.4)(1)])
cBase = (T(2)(2)(MAP(disk2D)(domain2D)))
#END

#ALI PIANO 5
ala15 = T(3)(26)(STRUCT([COLOR(WHITE)(cBase),COLOR(RED)(rettangolo([[-0.4,-0.5],[0.4,-0.5],[0.4,2],[-0.4,2]]))]))
ala15_mod = T(3)(26)(STRUCT([COLOR(WHITE)(cBase),COLOR(RED)(rettangolo([[-0.4,-0.2],[0.4,-0.2],[0.4,2],[-0.4,2]]))]))
ala16 = (R([1,2])(90)((ala15_mod)))
ala17 = (R([1,2])(PI+(PI/3)+(PI/40))((ala15)))
#END ALI PIANO 5

# PIANO 5
floor5 = STRUCT([ala15,ala16,ala17])
#END PIANO 5

#DIMENSIONO CERCHIO 6
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(0.4)(1)])
cBase = (T(2)(2)(MAP(disk2D)(domain2D)))
#END

#ALI PIANO 6
ala18 = T(3)(29)(STRUCT([COLOR(GREEN)(cBase),COLOR(YELLOW)(rettangolo([[-0.4,-0.5],[0.4,-0.5],[0.4,2],[-0.4,2]]))]))
ala18_mod = T(3)(29)(STRUCT([COLOR(GREEN)(cBase),COLOR(YELLOW)(rettangolo([[-0.4,-0.2],[0.4,-0.2],[0.4,2],[-0.4,2]]))]))
ala19 = (R([1,2])(90)((ala18_mod)))
ala20 = (R([1,2])(PI+(PI/3)+(PI/40))((ala18)))
#END ALI PIANO 6

# PIANO 6
floor6 = STRUCT([ala18,ala19,ala20])
#END PIANO 6

#DIMENSIONO CERCHIO 7
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(0.1)(1)])
cBase = (T(2)(2)(MAP(disk2D)(domain2D)))
#END

#ALI PIANO 7
ala21 = T(3)(32)(STRUCT([COLOR(ORANGE)(cBase),COLOR(BLACK)(rettangolo([[-0.1,-0.2],[0.1,-0.2],[0.1,2],[-0.1,2]]))]))
ala21_mod = T(3)(32)(STRUCT([COLOR(ORANGE)(cBase),COLOR(BLACK)(rettangolo([[-0.1,-0.2],[0.1,-0.2],[0.1,2],[-0.1,2]]))]))
ala22 = (R([1,2])(90)((ala21_mod)))
ala23 = (R([1,2])(PI+(PI/3)+(PI/40))((ala21)))
#END ALI PIANO 7

# PIANO 7
floor7 = STRUCT([ala21,ala22,ala23])
#END PIANO 7

#ALI PIANO 8
ala24 = T(3)(34)(STRUCT([COLOR(PURPLE)(cBase),COLOR(CYAN)(rettangolo([[-0.1,-0.2],[0.1,-0.2],[0.1,2],[-0.1,2]]))]))
#END ALI PIANO 8

# PIANO 8
floor8 = STRUCT([ala24])
#END PIANO 8

#ANTENNA
domain2D_P = PROD([INTERVALS(2*PI)(32), INTERVALS(0.2)(1)])
center = COLOR(RED)(T(2)(-1)(T(1)(1)(MAP(disk2D)(domain2D_P))))
antenna = T(3)(37)(T(1)(-1)(T(2)(1)(STRUCT([center]))))
#END ANTENNA

building = STRUCT([floor0, floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8, antenna])

VIEW(building)




