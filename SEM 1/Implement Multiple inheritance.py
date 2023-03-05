class OfficeStaff:
    def __init__(self, designation):
    	self.designation = designation

class FactoryStaff:
    def __init__(self, factory):
    	self.factory = factory

class CompanyMember(OfficeStaff, FactoryStaff):
    def __init__(self, name, id, designation, factory):
    	self.name = name
    	self.id = id
    	OfficeStaff.__init__(self, designation)
    	FactoryStaff.__init__(self, factory)

q = "y"
while q.lower() == 'y':
    	print("Enter Employee Details: ")
    	emp_id = input("Enter the ID: ")
    	name = input("Enter the name: ")
    	designation = input("Enter the Designation: ")
    	factory = input("Enter the Factory number: ")
    	#employee = CompanyMember("John Doe", "1234", "Manager", "Factory 1")
    	employee = CompanyMember(emp_id,name,designation,factory)
    	print("\nEmployee Details: ")
    	print("Employee Name: ",employee.name)
    	print("Employee ID: ",employee.id)
    	print("Employee Designation: ",employee.designation)
    	print("Employee Factory: ",employee.factory)
    	q = input("\nwant to continue?(y/n): ")
