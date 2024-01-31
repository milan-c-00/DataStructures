class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        return sum(self.marks)

    def determine_maximum_mark(self):
        return max(self.marks)

    def determine_minimum_mark(self):
        return min(self.marks)

    def determine_average(self):
        return self.get_total_sum_of_marks()/self.get_number_of_marks()

    def add_new_mark(self, mark):
        self.marks.append(mark)

    def remove_mark_at_index(self, index):
        del self.marks[index]


student = Student("Ranga", [23, 45, 56, 75])
number = student.get_number_of_marks()
print(f"Student[number_of_marks-{number}]")
sum_ = student.get_total_sum_of_marks()
maximum_mark = student.determine_maximum_mark()
minimum_mark = student.determine_minimum_mark()
average = student.determine_average()
student.add_new_mark(35)
student.remove_mark_at_index(2)

print(student.marks)
print(f"""Student[
    number_of_marks-{number} 
    max-{maximum_mark} 
    min-{minimum_mark} 
    avg-{average}]""")














