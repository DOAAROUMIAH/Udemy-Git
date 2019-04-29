grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}


def students_names(grade) :
    return grade.keys()

def students_score(grade, name) :
    return grade.get(name, "Student not found")

def student_count(grade) :
    return len(grade)

def StringToDict (str) :
    if str=="grade_one" :
        return grade_one
    elif str=="grade_two" :
        return grade_two
    else :
         return grade_three

OnOff=True

while OnOff==True :

 fun=input("Choose one: students_names, student_score, student_count : ")

 if fun=="students_names" :
     grd=input("Enter the class name: ")
     print(students_names(StringToDict(grd)))

 elif fun=="student_score" :
        grd=input("Enter the class name: ")
        name=input("Enter the student name: ")
        print(students_score(StringToDict(grd), name))

 elif fun=="student_count" :

        grd=input("Enter the class name: ")
        print(student_count(StringToDict(grd)))

 else :
        print("This function does not exist!")

 order=input("Enter done to exit or more to continue: ")
 if order=="done" :
     OnOff=False
     exit()
