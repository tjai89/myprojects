#это словарь студентов

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
#эта функция считает среднюю оценку для каждого студента по разным пунктам
def average (number):
    total = sum(number)
    total = float(total)
    total = total/len(number)
    return total
#Эта функция присваивает приоритет каждому пункту и выдает общую оценку по всем 3-м пунктам    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1*homework+0.3*quizzes+0.6*tests
#Эта функция просчитывает балл, присваиваемый результату    
def get_letter_grade (score):
    score = float(score)
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
        
#Выдает на консоль оценки каждого студента
print "Grade %s."% get_letter_grade(get_average(lloyd))
print "Grade %s."%get_letter_grade(get_average(alice))
print "Grade %s."%get_letter_grade(get_average(tyler))
#Функция считает среднюю оценку всего класса
def get_class_average (students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
#Список студентов    
students = [lloyd,alice,tyler] 

print "Average of the class is %s."%get_class_average(students)
print "Middle grade of all class is %s."%get_letter_grade(get_class_average(students))
