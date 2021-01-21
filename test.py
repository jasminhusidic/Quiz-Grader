"""
Name: Jasmin Husidic
File: quizGrader.py
Description: A program that grades a classes quizzes.
"""

from os.path import exists
import os.path
import os

TEXT_FILE = "students.txt"

def main():
    """Calls reportGenerator to create the report text file"""
    reportGenerator()
    
def studentDictionary():
    """Creates a dictionary for each student in the text file, /n
    with an empty dictionary as the value"""
    studentDict={}
    myFile = open(TEXT_FILE, 'r')
    for line in myFile:
        line = line.lower()
        line = line.rstrip()
        line = line.replace(',','_')
        line = line.replace(' ','')
        studentDict[line] = {}
    return studentDict
        

def quizAnswers():
    """Creates a list of the correct answers from all the quizzes"""
    directoryList = os.listdir('.')
    answersList = []
    for dirItem in directoryList:
        if os.path.isdir(dirItem):
            os.chdir(dirItem)
            answers = open("answers.txt",'r')
            for line in answers:
                line = line.rstrip()
                answersList.append(line)
            os.chdir('..')
    return answersList
        
def studentAnswers():
    """Creates a list of each students answers, and sets the value of \n
    that student's dictionary to be the list of their answers"""
    directoryList = os.listdir('.')
    studentDict = studentDictionary()
    studentAnswersList = []
    for student in studentDict:
        studentAnswersList = []
        for dirItem in directoryList:
            if os.path.isdir(dirItem):
                os.chdir(dirItem)
                fileName = student
                if exists("%s.txt" %(fileName)):
                    answersFile= open("%s.txt"%(fileName),'r')
                    for line in answersFile:
                        line = line.rstrip()
                        studentAnswersList.append(line)
                        studentDict[student]= studentAnswersList
                    os.chdir('..')
    return studentDict

def quizGrader():
    """Compares the student's answers to the correct answers, \n
    and returns a dictionary of the student's score"""
    studentScoresDict = {}
    indexCounter = 0
    correctCounter = 0
    studentDict = studentAnswers()
    answersList = quizAnswers()
    for student in studentDict:       
        for item in answersList:
            if item == studentDict[student][indexCounter]:
                correctCounter += 1
            indexCounter +=1
        studentScoresDict[student] = correctCounter
        correctCounter = 0
        indexCounter = 0
    return studentScoresDict

def reportGenerator():
    """Creates a report text file using the scores of each student"""
    totalQuestions = len(quizAnswers())
    studentScoresDict = quizGrader()
    myList = []
    studentFile = open("gradeReport.txt","w")
    studentFile.write("Student Quiz Report".center(36)+"\n\n\n")
    studentFile.write("%-15s %20s %20s\n" % ("Student","Total Quiz Points","Overall Quiz %"))
    studentFile.write("-"*57+"\n")
    for student in studentScoresDict:
        correct = (studentScoresDict.get(student))
        studentName = student
        total = totalQuestions
        percent = correct / total * 100
        studentFile.write("%-15s %20d %20.3f\n" % (studentName, correct, percent)+"\n\n")
    studentFile.write("Points Possible" "%5s"%(total))
    studentFile.close()

main()
    
        
    
    
                
    
                
                
                
            
    
        
            
    
