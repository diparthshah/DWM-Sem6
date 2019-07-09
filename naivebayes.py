age = ["<=30", "<=30", "31to40", ">40", ">40", ">40", "31to40", "<=30", "<=30", ">40", "<=30", "31to40", "31to40", ">40"]
student = ["n","n","n","n","y","y","y","n","y","y","y","n","y","n"]
cl = ["n","n","y","y","y","n","y","n","y","y","y","y","y","n"]
income=["high","high","high","med","low","low","low","med","low","med","med","med","high","med"]
credit=["fair","excel","fair","fair","fair","excel","excel","fair","fair","fair","excel","excel","fair","excel"]
n = 14
pyes = cl.count("y")
pno = cl.count("n")
p_age_l30_yes = 0
p_age_l30_no = 0
p_age_g40_yes = 0
p_age_g40_no = 0
p_age_3140_yes = 0
p_age_3140_no = 0
for i in range(0,n):
    if(age[i]=="<=30" and cl[i]=="y"):
        p_age_l30_yes = p_age_l30_yes + 1
    elif(age[i]=="<=30" and cl[i]=="n"):
        p_age_l30_no = p_age_l30_no + 1
    elif(age[i]==">40" and cl[i]=="y"):
        p_age_g40_yes = p_age_g40_yes + 1
    elif(age[i]==">40" and cl[i]=="n"):
        p_age_g40_no = p_age_g40_no + 1
    elif(age[i]=="31to40" and cl[i]=="y"):
        p_age_3140_yes = p_age_3140_yes + 1
    elif(age[i]=="31to40" and cl[i]=="n"):
        p_age_3140_no = p_age_3140_no + 1
p_age_l30_yes = p_age_l30_yes / pyes
p_age_l30_no =  p_age_l30_no / pno
p_age_g40_yes = p_age_g40_yes/ pyes
p_age_g40_no = p_age_g40_no / pno
p_age_3140_yes = p_age_3140_yes / pyes
p_age_3140_no = p_age_3140_no / pno

p_income_high_yes = 0
p_income_high_no = 0
p_income_med_yes = 0
p_income_med_no = 0
p_income_low_yes = 0
p_income_low_no = 0
for i in range(0,n):
    if(income[i]=="high" and cl[i]=="y"):
        p_income_high_yes = p_income_high_yes + 1
    elif(income[i]=="high" and cl[i]=="n"):
        p_income_high_no = p_income_high_no + 1 
    elif(income[i]=="med" and cl[i]=="y"):
        p_income_med_yes = p_income_med_yes + 1
    elif(income[i]=="med" and cl[i]=="n"):
        p_income_med_no = p_income_med_no + 1
    elif(income[i]=="low" and cl[i]=="y"):
        p_income_low_yes = p_income_low_yes + 1
    elif(income[i]=="low" and cl[i]=="n"):
        p_income_low_no = p_income_low_no + 1

p_income_high_yes = p_income_high_yes/ pyes
p_income_high_no = p_income_high_no / pno
p_income_med_yes = p_income_med_yes / pyes
p_income_med_no = p_income_med_no / pno
p_income_low_yes = p_income_low_yes /pyes
p_income_low_no = p_income_low_no /pno

p_stu_yes_yes = 0
p_stu_yes_no = 0
p_stu_no_yes = 0
p_stu_no_no = 0

for i in range(0,n):
    if(student[i]=="y" and cl[i]=="y"):
        p_stu_yes_yes = p_stu_yes_yes + 1
    elif(student[i]=="y" and cl[i]=="n"):
        p_stu_yes_no = p_stu_yes_no  + 1
    elif(student[i]=="n" and cl[i]=="y"):
        p_stu_no_yes = p_stu_no_yes + 1
    elif(student[i]=="n" and cl[i]=="n"):
        p_stu_no_no = p_stu_no_no + 1

p_stu_yes_yes = p_stu_yes_yes / pyes
p_stu_yes_no = p_stu_yes_no / pno
p_stu_no_yes = p_stu_no_yes / pyes
p_stu_no_no = p_stu_no_no / pno

p_credit_fair_yes = 0
p_credit_fair_no = 0
p_credit_excel_yes = 0
p_credit_excel_no = 0

for i in range(0,n):
    if(credit[i]=="fair" and cl[i]=="y"):
        p_credit_fair_yes = p_credit_fair_yes + 1
    elif(credit[i]=="fair" and cl[i]=="n"):
        p_credit_fair_no = p_credit_fair_no + 1
    elif(credit[i]=="excel" and cl[i]=="y"):
        p_credit_excel_yes = p_credit_excel_yes + 1
    elif(credit[i]=="excel" and cl[i]=="n"):
        p_credit_excel_no = p_credit_excel_no + 1

p_credit_fair_yes = p_credit_fair_yes / pyes
p_credit_fair_no = p_credit_fair_no / pno
p_credit_excel_yes = p_credit_excel_yes / pyes
p_credit_excel_no = p_credit_excel_no / pno

pyes = pyes / n
p_x_yes = p_age_l30_yes * p_income_med_yes * p_stu_yes_yes * p_credit_fair_yes * pyes
print("Class label value when YES: ",p_x_yes)
pno = pno / n
p_x_no = p_age_l30_no * p_income_med_no * p_stu_yes_no * p_credit_fair_no * pno
print("Class label value when NO: ",p_x_no)

if(p_x_yes > p_x_no):
    print("Class Label is Yes")
else:
    print("Class Label is No")
"""
E:\dwm>python naivebayes.py
Class label value when YES:  0.028218694885361547
Class label value when NO:  0.006857142857142858
Class Label is Yes
"""
