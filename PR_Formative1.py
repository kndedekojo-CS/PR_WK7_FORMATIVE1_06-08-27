#STUDENT GRADE / ASSIGNMENT TRACKER.

#ASSIGNMENT CLASS
#This will be the parent class for all assignments. It will contain information that both homework and exams will have.

from calendar import month


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

    def add_exam(self):
        #This will ask the user for the information needed to create the exam object.
        subject = input("Enter the subject: ")
        title = input("Enter the title of the exam: ")

        #Using get_score so the program can validate the score.
        score =  get_score("Enter the score received: ")
        max_score = get_score("Enter the maximum score of your work: ")

        #Check that the score is not bigger than the max score.
        if score > max_score:
            print("Score cannot be greater than max score. Exam not added.")
            return

        due_date = input("Enter the due date (dd/mm/yyyy): ")

        #This will create the Exam object using the information entered by the user.
        exam = Exam(subject, title, score, max_score, due_date)

        #This will add the exam to the list of assignments in the GradeTracker class.
        self.add_assignment(exam)
        print("Exam added successfully!")

    def list_assignments(self):
        #This will go through each assignment in the list and display the information stored in the assignment object.

        print("\n~~~~~~~~~~~~LIST OF ALL ASSIGNMENTS~~~~~~~~~~~~")


        if len(self.assignments) == 0:
            print("No assignments have been added yet.")
            return

        for assignment in self.assignments:
            print(f"\nSubject: {assignment.subject}")
            print(f"Title: {assignment.title}")
            print(f"Score: {assignment.score}/{assignment.max_score}")
            print(f"Due Date: {assignment.due_date}")
            print(f"Type: {assignment.assignment_type}")

    def filter_assignments_by_subject(self, subject):
        #This will ask the user how they want to filter the assignments.

        print(f"\n~~~~~~~~~~~~FILTER ASSIGNMENTS~~~~~~~~~~~~")

        print(f"\nHow would you like to filter the assignments?")
        print(f"1. Filter by subject")
        print(f"2. Filter by assignment type(Homework or Exam)")
        print(f"3. Filter by Month(MM/YYYY )")

        choice = input("Enter your choice (1-3): ")

        matches = []

        #Filter assignment by subject
        if choice == "1":
            subject = input("Enter the subject to filter by: ")
            for assignment in self.assignments:
                if assignment.subject.lower() == subject.lower():
                    matches.append(assignment)

        #Filter assignment by type
        elif choice == "2":
            assignment_type = input("Enter the assignment type to filter by (Homework or Exam): ")
            for assignment in self.assignments:
                if assignment.assignment_type.lower() == assignment_type.lower():
                    matches.append(assignment)

        #Filter assignment by month
        elif choice == "3":
            month_year = input("Enter the month and year to filter by (MM/YYYY): ")
            for assignment in self.assignments:
                 #due_date looks like 15/08/2026, so characters 3 to 10 are 08/2026
                if assignment.due_date[3:10] == month:
                    matches.append(assignment)

        else:
            print("Invalid choice. Please try again.")
            return

        #This will display the matches found based on the filter criteria.
        show_matches(matches)

    def show_summary(self):
        #This will calculate the total score and max score for each subject and display the grade percentage.

        print("\n~~~~~~~~~~~~GRADE SUMMARY~~~~~~~~~~~~")

        if len(self.assignments) == 0:
            print("No assignments have been added yet.")
            return

        #This calculates the overall average for all assignments.
        total_score = 0
        total_max_score = 0

        for assignment in self.assignments:
            total_score += assignment.score
            total_max_score += assignment.max_score

        overall_average = (total_score / total_max_score) * 100
        print("Overall average:", round(overall_average, 2), "%")

        #This calculates the average for each subject.
        print("\nSubject Averages:")
        subjects = []

        for assignment in self.assignments:
            if assignment.subject not in subjects:
                subjects.append(assignment.subject)

        for subject in subjects:
            subject_score = 0
            subject_max_score = 0

            for assignment in self.assignments:
                if assignment.subject == subject:
                    subject_score += assignment.score
                    subject_max_score += assignment.max_score

            subject_average = (subject_score / subject_max_score) * 100
            print(subject, "average:", round(subject_average, 2), "%")


        #To find the highest and lowest scoring assignments, we will sort the assignments by score.
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

            print("\nHighest scoring assignment:", highest.title)
            print("Lowest scoring assignment:", lowest.title)


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


# TO SHOW FILTER RESULTS
#This function takes a list of assignments and prints their titles.If the list is empty, it tells the user nothing was found.We also use this so we don't have to repeat the same print logic for subject, type, and month filters.
 
def show_matches(matches):
    if len(matches) == 0:
        print("No assignments found.")
    else:
        for assignment in matches:
            print(assignment.title)

    