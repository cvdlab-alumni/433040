""" progressive refinement of a block diagram """
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

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#Funzione MergeList (no doppioni) V1-->V0#
def mergeLists(V0,V1) :
    V = []
    isPresente = False
    for v1 in V1:
        for v0 in V0:
            if(v1==v0):
                isPresente = True
                break
        if(isPresente==False):
            V.append(v1)
            isPresente = False
    if(len(V)==0):
        return V0
    return V
#END#

#FUNZIONE Automatize#
def Automatize(diagram, master, toMergeCells) :
    masterFinal = master
    hpc_list = []
    V_final = []
    CV_final = []
    for cell in toMergeCells :
        masterFinal = diagram2cellNEW(diagram,master,cell)
        hpc = SKEL_1(STRUCT(MKPOLS(masterFinal)))
        hpc = cellNumbering (masterFinal,hpc)(range(len(masterFinal[1])),CYAN,2)
        hpc_list.append(hpc)
        #CV_final.pop(cell)
        if(len(CV_final)==0):
            CV_final = masterFinal[1]
            V_final = masterFinal[0]
        else:
            V_final = mergeLists(V_final,masterFinal[0])
        VIEW(hpc)
    #TODO rimuovo celle doppie
    hpc_Final = STRUCT(hpc_list)
    larModel = V_final,CV_final
    master_result = cellNumbering (larModel,hpc_Final)(range(len(CV_final)),CYAN,2)
    VIEW(hpc_Final)
    VIEW(SKEL_1(STRUCT([master_result])))
    def Automatize0(toRemoveCells) :
        masterRem = V_final, [cell for k,cell in enumerate(CV_final) if not (k in toRemoveCells)]
        return masterRem
    return Automatize0
#END#

def diagram2cellNEW(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   V,CV1,CV2,n12 = vertexSieve(master,diagram)
   VIEW(SKEL_1(STRUCT(MKPOLS([V,CV1]))))
   VIEW(SKEL_1(STRUCT(MKPOLS([V,CV2]))))
   
   V = master[0] + diagram[0]
   offset = len(master[0])
   CV = [c for k,c in enumerate(master[1]) if k != cell] + [[v+offset for v in c] for c in diagram[1]]
   master = V, CV
   return master

#ESEMPIO#
master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)
diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])

VIEW(SKEL_1(STRUCT(MKPOLS(Automatize(diagram, master, [39,31])([31])))))
#END#