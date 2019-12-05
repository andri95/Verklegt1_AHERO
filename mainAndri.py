#from IO.updateIO import UpdateIO
#from IO.readIO import ReadIO
#from IO.createIO import CreateIO
from LL.mainLL import MainLL


iotest = MainLL()

for x in iotest.getAllCabinCrewLL():
    print(x.getName())
