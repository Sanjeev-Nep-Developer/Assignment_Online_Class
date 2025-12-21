# Create a Python class to represent a University. The university should have attributes like name, location, and a list of departments. Implement encapsulation to protect the internal data of the University class. Create a Department class that inherits from the University class. The Department class should have attributes like department name, head of the department, and a list of courses offered. Implement polymorphism by defining a common method for both the University and Department classes to display their details.

class University:
    def __init__(self, name, location, list_of_departments):
        self.name = name
        self.location = location
        self.list_of_departments = list_of_departments
        print("University Method init.. ")

    def printDetails(self):
        print("University Name : ", self.name)
        print("University Location : ", self.location)
        print("University List of Departments : ", self.list_of_departments)


class Department(University):
    def __init__(self, university_name, university_location, university_list_of_departments, department_name, head_of_department, list_courses_offered):
        self.department_name = department_name
        self.head_of_department = head_of_department
        self.list_courses_offered = list_courses_offered
        self.university = University(
            university_name, university_location, university_list_of_departments)
        print("Department Method Called... ")

    def printDetails(self):
        print("Department Name : ", self.department_name)
        print("Head of Department  : ", self.head_of_department)
        print(" List of Courses Offered : ", self.list_courses_offered)


HM_DEPT = Department('New Capital College ', 'Tandi',
                 ["Management", "Science", "Bio"],"HM","Madhu_Nepal",["Hm_1","Hm_2","Hm_3"])

HM_DEPT.printDetails()
