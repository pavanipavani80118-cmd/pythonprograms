class student:
 def __init__(self,name,marks):
        self.name=name
        self.marks=marks
def print__student__info(student):
     print(f"Name:{student.name},marks:{student.marks}")
s1=student("tillu",92)
print__student__info(s1)
