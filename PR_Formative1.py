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