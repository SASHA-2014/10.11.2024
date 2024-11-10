
class NameSurname:
    def __init__(self, name, surname):
        if(type(name) !=str):
           raise TypeError("Name is not a string")
        if(type(surname) !=str):
            raise TypeError("Surname is not a string")
        self.name = name
        self.surname = surname
class Student:
    student_amount = 0

if('age <= 0'):
    print("You have got a problem")
else:
    print("True")


    def __init__(self,name, surname, age,  height=160):
        self.heilght = height
        self.name = name
        self.surname = surname
        self.age = age
        Student.student_amount += 1
        self.ns = NameSurname(name, surname)
        self.age = age
        self.height = height
        Student.student_amount += 1
def printStudent(self):
    print(f'Heilght: {self.height}')
    print(f'Name: {self.name}')
    print(f'Surname: {self.surname}')
    print(f'Age: {self.age}')

def Birthday(self):
    self.age += 1
    print(f'Happy Birthday to {self.ns.name}. Now you {self.age}!')

try:
  Andriy = Student( 'Andriy', "Dzekish",  13 )
except Exception as error:
    print(error)

print(f'befor creating Student object {Student.student_amount}')
print()
class NameSurname:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

def Birthday(self):
    self.age += 1
    print(f'Happy Birthday to {self.ns.name}. Now you {self.age}!')

Andriy = Student( "Andriy", "Dzekish",  13 )

print(f'befor creating Student object {Student.student_amount}')
print(Andriy.heilght, Andriy.name, Andriy.surname, Andriy.age)
print(Student.student_amount)
print(Andriy.student_amount )
#print(f'after creating Student object {Student.student_amount}').heilght, Andriy.name, Andriy.surname, Andriy.age))
print(Student.student_amount)
print(Andriy.student_amount )
print(f'after creating Student object {Student.student_amount}')