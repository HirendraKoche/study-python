class Person:
    def __init__(self, fname: str, mname: str, lname: str, age: int, addr: dict, gender: str, pin: int) -> None:
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.age = age
        self.addr = addr
        self.gender = gender
        self.pin = pin
    
    def getInfo(self) -> dict:
        return {
            "FirstName": self.fname,
            "MiddleName": self.mname,
            "LastName": self.lname,
            "Age": self.age,
            "Address": self.addr,
            "Gender": self.gender,
            "PIN": self.pin
        }
    
    def updateInfo(self, info: dict):
        keys = info.keys()
        if "FirstName" in keys:
            self.fname = info['FirstName']
        if "MiddleName" in keys:
            self.mname = info['MiddleName']
        if "LastName" in keys:
            self.lname = info['LastName']
        if "Age" in keys:
            self.age = info['Age']
        if "Address" in keys:
            self.addr = info['Address']
        if "Gender" in keys:
            self.gender = info['Gender']
        if "PIN" in keys:
            self.pin = info['PIN']


class Student(Person):
    def __init__(self, fname: str, mname: str, lname: str, age: int, addr: dict, gender: str, pin: int, qualification: str, grade: str, university: str, specification: str) -> None:
        super().__init__(fname, mname, lname, age, addr, gender, pin)
        self.qualification = qualification
        self.grade = grade
        self.university = university
        self.specification = specification

    def getInfo(self) -> dict:
        info = super().getInfo()
        info['Qualification'] = self.qualification
        info['Grade'] = self.grade
        info['University'] = self.university
        info['Specification'] = self.specification
        return info
    
    def updateInfo(self, info: dict):
        super().updateInfo(info)
        keys = info.keys()
        if "Qualification" in keys:
            self.qualification = info['Qualification']
        if "Grade" in keys:
            self.grade = info['Grade']
        if "University" in keys:
            self.university = info['University']
        if "Specification" in keys:
            self.specification = info['Specification']
        
        
class Employee(Student):
    def __init__(self, fname: str, mname: str, lname: str, age: int, addr: dict, gender: str, pin: int, qualification: str, grade: str, university: str, specification: str, empNo: int, employer: str, salary: float) -> None:
        super().__init__(fname, mname, lname, age, addr, gender, pin, qualification, grade, university, specification)
        self.empNo = empNo
        self.employer = employer
        self.salary = salary
    
    def getInfo(self) -> dict:
        info = super().getInfo()
        info['EmployeeNo'] = self.empNo
        info['Employer'] = self.employer
        info['Salary'] = self.salary
        return info
    
    def updateInfo(self, info: dict):
        super().updateInfo(info)
        keys = info.keys()
        if "EmployeeNo" in keys:
            self.empNo = info['EmployeeNo']
        if "Employer" in keys:
            self.employer = info['Employer']
        if "Salary" in keys:
            self.salary = info['Salary']
