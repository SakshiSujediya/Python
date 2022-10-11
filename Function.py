#Basic python function
from os import makedirs


def Nanna():
     print("Nanna learn python")
     print("Also use slowlearn app for learning")

Nanna()
 
 #Add Numbers
def add_no(n1,n2):
     result = n1+n2
     print("The sum is",result)

num1=10
num2=15

add_no(num1,num2)

#Function to find average marks
def find_average_marks (marks):
     sum_of_marks = sum(marks)
     Total_no_of_subject = len(marks)
     average_marks= sum_of_marks / Total_no_of_subject
     return average_marks

#find the grade of student
def grade_marks(average_marks):
   if average_marks >= 80:
     grade ='A'
   elif average_marks >=60:
      grade ='b'
   elif average_marks >=50:
       grade='c'
   else:
      grade ='F'
      return grade

marks = [70,80,100,80,90]
average_marks = find_average_marks(marks)
print("your average marks is",average_marks)

grade =grade_marks(average_marks)
print("your grade is",grade)

