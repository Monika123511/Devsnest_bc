stud_grades=[]
for _ in range(int(input("Enter the range:"))):
        name = input("Enter the name:")
        score = float(input("Enter the score:"))
        stud_grades.append([name,score])
sorted_scores=sorted(list(set([x[1] for x in stud_grades])))
second_lowest=sorted_scores[1]
low_final_list=[]
for student in stud_grades:
        if second_lowest==student[1]:
                low_final_list.append(student[0])
for student in sorted(low_final_list):
        print(student)
