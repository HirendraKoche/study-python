from classStudy import Employee
from random import randint
import json


def getNewPIN():
    return randint(100000000000, 999999999999)

def getNewEMPNo():
    return randint(100000,999999)

emp1pin = getNewPIN()
emp1empNo = getNewEMPNo()
emp1Addr = {
    "FlatNo": "E704",
    "SocietyName": "Kohinoor Sapphire",
    "AddressLine1": "Ram Nagar",
    "AddressLine2": "",
    "Locality": "Tathawade",
    "City": "Pune",
    "State": "Maharashtra",
    "Country": "India",
    "ZipCode": 411033
}
emp1 = Employee("Hirendra","Mukesh","Koche","32", emp1Addr, 'Male', emp1pin, "B.E.", 'First', 'SGBAU, Amravati', 'Computer Science', emp1empNo, 'Wipro PVT Ltd.', 3200000.00)

emp1Info = emp1.getInfo()
print(json.dumps(emp1Info, indent=4))

emp1changeInfo = {
    "Employer": "Google Pvt Ltd.",
    "Salary": 5400000.00
}

emp1changeInfo['EmployeeNo'] = getNewEMPNo()

emp1.updateInfo(emp1changeInfo)
emp1Info = emp1.getInfo()
print(json.dumps(emp1Info, indent=4))
