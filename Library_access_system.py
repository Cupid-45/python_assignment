# 1. Library Access System

class Member:
          def __init__(self,name,id):
                 self.name=name
                 self.id=id

class StudentMember(Member):
       def __init__(self,name,id): 
              super().__init__(name,id)
              self.books_borrowed=0

       def add_book(self):
                  self.books_borrowed+=1

       def return_books(self):
            if self.books_borrowed>0:
                self.books_borrowed-=1

       def display_status(self):
              print(self.name,"has borrowed",self.books_borrowed,"books")

student=StudentMember('Rahul','M101')
student.add_book()
student.add_book()
student.return_books()
student.display_status()


