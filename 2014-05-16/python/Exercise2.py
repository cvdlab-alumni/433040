#IMPORT#
""" testing initial steps of Assembly Diagram construction """
from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *
from splines import *
#END IMPORT#

#def some utility funtions 
DRAW = COMP([VIEW,STRUCT,MKPOLS])
BROWN = [0.58823529411,0.29411764705,0]
SK = COMP([VIEW,SKEL_1,STRUCT,MKPOLS])
def larDom(knots,tics=32):
    domain = knots[-1]-knots[0]
    return larIntervals([tics*domain])([domain])
#end

#Def Door function
def Door(width) :
    diagram = assemblyDiagramInit([2,2,3])([[.3,.1],[width-.3,.3],[1.25,.1,1.35]])
    manigliaDiagram = assemblyDiagramInit([1,1,1])([[0.3],[.1],[.1]])
    out = Automatize(manigliaDiagram,diagram,[11])
    toRemoveCells = [6,7,8,9,11]
    door = out(toRemoveCells)
    return door
#end

#Def Windows function
def Windows(width) :
    diagram = assemblyDiagramInit([2,5,4])([[.1,.3],[.1,1.15,.1,1.15,.1],[.3,.1,.5,.1]])
    out = Automatize(None,diagram,None)
    toRemoveCells = [14,34,6,26,12,4]
    win = out(toRemoveCells)
    return win
#end

#Def Automatize function
def Automatize(diagram, master, toMergeCells) :
    if not(toMergeCells == None):
        ToMerge=list.sort(toMergeCells)
        ToMerge=list.reverse(toMergeCells)	
        for k in toMergeCells:
            master = diagram2cell(diagram,master,k)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = AutomatizeCellNumbering(master, hpc)
    #VIEW(hpc)
    def Automatize0(toRemoveCells) :
        if(toRemoveCells == None) :
            #nothing to remove
            return master
        else :
            V_final,CV_final = master
            hpcFinal = V_final, [cell for k,cell in enumerate(CV_final) if not (k in toRemoveCells)]
            #DRAW(hpcFinal)
            return hpcFinal
    return Automatize0
#end

#Def AutomatizeCellNumbering function
def AutomatizeCellNumbering(master, hpc) :
    hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,2)
    return hpc
#end

#BLOCCO #1 : Stanza Antonio
def AntoRoom() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,9,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([1,3,2])([[.3],[5,1,3],[2.2,.5]])
    out = Automatize(diagram,master,[15])
    out = Automatize(Door(1),out(None),[19])
    out = Automatize(Windows(1),out(None),[3])
    masterFinal = out([4,8])
    return masterFinal
#END#

#BLOCCO #2 : Stanza Vladi
def VlaRoom() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,7,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([1,3,2])([[.3],[5,1,1],[2.2,.5]])
    out = Automatize(diagram,master,[15])
    out = Automatize(Door(1),out(None),[19])
    out = Automatize(Windows(1),out(None),[3])
    masterFinal = out([4,8])
    return masterFinal
#END#

#BLOCCO #3 : Stanza Nico
def NikRoom() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,9,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([1,3,2])([[.3],[5,1,3],[2.2,.5]])
    out = Automatize(diagram,master,[15])
    out = Automatize(Door(1),out(None),[19])
    out = Automatize(Windows(1),out(None),[3])
    masterFinal = out([4,8])
    return masterFinal
#END#

#BLOCCO #4 : Ingresso
def Ingresso() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,10,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([3,1,2])([[4.5,1.5,3],[.3],[2.2,.5]])
    out = Automatize(diagram,master,[11])
    masterFinal = out([9,19])
    return masterFinal
#END#

