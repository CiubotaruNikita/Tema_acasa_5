names = input("Introduceți lista de nume, separate prin virgulă: ")
list_of_names = names.split(",")
list_of_marks = []
for name in list_of_names:
    mark = int(input(f"Introduceți nota pentru elevul {name}: "))
    list_of_marks.append(mark)
marks_sum = 0
for mark in list_of_marks:
    marks_sum += mark
for i in range(len(list_of_names)):
    name = list_of_names[i]
    mark = list_of_marks[i]
    print(f"Nota pentru {name}: {mark}")
print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / len(list_of_marks)}")