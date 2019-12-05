#from IO.createIO import CreateIO
#from Models.staffData import StaffData

from IO.updateIO import UpdateIO
from IO.readIO import ReadIO
from IO.createIO import CreateIO
from mainIO import MainIO

ioTest = MainIO(['Nuuk','Gummi','420420420'])
ioTest.updateDestIO()


#ioTest = CreateIO()
#new_staff = StaffData('420420420','voldemort','iamawizard','86940129','2358266','voldemortsexy@nanair.com','Cabincrew','Flight Attendant','N/A')
#ioTest.addNewStaff(new_staff)
