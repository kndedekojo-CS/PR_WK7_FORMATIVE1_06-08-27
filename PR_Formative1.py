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
    #This will go through each assignment in the list and display the information stored in it.
    for assignment in self.assignments:
        print(f"Subject: {assignment.subject}")
        print(f"Title: {assignment.title}")
        print(f"Score: {assignment.score}/{assignment.max_score}")
        print(f"Due Date: {assignment.due_date}")
        print(f"Type: {assignment.assignment_type}")
        print()
def filter_assignments(self):
    #This will ask the user how they want to filter the assignments.
    print("How would you like to filter the assignments?")
    print("1. By Subject")
    print("2. By Type (Homework or Exam)")
    print("3. By month")

    choice = input("Choose an option (1-3): ")
     #Filter assignment by subject.
    if choice == "1":
        subject = input("Enter the subject: ")
        for assignment in self.assignments:
            if assignment.subject.lower() == subject.lower():
                print(assignment.title)

    elif choice == "2":
        assignment_type = input("Enter your assignmnet type(Homework/Exam):")
        for assignment in self.assignments:
            if assignment.type.lower() == assignment_type.lower():
                print(assignment.title)

    elif choice == "3":
        month = input("Enter the month (MM): ")
        for assignment in self.assignments:
            assignment_month = assignment.due_date.split("/")[0]
            if assignment_month == month:
                print(assignment.title)


def show_summary(self):

        # Calculate the overall average of all assignments.
        total = 0

        for assignment in self.assignments:

            percentage = (assignment.score / assignment.max_score) * 100
            total = total + percentage

        if len(self.assignments) > 0:
            average = total / len(self.assignments)
            print("Overall average:", average)
        else:
            print("No assignments available.")


def show_summary(self):

        # Calculate the overall average of all assignments.
        total = 0

        for assignment in self.assignments:

            percentage = (assignment.score / assignment.max_score) * 100
            total = total + percentage

        if len(self.assignments) > 0:
            average = total / len(self.assignments)
            print("Overall average:", average)
        else:
            print("No assignments available.")

def show_summary(self):

        # Calculate the overall average of all assignments.
        total = 0

        for assignment in self.assignments:
            percentage = (assignment.score / assignment.max_score) * 100
            total = total + percentage

        if len(self.assignments) > 0:
            average = total / len(self.assignments)
            print("Overall average:", average)

        else:
            print("No assignments available.")
            return

        # Calculate the average for each subject.
        subjects = []

        for assignment in self.assignments:
            if assignment.subject not in subjects:
                subjects.append(assignment.subject)

        for subject in subjects:

            subject_total = 0
            subject_count = 0

            for assignment in self.assignments:

                if assignment.subject == subject:
                    percentage = (assignment.score / assignment.max_score) * 100
                    subject_total = subject_total + percentage
                    subject_count = subject_count + 1

            subject_average = subject_total / subject_count

            print(subject, "average:", subject_average)

        # Find the highest and lowest assignment.
        highest = self.assignments[0]
        lowest = self.assignments[0]

        for assignment in self.assignments:

            current_percentage = (assignment.score / assignment.max_score) * 100
            highest_percentage = (highest.score / highest.max_score) * 100
            lowest_percentage = (lowest.score / lowest.max_score) * 100

            if current_percentage > highest_percentage:
                highest = assignment

            if current_percentage < lowest_percentage:
                lowest = assignment

        print("Highest assignment:", highest.title)
        print("Lowest assignment:", lowest.title)

# Creating  the tracker and giving the user a menu to choose what they want the program to do.

tracker = GradeTracker()

while True:

    print("\nStudent Grade Tracker")
    print("1. Add homework")
    print("2. Add exam")
    print("3. List assignments")
    print("4. Filter assignments")
    print("5. Show summary")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        tracker.add_homework()

    elif choice == "2":
        tracker.add_exam()

    elif choice == "3":
        tracker.list_assignments()

    elif choice == "4":
        tracker.filter_assignments()

    elif choice == "5":
        tracker.show_summary()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")        

