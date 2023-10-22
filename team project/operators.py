import sqlite3
import random

def operators():
    with sqlite3.connect("User_Vehicle.db") as db:
        cursor = db.cursor()

    place = list()

    cursor.execute("SELECT place_name FROM Vehicles") 
    for x in cursor.fetchall():
        x = str(x)[str(x).find("(") + 2:-3]
        place.append(x)

    cursor.execute("SELECT vehicle_id, vehicle_type, location_x, location_y FROM Vehicles") 
    for x in cursor.fetchall():
        print("id:{}, type:{}, location: {} ({},{})".format(x[0], x[1], place[x[0] - 1], x[2], x[3]))

    print()

    status = list()

    cursor.execute("SELECT vehicle_status FROM Vehicles") 
    for x in cursor.fetchall():
        status.append(int(str(x)[str(x).find("(") + 1:str(x).find(",")]))

    if 2 in status:
        print("The list below contains the vehicle that should be repaired: ")
        cursor.execute("SELECT vehicle_id FROM Vehicles WHERE vehicle_status = 2") 
        for x in cursor.fetchall():
            print("id: {}".format(str(x)[str(x).find("(") + 1:str(x).find(",")]))
        

        cursor.execute("SELECT vehicle_id FROM Vehicles WHERE vehicle_status = 2") 
        for x in cursor.fetchall():
            id = int(input("Type the id above one by one which needs to be repaired: "))
            cursor.execute("UPDATE Vehicles SET vehicle_status = 0 WHERE vehicle_id = ?",[id])
            db.commit()
    else:
        print("There's no vehicle needs to be repaired.")

    battery = list()

    cursor.execute("SELECT battery FROM Vehicles") 
    for x in cursor.fetchall():
        battery.append(int(str(x)[str(x).find("(") + 1:str(x).find(",")]))

    if 0 in battery:
        print("The list below contains the vehicle's battery which should be charged: ")
        cursor.execute("SELECT vehicle_id FROM Vehicles WHERE battery = 0") 
        for x in cursor.fetchall():
            print("id: {}".format(str(x)[str(x).find("(") + 1:str(x).find(",")]))

        cursor.execute("SELECT vehicle_id FROM Vehicles WHERE battery = 0") 
        for x in cursor.fetchall():
            id = int(input("Type the id above one by one which needs to be charged: "))
            cursor.execute("UPDATE Vehicles SET battery = 100 WHERE vehicle_id = ?",[id])
            db.commit()
    else:
        print("There's no vehicle needs to be charged.")

    location_x = 1
    location_y = 1 

    move = input("Do you wnat to move any vehicle (y/n)? " + '\n' + 
    "You can enter the place among (Bridge Street, Buchanan Street, Cessnock, Cowcaddens, Govan, Hillhead, Ibrox, Kelvinhall, Kelvinbridge, Kinning Park)" + 
    '\n' + "If you want to move, you can type y.")
    while move == 'y':
        id = int(input("Type an vehicle id which do you want to move (from 1 to 40): "))
        move_name = input("Enter the name of the lacation: ")

        if move_name == 'Bridge Street':
            location_x = random.randint(0,101)
            location_y = random.randint(0,251)
        elif move_name == 'Buchanan Street':
            location_x = random.randint(0,101)
            location_y = random.randint(251,501)
        elif move_name == 'Cessnock':
            location_x = random.randint(101,201)
            location_y = random.randint(0,251)
        elif move_name == 'Cowcaddens':
            location_x = random.randint(101,201)
            location_y = random.randint(251,501)
        elif move_name == 'Govan':
            location_x = random.randint(201,301)
            location_y = random.randint(0,251) 
        elif move_name == 'Hillhead':
            location_x = random.randint(201,301)
            location_y = random.randint(251,501)
        elif move_name == 'Ibrox':
            location_x = random.randint(301,401)
            location_y = random.randint(0,251)
        elif move_name == 'Kelvinhall':
            location_x = random.randint(301,401)
            location_y = random.randint(251,501)
        elif move_name == 'Kelvinbridge':
            location_x = random.randint(401,501)
            location_y = random.randint(0,251)
        elif move_name == 'Kinning Park':
            location_x = random.randint(401,501)
            location_y = random.randint(251,501)      
        cursor.execute("UPDATE Vehicles SET location_x = ?, location_y = ?, place_name = ? WHERE vehicle_id = ?",[location_x, location_y, move_name, id])
        db.commit()
        move = input("Do you wnat to move any other vehicle (y/n)? ")

    print()

    place = list()
    cursor.execute("SELECT place_name FROM Vehicles") 
    for x in cursor.fetchall():
        x = str(x)[str(x).find("(") + 2:-3]
        place.append(x)

    again = input("Do you want to show all the vehicle's location again(y/n)? ")
    if again == 'y':
        print("Show all the vehicle's location again:")
        cursor.execute("SELECT vehicle_id, vehicle_type, location_x, location_y FROM Vehicles") 
        for x in cursor.fetchall():
            print("id:{}, type:{}, location: {} ({},{})".format(x[0], x[1], place[x[0] - 1], x[2], x[3]))
    else:
        pass

# operators()