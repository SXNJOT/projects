import csv
employees=[]
#salary=float(input("How much do you earn?"))

def tax_func (salary):

    if salary <= 12570:

        tax=0

    elif salary <= 50270:

        tax_salary=salary-12570

        tax = tax_salary*.2

 

    elif salary <= 150000:

        higher_rate= salary - 50270

        higher_tax=higher_rate*.4

 

        basic_rate=50270-12570

        basic_tax=basic_rate*.2

 

        tax=higher_tax+basic_tax

 

    else:

        additional_rate=salary-150000

        additional_tax=additional_rate*.45

 

        higher_rate= 150000 - 50270

        higher_tax=higher_rate*.4

 

        basic_rate=50270-12570

        basic_tax=basic_rate*.2

 

        tax=additional_tax+higher_tax+basic_tax

 

    return tax

#def student_financer(salary):

    student_threshold=2274*12

    student_payment=(salary-student_threshold)*.09

 

    return student_payment

def national_insurance(salary):

    lower=1048.01*12

    higher=4189*12

 

    if salary <= lower:

        ni=0

    elif salary <= higher:

        ni=(salary-lower)*.12

    elif salary > higher:

        ni_lower = (higher-lower)*.12

        ni_higher= (salary-higher)*.02

        ni=ni_lower+ni_higher

   

    return ni

def pension (salary):

    pension=0

 

    if salary >= 84194.99:

        pension=salary*.117

    elif salary >= 61743.99:

        pension=salary*.113

    elif salary >= 46586.99:

        pension=salary*.096

    elif salary >= 39291:

        pension=salary*.086

    elif salary >= 29188:

        pension=salary*.086

    else:

        pension=salary*.074

   

    return pension

def payslip(salary,name):

    tax_amount=tax_func(salary)
    n1_amount=national_insurance(salary)
    sf_amount=student_financer(salary)
    pension_amount=pension(salary)

    tax_amount=round(tax_amount/12,2)
    n1_amount=round(n1_amount/12,2)
    sf_amount=round(sf_amount/12,2)
    pension_amount=round(pension_amount)

    takehome=salary-tax_amount-n1_amount-sf_amount-pension_amount
    takehome=round(takehome/12,2)
    print("*********************************************")
    print("Name:                     ",name)
    print("Salary:                  £",salary)
    print("Tax:                     £",tax_amount)
    print("National Insurance:      £",n1_amount)
    print("Student Finance:         £",sf_amount)
    print("Pension Amount:          £",pension_amount)
    print("\n take home pay:        £",takehome,"\n")
    print("*********************************************")

def database_create():
    salary=[["Watts",45000],["Conner",10000],["Nagra",150000]]

    file=open("employee_database.csv","w", newline="")
    csv_writer=csv.writer(file)

    for i in salary:
        csv_writer.writerow(i)

    file.close()
    database_create()

def database_read():
    file=open("employee_database.csv","r")
    file_reader=csv.reader(file)

    for row in file_reader:
        employees.append(row)
    file.close()


def payslip_spawn():
    for i in employees:
        print(i)
        name=i[0]
        salary=i[1]
        print(name)
        print(salary)
        salary=int(salary)
        payslip(salary,name)


#payslip(salary)
database_read()
payslip_spawn()