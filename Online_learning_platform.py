3.Online Learning platform

class User:
          def __init__(self,name,email)
                self.name=name
                self.email=email

        def display_info(self)
               print("User: ",self.name,"Email: ",self.email)

class Instructor(User):
          def __init__(self,name,email,subjects):
                 super().__init__(name,email)
                 self.subject=subject

         def upload_content(self):
                print(self.name,"upload content on",self.subject)

        def display_info(self):
                print("instructor:",self.name,"Subject: ",self.subject)
              
class CourseCreator(Instructor):
          def __init__(self,name,email,subject,modules)
                super().__init__(self,name,email,subject)
                self.modules=modules
        def create(self):
               print("Creating course")
               for module in self.modules:
                       print("-",module)

       def display_info(self):
               print("CourseCreator: ",self.name,"Modules: ",self.modules)
