#from IO.updateIO import UpdateIO
#from IO.readIO import ReadIO
#from IO.createIO import CreateIO
from mainIO import MainIO


iotest = MainIO()
for x in iotest.getStaffIO():
    print(x.getName())
