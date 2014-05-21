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
def MasterDwelling() :
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
    return masterFinal
#END#

DRAW(MasterDwelling())