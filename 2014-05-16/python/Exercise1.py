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
BROWN = [0.58823529411,0.29411764705,0]

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
    hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1.5)
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
def MasterDwelling() :
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
    return dwelling
#END#

DRAW(MasterDwelling())