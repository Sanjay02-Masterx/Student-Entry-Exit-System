import datetime

while True:
    print("\n----- Hostel Entry-Exit System -----")
    print("1. Add Student")
    print("2. Entry / Exit")
    print("3. View Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        department = input("Enter Department: ")

        file = open("data.txt", "a")
        file.write(student_id + "," + name + "," + department + "\n")
        file.close()

        print("✅ Student added successfully")

    elif choice == "2":
        student_id = input("Enter Student ID: ")
        status = input("Enter status (IN/OUT): ").upper()
        time = datetime.datetime.now()

        file = open("data.txt", "a")
        file.write(student_id + "," + status + "," + str(time) + "\n")
        file.close()

        print("✅ Entry/Exit recorded")

    elif choice == "3":
        print("\n📄 All Records:\n")

        file = open("data.txt", "r")
        for line in file:
            print(line.strip())
        file.close()

    elif choice == "4":
        print("👋 Exiting ...")
        break

    else:
        print("❌ Invalid choice! Please select 1–4.")
