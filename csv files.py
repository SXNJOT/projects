import csv
with open ('cars.csv', mode='w', newline='')as car_file:
    car_writer=csv.writer(car_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

    car_writer.writerow(['TH56NQM' , " 96.25"])
    car_writer.writerow(['TT51BDA' , " 63.84"])
    car_writer.writerow(['ed35pjj' , " 74.57"])
    car_writer.writerow(['DM35HMU' , " 91.46"])
    car_writer.writerow(['UX92EUS' , " 67.39"])
    car_writer.writerow(['TT51BDA' , " 34.91"])



found = False
file=open("cars.csv","r")
limit=int(input("Please enter the speed limit: "))
for line in file:
    details=line.split(",")
    speed=float(details[1])
    if speed >limit:
        found= True
        print(details[0] + ""+details[1])
if found==False:
    print("There are no speeding cars")
        