#BLOCCO #5 : Cucina
def Cucina() :
    master = assemblyDiagramInit([5,5,2])([[.3,4,.3,9,.3],[.3,11,.3,6,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([3,1,2])([[0.1,6,0.1],[.3],[2.2,.5]])
    out = Automatize(diagram,master,[15])
    toRemove = [12,18,26,16,36,32,34]
    masterFinal = out(toRemove)
    return masterFinal
#END#

#BLOCCO #6 : Corridoio
def Corridoio() :
    master = assemblyDiagramInit([3,3,2])([[.3,3,.3],[.3,12,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([1,3,2])([[.3],[0.1,10.5,1.5],[2.2,.5]])
    out = Automatize(diagram,master,[15])
    toRemove = [9,21]
    masterFinal = out(toRemove)
    return masterFinal
#END#

#BLOCCO #7 : Bagno
def Bagno() :
    master = assemblyDiagramInit([3,3,2])([[.3,3,.3],[.3,5,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([3,1,2])([[3,3,3],[.3],[2.2,.5]])
    out = Automatize(diagram,master,[11])
    toRemove = [9,19]
    masterFinal = out(toRemove)
    return masterFinal
#END#

#BLOCCO #8 : Balcone_Cucina
def Balcone_Cucina() :
    master = assemblyDiagramInit([3,3,2])([[.3,15,.3],[.3,2,.3],[.3,2.7]])
    diagram = assemblyDiagramInit([3,1,2])([[10.5,1.5,3],[.3],[2.2,.5]])
    out = Automatize(diagram,master,[11])
    diagramSep = assemblyDiagramInit([1,1,2])([[.3],[.3],[1.35,1.35]])
    out = Automatize(diagramSep, out(None), [7])
    toRemove = [18,8,23]
    masterFinal = out(toRemove)
    return masterFinal
#END#

#FUNZIONE GENERA MASTER#
def MasterPalace() :
    master = assemblyDiagramInit([3,2,2])([[7,3,13],[2,19],[.3,2.7]])
    out = Automatize(Cucina(),master,[11])
    out = Automatize(Corridoio(),out(None),[7])
    diagramSplitBC = assemblyDiagramInit([1,3,2])([[7],[9,1,8.5],[.3,2.7]])
    out = Automatize(diagramSplitBC,out(None),[3])
    out = Automatize(NikRoom(),out(None),[79])
    out = Automatize(VlaRoom(),out(None),[82])
    content = assemblyDiagramInit([1,3,2])([[21],[23,19,7],[.3,2.7]])
    out = Automatize(out(None),content,[1])
    diagramSplitAIV = assemblyDiagramInit([3,1,2])([[7,7,9],[19],[.3,2.7]])
    out = Automatize(diagramSplitAIV,out(None),[2])
    out = Automatize(AntoRoom(),out(None),[207])
    out = Automatize(Ingresso(),out(None),[208])
    out = Automatize(Bagno(),out(None),[8])
    out = Automatize(Balcone_Cucina(),out(None),[10])
    toRemoveChain = [3,62,37,18,66,271,275]
    dwelling = out(toRemoveChain)
    dwellingA = STRUCT(MKPOLS(dwelling))
    dwellingRot = R([1,2])(PI)(dwellingA)
    dwellingB = T(1)(21)(T(2)(98)(dwellingRot))
    halfFloor = STRUCT([dwellingB,dwellingA])
    chainA = STRUCT([halfFloor, T(1)(21)]*2)
    palace = STRUCT([chainA, T(3)(3)]*10)
    return palace
#END#

#Def rampaScale function#
def rampaScale():
    V0 = [[0,0],[14,0],[14,4],[0,4]]
    V1 = [[0,0],[12,0],[12,4],[0,4]]
    V2 = [[0,0],[10,0],[10,4],[0,4]]
    V3 = [[0,0],[8,0],[8,4],[0,4]]
    V4 = [[0,0],[6,0],[6,4],[0,4]]
    V5 = [[0,0],[4,0],[4,4],[0,4]]
    V6 = [[0,0],[2,0],[2,4],[0,4]]
    FV = [[0,1,2,3,0]]
    pol0 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V0[v] for v in cell] for cell in FV])))
    solid0 = PROD([pol0, QUOTE([.5])])
    pol1 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V1[v] for v in cell] for cell in FV])))
    solid1 = PROD([pol1, QUOTE([-.5,.5])])
    pol2 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V2[v] for v in cell] for cell in FV])))
    solid2 = PROD([pol2, QUOTE([-1,.5])])
    pol3 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V3[v] for v in cell] for cell in FV])))
    solid3 = PROD([pol3, QUOTE([-1.5,.5])])
    pol4 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V4[v] for v in cell] for cell in FV])))
    solid4 = PROD([pol4, QUOTE([-2,.5])])
    pol5 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V5[v] for v in cell] for cell in FV])))
    solid5 = PROD([pol5, QUOTE([-2.5,.5])])
    pol6 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V6[v] for v in cell] for cell in FV])))
    solid6 = PROD([pol6, QUOTE([-3,.5])])
    return STRUCT([solid0,solid1,solid2,solid3,solid4,solid5,solid6])
