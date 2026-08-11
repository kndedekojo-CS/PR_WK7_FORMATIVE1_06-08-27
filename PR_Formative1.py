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
#This will be a child class of  the Assignment. It will contain  information it inherits from Assignment.

class Homework(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        #This will use the Assignment class to store the  information about the homework.
        super().__init__(subject, title, score, max_score, due_date, "Homework")

#EXAM CLASS
#This will be a child class of the Assignment. It will contain  information it inherits from Assignment.

class Exam(Assignment):
    def __init__(self, subject, title, score, max_score, due_date):
        #This will use the Assignment class to store the information about the exam.
        super().__init__(subject, title, score, max_score, due_date, "Exam")

#FUNCTION TO GET A VALID SCORE
#This function keeps asking the user until they type in a real number.This stops the program from crashing if the user types letters by mistake.

def get_score(message):
    while True:
        score = input(message)

        try:
            score = float(score)

            if score < 0:
                print("Score cannot be negative. Try again.")
            else:
                return score

        except:
            print("Please enter a number.")


#GRADE TRACKER CLASS
#The grade tracker class will be used to store all of the assignments and later list,filter and calculate grade for each subject.

class GradeTracker:
    def __init__(self):
        #This will start with an empty list of assignments, because none has been added yet.
        self.assignments = []

    def add_assignment(self, assignment):
        #This will add the homework or exam object to the the list.
        self.assignments.append(assignment)

    def add_homework(self):
        #This will ask the user for the information needed to create the homework object.
        subject = input("Enter the subject: ")
        title = input("Enter the title of the homework: ")



        #Using get_score so the program can validate the score.
        score =  get_score("Enter the score received: ")
        max_score = get_score("Enter the maximum score of your work: ")

        #Check that the score is not bigger than the max score.
        if score > max_score:
            print("Score cannot be greater than max score. Homework not added.")
            return

        due_date = input("Enter the due date (dd/mm/yyyy): ")
 
        #This will create the Homework object using the information entered by the user.
        homework = Homework(subject, title, score, max_score, due_date)
 
        #This will add the homework to the list of assignments in the GradeTracker class.
        self.add_assignment(homework)
        print("Homework added successfully!")