from secrets import choice


seats = []
seats.append([0,0,1,1,0,1,1,1])
seats.append([0,1,1,0,0,1,0,1])
seats.append([1,0,0,1,0,1,1,0])
seats.append([0,1,1,1,0,0,0,1])
seats.append([0,0,1,1,0,1,0,0])
seats.append([1,0,1,1,0,0,1,1])


def displayBookings():
    print("")
    print("==============================")
    print("")
    for row in seats:
        print(row)
    print("")
    print("==============================")

def checkSeat():
    booked = False
    while booked == False:
        row = int(input("Please enter a row number from 0-5"))
        column = int(input("Please enter a column number between 0-7"))
    
        if seats[row][column]==1:
            print("Sorry, this seat is already booked.")
        else:
            print("This seat is empty.")
            print("Processing booking...")
            seats[row][column]=1
            print("Seat has been sucessfully booked.")
            booked = True


def frontbooking():
    print("Booking seat at the front")
    for row in range(0,6):
        for column in range(0,8):
            if seats[row][column]==0:
                print("Processing Booking...")
                print("Row: " + str(row))
                print("Column: " + str(column))
                print("Seat has been succesfully booked.")

                return True
            print("Sorry the cinema is full, can not book a seat.")
            return False

def backbooking():
    print("Booking seat at the back")
    for row in range(5,-1,-1):
        for column in range(7,-1,-1):
            if seats[row][column]==0:
                print("Booking is processing...")
                print("Row: " + str(row))
                print("Column: " + str(column))
                seats[row][column]=1
                print("Seat has been succesfully booked")

                return True

            print("Sorry Cinema is full, booking cannot be processed")
            return False


print("=======================================")
print("This is the cinema booking system")
print("=======================================")
print("")
print("Please choose one of the following options:")
print("Option 1 - Book a seat by row/column")
print("Option 2 - book at the front")
print("Option 3 - book a seat at the back")


choice = input("Please enter the option you want to use.")
if choice=="1":
    checkSeat()
    displayBookings()
elif choice=="2":
    frontbooking()
    displayBookings()
elif choice=="3":
    backbooking()
    displayBookings()


    


