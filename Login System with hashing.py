import time, csv, hashlib

login_Array=[]

def read_csv():
    file=open("Login system\\login.csv" ,"r")
    file_reader=csv.reader(file)

    for row in file_reader:
        login_Array.append(row)
    file.close()

    
def csv_create():
    file=open("Login system\\login.csv","w",newline="")
    csv_writer=csv.writer(file)
    for i in login_Array:
        csv_writer.writerow(i)
    file.close()


def login(username,password):

    username_flag=False
    hash=hashlib.md5(password.encode())
    password=hash.hexdigest()
    
    for i in range(len(login_Array)):

        
        if username==login_Array[i][0]:
            print("Username Found.")
            username_flag=True
            if password==login_Array[i][1]:
                print("Welcome", username)
                return True
            else:
                print("Password Incorrect")
                timer=10
                counter=0
                while password != login_Array[i][1]:
                    counter+=1
                    password=input("Password:")

                    if counter >2:
                        print("You are locked out for ",timer,"Seconds.")
                        time.sleep(timer)
                        timer=timer*2

                    password=input("Password:")
                    hash=hashlib.md5(password.encode())
                    password=hash.hexdigest()
                return True 
        
                    



        if username_flag==False:
            print("Username not found")
            return  False

        return False


def create_account():
    username=input("Please enter a unqiue username:")
    flag=False
    for i in range (len(login_Array)):
        if username.upper()==login_Array[i][0].upper():
            print("Username already exists")
            flag=True

        if flag==False:
            print("Username Accepted.")
            password=input("Please enter a password:")
            while len(password)<8:
                print("Please enter a password with at least 8 characters.")
                password=input("Please enter a password")
            hash=hashlib.md5(password.encode())
            password=hash.hexdigest()

            temp=[username,password]
            login_Array.append(temp)

            file=open("Login system\\login.csv","a",newline="")
            csv_writer=csv.writer(file)
            csv_writer.writerow(temp)
            file.close()
            
            
        else:
            create_account()



        

def menu():
    print("****** Welcome to the Sanjot login system! ******")
    print()
    print(" 1.) Login \n 2.) Create an Account" )
    pick=input("...")
    if pick =="1":
        while flag==False:
            username=input("Username:")
            password=input("Password:")
            flag=login(username,password)


    if pick=="2":
        create_account()


    #change account details

read_csv()
menu()

flag=False

while flag==False:

    username=input("Username:")
    password=input("Password:")
    flag=login(username,password)
