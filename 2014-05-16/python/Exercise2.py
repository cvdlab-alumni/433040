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
#END IMPORT#

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#BLOCCO #1 : Stanza Antonio
def AntoRoom() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,9,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 15
    diagram = assemblyDiagramInit([1,3,2])([[.3],[5,1,3],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [9,19]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#BLOCCO #2 : Stanza Vladi
def VlaRoom() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,7,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 15
    diagram = assemblyDiagramInit([1,3,2])([[.3],[5,1,1],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [9,19]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#BLOCCO #3 : Stanza Nico
def NikRoom() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,9,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 15
    diagram = assemblyDiagramInit([1,3,2])([[.3],[5,1,3],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [9,19]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#BLOCCO #4 : Ingresso
def Ingresso() :
    master = assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,10,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 11
    diagram = assemblyDiagramInit([3,1,2])([[4.5,1.5,3],[.3],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [9,19]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#BLOCCO #5 : Cucina
def Cucina() :
    master = assemblyDiagramInit([5,5,2])([[.3,4,.3,9,.3],[.3,11,.3,6,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 15
    diagram = assemblyDiagramInit([3,1,2])([[0.1,6,0.1],[.3],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [12,18,26,16,36,32,34]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#BLOCCO #6 : Corridoio
def Corridoio() :
    master = assemblyDiagramInit([3,3,2])([[.3,3,.3],[.3,12,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 15
    diagram = assemblyDiagramInit([1,3,2])([[.3],[0.1,10.5,1.5],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [9,21]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#BLOCCO #7 : Bagno
def Bagno() :
    master = assemblyDiagramInit([3,3,2])([[.3,3,.3],[.3,5,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 11
    diagram = assemblyDiagramInit([3,1,2])([[3,3,3],[.3],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [9,19]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#BLOCCO #8 : Balcone_Cucina
def Balcone_Cucina() :
    master = assemblyDiagramInit([3,3,2])([[.3,15,.3],[.3,2,.3],[.3,2.7]])
    V,CV = master
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
    toMerge = 11
    diagram = assemblyDiagramInit([3,1,2])([[10.5,1.5,3],[.3],[2.2,.5]])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toRemove = [9,19]
    master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master
#END#

#FUNZIONE GENERA MASTER#
def MasterPalazzo() :
    master = assemblyDiagramInit([3,2,2])([[7,3,13],[2,19],[.3,2.7]])
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toMerge = 11
    master = diagram2cell(Cucina(),master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toMerge = 7
    master = diagram2cell(Corridoio(),master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toMerge = 3
    diagramSplitBC = assemblyDiagramInit([1,3,2])([[7],[9,1,8.5],[.3,2.7]])
    master = diagram2cell(diagramSplitBC,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toMerge = 79
    master = diagram2cell(NikRoom(),master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    toMerge = 82
    master = diagram2cell(VlaRoom(),master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
    content = assemblyDiagramInit([1,2,2])([[23],[21,19],[.3,2.7]])
    hpc_content = SKEL_1(STRUCT(MKPOLS(content)))
    hpc_content = cellNumbering (content,hpc_content)(range(len(content[1])),CYAN,2)
    toMerge = 1
    masterFinal = diagram2cell(master,content,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(masterFinal)))
    hpc = cellNumbering (masterFinal,hpc)(range(len(masterFinal[1])),CYAN,2)
    toMerge = 2
    diagramSplitAIV = assemblyDiagramInit([3,1,2])([[7,7,9],[10],[.3,2.7]])
    masterFinal = diagram2cell(diagramSplitAIV,masterFinal,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(masterFinal)))
    hpc = cellNumbering (masterFinal,hpc)(range(len(masterFinal[1])),CYAN,2)
    toMerge = 127
    masterFinal = diagram2cell(AntoRoom(),masterFinal,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(masterFinal)))
    hpc = cellNumbering (masterFinal,hpc)(range(len(masterFinal[1])),CYAN,2)
    toMerge = 128
    masterFinal = diagram2cell(Ingresso(),masterFinal,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(masterFinal)))
    hpc = cellNumbering (masterFinal,hpc)(range(len(masterFinal[1])),CYAN,2)
    toMerge = 6
    masterFinal = diagram2cell(Bagno(),masterFinal,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(masterFinal)))
    hpc = cellNumbering (masterFinal,hpc)(range(len(masterFinal[1])),CYAN,2)
    toMerge = 8
    masterFinal = diagram2cell(Balcone_Cucina(),masterFinal,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(masterFinal)))
    hpc = cellNumbering (masterFinal,hpc)(range(len(masterFinal[1])),CYAN,2)
    VIEW(hpc)
    toRemove = [152,60,16,156,64,35,198]
    masterFinal = masterFinal[0],[cell for k,cell in enumerate(masterFinal[1]) if not (k in toRemove)]
    dwellingA = STRUCT(MKPOLS(masterFinal))
    dwellingB = T(1)(23)(T(2)(80)(R([1,2])(PI)(dwellingA)))
    chainA = STRUCT([dwellingB,dwellingA, T(1)(23)]*2)
    chainB = STRUCT([chainA, T(3)(3)]*10)
    return chainB
#END#

#FUNZIONE GENERA SCALA#
def spiralStair(thickness=0.2,R=1.,r=0.5,riser=0.1,pitch=2.,nturns=2.,steps=18):
    V,CV = larSolidHelicoid(thickness,R,r,pitch,nturns,steps)()
    W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+[SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
        for k,v in enumerate(V[:-4]) if k%4==0])
    for k,w in enumerate(W[:-12]):
        if k%6==0: W[k+1][2]=W[k+10][2]; W[k+3][2]=W[k+11][2]
    nsteps = len(W)/12
    CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*8])
            for k in range(nsteps)]
    return W,CW
#END#

#FUNZIONE VETRATA#
def PareteVetro() :
    V = [[0,0],[22,0],[22,0.3],[0,0.3],[0,0]]
    FV = [[1,2,3,4,1]]
    pol0 =  SOLIDIFY(STRUCT(AA(POLYLINE)([[V[v] for v in cell] for cell in FV])))
    solid0 = PROD([pol0, QUOTE([-3,27])])
    vetrata = STRUCT([COLOR([0.274,0.509,0.705])(solid0)])
    return vetrata
#END#

stair = STRUCT(MKPOLS(spiralStair(0.2,1,0.5,0.1,2,27.3,18)))
stairT = T(2)(40)(stair)
vetrata = T(2)(7)(T(1)(46)(R([1,2])(PI/2)(T(1)(20)(PareteVetro()))))
VIEW(STRUCT([stairT, MasterPalazzo(), vetrata]))

