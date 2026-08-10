#STUDENT GRADE / ASSIGNMENT TRACKER.

#ASSIGNMENT CLASS
#This will be the parent class for all assignments. It will contain information that both homework and exams will have.

class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, assignment_type):
        #This is to store the information about the  assignment, so it can be used later to calculate the grade.
        self.subject = subject
        self.title = title
        self.score = float(score)
        self.max_score = float(max_score)
        self.due_date = due_date
        self.assignment_type = assignment_type

#HOMEWORK CLASS
#This will be a child class of  the Assignment. It will contain  information it inherits from Assignment, as well as information specific to homework assignments.

class Homework(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        #This will use the Assignment class to store the 
        super().__init__(subject, title, score, max_score, due_date, "Homework")

class Exam(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        #This will use the Assignment class to store the information about the exam.
        super().__init__(subject, title, score, max_score, due_date, "Exam")


#Grade Tracker class
#The grade tracker class will be used to store all of the assignments and later list,filter and calculate grade for each subject.

class GradeTracker:
    def __init__(self):
        #This will start with an empty list of assignments, because none has been added yet.
        self.assignments = []
    def add_assignment(self, assignment):
        #This will add the homework or exam object to the the list.
        self.assignments.append(assignment)

def add_homework(self):
    #This will ask the user for the information  needed to create the homework object.
    subject = input("Enter the subject: ")
    title = input("Enter the title of the homework: ")
    score = input("Enter the score received: ")
    max_score = input("Enter the maximum score of your work: ")
    due_date = input("Enter the due date (MM/DD/YYYY): ")
    #This will create the Homework object using the information entered by the user.
    homework = Homework(subject, title, score, max_score, due_date)
    #This will add the homework to the list of assignments in the GradeTracker class.
    self.add_assignment(homework)

def add_exam(self):
    #This will ask the user for the information needed to create the exam object.
    subject = input("Enter the subject: ")
    title = input("Enter the title of the exam: ")
    score = input("Enter the score received: ")
    max_score = input("Enter the maximum score of your work: ")
    due_date = input("Enter the due date (MM/DD/YYYY): ")
    #This will create the Exam object using the information entered by the user.
    exam = Exam(subject, title, score, max_score, due_date)
    #This will add the exam to the list of assignments in the GradeTracker class.
    self.add_assignment(exam)

tracker = GradeTracker()
tracker.add_homework()
print("\nHomework added successfully!")
print(len(tracker.assignments))

def list_assignments(self):
    #This will go through each assigment in the list and display the the information stored in it.
    for assignment in self.assignments:
        print(f"Subject: {assignment.subject}")
        print(f"Title: {assignment.title}")
        print(f"Score: {assignment.score}/{assignment.max_score}")
        print(f"Due Date: {assignment.due_date}")
        print(f"Type: {assignment.assignment_type}")
        print()
        