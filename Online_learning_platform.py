#3.Online Learning platform

class User:
       def __init__(self,name,email):
                self.name=name
                self.email=email

       def display_info(self):
               print("User: ",self.name,"Email: ",self.email)

class Instructor(User):
       def __init__(self,name,email,subjects):
              super().__init__(name,email)
              self.subjects=subjects

       def upload_content(self):
              print(self.name,"upload content on",self.subjects)

       def display_info(self):
              print("instructor:",self.name,"Subject: ",self.subjects)
              
class CourseCreator(Instructor):
       def __init__(self,name,email,subjects,modules):
              super().__init__(name,email,subjects)
              self.modules=modules
       def create(self):
              print("Creating course")
              for module in self.modules:
                     print("-",module)

       def display_info(self):
              print("CourseCreator: ",self.name,"Modules: ",self.modules)
       
user = User("Anita", "anita@mail.com")
user.display_info()

instructor = Instructor("Raj", "raj@mail.com", "Math")
instructor.display_info()
instructor.upload_content()

creator = CourseCreator("Kiran", "kiran@mail.com", "Science", ["Module1", "Module2"])
creator.display_info()
creator.create()
