def process_scores(students):
    averages={}#{["Alice"]:85+90+70/3,["David"]:95+90+93/3,["Bob"]:72+85+77/3}
    for name,score in students.items():
        if(len(score)>0):
            avg=sum(score)/len(score)#85+90+70/3---->95+90+93/3---->72+85+77/3
            averages[name]=round(avg,2)#averages["Alice"]=85+90+70/3---->
        else:
            averages[name]=0.00
    return averages
        
def classify_grades(averages):
    classified={}
    for name,avg in averages.items():
        if(avg>=90.00):
            grade="A"
        elif(avg>=75.00):
            grade="B"
        elif(avg>=60.00):
            grade="C"
        else:
            grade="F"
        classified[name]=(avg,grade)            
    return classified

def generate_report(classified,passing_avg=70):
    print("===== Student Grade Report =====")
    pass_count=0
    for name,(avg,grade) in classified.items():
        if(avg>passing_avg):
            status="PASS"
            pass_count=pass_count+1
        else:
            status="FAIL"
        # result[name]=(avg,grade,status)
        print(f"{name:<10} | Avg: {avg:<6} | Grade: {grade} | Status: {status}")
        # print(f"{name}  | Avg:  {avg}  | Grade: {grade}  | Status: {status}")
    total_students=len(classified)
    passed_students=pass_count
    failed_students=total_students-passed_students
    print(f"Total Students      : {total_students}")
    print(f"Passed              : {passed_students}")
    print(f"Failed              : {failed_students}")

students = {"Alice":[85,90,70],"David":[95,90,93],"Bob":[72,85,77]}
averages = process_scores(students)
grades=classify_grades(averages)
generate_report(grades,75)


# print(averages)
# print(grades)

