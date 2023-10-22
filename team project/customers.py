import sqlite3
from datetime import datetime
import random
import math


def customers():

    with sqlite3.connect("User_Vehicle.db") as db:
        cursor = db.cursor()

    money = random.randint(0,10)

    cursor.execute("""CREATE TABLE IF NOT EXISTS Customers(
        customer_id integer PRIMARY KEY AUTOINCREMENT,
        account_money integer);""")

    cursor.execute("INSERT INTO Customers(account_money) VALUES(?)", (money,)) 
    db.commit() 

    customers_id = 0
    customers_account = 0

    cursor.execute("SELECT customer_id FROM Customers") 
    for x in cursor.fetchall():
        customers_id = int(str(x)[str(x).find("(") + 1:str(x).find(",")])
    
    cursor.execute("SELECT account_money FROM Customers WHERE customer_id=?", [customers_id]) 
    for x in cursor.fetchall():
        customers_account = int(str(x)[str(x).find("(") + 1:str(x).find(",")])


    rent_vehicle = input("Which knid of vehicle that you want to rent? (bike/scooter): ")

    vehicle_id_bike = 1
    vehicle_id_scooter = 1

    location_x = 1
    location_y = 1

    # Set the places' names
    cus_location_x = random.randint(0, 501)
    cus_location_y = random.randint(0, 501)
    place_names = ['Bridge Street','Buchanan Street','Cessnock','Cowcaddens','Govan','Hillhead','Ibrox','Kelvinhall', 'Kelvinbridge', 'Kinning Park']
    place = ''

    if cus_location_x <= 100:
        if cus_location_y <= 250:
            place = place_names[0]
        elif 250 <= cus_location_y < 500:
            place = place_names[1]
    elif 100 < cus_location_x <= 200:
        if cus_location_y <= 250:
            place = place_names[2]
        elif 250 <= cus_location_y < 500:
            place = place_names[3]
    elif 200 < cus_location_x <= 300:
        if cus_location_y <= 250:
            place = place_names[4]
        elif 250 <= cus_location_y < 500:
            place = place_names[5]
    elif 300 < cus_location_x <= 400:
        if cus_location_y <= 250:
            place = place_names[6]
        elif 250 <= cus_location_y < 500:
            place = place_names[7]
    elif 400 < cus_location_x <= 500:
        if cus_location_y <= 250:
            place = place_names[8]
        elif 250 <= cus_location_y < 500:
            place = place_names[9]

    z = 0

    print("Your location is at {} ({}, {})".format(place, cus_location_x, cus_location_y))

    if rent_vehicle == 'bike':
        cursor.execute("SELECT vehicle_id, place_name, location_x, location_y FROM Vehicles WHERE vehicle_type = 'bike' AND vehicle_status = 0 AND battery > 0")
        print("These availablie vehicles are near you:")
        for x in cursor.fetchall():
            # customers_id = int(str(x)[str(x).find("(") + 1:str(x).find(",")])
            # print("id: {} ({}, {})".format(x[0],x[1],x[2]))
            if math.sqrt(((cus_location_x - cus_location_y) **2) + ((x[2] - x[3]) **2)) <= 180 :
                print("id: {} location: {} ({}, {})".format(x[0],x[1],x[2],x[3]))
                z += 1
        if z == 0:
                print("Sorry, there are no vehicles near you. All available vehicles are shown below:")
                cursor.execute("SELECT vehicle_id, place_name, location_x, location_y FROM Vehicles WHERE vehicle_type = 'bike' AND vehicle_status = 0 AND battery > 0")
                for x in cursor.fetchall():
                    print("id: {} location: {} ({}, {})".format(x[0],x[1],x[2],x[3]))
        vehicle_id_bike = int(input("Type an id that you want to rent: "))
    elif rent_vehicle == 'scooter':
        cursor.execute("SELECT vehicle_id, place_name, location_x, location_y FROM Vehicles WHERE vehicle_type = 'scooter' AND vehicle_status = 0 AND battery != 0") 
        print("These avaliablie vehicles are near you:")
        for x in cursor.fetchall():
            # customers_id = int(str(x)[str(x).find("(") + 1:str(x).find(",")])
            # print("id: {} ({}, {})".format(x[0],x[1],x[2]))
            if math.sqrt(((cus_location_x - cus_location_y) **2) + ((x[2] - x[3]) **2)) <= 180:
                print("id: {} location: {} ({}, {})".format(x[0],x[1],x[2],x[3]))
                z += 1
        if z == 0:
            print("Sorry, there are no vehicles near you. All available vehicles are shown below:")
            cursor.execute("SELECT vehicle_id, place_name, location_x, location_y FROM Vehicles WHERE vehicle_type = 'scooter' AND vehicle_status = 0 AND battery != 0")
            for x in cursor.fetchall():
                print("id: {} location: {} ({}, {})".format(x[0],x[1],x[2],x[3]))
        vehicle_id_scooter = int(input("Type an id that you want to rent: "))

    time_start=datetime.now()
    
    
    scooter_status = list()
    bike_status = list()

    scooter_battery = list()
    bike_battery = list()

    scooter_use = list()
    bike_use = list()

    cursor.execute("SELECT vehicle_status FROM Vehicles WHERE vehicle_id=?", [vehicle_id_scooter]) 
    for x in cursor.fetchall():
        scooter_status.append(x)

    cursor.execute("SELECT vehicle_status FROM Vehicles WHERE vehicle_id=?", [vehicle_id_bike]) 
    for x in cursor.fetchall():
        bike_status.append(x)

    cursor.execute("SELECT battery FROM Vehicles WHERE vehicle_id=?", [vehicle_id_scooter]) 
    for x in cursor.fetchall():
        scooter_battery.append(x)

    cursor.execute("SELECT battery FROM Vehicles WHERE vehicle_id=?", [vehicle_id_bike]) 
    for x in cursor.fetchall():
        bike_battery.append(x)

    cursor.execute("SELECT vehicle_use FROM Vehicles WHERE vehicle_id=?", [vehicle_id_scooter]) 
    for x in cursor.fetchall():
        scooter_use.append(x)

    cursor.execute("SELECT vehicle_use FROM Vehicles WHERE vehicle_id=?", [vehicle_id_bike]) 
    for x in cursor.fetchall():
        bike_use.append(x)
    
    bike_battery = int(str(bike_battery)[str(bike_battery).find("(") + 1:str(bike_battery).find(",")])
    scooter_battery = int(str(scooter_battery)[str(scooter_battery).find("(") + 1:str(scooter_battery).find(",")])

    bike_use = int(str(bike_use)[str(bike_use).find("(") + 1:str(bike_use).find(",")])
    scooter_use = int(str(scooter_use)[str(scooter_use).find("(") + 1:str(scooter_use).find(",")])

    # location_x = random.randint(0, 501)
    # location_y = random.randint(0, 501)

    if rent_vehicle == "bike" and bike_status[0][0] == 0 and bike_battery > 0:
        cursor.execute("UPDATE Vehicles SET vehicle_status = 1, vehicle_use = ? WHERE vehicle_id = ?",[bike_use + 1, vehicle_id_bike])
        db.commit()
    elif rent_vehicle == "scooter" and scooter_status[0][0] == 0 and scooter_battery > 0:
        cursor.execute("UPDATE Vehicles SET vehicle_status = 1, vehicle_use = ? WHERE vehicle_id = ?",[scooter_use + 1, vehicle_id_scooter])
        db.commit()
    else:
        print("The vehicle needs to be repaired, please choose another one.")
        exit()
    if rent_vehicle == "bike":
        cursor.execute("SELECT location_x, location_y FROM Vehicles WHERE vehicle_id=?", [vehicle_id_bike]) 
        for x in cursor.fetchall():
            location_x = x[0]
            location_y = x[1]
    elif rent_vehicle == 'scooter':
        cursor.execute("SELECT location_x, location_y FROM Vehicles WHERE vehicle_id=?", [vehicle_id_scooter]) 
        for x in cursor.fetchall():
            location_x = x[0]
            location_y = x[1]

    
    # print(location_x, location_y)

    moving = input("Do you want to continue? (y/n) " + '\n' + "(If you still want to use the vehicle, enter y. If you want to return the vehicle, enter n.)")

    while moving == 'y':
        if rent_vehicle == "bike" and bike_battery > 5:
            bike_battery = list()
            location_x = random.randint(0, 501)
            location_y = random.randint(0, 501)
            if location_x <= 100:
                if location_y <= 250:
                    place = place_names[0]
                elif 250 <= location_y < 500:
                    place = place_names[1]
            elif 100 < location_x <= 200:
                if location_y <= 250:
                    place = place_names[2]
                elif 250 <= location_y < 500:
                    place = place_names[3]
            elif 200 < location_x <= 300:
                if location_y <= 250:
                    place = place_names[4]
                elif 250 <= location_y < 500:
                    place = place_names[5]
            elif 300 < location_x <= 400:
                if location_y <= 250:
                    place = place_names[6]
                elif 250 <= location_y < 500:
                    place = place_names[7]
            elif 400 < location_x <= 500:
                if location_y <= 250:
                    place = place_names[8]
                elif 250 <= location_y < 500:
                    place = place_names[9]
            cursor.execute("SELECT battery FROM Vehicles WHERE vehicle_id=?", [vehicle_id_bike])
            for x in cursor.fetchall():
                bike_battery.append(x)
            bike_battery = int(str(bike_battery)[str(bike_battery).find("(") + 1:str(bike_battery).find(",")])
            cursor.execute("UPDATE Vehicles SET battery = ?, location_x = ?, location_y = ?, place_name = ? WHERE vehicle_id = ?",
            [bike_battery - 5, location_x, location_y, place, vehicle_id_bike])
            db.commit()
            moving = input("Do you want to continue? (y/n) ")
        elif rent_vehicle == "scooter" and scooter_battery > 5:
            scooter_battery = list()
            location_x = random.randint(0, 501)
            location_y = random.randint(0, 501)
            if location_x <= 100:
                if location_y <= 250:
                    place = place_names[0]
                elif 250 <= location_y < 500:
                    place = place_names[1]
            elif 100 < location_x <= 200:
                if location_y <= 250:
                    place = place_names[2]
                elif 250 <= location_y < 500:
                    place = place_names[3]
            elif 200 < location_x <= 300:
                if location_y <= 250:
                    place = place_names[4]
                elif 250 <= location_y < 500:
                    place = place_names[5]
            elif 300 < location_x <= 400:
                if location_y <= 250:
                    place = place_names[6]
                elif 250 <= location_y < 500:
                    place = place_names[7]
            elif 400 < location_x <= 500:
                if location_y <= 250:
                    place = place_names[8]
                elif 250 <= location_y < 500:
                    place = place_names[9]
            cursor.execute("SELECT battery FROM Vehicles WHERE vehicle_id=?", [vehicle_id_scooter])
            for x in cursor.fetchall():
                scooter_battery.append(x)
            scooter_battery = int(str(scooter_battery)[str(scooter_battery).find("(") + 1:str(scooter_battery).find(",")])
            cursor.execute("UPDATE Vehicles SET battery = ?, location_x = ?, location_y = ?, place_name = ? WHERE vehicle_id = ?",[scooter_battery - 5, location_x, location_y, place, vehicle_id_scooter])
            db.commit()
            moving = input("Do you want to continue? (y/n) ")
        else:
            print("The vehilce battery is zero, it cannot work for now.")
            break
        
     # Get place name from database
    vehicle_place = ''
    if rent_vehicle == 'bike':
        cursor.execute("SELECT place_name FROM Vehicles WHERE vehicle_id=?", [vehicle_id_bike]) 
        for x in cursor.fetchall():
            vehicle_place = str(x)[str(x).find("(") + 2:-3]
    elif rent_vehicle == 'scooter':
        cursor.execute("SELECT place_name FROM Vehicles WHERE vehicle_id=?", [vehicle_id_scooter]) 
        for x in cursor.fetchall():
            vehicle_place = str(x)[str(x).find("(") + 2:-3]

    print("The vehicle has been returned, the location is {} ({}, {}).".format(vehicle_place, location_x, location_y))
    if rent_vehicle == "bike":
        cursor.execute("UPDATE Vehicles SET vehicle_status = 0 WHERE vehicle_id = ?",[vehicle_id_bike])
        db.commit()
    elif rent_vehicle == "scooter":
        cursor.execute("UPDATE Vehicles SET vehicle_status = 0 WHERE vehicle_id = ?",[vehicle_id_scooter])
        db.commit()
    time_end=datetime.now()

    

    # print(time_start)
    # print(time_end)
    vehicle_time = int(datetime.strptime(str(time_end), '%Y-%m-%d %H:%M:%S.%f').timestamp()) - int(datetime.strptime(str(time_start), '%Y-%m-%d %H:%M:%S.%f').timestamp())
    # print(vehicle_time)

    vehicle_start_time = int(datetime.strptime(str(time_start), '%Y-%m-%d %H:%M:%S.%f').timestamp())
    vehicle_end_time = int(datetime.strptime(str(time_end), '%Y-%m-%d %H:%M:%S.%f').timestamp())
    if rent_vehicle == 'bike':
        cursor.execute("""INSERT INTO Orders (vehicle_id, vehicle_start_time, vehicle_end_time) VALUES(?, ?, ?)""", (vehicle_id_bike, vehicle_start_time, vehicle_end_time))
        db.commit()
    elif rent_vehicle == 'scooter':
        cursor.execute("""INSERT INTO Orders (vehicle_id, vehicle_start_time, vehicle_end_time) VALUES(?, ?, ?)""", (vehicle_id_scooter, vehicle_start_time, vehicle_end_time))
        db.commit()
    
    if vehicle_time <= 30:
        charge_bike = 2
        charge_scooter = 1
        time = 30
    elif vehicle_time <= 60:
        charge_bike = 4
        charge_scooter = 2
        time = 60
    elif vehicle_time <= 90:
        charge_bike = 6
        charge_scooter = 3
        time = 90
    else:
        charge_bike = 8
        charge_scooter = 4
        time = vehicle_time

    print("Your account have {} pounds".format(customers_account))

    if rent_vehicle == "bike" and customers_account < charge_bike:
        num = int(input("You need to pay for your account at least {} pounds: ".format(charge_bike - customers_account)))
        cursor.execute("UPDATE Customers SET account_money = ? WHERE customer_id = ?",[num + customers_account, customers_id])
        db.commit()
        cursor.execute("SELECT account_money FROM Customers WHERE customer_id=?", [customers_id]) 
        for x in cursor.fetchall():
            customers_account = int(str(x)[str(x).find("(") + 1:str(x).find(",")])
    elif rent_vehicle == "scooter" and customers_account < charge_scooter:
        num = int(input("You need to pay for your account at least {} pounds: ".format(charge_scooter - customers_account)))
        cursor.execute("UPDATE Customers SET account_money = ? WHERE customer_id = ?",[num + customers_account, customers_id])
        db.commit()
        cursor.execute("SELECT account_money FROM Customers WHERE customer_id=?", [customers_id]) 
        for x in cursor.fetchall():
            customers_account = int(str(x)[str(x).find("(") + 1:str(x).find(",")])
            
    if rent_vehicle == "bike":
        print("You rode {} seconds, and you rode {}, the time you rode is between {} to {} seconds".format(vehicle_time, rent_vehicle, time - 30, time) + '\n' + "Your account will be charged {} pound(s) automatically".format(charge_bike))
        cursor.execute("UPDATE Customers SET account_money = ? WHERE customer_id = ?",[customers_account - charge_bike, customers_id])
        db.commit()
        print("Your account have {} pounds.".format(customers_account - charge_bike))
    elif rent_vehicle == "scooter":
        print("You rode {} seconds, and you rode {}, the time you rode is between {} to {} seconds".format(vehicle_time, rent_vehicle, time - 30, time) + '\n' + "Your account will be charged {} pound(s) automatically".format(charge_scooter))
        cursor.execute("UPDATE Customers SET account_money = ? WHERE customer_id = ?",[customers_account - charge_scooter, customers_id])
        db.commit()
        print("Your account have {} pounds.".format(customers_account - charge_scooter))

    repair = input("Is this vehicle needs to be repaired(y/n)? ")
    if repair == 'y' and rent_vehicle == "bike":
        cursor.execute("UPDATE Vehicles SET vehicle_status = 2 WHERE vehicle_id = ?",[vehicle_id_bike])
        db.commit()
    elif repair == 'y' and rent_vehicle == "scooter":
        cursor.execute("UPDATE Vehicles SET vehicle_status = 2 WHERE vehicle_id = ?",[vehicle_id_scooter])
        db.commit()
    else:
        pass

    # print(vehicle_time)

    if rent_vehicle == "bike":
        cursor.execute("SELECT total_time FROM Vehicles WHERE vehicle_id=?", [vehicle_id_bike]) 
        for x in cursor.fetchall():
            total_time = int(str(x)[str(x).find("(") + 1:str(x).find(",")]) + vehicle_time
    elif rent_vehicle == "scooter":
        cursor.execute("SELECT total_time FROM Vehicles WHERE vehicle_id=?", [vehicle_id_scooter]) 
        for x in cursor.fetchall():
            total_time = int(str(x)[str(x).find("(") + 1:str(x).find(",")]) + vehicle_time

    if rent_vehicle == "bike":
        cursor.execute("UPDATE Vehicles SET total_time = ? WHERE vehicle_id = ?",[total_time, vehicle_id_bike])
        db.commit()
    elif rent_vehicle == "scooter":
        cursor.execute("UPDATE Vehicles SET total_time = ? WHERE vehicle_id = ?",[total_time, vehicle_id_scooter])
        db.commit()

    # print(total_time)

# customers()


# cursor.execute("UPDATE Vehicles SET vehicle_use = 1 WHERE vehicle_id = ?", [vehicle_id_bike])