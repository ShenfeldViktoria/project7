class Mark:
    def __init__ (self, subject, value):
        self.subject = subject
        self.value = value

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, subject, value):
        mark = Mark(subject, value)
        self.marks.append(mark)

    def remove_mark(self, subject):
        self.marks = [mark for mark in self.marks if mark.subject != subject]

    def update_mark(self, subject, new_value):
        for mark in self.marks:
            if mark.subject == subject:
                mark.value = new_value
                break

    def print_marks(self):
        if self.marks:
            print(f"Marks for {self.name}:")
            for mark in self.marks:
                print(f"{mark.subject}: {mark.value}")
        else:
            print(f"No marks for {self.name}")

student1 = Student("Abobik")
student1.add_mark("Math", 85)
student1.add_mark("History", 90)
student1.print_marks()

student1.add_mark("Physics", 75)
student1.print_marks()

student1.remove_mark("Math")
student1.print_marks()

student1.update_mark("History", 95)
student1.print_marks()
