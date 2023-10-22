import sqlite3
import random

def vehicles():
    with sqlite3.connect("User_Vehicle.db") as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Vehicles(
            vehicle_id integer PRIMARY KEY AUTOINCREMENT,
            vehicle_type text,
            battery integer,
            vehicle_status ingeter,
            earned_money integer,
            total_time datatime,
            vehicle_use integer,
            location_x integer,
            location_y integer,
            place_name text);""")
        
    place_names = ['Bridge Street','Buchanan Street','Cessnock','Cowcaddens','Govan','Hillhead','Ibrox','Kelvinhall', 'Kelvinbridge', 'Kinning Park']

    for i in range(20):

        location_start_x = random.randint(0, 501)
        location_start_y = random.randint(0, 501)

        if location_start_x <= 100:
            if location_start_y <= 250:
                place = place_names[0]
            elif 250 <= location_start_y < 500:
                place = place_names[1]
        elif 100 < location_start_x <= 200:
            if location_start_y <= 250:
                place = place_names[2]
            elif 250 <= location_start_y < 500:
                place = place_names[3]
        elif 200 < location_start_x <= 300:
            if location_start_y <= 250:
                place = place_names[4]
            elif 250 <= location_start_y < 500:
                place = place_names[5]
        elif 300 < location_start_x <= 400:
            if location_start_y <= 250:
                place = place_names[6]
            elif 250 <= location_start_y < 500:
                place = place_names[7]
        elif 400 < location_start_x <= 500:
            if location_start_y <= 250:
                place = place_names[8]
            elif 250 <= location_start_y < 500:
                place = place_names[9]

        cursor.execute("""INSERT INTO Vehicles(vehicle_type, battery, vehicle_status, earned_money, total_time, vehicle_use, location_x, location_y, place_name)
        VALUES ("bike", 100, 0, 0, 0, 0, ?, ?, ?)""", (location_start_x, location_start_y, place))
        db.commit()

        location_start_x = random.randint(0, 501)
        location_start_y = random.randint(0, 501)
        
        if location_start_x <= 100:
            if location_start_y <= 250:
                place = place_names[0]
            elif 250 <= location_start_y < 500:
                place = place_names[1]
        elif 100 < location_start_x <= 200:
            if location_start_y <= 250:
                place = place_names[2]
            elif 250 <= location_start_y < 500:
                place = place_names[3]
        elif 200 < location_start_x <= 300:
            if location_start_y <= 250:
                place = place_names[4]
            elif 250 <= location_start_y < 500:
                place = place_names[5]
        elif 300 < location_start_x <= 400:
            if location_start_y <= 250:
                place = place_names[6]
            elif 250 <= location_start_y < 500:
                place = place_names[7]
        elif 400 < location_start_x <= 500:
            if location_start_y <= 250:
                place = place_names[8]
            elif 250 <= location_start_y < 500:
                place = place_names[9]

        cursor.execute("""INSERT INTO Vehicles(vehicle_type, battery, vehicle_status, earned_money, total_time, vehicle_use, location_x, location_y, place_name)
        VALUES ("scooter", 100, 0, 0, 0, 0, ?, ?, ?)""", (location_start_x, location_start_y, place))
        db.commit()

def orders():
    with sqlite3.connect("User_Vehicle.db") as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Orders(
            id integer PRIMARY KEY AUTOINCREMENT,
            vehicle_id integer,
            vehicle_start_time integer,
            vehicle_end_time integer);""")

vehicles()
orders()
        
