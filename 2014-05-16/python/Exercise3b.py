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

#Funzione diagram2cell modificata (corretto bug numerazione celle)
def diagram2cellNEW(diagram,master,toMerge):
    ToMerge=list.sort(toMerge)
    ToMerge=list.reverse(toMerge)	
    cont=0
    for k in toMerge:
        master = diagram2cell(diagram[cont],master,k)
        cont=cont+1;
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumberingNEW(master, hpc)
    return hpc
#END#

#Funzione numera celle
def cellNumberingNEW(master,hpc):
    hpc = cellNumbering(master,hpc)(range(len(master[1])),RED,2)
    return hpc
#END

#ESEMPIO#
master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumberingNEW (master,hpc)
VIEW(hpc)
ToRemove=[31,39]
master = master[0],[cell for k,cell in enumerate(CV) if not (k in ToRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumberingNEW(master, hpc)
VIEW(hpc)
diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
ToMerge = [34]
hpc = diagram2cellNEW([diagram],master,ToMerge)
VIEW(hpc)
ToRemove=[19]
master = master[0],[cell for k,cell in enumerate(CV) if not (k in ToRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumberingNEW(master, hpc)
VIEW(hpc)
#END#

