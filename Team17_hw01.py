'''
Jared Vreeland
Amelia McIe
Jonathon Moss
Kelsea McGraw

Dr. Alomari
CSE211

This program will take a text file "studentGrades.txt" and process the information in order to 
return a "studentGradesFinal.txt" containing just the students last names, the course average, and 
the final letter grade.

Python Version 3.7

'''
import os
import sys
'''
read_file


This will read a file, split it by lines, then return the list of strings

Args:
Returns:
    list: A list of strings containing by element:
        0: student last name
        1-4: quiz grades 1-3
        4-8: homework grades 1-4
        8-9: exams 1-2
'''
def read_file():
    with open(os.path.join(sys.path[0], "studentGrades.txt")) as student_file:
        file_data = student_file.read()
        unprocessed_students = file_data.split('\n')
    return unprocessed_students

'''
write_file

This will format the output, given by a dictionary of students, and print it into a file, studentGradesFinal.txt

Args:
    param1 (dict): A dictionary containing:
        key:     'studentName'
        value    [course_avg, course_letter_grade]
Returns:
    none
'''
def write_file(student_dictionary):
    output_file = open('studentGradesFinal.txt', 'w')
    for student, grades in student_dictionary.items():
        student_string = "{:>20}{:5.1f} {:.1}".format(student, grades[0], grades[1])
        output_file.write(student_string)
        output_file.write('\n')
    output_file.close()

'''
process_students

This will take a list of student strings, from read_file, and split them into a list containing 4 elements,
name, list of quiz grades, list of homework grades, and a list of exam grades.

Args:
    param1 (list): A list containing strings formatted like:
        'Alomari  67  76  56  88  85  76  99  88  77  66'
Returns:
    A list containing:
        list[1]     'student_name'
        list[2]    [quiz_grade_1, quiz_grade_2, quiz_grade_3]
        list[3]    [homework_grade_1, homework_grade_2, homework_grade_3, homework_grade_4]
        list[4]    [exam_grade_1, exam_grade_2]
'''
def process_students(list_student):
    
    """ Take list of student strings and split into a list
        containing 4 elements: student name, quiz grades,
        hw grads, exam grade"""
    processed_students = []
    for student_string in list_student:
        temp_student = student_string.split()
        processed_students.append([
            temp_student[0],          #Student name
            temp_student[1:4],        #Quiz scores
            temp_student[4:9],        #HW Scores
            temp_student[9:]          #Exam Scores
            ])
    return processed_students

'''
get_average
This will take a list of grades and return the average

Args:
    param1 (list): Grades in type (str)
    
Returns:
    Float: Average grade
'''
def get_average(list_grade):
    #Take list of student grades as string, cast as int, take average, return float
    grades = []
    for grade in list_grade:
        grades.append(int(grade))
    total_grade = sum(grades)
    average = float(total_grade/len(grades))
    return average

'''
get_course_average

This will take the quiz, hw, and exam average, weigh them appropriately, then return the overall grade

Args:
    param1 (float): quiz_avg
    param2 (float): hw_avg
    param3 (float): exam_avg
    
Returns
    Float: weighted_grade
'''
def get_course_average(quiz_avg, hw_avg, exam_avg):
    weighted_exam = exam_avg * .5
    weighted_quiz = quiz_avg * .2
    weighted_hw = hw_avg * .3
    return (weighted_exam + weighted_hw + weighted_quiz)

'''
get_letter_grade

Given a course average, return the letter grade associated

Args:
    param1 (float): course_avg

Returns
    Str: letter_grade
'''
def get_letter_grade(course_avg):
    if(course_avg < 60):
        return 'F'
    elif(course_avg < 63):
        return 'D-'
    elif(course_avg < 67):
        return 'D'
    elif(course_avg < 70):
        return 'D+'
    elif(course_avg < 73):
        return 'C-'
    elif(course_avg < 77):
        return 'C'
    elif(course_avg < 80):
        return 'C+'
    elif(course_avg < 83):
        return 'B-'
    elif(course_avg < 87):
        return 'B'
    elif(course_avg < 90):
        return 'B+'
    elif(course_avg < 93):
        return 'A-'
    elif(course_avg < 97):
        return 'A'
    else:
        return 'A+'

def main():
#     file_name = input("Input the full directory path to your studentGrades.txt file\n")
#     unprocessed_students = read_file(file_name)
    unprocessed_students = read_file()
    processed_students = process_students(unprocessed_students)
    student_dict = {}
    for student in processed_students:
        name = student[0]
        quiz_avg = get_average(student[1])
        hw_avg = get_average(student[2])
        exam_avg = get_average(student[3])
        course_avg = round(get_course_average(quiz_avg, hw_avg, exam_avg), 1)
        letter_grade = get_letter_grade(course_avg)
        student_dict[name] = [course_avg, letter_grade]
    write_file(student_dict)
    print('Done')
    
if __name__ == "__main__":
    main()
        
    
    