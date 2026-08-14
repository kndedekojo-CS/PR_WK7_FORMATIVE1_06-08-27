# ***Student Grade / Assignment Tracker**

## **Project Overview**
This Student Grade / Assignment Tracker was developed as part of the ** Week 7 Formative Assessment for Programming 1.**

The task involved building a menu-driven Python program that allows students to:

# *Record homework and exam assignments
 *View all recorded assignments
 _
 *Filter assignments based on different criteria
 *Generate a grade summary

The project demonstrates key programming concepts taught in class, including:

 *Functions
 *Loops and conditionals
 *Input validation
 *Collections
 *Object-Oriented Programming (OOP)
 *Inheritance

The program runs entirely in the terminal and stores assignment information in memory while the program is running. The menu-driven structure allows users to manage and review their assignments within a single session.

## **Key Features**
- **Add Assignments**
   -Add Homework
   -Add Exam
- **Store Assignment Information**
   -Subject
   -Assignment title
   -Score received
   -Maximum score
   -Due date
   -Assignment type
- **List All Assignments** in a clear and formatted view
   -Filter Assignments by:
   -Subject
   -Assignment type
   -Month and year
- **View Grade Summary** including:
   -Overall average
   -Average for each subject
   -Highest-scoring assignment
   -Lowest-scoring assignment
- **Input Validation** for:
   -Negative scores
   -Non-numeric scores
   -Empty text inputs
   -Scores greater than the maximum score
- **OOP Design** using:
   -'Assignment'
   -'Homework'
   -'Exam'
   -GradeTracker
- **Inheritance** is used so that Homework and Exam inherit common information from the Assignment parent class.

## **How to Run the Program**

###  *1. Ensure Python 3 is installed*
   Check that Python is installed by running:
    python --version

###  *2. Clone the project repository*
   Clone the project from GitHub:
    git clone (https://github.com/kndedekojo-CS/PR_WK7_FORMATIVE1_06-08-27)

###  *3. Navigate into the project directory*
    cd PR_WK7_FORMATIVE1_06-08-27

###  *4. Run the program*
    Run the Python file:
      python main.py

5. Follow the on-screen menu instructions



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

    git clone YOUR_GITHUB_REPOSITORY_URL

### **3. Navigate into the project directory**

    cd YOUR_PROJECT_FOLDER

### **4. Run the program**

    python YOUR_PYTHON_FILE.py

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

    Enter the subject: Programming
    Enter the title of the homework: Python Classes
    Enter the score received: 18
    Enter the maximum score: 20
    Enter the due date (dd/mm/yyyy): 15/08/2026

    Homework added successfully!

### **Viewing All Assignments**

    Enter your choice (1-6): 3

    ~~~~~~~~~~~~LIST OF ALL ASSIGNMENTS~~~~~~~~~~~~

    Subject: Programming
    Title: Python Classes
    Score: 18.0/20.0
    Due Date: 15/08/2026
    Type: Homework

### **Viewing the Grade Summary**

    Enter your choice (1-6): 5

    ~~~~~~~~~~~~GRADE SUMMARY~~~~~~~~~~~~

    Overall average: 90.0 %

    Subject Averages:
    Programming average: 90.0 %

    Highest scoring assignment: Python Classes
    Lowest scoring assignment: Python Classes

---

## **Additional Notes**

### **Key Learnings**

- Applying OOP principles in Python
- Creating parent and child classes using inheritance
- Using `super()` to initialise inherited attributes
- Designing a user-friendly CLI interface
- Implementing input validation
- Managing data using custom classes and lists
- Using loops and conditionals to process assignment data
- Calculating overall and subject grade averages

### **Challenges Encountered**

- Ensuring scores are entered correctly
- Preventing scores from being greater than the maximum score
- Handling invalid menu selections
- Filtering assignments correctly
- Calculating overall and subject averages
- Finding the highest and lowest scoring assignments
- Organising the program using classes and inheritance

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