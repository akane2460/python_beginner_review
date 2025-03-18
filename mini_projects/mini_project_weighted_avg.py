# Python Tutorial for Beginners: Episode 8, Mini Project
# Weighted Exam Score Average

# How many exams have you done
number_of_exams = int(input("Enter number of exams:"))
    # takes integer input and sets equal to number_of_exams

# How many credits these exams cover
total_credits = int(input("Enter how many credits these exams cover:"))

# for loop
## set the initial average to equal 0 and then add up the percentages from each exam
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam score:"))
    exam_credits = int(input("Enter how many exam credits this exam covered:"))
    average = average + (score*exam_credits/total_credits)
print("Your average is", average)