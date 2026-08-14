# **Student Grade / Assignment Tracker**

## **Project Overview**

This Student Grade / Assignment Tracker application was developed as part of the **Week 7 Formative Assessment for Programming 1**.  
The task involved building a **menu-driven Python program** that allows students to:

- Record homework and exam assignments
- View all assignments
- Filter assignment data
- Generate a grade summary

The project demonstrates key programming concepts taught in class, including:

- Functions
- Loops and conditionals
- Input validation
- Collections
- Object-Oriented Programming (OOP)
- Inheritance

The program runs entirely in the terminal, storing assignment data in memory during runtime. Its structured interface helps students manage and review their assignments within a single session.

---

## **Key Features**

- **Add Assignments** (Homework or Exam)
- **List All Assignments** in a clean formatted view
- **Filter Assignments** by:
  - Subject
  - Assignment type (Homework or Exam)
  - Month (MM/YYYY)
- **View Grade Summary** including:
  - Overall average
  - Subject averages
  - Highest-scoring assignment
  - Lowest-scoring assignment
- **Input Validation** for:
  - Negative scores
  - Non-numeric scores
  - Empty text inputs
  - Scores greater than the maximum score
- **OOP Design** using:
  - `Assignment`
  - `Homework`
  - `Exam`
  - `GradeTracker`
- **Inheritance** using `Homework` and `Exam` as child classes of `Assignment`

---

## **How to Run the Program**

### **1. Ensure Python 3 is installed**

Check using:

    python --version

### **2. Clone the project repository**

    git clone https://github.com/kndedekojo-CS/PR_WK7_FORMATIVE1_06-08-27

### **3. Navigate into the project directory**

    cd PR_WK7_FORMATIVE1_06-08-27

### **4. Run the program**

    python PR_Formative1.py

### **5. Follow the on-screen menu instructions**

The program will display the Grade Tracker menu. Enter the number of the option you want to use and follow the prompts.

---

## **Menu Structure**

The main program menu provides the following options:

    1) Add Homework
    2) Add Exam
    3) List All Assignments
    4) Filter Assignments
    5) Show Grade Summary
    6) Exit

### **Filter Menu**

When **Filter Assignments** is selected, the user can choose:

    1) Filter by Subject
    2) Filter by Assignment Type
    3) Filter by Month (MM/YYYY)

---

## **Sample Interactions**

### **Adding a Homework Assignment**

    Enter your choice (1-6): 1

    Enter the subject: English
    Enter the title of the homework: Subject-Verb
    Enter the score received: 18
    Enter the maximum score: 20
    Enter the due date (dd/mm/yyyy): 15/08/2026

##     Homework added successfully!

### **Adding an Exam**

    Enter your choice (1-6): 2

    Enter the subject: Mathematics
    Enter the title of the exam: Midterm Exam
    Enter the score received: 42
    Enter the maximum score: 50
    Enter the due date (dd/mm/yyyy): 20/08/2026

##     Exam added successfully!

### **Viewing All Assignments**

    Enter your choice (1-6): 3

    ~~~~~~~~~~~~LIST OF ALL ASSIGNMENTS~~~~~~~~~~~~

    Subject: English
    Title: Subject-Verb
    Score: 18.0/20.0
    Due Date: 15/08/2026
    Type: Homework 

    Subject: Mathematics
    Title: Midterm Exam
    Score: 42.0/50.0
    Due Date: 20/08/2026
    Type: Exam

### **Filtering Assignments**

    Enter your choice (1-6): 4

    ~~~~~~~~~~~~FILTER ASSIGNMENTS~~~~~~~~~~~~

    How would you like to filter the assignments?
    1. Filter by subject
    2. Filter by assignment type(Homework or Exam)
    3. Filter by Month(MM/YYYY)

    Enter your choice (1-3): 2
    Enter the assignment type to filter by (Homework or Exam): Exam

    Midterm Exam


### **Viewing the Grade Summary**

    Enter your choice (1-6): 5

    ~~~~~~~~~~~~GRADE SUMMARY~~~~~~~~~~~~

    Overall average: 90.0 %

    Subject Averages:
    English average: 90.0 %
    Mathematics average: 84.0 %

    Highest scoring assignment: Subject-Verb
    Lowest scoring assignment: Midterm Exam

---

## **Additional Notes**

### **Key Learnings**

- Applying OOP principles in Python
- Creating parent and child classes using inheritance
- Using `super()` to initialize inherited attributes
- Designing a user-friendly Command-Line Interface(CLI)
- Implementing input validation
- Managing data using custom classes and lists
- Using loops and conditionals to process assignment data
- Calculating overall and subject grade averages

### **Challenges Encountered**

- Ensuring  that the dates are entered correctly
- Preventing scores from being greater than the maximum score
- The use of the get fuctions in the program
- Filtering assignments correctly
- Calculating overall and subject averages
- Finding the highest and lowest scoring assignments
- Organizing the program using classes and inheritance

### **Future Enhancements**

- Add stronger date validation
- Allow users to edit existing assignments
- Allow users to delete assignments
- Save and load assignment data using CSV or JSON
- Improve the formatting of assignment lists
- Add automated tests
- Add more detailed grade reports

---

## **Author**

**Korkor Ndede Kojo**