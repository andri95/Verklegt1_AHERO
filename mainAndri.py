#from IO.updateIO import UpdateIO
#from IO.readIO import ReadIO
#from IO.createIO import CreateIO
from LL.mainLL import MainLL


iotest = MainLL()
var = iotest.getAllStaffLL()

for x in iotest.getAllStaffLL():
    print(x.getName())
