# B. Create a console application for an IT Academy with the
# following features:
# a) The academy program should have a fixed course of study.
# b) If a new student is interested in the academy program the student can inquiry about the course of study.
# c) Student Registration with Rs. 20000 (deposit). Students are allowed to pay in two installments with Rs. 10000 each.
# d) Display all the student’s information from the academy with their payments and remaining payments.
# e) Update the student information if needed.
# f) Delete the student information if he/she left the program.
# g) Return the deposit amount to the students after the successful completion of the course and check the balance.
# Remember it should be a full feature CONSOLE APP. You can store the course of study and the student’s detail in your
# preferred file format. Ignore the permissions for now.
# Anyone who runs the script is allowed to access all the features.
# Develop the app with OOP Approach.


import csv
import pandas as pd


class Academy:

    def displayTitle(self):
        print("\t**********************************************")
        print("\t******  Welcome to Learner's Academy!  *******")
        print("\t**********************************************")
        print("\n")
        print("\t******************  NOTE  *******************")
        print("\t** user's phone number is being used as id **")

    def repeatService(self):
        service = input('Do you want to continue with our service ? [y/n] : ')
        if service == 'n':
            return 'q'

    def displayCourse(self):
        with open('courses.csv', mode='r') as csv_file:
            read = pd.read_csv(csv_file)
            print(read)

    def recordEntry(self):
        name = input('enter name: ')
        phone = input('enter phone number: ')
        course = input('enter course you want to enroll in: ')
        payment = input('How much will you pay in advance? [Minimum amount 10000] : ')
        due = 20000 - int(payment)
        duplicate = 0
        refund = 0
        with open('students.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for item in reader:
                if item['Name'].upper() == name.upper() and item['Phone'] == phone and item['Course'].upper() == course.upper():
                    duplicate += 1

        if duplicate == 0:
            with open('students.csv', 'a+', newline='') as csv_write:
                writer = csv.writer(csv_write)
                writer.writerow(([name, phone, course, payment, due, refund]))
        else:
            reconfirm = input(
                'We have record present with same bio in this course, do you want to edit your information? [y/n]: ')
            if reconfirm == 'y':
                Academy().recordEntry()
            elif reconfirm == 'n':
                print("Thank you for taking out services")

    def displayRecord(self):
        number = input('Enter your phone number to display information associated with it : ')
        with open('students.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for item in reader:
                if item['Phone'] == number:
                    print(f"Name : {item['Name']}")
                    print(f"Course Enrolled : {item['Course']}")
                    print(f"Course Deposit  : {item['Payment']}")
                    print(f"Due Deposit : {item['Due Payment']}")
                    print('\n**********************************\n')
                    break
                else:
                    reconfirm = input('No account associated with provided number. Try again? [y/n]')
                    if reconfirm == 'y':
                        Academy().displayRecord()
                    else:
                        print("Thank you for taking out services")
                        break

    def deleteRecord(self):
        record = list()
        members = input("Please enter the name of student dropping out.")
        with open('students.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                record.append(row)
                for field in row:
                    if field == members:
                        record.remove(row)

        with open('students.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(record)

    def updateRecord(self):
        old_record = list()
        record = list()
        contact = input("Please enter the phone number of student whose data you wanna change : ")
        change_option = input("Enter 'N' to change name and 'C' to change course : ")
        if change_option == 'N':
            new_name = input('What is the name you wanted to change to : ')
            with open('students.csv', mode='r') as csv_file:
                read = csv.DictReader(csv_file)
                for field in read:
                    if field['Phone'] != contact:
                        old_record.append(field.values())
                    else:
                        field['Name'] = new_name
                        record.append(field.values())

        elif change_option == 'C':
            new_name = input('What is the course you want to switch to')
            with open('students.csv', mode='r') as csv_file:
                read = csv.DictReader(csv_file, delimiter=',')
                for field in read:
                    if field['Phone'] != contact:
                        old_record.append(field.values())
                    else:
                        field['Course'] = new_name
                        record.append(field.values())
        record.extend(old_record)
        with open('students.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow((['Name', 'Phone', 'Course', 'Payment', 'Due Payment']))
            writer.writerows(record)

    def complete(self):
        old_rec = []
        new_rec = []
        contact = input("Please enter your phone number : ")
        init = 0
        refund = 2000
        with open('students.csv', mode='r') as csv_file:
            read = csv.DictReader(csv_file, delimiter=',')
            for field in read:
                if field['Phone'] != contact:
                    old_rec.append(field.values())
                else:
                    field['Payment'] = init
                    field['Due Payment'] = init
                    field['Refund'] = refund
                    new_rec.append(field.values())

        new_rec.extend(old_rec)
        with open('students.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow((['Name', 'Phone', 'Course', 'Payment', 'Due Payment', 'Refund']))
            writer.writerows(new_rec)


choice = ''
Academy().displayTitle()

while choice != 'q':

    # Let users know what they can do.
    print("\n[Enter 1] To Display courses of study")
    print("[Enter 2] To Display existing student information")
    print("[Enter 3] To Add new student information")
    print("[Enter 4] To update student information")
    print("[Enter 5] To drop from the course ")
    print("[Enter c] To inform about completion of course ")
    print("[Enter q] To Quit")

    choice = input("Please select the service you like to take :  ")

    # Respond to the user's choice.
    if choice == '1':
        print("\nHere are the courses offered.\n")
        Academy().displayCourse()
        choice = Academy().repeatService()
    elif choice == '2':
        print("\nHere is the student information\n")
        Academy().displayRecord()
        choice = Academy().repeatService()
    elif choice == '3':
        print("\nPlease add student information\n")
        Academy().recordEntry()
        choice = Academy().repeatService()
    elif choice == '4':
        print("\nPlease add student information\n")
        Academy().updateRecord()
        choice = Academy().repeatService()
    elif choice == '5':
        print("\nPlease add student information\n")
        Academy().deleteRecord()
        choice = Academy().repeatService()
    elif choice == 'c':
        print("\nCongratulation on completion. Please check if your deposit has been refunded\n")
        Academy().complete()
        choice = Academy().repeatService()
    elif choice == 'q':
        print("\nThanks for taking our services. Bye.")
    else:
        print("\nI didn't understand that choice.\n")
        choice = Academy().repeatService()