#end

#Def bezierMirror function
def bezierMirror() :
    controls = [[2.33,1.33],[2.33,0.66],[0,0.66],[0,2.33],
                [1.33,2.33],[1.33,2.33],[1.33,3],[3,3],[3,2.33],
                [3,2.33],[3.5,2.33],[3.5,1.33],[2.33,1.33]]
    knots = [0,0,0,1,2,3,3,3,4,5,5,5,6,7,7,7]
    bspline = BSPLINE(2)(knots)(controls)
    obj = larMap(bspline)(larDom(knots))
    pol = SOLIDIFY(STRUCT(MKPOLS(obj)))
    mirror = PROD([pol, QUOTE([0.1])])
    mirror = R([3,2,1])((3*PI)/2)(mirror)
    return mirror

#FUNZIONE VETRATA#
def PareteVetro() :
    V = [[0,0],[22,0],[22,0.3],[0,0.3]]
    FV = [[0,1,2,3,0]]
    pol0 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V[v] for v in cell] for cell in FV])))
    solid0 = PROD([pol0, QUOTE([-3,27])])
    vetrata = STRUCT([COLOR([0.274,0.509,0.705])(solid0)])
    return vetrata
#END#

#Def groundFloor function
def groundFloor():
    content = assemblyDiagramInit([2,6,2])([[21,21],[23,19,7,7,19,23],[-3,-0.3]])
    toRemoveChain = [4,6,16,18]
    out = Automatize(None,content,None)
    ground = out(toRemoveChain)
    ground = STRUCT(MKPOLS(ground))
    mirror = T(1)(10)(T(3)(-3.5)(T(2)(42.2)(bezierMirror())))
    scal = R([1,2])(PI/2)(rampaScale())
    scal = T(1)(4)(T(3)(-3)(T(2)(42)(scal)))
    elevator = COLOR(BLACK)(T(1)(10)(T(3)(-3.5)(T(2)(55.8)(CUBOID([2,0.1,3])))))
    picture = DIFFERENCE([CUBOID([3,0.1,2]), T(1)(0.5)(T(3)(0.5)(CUBOID([2,0.1,1])))])
    picture = COLOR(BROWN)(T(1)(20)(T(3)(-2.5)(T(2)(42.2)(picture))))
    VIEW(STRUCT([ground,COLOR(CYAN)(mirror),scal,elevator,picture]))
    #return STRUCT([ground,COLOR(CYAN)(mirror)])
#end

stepsR = R([1,2])(PI/2)(rampaScale())
steps = T(1)(4)(T(3)(-3)(T(2)(42)(stepsR)))
rampe = STRUCT([steps, T(3)(3)]*10)

#ESEMPIO ESECUZIONE
groundFloor()
VIEW(STRUCT([rampe,MasterPalace()]))

