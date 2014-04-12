from pyplasm import *
from larcc import *
from lar2psm import *
from mapper import *

#FUNZIONE GENERA GRATTACIELI (VERY SIMPLE)
def skyscraper(dim):
    x,y,z = dim
    skycraper = COLOR([0.753,0.753,0.753])(EXPLODE(1.1,1.1,1.1)(MKPOLS(larCuboids([x,y,z],True))))
    return skycraper
#END

#FUNZIONE GENERA SUOLO
def background():
    ground = COLOR([0.957,0.643,0.376])(T(2)(-75)(T(1)(-75)(CUBOID([150,150,0.1]))))
    return ground
#END


skyscraper0 = T(2)(10)(T(1)(10)(COLOR(GRAY)(skyscraper([3,3,8]))))
skyscraper2 = T(2)(-30)(T(1)(-14)(COLOR(GRAY)(skyscraper([2,2,7]))))
skyscraper3 = T(2)(-14)(T(1)(14)(COLOR(GRAY)(skyscraper([4,4,9]))))
skyscraper4 = T(2)(-26)(T(1)(-12)(COLOR(GRAY)(skyscraper([4,6,10]))))
skyscraper5 = T(2)(-4)(T(1)(20)(COLOR(GRAY)(skyscraper([6,6,10]))))
neighbouring_Buildings = STRUCT([skyscraper0, skyscraper2, skyscraper3, skyscraper4, skyscraper5])


burjKhalifa_neighbouring_Buildings = STRUCT([background(), neighbouring_Buildings])



VIEW(burjKhalifa_neighbouring_Buildings)


