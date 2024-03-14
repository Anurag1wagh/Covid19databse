
import mysql.connector as connector

conn = connector.connect(host="localhost", user = "root", password = "admin123")
cur = conn.cursor()

#cur.execute("show databases")
#results = cur.fetchall()yes

#cur.execute("create database phone_directory")
cur.execute("use covid_19database")
#cur.execute("create table directory(ID bigint(10), First_Name varchar(45), Last_Name varchar(45), Phone_Number bigint(10), Alternate_Phone_Number bigint(10), Permanent_Address varchar(45))")

while True:
        print("")
        print("Welcome covid data base")
        print("")
        print("1. Inserting user information")
        print("2. Deleting user information")
        print("3. Updating user information")
        print("4. Exit")
        print("")

        user_choice = input(str("Selecting option: "))
        if user_choice == "1":

            ab = 0
            inserting_val = int(input("Enter your name: "))
            if inserting_val == 0:
                pass
            else:
                while ab < inserting_val:
                    inserting_val-= 1
                    
                    i_d = input("Enter ID number: ")
                    first_name = input("Enter the first name: ")
                    last_name = input("Enter the last name: ")
                    phone_number = input("Enter the phone number: ")
                    alt_phone_number = input("Enter an alternate phone number: ")
                    per_address = input("Enter permanent address: ")
                                                           
                    cur.execute(f"insert into covid-19 database({i_d},'{first_name}','{last_name}',{phone_number},{alt_phone_number},'{per_address}')")
                    cur.execute("select * from phone_directory.directory")
                    
                    e = cur.fetchall()
                    print(e)
                    conn.commit()
                    
            cur.execute("select * from phone_directory.directory")        
            file = cur.fetchall()
            print(file)


        elif user_choice == "2":

            known = 0
            deleting_val = int(input("How many user you want to delete: "))
            if deleting_val == 0:
                pass
            else:
                while known < deleting_val:
                    deleting_val-= 1
                    i_d = input("Enter the ID number of the contact you want to delete: ")
                    
                    cur.execute(f"delete from covid-19database.database where id = {i_d}")
                    cur.execute("select * from covid-19database.database")
                    e = cur.fetchall()
                    print(e)
                    conn.commit()
                    

        elif user_choice == "3":
            
            i_d = int(input("Enter the ID number of contact you want to update: "))
            cur.execute(f"select * from covid-19database.database where id = {i_d}")
            fetch1= cur.fetchone()
            print(fetch1)
            print("Select what you want to update: ")
            print("1. Phone Number")
            print("2. Alternate Phone Number")
            print("3. Permanent Address")

            update_choice = input(str("Selecting option: "))
            if update_choice == "1":
                phone_val = int(input("Enter the new phone number you want to update: "))
                cur.execute(f"Update covid-19database.database set phone_number = {phone_val} where id = {i_d}")
                cur.execute("select * from phone_directory.directory")
                e = cur.fetchall()
                print(e)
                conn.commit()
            
            elif update_choice == "2":
                alt_phone_val = int(input("Enter the new alternate phone number you want to update: "))
                cur.execute(f"Update covid-19database.database set alternate_phone_number = {alt_phone_val} where id = {i_d}")
                cur.execute("select * from phone_directory.directory")
                e = cur.fetchall()
                print(e)
                conn.commit()

            elif update_choice == "3":
                per_address_val = str(input("Enter the new permanent address you want to update: "))
                cur.execute(f"Update covid-19database.database set permanent_address = '{per_address_val}' where id = {i_d}")
                cur.execute("select * from covid-19database.database")
                e = cur.fetchall()
                print(e)
                conn.commit()
            
            else:
                print("Unknown command")

        
        elif user_choice == "4":
            break
        else:
            print("Invalid option")