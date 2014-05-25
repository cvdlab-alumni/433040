from larcc import *
from boolean import *

def diagram2cellNEW(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   V,CV = master
   #remove cell in master
   CV = [c for k,c in enumerate(CV) if k != cell]
   #sieve vertex
   V, CV1, CV2, NN = vertexSieve((V,CV),diagram)
   CV = CV1+CV2
   master = V,CV
   return master