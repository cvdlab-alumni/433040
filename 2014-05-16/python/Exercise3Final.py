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

#Def Draw function
DRAW = COMP([VIEW,STRUCT,MKPOLS])
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
    VIEW(hpc)
    def Automatize0(toRemoveCells) :
        V_final,CV_final = master
        hpcFinal = V_final, [cell for k,cell in enumerate(CV_final) if not (k in toRemoveCells)]
        DRAW(hpcFinal)
        return hpcFinal
    return Automatize0
#end

#Def AutomatizeCellNumbering function
def AutomatizeCellNumbering(master, hpc) :
    hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,2)
    return hpc
#end

#TEST#####################################################################################
master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
hpcDIA = SKEL_1(STRUCT(MKPOLS(diagram)))
hpcDIA = cellNumbering (diagram,hpcDIA)(range(len(diagram[1])),CYAN,2)
VIEW(hpcDIA)

toMergeChain = [19,31,39]

#partial application of Automatize function
out = Automatize(diagram,master,toMergeChain)

toRemoveChain = [13,17,31,35,55,49,61]

out(toRemoveChain)
#END######################################################################################

